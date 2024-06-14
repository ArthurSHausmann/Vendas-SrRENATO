
#class Usuario(Model):
#    nome = CharField()
#    email = CharField
#    cpf = DecimalField
#
#    class Meta:
#        database = db

#class Emprestimo(Model):
#    usuario = ForeignKeyField(Usuario, backref='usuarios')
#    titulo = CharField()
#    descricao = CharField()
#    tempo = TimeField()
#    class Meta:
#        database = db

#class Tipos(Model):
#    tipo = CharField()
#    class Meta:
#        database = db
from peewee import *
db = SqliteDatabase('AplicacaoSrRenato.db')


class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    nome = CharField()
    email = CharField()
    cpf = CharField()


class Objeto(BaseModel):
    NomeDaFerramenta = CharField()
    MarcaDaFerramenta = CharField()
    estado_ferramentas = CharField()
    class Meta:
        database = db

class Manutencao(BaseModel):
    NomeDaFerramenta = CharField()
    dia_inicio = DecimalField()
    mes_inicio = DecimalField()
    ano_inicio = DecimalField()
    datamanut = dia_inicio,"/",mes_inicio,"/",ano_inicio
    class Meta:
        database = db
    
class FerramentasEmManutencao(BaseModel):
    NomeDaFerramenta = CharField()
    MarcaDaFerramenta = CharField()
    estado_ferramentas = CharField()
    dia_inicio = DecimalField()
    mes_inicio = DecimalField()
    ano_inicio = DecimalField()