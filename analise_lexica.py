from lib2to3.pgen2 import token
import palavras_reservadas

'''
ideia da separação em tokens

100 = iniciadores variaveis

150 - iniciadores 

200 = palavras reservadas

300 = operadoes

350 = comparadores

400 = delimitadores iniciais

450 = delimitadores final

500 = final da linha

600 = valores inteiros

700 = variaveis

800 = atribuidor

token = TKN +_+ codigo +_+ definição + _ + numero da lina + _ + palavra

exemplo: TKN_100_var_10_valorEncontrado


'''

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
    array_final = string_array.split()
    print(array_final)
    return array_final

def tratar_string(valor):
    array = separador_palavras(valor)
    return array

def identificar_palavra(linha,num_linha):
    linha_tratada = tratar_string(linha)
    tokens = []
    for aux in linha_tratada:
        if aux == "\n":
            tokens.append("\n")
        else:
            aux = aux.strip('\n')
            if aux in palavras_reservadas.P_R_iniciadores_variaveis:
                tokens.append("TKN_"+"100_"+"inic-var_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_iniciadores:
                tokens.append("TKN_"+"150_"+"inic_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_reserved_words:
                tokens.append("TKN_"+"200_"+"reser_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_operadores:
                tokens.append("TKN_"+"300_"+"opera_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_comparadores:
                tokens.append("TKN_"+"350_"+"compa_"+str(num_linha)+"_"+str(aux))
            
            elif aux in palavras_reservadas.P_R_comparadores_351:
                tokens.append("TKN_"+"351_"+"compa351_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_comparadores_352:
                tokens.append("TKN_"+"352_"+"compa352_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_delimitadores_iniciadores:
                tokens.append("TKN_"+"400_"+"delimi-inic_"+str(num_linha)+"_"+str(aux))
            
            elif aux in palavras_reservadas.P_R_delimitadores_finalizadores:
                tokens.append("TKN_"+"450_"+"delimi-final_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_final_linha:
                tokens.append("TKN_"+"500_"+"final_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_return:
                tokens.append("TKN_"+"505_"+"return_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_igual:
                tokens.append("TKN_"+"800_"+"atribui_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_simbolos:
                tokens.append("TKN_"+"50_"+"simbolos_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_aspas:
                tokens.append("TKN_"+"25_"+"aspas_"+str(num_linha)+"_"+str(aux))

            elif aux in palavras_reservadas.P_R_externo:
                tokens.append("TKN_"+"01_"+"includes_"+str(num_linha)+"_"+str(aux))

            else:
                if aux.isdigit():
                    tokens.append("TKN_"+"600_"+"valor_"+str(num_linha)+"_"+str(aux))
                else:
                    tokens.append("TKN_"+"700_"+"var_"+str(num_linha)+"_"+str(aux))
        
    return tokens
        
        

        
    
