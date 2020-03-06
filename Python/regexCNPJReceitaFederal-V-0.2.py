import re

def substituir(campo):
    str(campo)
    tam = len(campo)
    arquivo = open('exemplo','r')
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
    arquivo.close

    return novo_campo

print(substituir("telefone"))