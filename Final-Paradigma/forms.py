from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import Required, Length

#Clase para crear el formulario de la busqueda del Cliente, donde sus validaciones seran que es "requerido" y que tenga "minimo 3 caracteres"
class ClienteForm(FlaskForm):
    cliente = StringField('Ingresar Cliente: ', validators=[Required(), Length(min=3, message="Ingresa minimo 3 caracteres.")])
    buscar = SubmitField('Buscar')

#Clase para crear el formulario de la busqueda del Producto, donde sus validaciones seran que es "requerido" y que tenga "minimo 3 caracteres"
class ProductoForm(FlaskForm):
    producto = StringField('Ingresar Producto: ', validators=[Required(), Length(min=3,message="Ingresa minimo 3 caracteres.")])
    buscar = SubmitField('Buscar')

class VentaForm(FlaskForm):
    codigo = StringField('Ingresar Codigo: ', validators=[Required(), Length(min=6, message="Ingresa 6 caracteres."), Length(max=6, message="Ingresa 6 caracteres.")])
    producto = StringField('Ingresar Producto: ', validators=[Required(), Length(min=3, message="Ingresa minimo 3 caracteres.")])
    cliente = StringField('Ingresar Cliente: ', validators=[Required(), Length(min=3, message="Ingresa minimo 3 caracteres.")])
    cantidad = IntegerField('Ingresar Cantidad: ', validators=[Required("Solo numeros enteros")])
    precio = FloatField('Ingresar Precio: ', validators=[Required("Solo numeros decimales")])
    buscar = SubmitField('Confirmar')