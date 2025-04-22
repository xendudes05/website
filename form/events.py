from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SubmitField
from wtforms.validators import DataRequired


class EventsForm(FlaskForm):
    title = StringField('Название события', validators=[DataRequired()])
    time = TimeField('Время события', validators=[DataRequired()])
    activity_type = StringField('Тип активности', validators=[DataRequired()])
    mood = StringField('Настроение', validators=[DataRequired()])
    music = StringField('Музыкальное сопровождение', validators=[DataRequired()])
    submit = SubmitField('Применить')
