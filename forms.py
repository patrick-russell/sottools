"""WTF form definitions"""

from wtforms import SelectField, IntegerField, FieldList, FormField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class LootCalcForm(FlaskForm):
    lootz = FieldList(FormField(IntegerField(default=0)), min_entries=1)
