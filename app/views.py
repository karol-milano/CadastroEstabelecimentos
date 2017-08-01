# -*- coding: utf8 -*-

from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
from flask_login import login_user, logout_user, current_user, login_required

from flask_sqlalchemy import get_debug_queries
from sqlalchemy.sql import func

from app import app, db, login_manager

from .forms import *
from .models import *

@login_manager.user_loader
def user_loader(email):
	return User.query.filter_by(email=email)

######################################################################################

@app.route('/')
@app.route('/index')
def index():
	listItems = Item.query.all()
	listEnterprises = Enterprise.query.all()
	return render_template('index.html', 
		title='Home',
		listEnterprises=listEnterprises, 
		listItems=listItems)

######################################################################################

@app.route('/enterprise/search', methods=['POST'])
def searchEnterprise():
	name = request.form['estabelecimento']
	infra = request.form.getlist('infraestrutura')

	if name != '':
		if infra:
			enterprises = Enterprise.query.join(enterprise_items).filter(and_(enterprise_items.c.item_id.in_(infra), Enterprise.name == name)).all()
		else:
			enterprises = Enterprise.query.filter_by(name=name)
	else:
		if infra:
			enterprises = Enterprise.query.join(enterprise_items).filter(enterprise_items.c.item_id.in_(infra))
		else:
			enterprises = Enterprise.query.all()
	
	print(enterprises)

	return render_template('enterprise_search.html', enterprises=enterprises, title='title')

######################################################################################		

@app.route('/enterprise/add', methods=['GET', 'POST'])
def addEnterprise():

	form = EnterpriseForm()
	form.items.choices = [(i.id, i.description) for i in Item.query.all()]

	if form.validate_on_submit():
		enterprise = Enterprise(form.name.data, form.phone.data, form.address.data)

		for i in form.items.data:
			item = Item.query.get(i)
			enterprise.enterprise_items.append(item)

		db.session.add(enterprise)
		db.session.commit()

		flash('Estabelecimento adicionado')
		return redirect(url_for('index'))

	return render_template('enterprise_add.html', 
		title='Cadastro de Estabelecimento',
		form=form)

######################################################################################		

@app.route('/enterprise/show/<enterprise_id>', methods=['GET', 'POST'])
def showEnterprise(enterprise_id):
	enterprise = Enterprise.query.get(enterprise_id)
	listItems = Item.query.all()
	choices = [i.id for i in enterprise.enterprise_items]
	
	count = 0
	avg = 0
	for er in enterprise.enterprise_ratings:
		avg += er.grade
		count+= 1

	if count == 0:
		average = '{:6.1f}'.format(0)
	else:
		average = '{:6.1f}'.format(avg / count)

	if request.method == 'POST':
		print(request.form)

		if request.form['comment'] != '':
			comment = Comment(request.form['comment'])
			enterprise.comments.append(comment)
			db.session.add(enterprise)
			db.session.commit()
		if request.form['grade'] != '':
			er = EnterpriseRating(request.form['grade'])
			enterprise.enterprise_ratings.append(er)
			db.session.add(enterprise)
			db.session.commit()

	return render_template('enterprise_show.html', 
		title='Edição de Estabelecimento',
		enterprise=enterprise,
		choices=choices,
		average=average,
		count=count,
		listItems=listItems)

######################################################################################		

@app.route('/item/add', methods=['GET', 'POST'])
def addItem():

	return render_template('enterprise.html', 
		title='Cadastro de Filtros')

######################################################################################		

@app.route('/item/edit', methods=['GET', 'POST'])
def editItem():

	return render_template('enterprise.html', 
		title='Edição de Filtros')

######################################################################################		

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		login_user(user)
		flash('Logado com sucesso')
		next = request.args.get('next')
		return redirect(next)
	return render_template('login.html', title='Login', form=form)

######################################################################################		

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegistrationForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User(form.name.data, form.phone.data, form.email.data)
			db.session.add(user)
			db.session.commit()
			flash('Conta criada com sucesso')
			return redirect(url_for('index'))
		else:
			print(form.errors)
	return render_template('signup.html', title='Login', form=form)