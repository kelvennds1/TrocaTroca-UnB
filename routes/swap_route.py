from flask import Flask, render_template, request, redirect, session , jsonify, Blueprint
from sqlalchemy import create_engine, cast, select
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import *
from base64 import encode, decode, decodebytes
import pytz
from datetime import datetime, timedelta
import sys

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
db_session = Session()

sys.path.append("../routes")
swap_bp = Blueprint('swap', __name__)
# Route for the swap page

# Route for the swap page
@swap_bp.route('/swap', methods=['GET', 'POST'])
def swap():
    #if 'idperson_this_party' not in session:
    #    return redirect('/login')
    if request.method == 'POST':
        idperson_this_party = request.form['idperson_this_party']
        iditem_give = request.form['iditem_give']
        idperson_other_party = request.form['idperson_other_party']
        iditem_receive = request.form['iditem_receive']
        # !TODO update item.person_idperson in swap
        answ_route, idswap = save_swap_data(idperson_this_party, iditem_give, idperson_other_party, iditem_receive) #  'swap_waiting_2nd_party' 'swap_success' or 'swap_time_expired_try_again'
        if idswap:
            return redirect(str(answ_route) + '?idswap=' + str(idswap))
        else:
            print('l32,')
            return redirect(str(answ_route))
    return render_template('swap.html')

def save_swap_data(idperson_this_party, iditem_give, idperson_other_party, iditem_receive):
    session = Session()
    current_time = datetime.now(pytz.timezone('America/Sao_Paulo'))  # Get current time with UTC timezone
    swap_table = None
    idswap = None

    try: #!TODO: prevent multiple table creation entries from 1st party, giev item to person by item.person_idperson
        swap_table = session.query(Swap).filter_by(p1Key=idperson_other_party, p1kGive=iditem_receive, p1kReceive=iditem_give, p2Key=idperson_this_party).first()
        if swap_table is not None:
            max_time = swap_table.time_created + timedelta(minutes=50)
            max_time = max_time.replace(second=0, microsecond=0) # note: excluding max_time time formatting code may result in table not updating at 2nd party's input
            max_time = max_time.astimezone(pytz.timezone('America/Sao_Paulo'))

            if (current_time <= max_time):
                swap_table.p2kGive = iditem_give
                swap_table.p2kReceive = iditem_receive
                print('executando a Troca')
              
                idswap = swap_table.idswap

                # return 'success' # 
                item_receive = session.query(Item).filter_by(iditem=iditem_receive).first()
                item_give = session.query(Item).filter_by(iditem=iditem_give).first()
                person_this_party = session.query(Person).filter_by(idperson=idperson_this_party).first()
                person_other_party = session.query(Person).filter_by(idperson=idperson_other_party).first()

                print('trocando items')
                item_receive.person_idperson = idperson_this_party
                item_give.person_idperson = idperson_other_party
                session.commit()
                
                #check if items swapped owners
                item_gave = session.query(Item).filter_by(iditem=iditem_give).first()
                item_received = session.query(Item).filter_by(iditem=iditem_receive).first()
                if (item_received.person_idperson == person_this_party.idperson) and (item_gave.person_idperson == person_other_party.idperson):
                    print('Troca efetivada! O item é seu =)')
                    return '/swap_success', idswap
            else:
                print('demorou demais tenta dnv =DD')
                return '/swap_time_expired_try_again', idswap
        else:
            new_swap = Swap(p1Key=idperson_this_party, p1kGive=iditem_give, p1kReceive=iditem_receive, p2Key=idperson_other_party, time_created=current_time)
            session.add(new_swap)
            session.commit()
            idswap = new_swap.idswap
            return '/swap_waiting_other_party', idswap
    except Exception as e: 
        print(e)
        if swap_table == None:
            new_swap = Swap(p1Key=idperson_this_party, p1kGive=iditem_give, p1kReceive=iditem_receive, p2Key=idperson_other_party, time_created=current_time)
            session.add(new_swap)
            session.commit()
            idswap = swap_table.idswap
            return '/swap_waiting_other_party', idswap
        print('não foi possível efetuar a troca dos items :(( tente novamente))') 
    session.close()
    return '/swap_time_expired_try_again', idswap # !TODO return a single error page indicating time expiration but recognizing other mistakes


@swap_bp.route('/swap_status/check', methods=['GET'])
def check_swap_status():
    idswap = request.args.get('idswap')
    session = Session()
    swap = session.query(Swap).filter_by(idswap=idswap).first()
    session.close()

    if swap:
        # swap = get_swap_from_data(swap_data)  # Retrieve swap object based on your implementation
        if swap.p2kReceive is not None:
            return jsonify({'status': 'success'})

    return jsonify({'status': 'pending'})


# !TODO: implement css
@swap_bp.route('/swap_success')
def swap_success():
    return render_template('swap_success.html')

@swap_bp.route('/swap_time_expired_try_again')
def swap_time_expired_try_again():
    return render_template('swap_time_expired_try_again.html')

@swap_bp.route('/swap_waiting_other_party')
def swap_waiting_other_party():
    idswap = request.args.get('idswap')
    return render_template('swap_status.html', idswap=idswap)