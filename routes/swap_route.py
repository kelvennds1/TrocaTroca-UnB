from flask import Flask, render_template, request, redirect, session , jsonify, Blueprint
from sqlalchemy import create_engine, cast, select
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import *
import pytz
from datetime import datetime, timedelta
import sys

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
db_session = Session()

sys.path.append("../routes")
swap_bp = Blueprint('swap', __name__)

PLACEHOLDER_KEY_FOR_DONATION = 22

@swap_bp.route('/swap', methods=['GET', 'POST'])
def swap():
    #if 'idperson_this_party' not in session:
    #    return redirect('/login')
    if request.method == 'POST':
        idperson_this_party = request.form['idperson_this_party']
        iditem_give = request.form['iditem_give']
        idperson_other_party = request.form['idperson_other_party']
        iditem_receive = request.form['iditem_receive']
        swap_type = request.form['swap_type']



        answ_route, idswap = save_swap_data(idperson_this_party, iditem_give, idperson_other_party, iditem_receive, swap_type) #  'swap_waiting_2nd_party' 'swap_success' or 'swap_fail'
        if idswap:
            return redirect(str(answ_route) + '?idswap=' + str(idswap)) # /swap_waiting_other_party
        else:
            return redirect(str(answ_route)) #
    return render_template('swap.html')

# receives None from donation case where 1 party gives no item
def save_swap_data(idperson_this_party, iditem_give, idperson_other_party, iditem_receive, swap_type):
    session = Session()
    current_time = datetime.now(pytz.timezone('America/Sao_Paulo'))
    swap_table = None
    idswap = None

    try:
        item_receive = session.query(Item).filter_by(iditem=iditem_receive).first()
        item_give = session.query(Item).filter_by(iditem=iditem_give).first()
        person_this_party = session.query(Person).filter_by(idperson=idperson_this_party).first()
        person_other_party = session.query(Person).filter_by(idperson=idperson_other_party).first()
#----------------------------------------------------------------------------------------------
        # first considers this party as 2nd to insert, else creates new swap instance

        # if donation item belongs to party and only 1 party gives item
        if (swap_type == 'Doação'):  #!TODO: test when donation w item is 2nd party to insert vice versa. 2 cases.
            if (item_give.person == person_this_party and item_receive == None ):
                iditem_receive = PLACEHOLDER_KEY_FOR_DONATION;
                swap_table = session.query(Swap).filter(
                Swap.p1Key == idperson_other_party,
                Swap.p1kGive == PLACEHOLDER_KEY_FOR_DONATION,
                Swap.p1kReceive == iditem_give,
                Swap.p2Key == idperson_this_party,
                Swap.p2kGive.is_(None),
                Swap.p2kReceive.is_(None),
                Swap.time_created > min_time
                ).first() # ?TODO: consider 1st party is receiving donation
            elif ( item_receive.person == person_other_party and item_give == None ):
                iditem_receive = PLACEHOLDER_KEY_FOR_DONATION; # not strictly necessary (as swpa status cur define by p2kGive) but keep here anw, to fully fill swap table
                swap_table = session.query(Swap).filter(
                Swap.p1Key == idperson_other_party,
                Swap.p1kGive == iditem_receive,
                Swap.p1kReceive == PLACEHOLDER_KEY_FOR_DONATION,
                Swap.p2Key == idperson_this_party,
                Swap.p2kGive.is_(None),
                Swap.p2kReceive.is_(None),
                Swap.time_created > min_time
                ).first() # ?TODO: consider 1st party is receiving donation
        # if exchange items belong to parties
        elif (swap_type == 'Troca') and (item_give.person == person_this_party and item_receive.person == person_other_party):
            min_time = datetime.now(pytz.timezone('America/Sao_Paulo')) - timedelta(minutes=5)
            swap_table = session.query(Swap).filter(
            Swap.p1Key == idperson_other_party,
            Swap.p1kGive == iditem_receive,
            Swap.p1kReceive == iditem_give,
            Swap.p2Key == idperson_this_party,
            Swap.p2kGive.is_(None),
            Swap.p2kReceive.is_(None),
            Swap.time_created > min_time
            ).first() # ?TODO: consider 1st party is receiving donation

        # if 1st party began swap in less than expiration_time
        if swap_table is not None:
                swap_table.time_created = datetime.now(pytz.timezone('America/Sao_Paulo')) # resets swap time_created to 2nd party's insert moment
                idswap = swap_table.idswap
                swap_table.p2kReceive = iditem_receive
                swap_table.p2kGive = iditem_give
                if swap_type is not 'Doação':
                    print('transaction is not Doação..')
                    item_receive.person_idperson = idperson_this_party
                    item_give.person_idperson = idperson_other_party
                elif swap_type is 'Doação':
                    print('transaction is Doação..')
                    if(iditem_give != PLACEHOLDER_KEY_FOR_DONATION ):
                        item_give.person_idperson = idperson_other_party
                    elif(iditem_receive != PLACEHOLDER_KEY_FOR_DONATION ):
                        item_receive.person_idperson = idperson_this_party

                    # swap_table.p2kGive = PLACEHOLDER_KEY_FOR_DONATION
                    # item_give.person_idperson = PLACEHOLDER_KEY_FOR_DONATION
                session.commit()

                #check if items swapped owners
                item_gave = session.query(Item).filter_by(iditem=iditem_give).first()
                item_received = session.query(Item).filter_by(iditem=iditem_receive).first()
                if (swap_type is 'Troca' and item_received.person == person_this_party and item_gave.person == person_other_party) or (swap_type is 'Doação' and (item_received.person == person_this_party and item_gave.person != person_other_party) or (item_give.person == person_other_party and item_received.person != person_this_party )):
                    print('Transação efetivada! O item é seu =)')
                    return '/swap_success', idswap
#----------------------------------------------------------------------------------------------
    # else creates new swap instance, this is 1st party to insert
        else:
            new_swap = Swap(p1Key=idperson_this_party, p1kGive=iditem_give, p1kReceive=iditem_receive, p2Key=idperson_other_party, time_created=current_time)
            session.add(new_swap)
            session.commit()
            idswap = new_swap.idswap
            return '/swap_waiting_other_party', idswap


    except Exception as e:
        print(e)
        print('não foi possível efetuar a transação de items :(( verifique que os ids de pessoa e item todos foram cadastrados ))')
    session.close()
    return '/swap_fail', idswap

@swap_bp.route('/swap_status/check', methods=['GET'])
def check_swap_status():
    idswap = request.args.get('idswap')
    session = Session()
    swap = session.query(Swap).filter_by(idswap=idswap).first()
    session.close()
    if swap is not None:
        if swap.p2kGive is not None:
            return jsonify({'status': 'success'})
    return jsonify({'status': 'pending'})


# !TODO: implement css
@swap_bp.route('/swap_success')
def swap_success():
    return render_template('swap_success.html')

@swap_bp.route('/swap_fail')
def swap_fail():
    return render_template('swap_fail.html')

@swap_bp.route('/swap_waiting_other_party')
def swap_waiting_other_party():
    session = Session()
    idswap = request.args.get('idswap')
    swap_table = session.query(Swap).filter_by(idswap=idswap).first()
    session.close()
    return render_template('swap_status.html', idswap=idswap)