import os
from unicodedata import normalize
import nltk
import string
s = nltk.stem.RSLPStemmer()

def getItem(item):
    return item[1]

def ngrams(n,texto):
    '''n -> número
       texto -> String'''
    teste = []
    
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

#Abrindo aquivos
for arquivo in os.listdir('racismo'):
    arquivoR = open("racismo/"+arquivo, 'r',encoding='utf8').read().lower()
for arquivo in os.listdir('semRacismo'):
    arquivoSR = open("semRacismo/"+arquivo, 'r',encoding='utf8').read().lower()
artquivoTodasClasses = arquivoR + " " + arquivoSR

arquivo_normalizado = normalize('NFKD', artquivoTodasClasses).encode('utf8', 'ignore').decode('utf8')
tokens = nltk.word_tokenize(arquivo_normalizado)
radicais = []
arquivo_filtrado = []
for palavra in tokens:
    if not (palavra in nltk.corpus.stopwords.words('portuguese') or palavra in string.punctuation or palavra.isdigit()
            or len(palavra)<3 or palavra in "não pra porque ... http vascodagama"):
        arquivo_filtrado.append(palavra)

for word in arquivo_filtrado:
    radicais.append(s.stem(word))

    n = 3

    textoN_Grams = []

    for index in range(len(radicais)):

        textoTemp = ""
        if (index + n - 1) < len(radicais):
            for index in range(index, index + n):
                textoTemp += radicais[index] + " "

            textoN_Grams += [textoTemp.strip()]

    radicais = textoN_Grams

palavrasRelevantesClasse = []

frequencia_dic = nltk.FreqDist(radicais)
frequencia_lista = []
for i in frequencia_dic:
    frequencia_lista.append((i,frequencia_dic[i]))
frequencia_lista_ordenada = sorted(frequencia_lista,key=getItem,reverse=True)
print(frequencia_lista_ordenada)

semFrequenciaOrdenada = []
for i in frequencia_lista_ordenada:
    semFrequenciaOrdenada.append(i[0])

#Todas as palavras de todas as classes
for doc in os.listdir("red//corpus"):
    for doc2 in os.listdir("red/" + doc):
        arquivo2 = open("red//" + doc + "//" + doc2, 'r',encoding='utf8').read().lower()
        arquivo_normalizado2 = normalize('NFKD', arquivo2).encode('utf8', 'ignore').decode('utf8')
        tokens2 = nltk.word_tokenize(arquivo_normalizado2)
        radicais2 = []
        arquivo_filtrado2 = []
        for palavra2 in tokens2:
            if not (palavra2 in nltk.corpus.stopwords.words('portuguese') or palavra2 in string.punctuation or palavra2.isdigit() or len(palavra2) < 3 or palavra2 in "não pra porque ... http vascodagama"):
                arquivo_filtrado2.append(palavra2)
        for word2 in arquivo_filtrado2:
            radicais2.append(s.stem(word2))
        aux = 0
    #print(radicais2)
        for w in semFrequenciaOrdenada:
            if w in radicais2:
                if not (w in palavrasRelevantesClasse):
                    palavrasRelevantesClasse.append(w)
                aux = aux + 1
            if aux >= 2: #Quantidade de palavras por documento
                break;
print(palavrasRelevantesClasse)

dic1Preconceito = open("dic//ListaP.txt", 'r', encoding='utf8').read().lower()
dic2Preconceito = open("dic//dicRacista", 'r', encoding='utf8').read().lower()
dic2Neutro = open("dic//dicNeutro", 'r', encoding='utf8').read().lower()
dicFinal = dic1Preconceito + " " + dic2Preconceito + " " + dic2Neutro

arquivo_normalizadodic = normalize('NFKD', dicFinal).encode('utf8', 'ignore').decode('utf8')
tokensdic = nltk.word_tokenize(arquivo_normalizadodic)
radicaisdic = []
arquivo_filtradodic = []
for palavraDic in tokensdic:
    if not (palavraDic in nltk.corpus.stopwords.words('portuguese') or palavraDic in string.punctuation or palavraDic.isdigit() or len(palavraDic) < 3 or palavraDic in "não pra porque ... http vascodagama"):
        arquivo_filtradodic.append(palavraDic)
for wordDic in arquivo_filtradodic:
    radicaisdic.append(s.stem(wordDic))

#Incluindo o dicionario
for doc in os.listdir("red//corpus"):
    for doc2 in os.listdir("red//" + doc):
        arquivo3 = open("red//" + doc + "//" + doc2, 'r',encoding='utf8').read().lower()
        
        arquivoFinal = ""
        radicais3 = []
        arquivo_filtrado3 = []
        arquivo_normalizado3 = normalize('NFKD', arquivo3).encode('utf8', 'ignore').decode('utf8')

        tokens3 = nltk.word_tokenize(arquivo_normalizado3)
        for palavra3 in tokens3:
            if not (palavra3 in nltk.corpus.stopwords.words('portuguese') or palavra3 in string.punctuation or palavra3.isdigit() or len(palavra3) < 3 or palavra3 in "não pra porque ... http vascodagama"):
                arquivo_filtrado3.append(palavra3)
        for word3 in arquivo_filtrado3:
            radicais3.append(s.stem(word3))

        for word4 in radicais3:
            if (word4 in palavrasRelevantesClasse) or (word4 in radicaisdic):
                arquivoFinal = arquivoFinal + " " + word4

        #--------------------------------------------------------------
        saida = open("red//" + doc + "N1//" + doc2, 'w',errors='ignore')
        for word in ngrams(1,char_ngrams(4,arquivo_normalizado3)):
            saida.write(word+' ')
        saida.close()
        saida1 = open("red//" + doc + "N2//" + doc2, 'w',errors='ignore')
        for word in ngrams(2,char_ngrams(4,arquivo_normalizado3)):
            saida1.write(word+' ')
        saida1.close()
        #--------------------------------------------------------------
        print(arquivoFinal)
        
        #Salvando arquivo
        f = open("red//" + doc + "MFD2//" + doc2, 'w',errors='ignore')

        f.write(arquivoFinal) #Escreven o conteúdo do artigo
        print(f.name)
        f.close()
