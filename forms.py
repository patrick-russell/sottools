"""
    forms.py
    ~~~~~~~~

    WTF form definitions for sottools.com

    :copyright: © 2018 by Patrick Russell
    :license: MIT, see LICENSE for more details.
"""
from operator import itemgetter

from wtforms import SelectField, IntegerField, FieldList, FormField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from sotgame import sot


class LootCalcForm(FlaskForm):
    choices = [(k, v['item']) for k, v in sot.items.items()]
    choices.sort(key=itemgetter(1))
    loot_options = SelectField(label="What's your loot matey?",
                               id="loot-options",
                               choices=choices,
                               render_kw={'class': 'form-control'},
                               validators=[InputRequired])
    loot_count = IntegerField(label='How Many?',
                              id='loot-count',
                              render_kw={'class': 'form-control',
                                         'placeholder': '0'},
                              validators=[InputRequired])
