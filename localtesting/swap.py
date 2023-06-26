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
from sqlalchemy import func

from sqlalchemy import func
from flask import Flask, render_template, request, redirect, session
from datetime import datetime, timedelta
import random
import string


# Route for the swap page
@app.route('/swap', methods=['GET', 'POST'])
def swap():
    #if 'idperson_logged' not in session:
    #    return redirect('/login')

    if request.method == 'POST':
        idperson_logged = request.form['idperson_logged']
        iditem_give = request.form['iditem_give']
        idperson_other_party = request.form['idperson_other_party']
        iditem_receive = request.form['iditem_receive']
        # Save the swap details in the database
        save_swap_data(idperson_logged, iditem_give, idperson_other_party, iditem_receive)

        # Set the expiration time for the swap
        expiration_time = datetime.now(pytz.utc) + timedelta(minutes=5)

        # Store the swap details and expiration time in session
        session['swap_data'] = {
            'iditem_receive': iditem_receive,
            'iditem_give': iditem_give,
            'idperson_logged': idperson_logged,
            'idperson_other_party': idperson_other_party,
            'expiration_time': expiration_time
        }

        return redirect('/swap_status')

    return render_template('swap.html')


# Route for checking the swap status
@app.route('/swap_status')
def swap_status():
    # !TODO: how to pass session as arg? remem to close
    swap_data = session.get('swap_data')

    if swap_data:
        current_time = datetime.now(pytz.utc)  # Get current time with UTC timezone
        # current_time = datetime.now() + timedelta(minutes=0)
        if current_time <= swap_data['expiration_time']:
            # Swap attempt is within the valid time range
            return render_template('swap_status.html', status='success')
        else:
            # Swap attempt has expired
            return render_template('swap_status.html', status='expired')

    # No swap details found in session
    return redirect('/swap')


# !TODO: update swap_status to redirect user immediately after 2nd party inserts swap (success), or to display swap page link (fail)
def save_swap_data(idperson_logged, iditem_give, idperson_other_party, iditem_receive):
    session = Session()
    current_time = datetime.now(pytz.timezone('America/Sao_Paulo'))  # Get current time with UTC timezone
    swap_table = None

    try: #!TODO: prevent multiple table creation entries from 1st party
        swap_table = session.query(Swap).filter_by(p1Key=idperson_other_party, p1kGive=iditem_receive, p1kReceive=iditem_give, p2Key=idperson_logged).first()
        max_time = swap_table.time_created + timedelta(minutes=10)
        max_time = max_time.replace(second=0, microsecond=0) # note: excluding max_time time formatting code may result in table not updating at 2nd party's input
        max_time = max_time.astimezone(pytz.timezone('America/Sao_Paulo'))

        if (current_time <= max_time):
            swap_table.p2kGive = iditem_give
            swap_table.p2kReceive = iditem_receive
            session.commit()
            print('Troca efetivada! O item é seu =)')
        else:
            print('demorou demais tenta dnv =DD')
            return render_template('swap_status.html', status='expired')
    except: # ill advised code should use try except & if null
        if swap_table == None:
            new_swap = Swap(p1Key=idperson_logged, p1kGive=iditem_give, p1kReceive=iditem_receive, p2Key=idperson_other_party, time_created=current_time)
            session.add(new_swap)
            session.commit()

    session.close()



if __name__ == '__main__':
    app.run(debug=True)

