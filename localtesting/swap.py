from flask import Flask, render_template
from sqlalchemy import create_engine, cast, select
from sqlalchemy.orm import sessionmaker
# from base64 import encode, decode, decodebytes
from trocatroca0_orm import *
import base64
import requests
import pytz

app = Flask(__name__)
app.secret_key = 'your_secret_key'
engine = create_engine(
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
    #if 'idperson' not in session:
    #    return redirect('/login')

    if request.method == 'POST':
        idperson = request.form['idperson']
        iditem_receive = request.form['iditem_receive']
        iditem_give = request.form['iditem_give']
        # Save the swap details in the database
        save_swap_data(idperson, iditem_receive, iditem_give)

        # Set the expiration time for the swap
        expiration_time = datetime.now() + timedelta(minutes=5)

        # Store the swap details and expiration time in session
        session['swap_data'] = {
            'iditem_receive': iditem_receive,
            'iditem_give': iditem_give,
            'idperson': idperson,
            'expiration_time': expiration_time
        }

        return redirect('/swap_status')

    return render_template('swap.html')


# Route for checking the swap status
@app.route('/swap_status')
def swap_status():
    # session = Session()
    swap_data = session.get('swap_data')

    if swap_data:
        current_time = datetime.now(pytz.utc)  # Get current time with UTC timezone

        if current_time <= swap_data['expiration_time']:
            # Swap attempt is within the valid time range
            return render_template('swap_status.html', status='success')
        else:
            # Swap attempt has expired
            return render_template('swap_status.html', status='expired')

    # No swap details found in session
    return redirect('/swap')


# Helper function to save swap details in the database
def save_swap_data(idperson, iditem_receive, iditem_give):
    session = Session()
    new_swap = Swap(p1Key=idperson, p1kGive=iditem_receive, p1kReceive=iditem_give)
    session.add(new_swap)
    session.commit()
    session.close()



if __name__ == '__main__':
    app.run(debug=True)

