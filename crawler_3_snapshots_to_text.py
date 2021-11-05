import crawler_consts as cc
import re
import crawler_2_get_snapshots as c2
from sklearn.feature_extraction.text import CountVectorizer
import pdfkit
import nltk
from nltk import word_tokenize
import time
from selenium import webdriver
import cv2
from PIL import Image
import pytesseract
import numpy as np

occurrence = 4



def getK(fname):

    g = open(fname + ".txt", "r")
    for line in g:
        k = int(line)
        break
    g.close()

    return k


def resultText(fname):

    k = getK(fname)

    pattern = r'[0-9]'
    final_text = []
    for i in range(0,k):

        text1 = pytesseract.image_to_string(Image.open(fname + "_" + str(i) + ".png"))
        text = re.sub(pattern, '', text1)
        querywords = text.split()
        resultwords  = [word for word in querywords if word.lower() not in cc.stopwords]

        for words in resultwords:
            final_text.append(words)

    result = ' '.join(final_text)
    
    return result



def getWordsWithCounts(result):

    data = []
    data.append(result)

    vectorizer = CountVectorizer()
    # vectorizer = CountVectorizer(ngram_range=(1,4))

    X = vectorizer.fit_transform(data)

    return vectorizer.get_feature_names(), X.toarray()



def tokenizeText(result):

    feat_names, feat_counts = getWordsWithCounts(result)
    
    result1 = ' '.join(feat_names)
    tokens = word_tokenize(result1)
    tagged_tokens = nltk.pos_tag(tokens)
    
    return feat_names,feat_counts,tagged_tokens



def writeResults(fname, feat_names, feat_counts, tagged_tokens):

    N = len(feat_names)
    print(N)

    h = open(fname + "_word_count.txt","w")
    for i in range(0,N):
        h.write(feat_names[i] + "\t" + tagged_tokens[i][1] + "\t" + str(feat_counts[0][i]) + "\n")
    h.close()
    
    return


def main():

    f = open("data/final_searched_links.txt","r")
    
    for link in f:
    
        if link.find("linkedin.com/in") >= 0:
        
            print(link)
            fname = c2.findFileName(link)

            result = resultText(fname)
            print(result)
            
            tokenizeText(result)
        
            feat_names, feat_counts, tagged_tokens = tokenizeText(result)

            writeResults(fname, feat_names, feat_counts, tagged_tokens)
            
    f.close()
    
    return


if __name__ == "__main__":
    main()







