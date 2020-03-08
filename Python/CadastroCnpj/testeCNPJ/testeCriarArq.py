import re
import os
import shutil



""" shutil.copy2(caminhoOriginal, caminhoDestino)
os.rename('./Empresas/CadastroCNPJ_Base.sql','./Empresas/1922544646.sql') """

with open('listaExemploCnpj','r') as arquivoLista:
    listaCnpjs = arquivoLista.readlines()

listaCnpjs = [i.replace('\n','') for i in listaCnpjs]

""" for item in listaCnpjs:
    print(item) """

arquivoModeloScriptSql = 'CadastroCNPJ_Base.sql'
caminhoOriginal = './{}'.format(arquivoModeloScriptSql)
caminhoDestino = './Empresas'
caminhoOrigemScript = caminhoDestino+'/{}'.format(arquivoModeloScriptSql)

for item in listaCnpjs:
    caminhoDestinoEmpresa = caminhoDestino+'/{}.sql'.format(item)
    
    shutil.copy2(caminhoOriginal, caminhoDestino)
    os.rename(caminhoOrigemScript,caminhoDestinoEmpresa)
    #print(caminhoDestinoEmpresa)

""" for item in listaCnpjs:
    with open('{}.sql'.format(item),'w') as novoArquivoCnpj:
        novoArquivoCnpj.close() """
    