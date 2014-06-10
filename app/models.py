# -*- coding: utf-8 -*-
from app import db

class Escola(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cod_escola = db.Column(db.Integer)
    nome = db.Column(db.String(150))
    nome_mun = db.Column(db.String(150))
    rede = db.Column(db.String(20))
    ideb = db.Column(db.Float)
    nome_uf = db.Column(db.String(60))
    complexidade = db.Column(db.String(20))
    num_mat = db.Column(db.Integer)
    media_mat = db.Column(db.Float)
    nse_nivel_nome = db.Column(db.String(20))
    nse_valor = db.Column(db.String(20))
    infra = db.Column(db.String(20))
    ideb_relativo = db.Column(db.Float)    
    IdebMedio = db.Column(db.Float)
    Diff = db.Column(db.Float)
    NivelGeral = db.Column(db.Integer)
    
    def __init__(self, cod_escola, nome, nome_mun, rede, ideb ,nome_uf,
                 complexidade, num_mat, media_mat, nse_nivel_nome,  
                 nse_valor, infra, ideb_relativo, IdebMedio,
                     Diff, NivelGeral):

        self.cod_escola = cod_escola
        self.nome = nome
        self.nome_mun = nome_mun   
        self.rede = rede 
        self.ideb = ideb 
        self.nome_uf = nome_uf
        self.complexidade = complexidade 
        self.num_mat = num_mat
        self.media_mat = media_mat
        self.nse_nivel_nome = nse_nivel_nome
        self.nse_valor = nse_valor
        self.infra = infra
        self.ideb_relativo = ideb_relativo
        self.IdebMedio = IdebMedio 
        self.Diff = Diff
        self.NivelGeral  = NivelGeral
        
    def __repr__(self):
        return '<Escola %r>' % (self.nome)
    
