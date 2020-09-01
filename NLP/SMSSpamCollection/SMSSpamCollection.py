# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 09:52:17 2020
"""

#Data Loading
import pandas as pd
import csv
#Data Loading
messages = [line.rstrip() for line in open('SMSSpamCollection.csv')]
print(len(messages))


#Appending column headers
messages = pd.read_csv('SMSSpamCollection.csv', sep='\t', quoting=csv.QUOTE_NONE,names=["label", "message"])

#Data Analysis
data_size=messages.shape
print(data_size)

messages_col_names=list(messages.columns)
print(messages_col_names)

messages.groupby('label').describe()

messages.head(3)

#Target Identification
message_target=messages['label'] 
message_target

#import nltk
#nltk.download('all')

#Tokenization
from nltk.tokenize import word_tokenize

def split_tokens(message):
  message=message.lower()
  word_tokens =word_tokenize(message)
  return word_tokens

messages['tokenized_message'] = messages.apply(lambda row: split_tokens(row['message']),axis=1)


#Lemmatization
from nltk.stem.wordnet import WordNetLemmatizer

def split_into_lemmas(message):
    lemma = []
    lemmatizer = WordNetLemmatizer()
    for word in message:
        a=lemmatizer.lemmatize(word)
        lemma.append(a)
    return lemma

messages['lemmatized_message'] = messages.apply(lambda row: split_into_lemmas(row['tokenized_message']),axis=1)
#messages['lemmatized_message'] = messages['tokenized_message'].apply(lambda x: split_into_lemmas(x)) Other simple methods for individual rows


print('Tokenized message:',messages['tokenized_message'][11])
print('Lemmatized message:',messages['lemmatized_message'][11])

#Stop Word Removal
from nltk.corpus import stopwords
def stopword_removal(message):
    stop_words = set(stopwords.words('english'))
    filtered_sentence = []
    filtered_sentence = ' '.join([word for word in message if word not in stop_words])
    return filtered_sentence

messages['preprocessed_message'] = messages.apply(lambda row: stopword_removal(row['lemmatized_message']),axis=1)

Training_data=pd.Series(list(messages['preprocessed_message']))
Training_label=pd.Series(list(messages['label']))

#Bag Of Words(BOW)
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

tf_vectorizer = CountVectorizer(ngram_range=(1, 2),min_df = (1/len(Training_label)), max_df = 0.7)

Total_Dictionary_TDM = tf_vectorizer.fit(Training_data)
message_data_TDM = Total_Dictionary_TDM.transform(Training_data)

#Term Frequency Inverse Document Frequency (TFIDF
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2),min_df = (1/len(Training_label)), max_df = 0.7)
Total_Dictionary_TFIDF = tfidf_vectorizer.fit(Training_data)
message_data_TFIDF = Total_Dictionary_TFIDF.transform(Training_data)


#Train and Test Data.

from sklearn.model_selection import train_test_split #Splitting the data for training and testing

train_data,test_data, train_label, test_label = train_test_split(message_data_TDM, Training_label, test_size=.1)

#Decision Tree Classification
from sklearn.tree import DecisionTreeClassifier #Creating a decision classifier model
classifier=DecisionTreeClassifier() #Model training 

classifier = classifier.fit(train_data, train_label) #After being fitted, the model can then be used to predict the output.

message_predicted_target = classifier.predict(test_data)

score = classifier.score(test_data, test_label)
print('Decision Tree Classifier : ',score)

'''
It is one of the commonly used classification techniques for performing binary as well as multi-class classification.
The decision tree model predicts the class/target by learning simple decision rules from the features of the data.

'''

#Stochastic Gradient Descent Classifier
seed=7
from sklearn.linear_model import SGDClassifier
classifier =  SGDClassifier(loss='modified_huber', shuffle=True,random_state=seed)
classifier = classifier.fit(train_data, train_label)
score = classifier.score(test_data, test_label)
print('SGD classifier : ',score)

'''
It is used for large scale learning
It supports different loss functions & penalties for classification
'''

#Support Vector Machine
from sklearn.svm import SVC
classifier = SVC(kernel="linear", C=0.025,random_state=seed)
classifier = classifier.fit(train_data, train_label)
score = classifier.score(test_data, test_label)
print('SVM Classifier : ',score)

'''
Support Vector Machine(SVM) is effective in high-dimensional spaces.
It is effective in cases where the number of dimensions is greater than the number of samples.
It works well with a clear margin of separation.
'''

#Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=10,random_state=seed)
classifier = classifier.fit(train_data, train_label)
score = classifier.score(test_data, test_label)
print('Random Forest Classifier : ',score)

'''
Controls over fitting
Here, a random forest fits a number of decision tree classifiers on various sub-samples of the dataset and uses 
averaging to improve the predictive accuracy.
'''

#Model Tuning
classifier = RandomForestClassifier(max_depth=5, n_estimators=15, max_features=60,random_state=seed)
classifier = classifier.fit(train_data, train_label)
score=classifier.score(test_data, test_label)
print('Random Forest classification after model tuning',score)

#Partitioning the Data
'''
Split the data to train set, validation set and test set.
Training Set: The data used to train the classifier.
Validation Set: The data used to tune the classifier model parameters i.e.,
 to understand how well the model has been trained (a part of training data).
Testing Set: The data used to evaluate the performance of the classifier (unseen data by the classifier).
'''

#Cross Validation

'''
Cross validation is a model validation technique to evaluate the performance of a model on unseen data (validation set).
It is a better estimate to evaluate testing accuracy than training accuracy on unseen data.
'''

#Stratified Shuffle Split

seed=7
from sklearn.model_selection import StratifiedShuffleSplit
###cross validation with 10% sample size
n_splits=5
sss = StratifiedShuffleSplit(n_splits=n_splits,test_size=0.1, random_state=seed)
sss.get_n_splits(message_data_TDM,Training_label)
print(sss)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm
classifiers = [
    DecisionTreeClassifier(),
    SGDClassifier(loss='modified_huber', shuffle=True),
    SVC(kernel="linear", C=0.025),
    KNeighborsClassifier(),
    OneVsRestClassifier(svm.LinearSVC()),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=10),
   ]

for clf in classifiers:
    score=0
    for train_index, test_index in sss.split(message_data_TDM,Training_label):
       X_train, X_test = message_data_TDM [train_index], message_data_TDM [test_index]
       y_train, y_test = Training_label[train_index], Training_label[test_index]
       clf.fit(X_train, y_train)
       score=score+clf.score(X_test, y_test)
    print(score/n_splits)
    
#Classification Accuracy
    
from sklearn.metrics import accuracy_score
print('Accuracy Score',accuracy_score(test_label,message_predicted_target))  
classifier = classifier.fit(train_data, train_label)
score=classifier.score(test_data, test_label)
test_label.value_counts()

#Confusion Matrix
from sklearn.metrics import confusion_matrix

print('Confusion Matrix',confusion_matrix(test_label,message_predicted_target))

#Classification Report

from sklearn.metrics import classification_report
target_names = ['spam', 'ham']
print(classification_report(test_label, message_predicted_target, target_names=target_names))