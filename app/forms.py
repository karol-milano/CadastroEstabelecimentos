# -*- coding: utf8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectMultipleField, widgets, validators

class MultiCheckboxField(SelectMultipleField):
	widget = widgets.ListWidget(prefix_label=False)
	option_widget = widgets.CheckboxInput()	

class SearchForm(FlaskForm):
	name = StringField('Estabelecimento', validators=[validators.Optional()])
	items = MultiCheckboxField('', coerce=int)

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[validators.Email('Email inválido')])

class RegistrationForm(FlaskForm):
	name = StringField('Nome', [validators.DataRequired()])
	email = StringField('Email', [validators.Email('Email inválido')])
	phone = StringField('Telefone', [validators.DataRequired()])

class EnterpriseForm(FlaskForm):
	name = StringField('Nome', [validators.DataRequired()])
	phone = StringField('Telefone', [validators.DataRequired()])
	address = StringField('Endereço', [validators.DataRequired()])
	items = MultiCheckboxField('', coerce=int)