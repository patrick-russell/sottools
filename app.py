"""
    app.py
    ~~~~~~~~

    Flask app powering sottools.com

    :copyright: © 2018 by Patrick Russell
    :license: MIT, see LICENSE for more details.
"""

import os

from flask import Flask, render_template, url_for, redirect, abort, request, make_response, session, flash, jsonify
# from flask_cors import CORS
# from flask_s3 import FlaskS3

from forms import LootCalcForm
from tools import process_loot

# constants and environment variables
DEBUG = bool(int(os.environ.get('FLASK_DEBUG', 0)))
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
SECRET_KEY = os.environ.get('SECRET_KEY')

# application setup
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.config['FLASKS3_BUCKET_NAME'] = S3_BUCKET_NAME

# CORS(app)
# s3 = FlaskS3(app)


@app.route('/')
def index():
    return redirect(url_for('loot_calc'))


@app.route('/loot-calc', methods=['GET', 'POST'])
def loot_calc():
    """contains form to submit your haul.
    returns estimated $$ amount
    """
    if request.method == 'POST':
        loot, totals = process_loot(request.form)
        return render_template('loot_estimate.html', loot=loot, totals=totals)
    form = LootCalcForm()
    return render_template('loot_calc.html', form=form)


@app.route('/loot-submit')
def loot_submit():
    """contains form for submitting your loots
    type, level, sale point, count
    posts to api/loot-sumit
    """
    pass


@app.route('/api/calc', methods=['POST'])
def api_calc():
    """future ajax endpoint"""
    if request.method == 'POST':
        return jsonify('not yet implemented')


@app.route('/api/loot-submit', methods=['POST'])
def api_loot_submit():
    """future ajax endpoint
    submit loot, store in the database
    type
    level
    origin
    sale point
    amount
    quest
    """
    if request.method == 'POST':
        return jsonify('not yet implemented')
