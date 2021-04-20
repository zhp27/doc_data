# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 20:44:57 2021

@author: raha_
"""

from summa import summarizer
import spacy
import math
nlp = spacy.load("en_core_web_sm")

#return the summarized text
def summ(input_sent, ratio):
        
    LT=1000
    while LT>200:
        summarized_text = summarizer.summarize(
            input_sent, ratio=ratio, language="english", split=True, scores=True
        )
        T=str(summarized_text).split()
        LT=len(T)
    return summarized_text

#define an adaptive summerization ratio
def calc_ratio(input_sent):
    L=len(input_sent)
    ratio=math.ceil(20000/L)/100
    return ratio

#find main keywords    
def keywords(summarizedText):
    doc = nlp(str(summarizedText))
    title=[]
    for token in doc.ents:
        
        for x in token:        
            if x.dep_=='nsubj' or x.dep_=='nsubjpass':
                title.append(str(token))
                break
            
        for x in token:
            if x.dep_=='pobj':
                title.append(str(token))
                break
            
    Utitle=list(set(title))
    print(Utitle)
#read files
fileObject = open("b.txt", "r")
inputSent = fileObject.read() 
ratio=calc_ratio(inputSent)
summarizedText=summ(inputSent,ratio)
#change ratio step by step for small docs
while summarizedText==[]:
    ratio+=0.1
    summarizedText=summ(inputSent,ratio)
    
for sentence, score in summarizedText:
    print(sentence)

keywords(summarizedText)
