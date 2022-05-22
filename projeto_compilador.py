import palavras_reservadas
import analise_lexica
import analise_sintatica
import analise_semantica


if __name__=="__main__":
    #lendo arquivo
    arquivo_entrada = open(r"testes\teste1.txt","r")
    tokens = []
    contagem_linha = 0
    #iniciando analise lexica
    for line in arquivo_entrada:
        contagem_linha = contagem_linha + 1
        tokens.append( analise_lexica.identificar_palavra(line,contagem_linha))
    #print(tokens)


    #validando quantidade de validadores
    erro_validadores = 0
    linha = None
    erro_validadores, linha = analise_sintatica.tratar_validadores(tokens)


    if erro_validadores == 1:
        print(f"erro 400 na linha: {linha}")
    else:
        for aux in tokens:
            erro_validadores = analise_sintatica.estrutura_linguagem(aux)

    '''
    if erro_validadores != 1:
        #iniciando analise semantica
        resultado = analise_semantica.orquestrador_semantico(tokens)
    '''