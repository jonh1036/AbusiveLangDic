#def n_grams(self, twittes, n_grams):
teste = ["cbie", "informática", "educação", "tecnologia", "teste", "mais", "novo"]

n = 2

def ngrams(n,texto):
    '''n -> número
       texto -> String'''
    teste = [texto]
    textoN_Grams = []

    for index in range(len(teste)):

        textoTemp = ""
        if (index + n-1) < len(teste):
            for index  in range(index, index + n):
                textoTemp += teste[index]  + " "

            textoN_Grams += [textoTemp.strip()]

    return textoN_Grams
