from itertools import count
from lib2to3.pgen2 import token
from statistics import quantiles
import palavras_reservadas

'''
fazer: verificação de declaração de variaveis 80%

fazer: valor atribuidos as variaveis 0%

'''

def tratar_string(valor):
    array = valor.split('_')
    return array

def token_cod(token):
    array = tratar_string(token)
    valor_token = array[1]
    return valor_token

def token_palavra(token):
    array = tratar_string(token)
    valor_token = array[4]
    return valor_token

def nome_variavel(token):
    array = tratar_string(token)
    valor_token = array[1]
    return valor_token

def iniciadores_palavras(tokens):
    variaveis_iniciadas = []
    contador_erro = 0
    token_ant = ""
    cont_linha = 1
    for linha in tokens:
        for token_atual in linha:
            token_atual_cod = int(token_cod(token_atual))

            if token_atual_cod == 700:
                token_cod_ant =  int(token_cod(token_ant)) 

                if token_cod_ant == 100:
                    token_nome_ant = token_palavra(token_ant)
                    token_atual_nome = token_palavra(token_atual)
                    token_var = str(f"{token_nome_ant}_{token_atual_nome}")

                    if variaveis_iniciadas == []:
                        variaveis_iniciadas.append(token_var)

                    else:
                        var = nome_variavel(token_var)
                        for aux in variaveis_iniciadas:
                            aux_var = nome_variavel(aux)

                            if var == aux_var:
                                return 1,cont_linha

                        variaveis_iniciadas.append(token_var)
                           


            token_ant = token_atual
        cont_linha = cont_linha + 1
    return variaveis_iniciadas, linha

#orquestrador
def orquestrador_semantico(tokens):
    linha = None
    verificador,linha = iniciadores_palavras(tokens)

    print(f"verificador: {verificador}")

    if verificador == 1:
        print(f"erro na delcaração de variaveis, linha: {linha}")
