import re
from bs4 import BeautifulSoup

def substituir(campo):
    str(campo)
    tam = len(campo)
    
    with open('exemplo','r') as arquivo:
        text_unico = arquivo.read()
        campo = re.search('"{}*[ -~]*?,'.format(campo),text_unico)

    nome_campo = campo.group(0)
    #print(nome_campo)

    novo_campo=[]

    # Limpando String

    for letra in nome_campo:
        if (letra != "\"") and  (letra != ":") and (letra != ","):
            novo_campo.append(letra)
        
    # limpando palavra do tipo do campo
    novo_campo = ''.join(novo_campo)
    str(novo_campo)
    novo_campo = novo_campo[tam:]

    return novo_campo

tel= substituir("telefone")

print(tel)

with open('Arquivo.sql','r') as arquivoSql:
    sql = arquivoSql.read()

    #sql = sql.replace("telefone",{}).format(tel)
    sql = sql.replace('telefone',tel)

with open('Arquivo.sql','w') as arquivoSql:
    arquivoSql.write(sql)
