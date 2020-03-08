import re
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import json

""" pagina = requests.get('https://www.receitaws.com.br/v1/cnpj/27865757000102')

receita_data = json.loads(pagina.content)

for i in range(0,4):
    if pagina.status_code == 200:
        if receita_data['tipo'] == "MATRIZ":
            print("Matriz")
"""

    
 # Coletar dados da página da api
pagina = requests.get('https://www.receitaws.com.br/v1/cnpj/27865757000102')
soup = BeautifulSoup(pagina.text, 'html.parser')


# 
data = soup.prettify()
json_data = json.loads(data)
#print(json_data.keys())

for i in range(0,4):
        if json_data['tipo'] == "MATRIZ":
            print("Matriz")



""" with open('Arquivo.sql','r') as arquivoSql:
    sql = arquivoSql.read()

    #sql = sql.replace("telefone",{}).format(tel)
    sql = sql.replace('telefone',tel)

with open('Arquivo.sql','w') as arquivoSql:
    arquivoSql.write(sql) """
