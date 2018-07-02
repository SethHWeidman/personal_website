# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, SubmitField, validators
# from wtforms_alchemy import PhoneNumberField
#
# def CheckNameLength(form, field):
#   print(field)
#   if len(field.data) < 4:
#     raise ValidationError('Name must have more then 3 characters')
#
# class ContactForm(FlaskForm):
#     name = StringField('Your Name:', [validators.DataRequired(), CheckNameLength])
#     email = StringField('Your e-mail address:', [validators.DataRequired(), validators.Email('your@email.com')])
#     phone = PhoneNumberField('Your phone:', [validators.DataRequired()])
#     message = TextAreaField('Your message:', [validators.DataRequired()])
#     submit = SubmitField('Send Message')


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, validators

def CheckNameLength(form, field):
  if len(field.data) < 4:
    raise ValidationError('Name must have more then 3 characters')

class ContactForm(FlaskForm):
    name = StringField('Your Name:', [validators.DataRequired(), CheckNameLength])
    email = StringField('Your e-mail address:', [validators.DataRequired(), validators.Email('your@email.com')])
    phone = IntegerField('Telephone', [validators.NumberRange(min=0, max=10)])
    message = TextAreaField('Your message:', [validators.DataRequired()])
    submit = SubmitField('Send Message')
