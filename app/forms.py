from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length
from models import Escola

class Cod_escola_informado(Form):
    cod_escola_informado = TextField('cod_escola_informado', validators = [Required()])
    
class SearchForm(Form):
    search = TextField('search', validators = [Required()])