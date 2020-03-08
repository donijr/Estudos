import re
import requests
import json
import os
import shutil
import time

def criarListaCnpJS(arquivoLista):

    #lendo Lista de Cnpjs e criando listaCnpjs
    with open('{}'.format(arquivoLista),'r') as arquivoLista:
        listaCnpjs = arquivoLista.readlines()

    #limpando lixo do \n dos items da lista
    listaCnpjs = [i.replace('\n','') for i in listaCnpjs]

    return listaCnpjs

def copiarERenomear(cnpj,arquivoModeloScript,CaminhoPastaOrigemModeloScript,caminhoPastaDestinoCnpj):
    #arquivoModeloScriptSql = 'CadastroCNPJ_Base.sql'
    caminhoOriginal = '{0}{1}'.format(CaminhoPastaOrigemModeloScript,arquivoModeloScript)
    caminhoDestino = '{}'.format(caminhoPastaDestinoCnpj)
    caminhoOrigemScript = caminhoDestino+'{}'.format(arquivoModeloScript)

    caminhoDestinoEmpresa = caminhoDestino+'{}.sql'.format(cnpj)
        
    shutil.copy2(caminhoOriginal, caminhoDestino)
    os.rename(caminhoOrigemScript,caminhoDestinoEmpresa)
    #print(caminhoDestinoEmpresa)


def preencherScriptSql(CaminhoPastaOrigemModeloScript,cnpj):
    pagina = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))

    empresa_dados = json.loads(pagina.content)

    with open('{}{}.sql'.format(CaminhoPastaOrigemModeloScript,cnpj),encoding='latin-1',mode='r') as arquivoSql:
        campo = arquivoSql.read()

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
    
        #substituição dos campos
        campo = campo.replace('_CNPJ_',cnpjCompleto)
        campo = campo.replace('_razaoSocial_',empresa_dados['nome'])
        campo = campo.replace('_nomeFantasia_',empresa_dados['fantasia'])
        campo = campo.replace('_logradouro_',empresa_dados['logradouro'])
        campo = campo.replace('_numero_',empresa_dados['numero'])
        campo = campo.replace('_complemento_',empresa_dados['complemento'])
        campo = campo.replace('_bairro_',empresa_dados['bairro'])
        campo = campo.replace('_municipio_',municipio)
        campo = campo.replace('_cep_',cep)
        campo = campo.replace('_telefone_',telefone)
        campo = campo.replace('_email_',empresa_dados['email'])
        campo = campo.replace('_numeroCnpj_',numCnpj)
        campo = campo.replace('_numeroFilial_',numFilial)
        campo = campo.replace('_digitoCnpj_',digCnpj)

        if empresa_dados['tipo'] == 'MATRIZ':
            #pastaIntegra = 
            campo = campo.replace('_caminhoPastaIntegra_', '/complianceServer/ComplianceFiscal/Integra/{}'.format(cnpjCompleto))
        elif empresa_dados['tipo'] == 'FILIAL':
            campo = campo.replace('_caminhoPastaIntegra_', '')
    with open('{}{}.sql'.format(CaminhoPastaOrigemModeloScript,cnpj),encoding='latin-1',mode ='w') as arquivoSql:
        arquivoSql.write(campo)



listaCnpjs = criarListaCnpJS('listaExemploCnpj')

contador = 0
for cnpj in listaCnpjs:
    contador = contador + 1
    camiCaminhoPastaOrigemScript = './Empresas/'
    copiarERenomear(cnpj,'CadastroCNPJ_Base.sql','./',camiCaminhoPastaOrigemScript)
    preencherScriptSql(camiCaminhoPastaOrigemScript,cnpj)
    print('{} - script feito'.format(cnpj))
    if contador % 3 == 0:
        time.sleep(65)

print('Sucesso')