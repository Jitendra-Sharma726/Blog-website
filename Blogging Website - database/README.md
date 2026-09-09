Blogging website - database
In this lesson, you'll define the blueprints for your application's data using Flask-SQLAlchemy. We'll map out Python classes for User, Post, and Comment that SQLAlchemy will translate into database tables.

Goal: Define the structure for User, Post, and Comment models in a Python file (e.g., models.py), including their columns and relationships.

Key Concepts:

db.Model: The base class your models will inherit from.
db.Column: Defines a column in a database table, specifying its data type and constraints.
UserMixin: A helper class from Flask-Login for user session management methods.
Define the User Model
This class will represent users in your application.

Password Handling Methods: Add methods to handle password security.

A set_password method that takes a plain password, hashes it, and stores the hash in the password_hash column.
A check_password method that takes a plain password and compares it against the stored hash, returning True or False.
def set_password(self, password):
    # This function generates a secure hash of the password
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    # This function compares a provided password with the stored hash
    return check_password_hash(self.password_hash, password)
User Model Structure Summary:

Attribute	Type	Constraints/Details	Purpose
id	db.Integer	Primary Key	Unique identifier for the user.
username	db.String(100)	Unique, Not Nullable, Indexed	User's login name.
password_hash	db.String(256)	Not Nullable	Securely stored password hash.
set_password	Method	Takes password argument	Hashes and stores the password.
check_password	Method	Takes password argument, returns Boolean	Verifies a given password against the hash.
posts	db.relationship('Post')	back_populates='author'	Access this user's posts.
comments	db.relationship('Comment')	back_populates='user'	Access this user's comments.
