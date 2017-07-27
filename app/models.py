from app import db

enterprise_items = db.Table(
    'enterprise_items',
    db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
    db.Column('enterprise_id', db.Integer, db.ForeignKey('enterprises.id'))
)

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	phone = db.Column(db.String())
	email = db.Column(db.String())

	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3

	def __repr__(self):
		return '<User {}>'.format(self.name)


class Enterprise(db.Model):
	__tablename__ = 'enterprises'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	phone = db.Column(db.String())
	address = db.Column(db.String())

	enterprise_items = db.relationship('Item', secondary=enterprise_items,
		backref=db.backref('items', lazy='dynamic'))


	def __init__(self, name, phone, address):
		self.name = name
		self.phone = phone
		self.address = address

	def __repr__(self):
		return '<Enterprise {}>'.format(self.name)


class Item(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String())

	def __init__(self, description):
		self.description = description

	def __repr__(self):
		return '<Item {}>'.format(self.description)


class Comment(db.Model):
	__tablename__ = 'comments'

	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String())

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	user = db.relationship('User',
		backref=db.backref('comments', lazy='dynamic'))

	enterprise_id = db.Column(db.Integer, db.ForeignKey('enterprises.id'))
	enterprise = db.relationship('Enterprise',
		backref=db.backref('comments', lazy='dynamic'))

	def __init__(self, text):
		self.text = text

	def __repr__(self):
		return '<Comment {}>'.format(self.text)


class ItemRating(db.Model):
	__tablename__ = 'item_ratings'

	id = db.Column(db.Integer, primary_key=True)
	grade = db.Column(db.Float)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	user = db.relationship('User',
		backref=db.backref('item_ratings', lazy='dynamic'))

	enterprise_item_id = db.Column(db.Integer, db.ForeignKey('enterprise_items.id'))

	def __init__(self, grade):
		self.grade = grade

	def __repr__(self):
		return '<ItemRating {}>'.format(self.id)


class EnterpriseRating(db.Model):
	__tablename__ = 'enterprise_ratings'

	id = db.Column(db.Integer, primary_key=True)
	grade = db.Column(db.Float)

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	user = db.relationship('User',
		backref=db.backref('enterprise_ratings', lazy='dynamic'))

	enterprise_id = db.Column(db.Integer, db.ForeignKey('enterprises.id'))
	enterprise = db.relationship('Enterprise',
		backref=db.backref('enterprise_ratings', lazy='dynamic'))

	def __init__(self, grade):
		self.grade = grade

	def __repr__(self):
		return '<EnterpriseRating {}>'.format(self.id)