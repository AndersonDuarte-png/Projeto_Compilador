from itertools import count


def tratar_string(valor):
    array = valor.split('_')
    return array

def token_cod(token):
    array = tratar_string(token)
    valor_token = array[1]
    return valor_token

def token_linha(token):
    array = tratar_string(token)
    valor_token = array[3]
    return valor_token

def erro(linha):
    print(f"erro sintatico na linha {linha}")


def declarar_variaveis(lista_tokens):
    cont = 1
    proximo_2 = None
    for aux in lista_tokens:
        int_aux = int(aux)

        if int_aux == 100:

            try:
                proximo = int(lista_tokens[cont])
            except:
                return 0

            if proximo == 700:

                try:
                    proximo_2 = int(lista_tokens[cont + 1])
                except:
                    return 0

                if proximo_2 != 800:
                    return 1
                else:
                    return 0

        cont = cont + 1

def tratar_linha(lista_tokens,tamanho_lista):

    aux_anterior = None
    erro = 0
    cont = 0
    
    #definindo regras
    for aux in lista_tokens:

        int_aux = int(aux)

        #regra: se houver iniciadores eles serão os primeiros da linha      
        if int_aux == 100:
            if  aux_anterior != None:
                if aux_anterior != 500:
                    erro = 1
        #regra: variaveis não podem ter palavras reservadas (200), variaveis (700), valores (600) como anteriores,  ;
        if int_aux == 700:
            if aux_anterior == 200 or aux_anterior == 700 or aux_anterior == 600 or aux_anterior == 500:
                erro = 1
        
        #regra: palavras reservadas não podem ter basicamente nada antes deles
        if int_aux == 200 and aux_anterior != None:
            erro = 1


        # ; não pode ser declarado depois de delimitadores iniciadores
        if int_aux == 500 and aux_anterior == 400:
            erro = 1

        # ; não pode ser declarado depois de operadores (300), atribuidor (800), comparadores (350), palavras reservadas (200)
        if int_aux == 500:
            if aux_anterior == 300 or aux_anterior == 800 or aux_anterior == 350 or aux_anterior == 200:
               erro = 1
        
        #operadores so podem ser declarado depois de variaveis ou valores
        if int_aux == 300:
            if aux_anterior != 700 and aux_anterior != 600:
                erro = 1

        # comparadores so podem ser declarados depois de variaveis ou valores
        if int_aux == 350:
            if aux_anterior != 700 and aux_anterior != 600:
                erro = 1
        # regra deliminitadores iniciais podem ser declarados depois de variaveis, valores, palavras reservadas
        if int_aux == 400:
            if aux_anterior != 700 and aux_anterior != 600 and aux_anterior != 200:
                erro = 1

        # regra deliminitadores finais podem ser declarados depois de variaveis, valores
        if int_aux == 450:
            if aux_anterior != 700 and aux_anterior != 600:
                erro = 1
        
        # regra atribuidores podem ser declarados depois de variaveis, valores
        if int_aux == 800:
            if aux_anterior != 700 and aux_anterior != 600:
                erro = 1
        
        # regra valores podem ser declarados depois de atribuidores ou delimitadores iniciais
        if int_aux == 600:
            if aux_anterior != 800 and aux_anterior != 400 and aux_anterior != 300 and aux_anterior != 350:
                erro = 1

        aux_anterior = int(aux)   
    return erro 
        


def validador_linha(tokens_values,tamanho_lista):
    #casos especiais
    verificacao = 0
    verificacao = declarar_variaveis(tokens_values)

    if verificacao == 1:
        return 1

    else:
        print("verif")
        verificacao = tratar_linha(tokens_values,tamanho_lista)

    if verificacao == 1:
        return 1
            



def estrutura_linguagem(linha):

    tokens_values = []
    for token in linha:
        tokens_values.append(token_cod(token))
    
    tamanho_lista = len(tokens_values)
    validador = validador_linha(tokens_values,tamanho_lista)

    if validador == 1:
        linha_tokens = token_linha(token) 
        print(f"erro linha {linha_tokens}")