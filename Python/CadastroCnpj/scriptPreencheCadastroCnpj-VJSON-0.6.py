import re
import requests
import json

def preencheScriptSql(cnpj):
    pagina = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))

    empresa_dados = json.loads(pagina.content)

    with open('CadastroCNPJ_Base.sql',encoding='latin-1',mode='r') as arquivoSql:
        campo = arquivoSql.read()

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
        campo = campo.replace('_telefone_',empresa_dados['telefone'])
        campo = campo.replace('_email_',empresa_dados['email'])
        campo = campo.replace('_numeroCnpj_',numCnpj)
        campo = campo.replace('_numeroFilial_',numFilial)
        campo = campo.replace('_digitoCnpj_',digCnpj)

        if empresa_dados['tipo'] == 'MATRIZ':
            #pastaIntegra = 
            campo = campo.replace('_caminhoPastaIntegra_', '/complianceServer/ComplianceFiscal/Integra/{}'.format(cnpjCompleto))

    with open('CadastroCNPJ_Base.sql',encoding='latin-1',mode ='w') as arquivoSql:
        arquivoSql.write(campo)
