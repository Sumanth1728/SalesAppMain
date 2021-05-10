from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField,RadioField,SelectField,TextField,TextAreaField,SubmitField,SelectMultipleField
from wtforms.validators import DataRequired,Email,EqualTo,Length


class EvaluationForm(FlaskForm):
    Approve=SubmitField("Approve")
    Decline=SubmitField("Decline")

class ClientConfigurationForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    houseno=StringField('House No')
    street=StringField('Street')
    city=StringField('City',validators=[DataRequired()])
    Region=StringField('Region',validators=[DataRequired()])
    Country=SelectField('Country',choices=[('India', 'India'), ('USA', 'USA'),('Canada', 'Canada')],validators=[DataRequired()])
    postalcode=StringField('Postal Code',validators=[DataRequired()])
    phone=StringField('Phone Number',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    timezone=SelectField('Time Zone',choices=[('IST', 'IST'), ('EST', 'EST'),('CT', 'CT')],validators=[DataRequired()])
    functionalarea=SelectField('Functional Area',choices=[('SAP SD', 'SAP SD'), ('Service Now', 'Service Now'),('PEGA', 'PEGA')],validators=[DataRequired()])
    submit=SubmitField("Approve")


class searchform(FlaskForm):
    user=StringField('Enter Client Id ',validators=[DataRequired()])
    submit=SubmitField("Search")
