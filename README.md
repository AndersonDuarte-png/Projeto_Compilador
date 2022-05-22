# Projeto_Compilador
criando um compilador para trabalhos facultativos

Primeiro passo é definir as palavras reservadas da linguagem a ser analisada:
nesse passo é importate segregar o maximo possivel as palavras que serão reconhecidas pelo compilador e sua funções.

Na parte lexica o foco é pegar ler a linha de comando inserida pelo usuario e comparar com as palavras reservadas que foram definidas no sistema, e após isso gerar tokens representando os comandos inseridos pelo seu usuario.

Na parte sintatico o objetivo é verificar se os tokens criados estão estruturamente corretos, então um sistemas de regras é feito para avaliar a ordem em que os tokens estão estruturados.