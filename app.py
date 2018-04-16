import os

from flask import Flask, render_template, url_for, redirect, abort, request, make_response, session
# from flask_cors import CORS
# from flask_dynamo import Dynamo
# from flask_s3 import FlaskS3


# constants and environment variables
DEBUG = bool(os.environ.get('FLASK_DEBUG', 0))
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
SECRET_KEY = os.environ.get('SECRET_KEY')

# application setup
app = Flask(__name__)

# app.config['DYNAMO_TABLES'] = dynamo_tables
# app.config['FLASKS3_BUCKET_NAME'] = S3_BUCKET_NAME

# CORS(app)
# dynamo = Dynamo(app)
# s3 = FlaskS3(app)


@app.route('/')
def index():
    return redirect(url_for('loot_calc'))


@app.route('/loot-calc')
def loot_calc():
    '''contains form to submit your haul.
    returns estimated $$ amount
    '''
    return render_template('loot_calc.html')


@app.route('/loot-submit')
def loot_submit():
    '''contains form for submitting your loots
    type, level, sale point, count
    posts to api/loot-sumit
    '''
    pass


@app.route('/api/calc')
def api_calc():
    '''performs the estimated $$ amount for a haul'''
    pass


@app.route('/api/loot-submit')
def api_loot_submit():
    '''submit loot, store in the database
    type
    level
    origin
    sale point
    amount
    quest
    '''
    pass
