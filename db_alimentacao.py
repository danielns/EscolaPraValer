# -*- coding: utf-8 -*-
from app import db, models
a="C:\\Users\Daniel\\EscolaPraValer\\ExtracaoOrganizacao dos Bancos\\banco_final.txt"
b = a.decode('utf-8')

with open(b, "r") as escolas:
    # csvdata.next() #Skip headers. equivale a escolas.next()
    
    linhas = escolas.readlines()

for linha in linhas:
    # Split a linha por ;
    data = linha.split(";")
    cod_escola = data[0]
    nome = data[1]
    nome_mun = data[2]
    rede = data[3]
    ideb = data[4]
    nome_uf = data[5]
    complexidade = data[6]
    num_mat = data[7]
    media_mat = data[8]
    nse_nivel_nome = data[9]
    nse_valor = data[10]
    infra = data[11]
    ideb_relativo = data[12]
    IdebMedio = data[13]
    Diff = data[14]
    NivelGeral = data[15]
    print(ideb)
    print(type(ideb))
    # Put this through to SQL using an INSERT statement...
    u = models.Escola(cod_escola, nome.decode('utf-8'), nome_mun, rede, ideb ,nome_uf,
                 complexidade, num_mat, media_mat, nse_nivel_nome,  
                 nse_valor, infra, ideb_relativo, IdebMedio,
                     Diff, NivelGeral)
   
     
    db.session.add(u)
    
db.session.commit()
print("Banco Atualizado!")
