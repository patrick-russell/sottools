"""
    app.py
    ~~~~~~~~

    Flask app powering sottools.com

    :copyright: © 2018 by Patrick Russell
    :license: MIT, see LICENSE for more details.
"""

import os
import datetime as dt
import hashlib

from flask import (Flask, render_template, url_for, redirect, request,
                   session, flash)
from werkzeug.wsgi import DispatcherMiddleware
from flask_cors import CORS
from flask_s3 import FlaskS3

from forms import LootCalcForm
from tools import process_loot
from utils import whereami


def start_app():
    app = Flask(__name__)
    cors.init_app(app)
    s3.init_app(app)

    # application setup
    app.secret_key = os.environ.get('SECRET_KEY')
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.config['FLASKS3_BUCKET_NAME'] = os.environ.get('S3_BUCKET_NAME')
    app.config['STAGE'] = whereami()
    return app


cors = CORS()
s3 = FlaskS3()
app = start_app()


@app.before_request
def set_session():
    remote_addr = request.remote_addr.encode('utf-8')
    user_agent = request.user_agent.string.encode('utf-8')
    if 'sessionId' not in session:
        ts = dt.datetime.utcnow().isoformat().encode('utf-8')
        session['sessionId'] = hashlib.md5(ts + remote_addr).hexdigest()
        session['fs'] = ts
    session['ts'] = dt.datetime.utcnow().isoformat()
    session['tkn'] = hashlib.md5(remote_addr + user_agent).hexdigest()[:7]


@app.route('/')
def index():
    return redirect(url_for('loot_calc'))


@app.route('/loot-calc', methods=['GET', 'POST'])
def loot_calc():
    """contains form to submit your haul.
    returns estimated ducat amount
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
