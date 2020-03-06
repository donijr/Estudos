import re

arquivo = open('exemplo','r')
unica = arquivo.read()
#for linha in unica:
nome = re.search('"nome*[ -~]*?,',unica)
fantasia = re.search('"fantasia*[ -~]*?,',unica)

nome_fantasia = fantasia.group(0)
razao_social = nome.group(0)
print(fantasia.group(0))
print(razao_social)

#result = re.search('nome+*',arquivo.readlines())


arquivo.close