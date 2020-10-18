#def n_grams(self, twittes, n_grams):
teste = ["cbie informática educação tecnologia teste mais novo"]

n = 2
def ngrams(n,texto):
    '''n -> número
       texto -> String'''
    
    if(type(texto)==str):
        teste = [texto]
        
    textoN_Grams = []

    for index in range(len(teste)):

        textoTemp = ""
        if (index + n-1) < len(teste):
            for index  in range(index, index + n):
                textoTemp += teste[index]  + " "

            textoN_Grams += [textoTemp.strip()]
    return textoN_Grams

def char_ngrams(n,texto):
    '''n -> número
       texto -> String'''
    teste = [texto]
    textoN_Grams = []

    for item in teste:
        for index in range(len(item)):

            textoTemp = ""
            if (index + n-1) < len(item):
                textoN_Grams += [item[index:index+n]]

    return textoN_Grams

ngrams(2,char_ngrams(4,"cbie informática educação tecnologia teste mais novo"))
