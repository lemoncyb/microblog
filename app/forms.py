from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, RadioField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class LoginForm(Form):
    species = RadioField('species', choices=[('h','Human'), ('m','Mouse')], default='h')
    tech = MultiCheckboxField('crispr_tech', choices=[('l','All'), ('a','CRISPR a'), ('i', 'CRISPR i'), ('k','CRISPR ko')], default='l')
    cell_line = StringField('cell_line', validators=[DataRequired()])
    drug = StringField('drug', validators=[DataRequired()])
    gene = StringField('gene', validators=[DataRequired()])
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
