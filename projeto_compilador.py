import palavras_reservadas
import analise_lexica
import analise_sintatica


if __name__=="__main__":

    arquivo_entrada = open(r"testes\teste1.txt","r")
    tokens = []
    contagem_linha = 0
    for line in arquivo_entrada:
        contagem_linha = contagem_linha + 1
        tokens.append( analise_lexica.identificar_palavra(line,contagem_linha))

    for aux in tokens:
        analise_sintatica.estrutura_linguagem(aux)
    
