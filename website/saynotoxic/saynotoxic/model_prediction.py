from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.layers import Bidirectional, GlobalMaxPool1D
from keras.models import Model
from keras import initializers, regularizers, constraints, optimizers, layers
import codecs
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import re
import sys
import warnings
import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True
from tensorflow.keras.models import load_model
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore")



'''##########[!] Functions reused in Django###############'''
def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)
    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase
def cleanPunc(sentence): #function to clean the word of any punctuation or special characters
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    cleaned = cleaned.strip()
    cleaned = cleaned.replace("\n"," ")
    return cleaned
def clear_sentance(sentance):
    sentance= re.sub(r"http\S+", "", sentance)
    sentance = BeautifulSoup(sentance, 'lxml').get_text()
    sentance = decontracted(sentance)
    sentance = cleanPunc(sentance)
    sentance = re.sub("\S*\d\S*", "", sentance).strip()
    sentance = re.sub('[^A-Za-z]+', ' ', sentance)
    #sentance = stemming(sentance)
    # https://gist.github.com/sebleier/554280
    #https://towardsdatascience.com/journey-to-the-center-of-multi-label-classification-384c40229bff
    stop_words = set(stopwords.words('english'))
    stop_words.update(['zero','one','two','three','four','five','six','seven','eight','nine','ten','may','also','across','among','beside','however','yet','within'])
    sentance = ' '.join(e.lower() for e in sentance.split() if e.lower() not in  stopwords.words('english'))
    return sentance.strip()
def tokenize(sentance):
    import pickle
    MAX_SEQUENCE_LENGTH = 400
    #MAX_NB_WORDS = 50000
    with open('tokenizer.pickle', 'rb') as handle:
                    tokenizer = pickle.load(handle)
    test_sequences = tokenizer.texts_to_sequences([sentance])
    test_data = pad_sequences(test_sequences, maxlen=MAX_SEQUENCE_LENGTH)
    return test_data
def model_predict(test_data):
    model=load_model('LSTM_toxic_prediction_model.h5')
    prediction=model.predict(test_data)
    return prediction
def get_prediction(sentance):
    clear_text=clear_sentance(sentance)
    test_data=tokenize(clear_text)
    predicted_array=model_predict(test_data)
    #'identity_hate', 'insult', 'obscene', 'severe_toxic', 'threat', 'toxic'
    predicted_values={'Hate':round(predicted_array[0][0]),'Insult':round(predicted_array[0][1]), 'Obscene':round(predicted_array[0][2]), 'Severe Toxic':round(predicted_array[0][3]), 'Threat':round(predicted_array[0][4]), 'Toxic':round(predicted_array[0][5])}
    #print(clear_text)
    #print(test_data)
    #print(predicted_array)
    result=''
    for key in predicted_values:
        #print(key)
        #print(predicted_values[key])
        if(predicted_values[key]==1.0):
            result='Toxic text'
    if result=='':
        result='Non Toxic Text'
    return result
