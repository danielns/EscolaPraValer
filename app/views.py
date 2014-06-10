# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, session, url_for, request, g, jsonify, make_response
from app import app, db, models
from models import Escola
from forms import Cod_escola_informado, SearchForm
import math
import json

@app.route('/')
@app.route('/index')
def index():
    melhores_escolas = models.Escola.query.order_by(models.Escola.Diff.desc()).limit(10).all()
    return render_template('index.html', melhores_escolas=melhores_escolas)

@app.route('/busca', methods = ['POST'])
def busca(): # search_form -> validate=required
    return redirect(url_for('escola', cod_escola = g.search_form.cod_escola_informado.data)) # query - fruto da pesquisa


# Página da Escola selecionada
@app.route('/escola/<int:cod_escola>') # colocar o nome da escola na url
def escola(cod_escola):
    escola = models.Escola.query.filter_by(cod_escola=cod_escola).first()
    escolas_mesmo_perfil = models.Escola.query.filter_by(NivelGeral=escola.NivelGeral).order_by(models.Escola.ideb.desc()).all()
    valores_grafico = [escola.ideb,  escola.IdebMedio]
    if escola.ideb_relativo>=0:
        escola.porcentagem = math.fabs(escola.ideb_relativo)
        escola.grandeza="maior"
    else:
        escola.porcentagem = math.fabs(escola.ideb_relativo)
        escola.grandeza="menor"
    return render_template("escola.html",
        escola=escola,
        escolas_mesmo_perfil = escolas_mesmo_perfil,
        valores_grafico=valores_grafico,
        porcentagem=escola.porcentagem,
        grandeza=escola.grandeza)
    
@app.route('/_search_university')
def search_university():
    search = request.args.get('search')
    results = models.Escola.query.filter_by(nome.like('%' + search + '%')).all()
    return jsonify(results)

@app.route('/exemplosd3')
def exemplosd3():
    return render_template('exemplosd3.html')
    
@app.route('/grafico')
def grafico():
    escola_request = models.Escola.query.filter_by(cod_escola=41131460).first()
    escolas_comp = models.Escola.query.filter_by(cod_mun=escola_request.cod_mun).order_by(models.Escola.ideb.desc()).first()
    dados = [{ "nome": escola_request.nome, "ideb": escola_request.ideb},
             { "nome": escola_comp.nome, "ideb": escola_comp.ideb}]
    return json.dumps(dados)

@app.route('/graficobarras1')
def graficobarras1():
    escola_request = models.Escola.query.filter_by(cod_escola=41131460).first()
    escola_comp = models.Escola.query.filter_by(cod_mun=escola_request.cod_mun).order_by(models.Escola.ideb.desc()).first()
    dados = [{ "letter": escola_request.nome, "frequency": escola_request.ideb},
             { "letter": escola_comp.nome, "frequency": escola_comp.ideb}]
    tsv = """letter\tfrequency\nA\t.08167\nB\t.01492"""
    response = make_response(tsv)
    # This is the key: Set the right header for the response
    # to be downloaded, instead of just printed on the browser
    response.headers["Content-Disposition"] = "attachment; filename=data.tsv"
    x = [30,  30, 30,  30]
    w = jsonify(result=x)
    return w
    
    
  
    
@app.route('/graficobarras')
def graficobarras():
    x = [30,  30, 30,  30]
    return render_template('graficobarras.html', x=x)

@app.before_request
def before_request():
    g.search_form = SearchForm()

@app.route('/search', methods = ['POST'])
def search():
    #if not g.search_form.validate_on_submit():
     #   return redirect(url_for('index'))
    return redirect(url_for('busca_escola', query = g.search_form.search.data))

#@app.route('/base/<query>')
#def busca_escola(query):
 #   resultados = models.Escola.query.filter(models.Escola.nome.like("%" + query + "%")).all()
  #  return render_template('base.html',
   #     query = query,
    #    resultados = resultados)
    
@app.route('/busca_escola/<query>')
def busca_escola(query):
    resultados = models.Escola.query.filter(models.Escola.nome.like("%" + query + "%")).all()
    return render_template('busca_escola.html',
        query = query,
        resultados = resultados)
    
@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/como_funciona')
def como_funciona():
    return render_template('como_funciona.html')