P_R_reserved_words =(
                "asm",
                "double",
                "new",
                "switch",
                "auto",
                "else",
                "operator",
                "template",
                "break",
                "enum",
                "private",
                "this",
                "case",
                "extern",
                "protected",
                "throw",
                "catch",
                "float",
                "public",
                "try",
                "char",
                "for",
                "register",
                "typedef",
                "class",
                "friend",
                "union",
                "const",
                "goto",
                "short",
                "unsigned",
                "continue",
                "if",
                "signed",
                "virtual",
                "default",
                "inline",
                "sizeof",
                "void",
                "delete",
                "int",
                "static",
                "volatile",
                "do",
                "long",
                "struct",
                "while",
                "import",
                "include"
                )

P_R_operadores = ( "+", "-", "/", "*","+=","-=","*=")

P_R_comparadores =("==",">=","<=","&&","||","!=")

P_R_linhas_validacao =["+","-", "/", "*","+=","-=","*=","(","{","[",")","}","]",";",":","=","#","<",">"]

P_R_delimitadores_iniciadores = ("(","{","[","\"\"")

P_R_delimitadores_finalizadores =(")","}","]","\"\"")

P_R_comentario = ("//","/*","*/","#")

P_R_iniciadores = ("for","while","if","else","elif")

P_R_final_linha = (";",":")

P_R_igual = ("=","=")

P_R_iniciadores_variaveis =("int","float","string","char")

P_R_seta_2=(">",">")

P_R_seta_1= ("<","<")

P_R_simbolos=("#","#")

P_R_aspas=('\"\"','\"\"')

P_R_return=('return','return')