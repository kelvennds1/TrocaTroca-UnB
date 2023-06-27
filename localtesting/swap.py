from flask import Flask, render_template
from sqlalchemy import create_engine, cast, select
from sqlalchemy.orm import sessionmaker
# from base64 import encode, decode, decodebytes
from trocatroca0_orm import *
import base64
import requests
import pytz

app = Flask(__name__)
app.secret_key = 'app_secret_key'
engine = create_engine('mysql+pymysql://root:p@localhost/trocatroca0')
Session = sessionmaker(bind=engine)
from flask import Flask, render_template, request, redirect, session
from datetime import datetime, timedelta

# Route for the swap page
@app.route('/swap', methods=['GET', 'POST'])
def swap():
    #if 'idperson_this_party' not in session:
    #    return redirect('/login')

    if request.method == 'POST':
        idperson_this_party = request.form['idperson_this_party']
        iditem_give = request.form['iditem_give']
        idperson_other_party = request.form['idperson_other_party']
        iditem_receive = request.form['iditem_receive']
        # !TODO update item.person_idperson in swap
        answ_route = save_swap_data(idperson_this_party, iditem_give, idperson_other_party, iditem_receive) #  'swap_waiting_2nd_party.html' 'swap_success.html' or 'swap_time_expired_try_again.html'
        expiration_time = datetime.now(pytz.utc) + timedelta(minutes=5)

        return redirect(str(answ_route))
        # return render_template(str(answ_template))
        # return redirect('/swap_status')

    return render_template('swap.html')


# Route for checking the swap status
@app.route('/swap_status')
def swap_status():
    # Get swap data from session
    swap_data = session.get('swap_data')

    if swap_data:
        current_time = datetime.now(pytz.utc)
        expiration_time = swap_data['expiration_time']

        if current_time <= expiration_time:
            # Swap attempt is within the valid time range
            return render_template('swap_status.html', status='success')
        else:
            # Swap attempt has expired
            return render_template('swap_status.html', status='expired')

    # No swap details found in session
    return redirect('/swap')


# !TODO: update swap_status to redirect user immediately after 2nd party inserts swap (success), or to display swap page link (fail)
def save_swap_data(idperson_this_party, iditem_give, idperson_other_party, iditem_receive):
    session = Session()
    current_time = datetime.now(pytz.timezone('America/Sao_Paulo'))  # Get current time with UTC timezone
    swap_table = None

    try: #!TODO: prevent multiple table creation entries from 1st party, giev item to person by item.person_idperson
        swap_table = session.query(Swap).filter_by(p1Key=idperson_other_party, p1kGive=iditem_receive, p1kReceive=iditem_give, p2Key=idperson_this_party).first()
        max_time = swap_table.time_created + timedelta(minutes=50)
        max_time = max_time.replace(second=0, microsecond=0) # note: excluding max_time time formatting code may result in table not updating at 2nd party's input
        max_time = max_time.astimezone(pytz.timezone('America/Sao_Paulo'))

        if (current_time <= max_time):
            swap_table.p2kGive = iditem_give
            swap_table.p2kReceive = iditem_receive
            print('executando Troca')
            session.commit()
            # return 'success' # 
            item_receive = session.query(Item).filter_by(iditem=iditem_receive).first()
            item_give = session.query(Item).filter_by(iditem=iditem_give).first()
            person_this_party = session.query(Person).filter_by(idperson=idperson_this_party).first()
            person_other_party = session.query(Person).filter_by(idperson=idperson_other_party).first()

            
            print(item_give.iditem)
            print('item_give.idperson' + str(item_give.person_idperson))
            print(item_receive.iditem)
            print('item_receive.idperson' + str(item_receive.person_idperson))
            
            
            item_receive.person_idperson = idperson_this_party
            item_give.person_idperson = idperson_other_party
            session.commit()
            
            print(str(item_give.iditem) + 'item_give.idperson' + str(item_give.person_idperson))
            print(str(item_receive.iditem) + 'item_receive.idperson' + str(item_receive.person_idperson))

            #check if items swapped owners
            item_gave = session.query(Item).filter_by(iditem=iditem_give).first()
            item_received = session.query(Item).filter_by(iditem=iditem_receive).first()



            if (item_received.person_idperson == person_this_party.idperson) and (item_gave.person_idperson == person_other_party.idperson):
                print('Troca efetivada! O item é seu =)')
                return '/swap_success'
            else:
                print('não foi possível efetuar a troca dos items :(( tente novamente))')
            
            return '/swap_time_expired_try_again'
        else:
            print('demorou demais tenta dnv =DD')
            # return render_template('swap_status.html', status='expired')
            # return 'expired'
        #     return '/swap_time_expired_try_again'
        
        # return '/swap_time_expired_try_again'
    except Exception as e: 
        print(e)
        if swap_table == None:
            new_swap = Swap(p1Key=idperson_this_party, p1kGive=iditem_give, p1kReceive=iditem_receive, p2Key=idperson_other_party, time_created=current_time)
            session.add(new_swap)
            session.commit()
            # return 'waiting'
            return '/swap_waiting_other_party'
    return '/swap_time_expired_try_again'
    session.close()
# !TODO: implement 
@app.route('/swap_success')
def swap_success():
    return render_template('swap_success.html')

@app.route('/swap_time_expired_try_again')
def swap_time_expired_try_again():
    return render_template('swap_time_expired_try_again.html')

@app.route('/swap_waiting_other_party')
def swap_waiting_other_party():
    return render_template('swap_status.html')

if __name__ == '__main__':
    app.run(debug=True)

