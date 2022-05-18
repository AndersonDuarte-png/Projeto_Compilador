from re import I
from wsgiref.validate import validator
import palavras_reservadas



def separador_palavras(line):
    array = list(line)
    array_new = []
    for aux in array:
        try:
            index = palavras_reservadas.P_R_linhas_validacao.index(aux)
            array_new.append(' ')
            array_new.append(aux)
            array_new.append(' ')
        except:
            array_new.append(aux)
    string_array = "".join(array_new)
    array_final = string_array.split(' ')
    print(array_final)

#lendo arquivo
arquivo_entrada = open(r"teste1.txt","r")
tokens = []
contagem_linha = 0
for line in arquivo_entrada:
    contagem_linha = contagem_linha + 1
    tokens.append( separador_palavras(line))
#print(tokens)

