from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField

class TextAnalyzerForm(FlaskForm):
    text=TextAreaField('Input')
    delimiter=StringField('Delimiters')
    options = RadioField('Choices', choices = [('countword','Word Count'), 
					       ('countchar','Character Count'), 
					       ('top5', 'Most Frequent 5 words')])
    submit=SubmitField('Submit')
