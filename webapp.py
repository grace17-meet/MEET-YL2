from flask import Flask, render_template, request, redirect, url_for
from flask import session as web_session
app = Flask(__name__)


#SQLAlchemy stuff
from database import Base, Contact
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Webpage.db')
Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()
#APP CODE GOES HERE

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/bio')
def aboutme():
	return render_template('aboutme.html')
