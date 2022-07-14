from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, HiddenField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class MovimientosForm(FlaskForm):
    id = HiddenField()
    fecha = DateField("Fecha", validators=[DataRequired(
        message="Debes introducir una fecha")])
    concepto = StringField(
        "Concepto", validators=[
            DataRequired(message="Debes escribir un concepto del movimiento"),
            Length(min=3, max=25, message="Debe tener entre 3 y 25 caracteres")])
    tipo = RadioField(choices=[("I", "Ingreso"), ("G", "Gasto")])
    cantidad = FloatField("Cantidad", validators=[DataRequired(
        message="Debes indicar una cantidad válida")])

    submit = SubmitField("Guardar", render_kw={"class": "green-button"})
