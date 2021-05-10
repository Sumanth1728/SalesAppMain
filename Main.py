
from flask import Flask, render_template, session, redirect, url_for, session,flash,request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from datetime import datetime
from basecong import app,mail,mysql
from flask_mail import *
from forms import searchform,ClientConfigurationForm
import os

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html


@app.route('/', methods=['GET', 'POST'])
def index():
    form=ClientConfigurationForm()
    try:
        if form.validate_on_submit():
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO client_master(ClientID,Name,HomeNo,Street,City,Region,PostCode,TelephoneNo,Email,TiemZone,CreatedBy,CreatedDate) VALUES (%s, %s,%s, %s,%s, %s,%s,%s, %s, %s,%s,%s)", ("Client1", form.name.data, form.houseno.data, form.street.data, form.city.data, form.Region.data, int(form.postalcode.data), int(form.phone.data), form.email.data, form.timezone.data,"Sumanth","2021-05-06" ))
            mysql.connection.commit()
            cur.close()
            flash("success")
        else:
            err=form.errors
            for i in err:
                flash(i+"-"+str(err[i]))
    except Exception as e:
        flash(e)
    return render_template('index.html', form=form)

@app.route('/ViewClientDetails', methods=['GET', 'POST'])
def ViewClientDetails():

    form=searchform()
    client=False
    try:
        if form.validate_on_submit():
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM client_master WHERE ClientID = %s", (form.user.data,))
            client = cur.fetchone()
            print(client)
        else:
            err=form.errors
            for i in err:
                flash(i+"-"+str(err[i]))
    except Exception as e:

        flash(e)

    return render_template('viewclient.html',form=form, client=client)

@app.route('/SearchClient', methods=['GET', 'POST'])
def SearchClient():

    form=searchform()
    client=False
    if form.validate_on_submit():

        return redirect(url_for("EditClientDetails",Cid=form.user.data))



    else:
        err=form.errors
        for i in err:
            flash(i+"-"+str(err[i]))
    return render_template('searchclient.html',form=form)


@app.route('/EditClientDetails/<Cid>', methods=['GET', 'POST'])
def EditClientDetails(Cid):

    form=ClientConfigurationForm()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM client_master WHERE ClientID = %s", (Cid,))
    client = cur.fetchone()
    print(client)
    if client:
        form.name.data=client[1]
        form.houseno.data=client[2]
        form.street.data=client[3]
        form.city.data=client[4]
        form.Region.data=client[5]
        form.postalcode.data=client[6]
        form.phone.data=client[7]
        form.email.data=client[8]
        if form.validate_on_submit():
            print("-----------------------------------")
            print("-----------------------------------")
            print(client)
            print("----------------------")
            return form.name.data

            print("----------------------------------")
            print("----------------------------------")

        else:
            err=form.errors
            for i in err:
                flash(i+"-"+str(err[i]))
    else:
        flash("no records exist with this client id. Please check the value you entered")







    return render_template('editclient.html', client=client,form=form)








if __name__ == '__main__':
    app.run(debug=True)
