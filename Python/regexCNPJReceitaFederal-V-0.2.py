import re

def substituir(campo):
    arquivo = open('exemplo','r')
    text_unico = arquivo.read()
    campo = re.search('"{}*[ -~]*?,'.format(campo),text_unico)

    nome_campo = campo.group(0)
    print(nome_campo)

    novo_campo=[]

    # Limpando String

    for letra in nome_campo:
        if (letra != "\"") and  (letra != ":") and (letra != ","):
            print(letra)
            novo_campo.append(letra)

    novo_campo = ''.join(novo_campo)
    arquivo.close

    return novo_campo

substituir("municipio")



