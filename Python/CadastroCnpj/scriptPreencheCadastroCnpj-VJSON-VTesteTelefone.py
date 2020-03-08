import re
import requests
import json
#27865757000102
#07663140000431
pagina = requests.get('https://www.receitaws.com.br/v1/cnpj/27865757000102')

empresa_dados = json.loads(pagina.content)
print(empresa_dados.keys())

print(empresa_dados['tipo'])
print(empresa_dados['cnpj'])
print(empresa_dados['nome'])
print(empresa_dados['fantasia'])
print(empresa_dados['logradouro'])
print(empresa_dados['complemento'])
print(empresa_dados['bairro'])
print(empresa_dados['municipio'])
print(empresa_dados['cep'])
print(empresa_dados['telefone'])
print(empresa_dados['email'])


# Elimina caracteres não numericos do cep e CNPJ
cnpjCompleto = re.sub(r'[^0-9]','',empresa_dados['cnpj'])
cep = re.sub(r'[^0-9]','',empresa_dados['cep'])

#Separa partes do CNPJ: numeroCnpj, NumeroFilial e DigitoCnpj
numCnpj = cnpjCompleto[:8]
numFilial = cnpjCompleto[8:12]
digCnpj = cnpjCompleto[12:14]
    
#Deixar cada palavra do Municipio em maiuscula
municipio = str(empresa_dados['municipio'])
municipio = municipio.title()
  
#Seleciona somente primeiro telefone
telefone = empresa_dados['telefone']

print(empresa_dados['telefone'])
print(len(telefone))
if (len(telefone)  <= 15):
    telefone = empresa_dados['telefone']

else:
    telefone = re.search(r'[ -~]*?/',(empresa_dados['telefone']))
    telefone = str(telefone.group(0))

# Elimina caracteres não numericos do telefone
telefone = re.sub(r'[^0-9]','',telefone)


