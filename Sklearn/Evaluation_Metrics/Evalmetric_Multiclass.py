# ----------------Import the needed packages-------------
import numpy as np
import pandas as pd
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import jaccard_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import multilabel_confusion_matrix

actual_filename=pd.read_csv('data_actual.csv')
predicted_filename=pd.read_csv('data_predicted.csv')




actual_filename=list(actual_filename['Air_quality'])
predicted_filename=list(predicted_filename['Air_quality'])


'''
Write a function that returns the actual labels and predicted labels as a list from the corresponding input data given.

Sample File names 

* Actual label File name : `data_actual.csv`
* Predicted label File name : `data_predicted.csv`
* Target column name : `Air_quality`

'''

def actual_predicted_list(actual_filename,predicted_filename):
    
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output:
    data_actual_values: list - Actual class labels in form of list
    data_predicted_values: list -predicted class labels in form of list
    '''
    
    actual_filename=pd.read_csv(actual_filename)
    predicted_filename=pd.read_csv(predicted_filename)
    
    data_actual_values=list(actual_filename['Air_quality'])
    data_predicted_values=list(predicted_filename['Air_quality'])
    return data_actual_values, data_predicted_values
    

'''
Question 1  

Write a function that returns Confusion Matrix using lists returned from 'actual_predicted_list' function

* Sort the labels in descending order
'''

def conf_matrix( actual_filename,predicted_filename):
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output: cm: Matrix - Confusion matrix 
    '''
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    cm=confusion_matrix(data_actual_values,data_predicted_values,labels=['Good', 'Moderate', 'Poor', 'Satisfactory', 'Severe', 'Very Poor'])
    return cm

'''    
Question 2 

Write a function that returns the dictionary storing the number of Satisfactory samples being classified as Good, Moderate,Poor, Satisfactory,Severe,Very Poor.

* Use the list returned from 'actual_predicted_list' function.
* Keys are the labels
* Values are the number of Satisfactory samples classified as the corresponding key.
* Return the dictionary with the keys ordered in ascending order

'''

def satisfactory_dictionary(actual_filename,predicted_filename):
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output:dict1: Dictionary 
    '''
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    df = pd.DataFrame(list(zip(data_actual_values, data_predicted_values)), columns =['actual', 'predicted'])
    df=df[df['actual']=='Satisfactory']
    dict1=df['predicted'].value_counts().sort_index().to_dict()
    return dict1


'''
Question 3
Extract True negative, False Positive,false negative and true positive values from the confusion matrix of class label "Poor" (2*2 matrix) and return them as a tuple in order of True negative, False Positive,false negative and true positive.

* Hint : Use multilabel_confusion_matrix
* Use the list returned from 'actual_predicted_list' function.   
 
'''

def extract_metrics_cm(actual_filename,predicted_filename):
    
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output:
    tuple_val: tuple - Tuple containing the values of True negative, False Positive,false negative and true postive
    '''
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    tuple_val=multilabel_confusion_matrix(data_actual_values, data_predicted_values,labels=["Poor"])
    tuple_val=tuple_val.tolist()
    tuple_val=tuple([j for i in tuple_val[0] for j in i])
    #tuple_val=_
    return tuple_val

'''
Question 4
Calculate the sensitivity and specificity from the confusion matrix of class label "Moderate" (2*2 matrix)

* Hint : Use multi-label confusion matrix
* Use the list returned from `actual_predicted_list` function.
* Find the sensitivity and specificity value from the matrix using the following formulas and return the same
* Round off to two decimal places.

Formulas:

sensitivity = TP/(FN + TP)

specificity = TN/(TN + FP)
'''


def sens_spec(actual_filename,predicted_filename):
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output: sensitivity,specificity 
    '''
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    tuple_val=multilabel_confusion_matrix(data_actual_values, data_predicted_values,labels=["Moderate"])
    a=tuple_val.tolist()     
    sensitivity=round(a[0][1][1]/(a[0][1][1]+a[0][1][0]),2)
    specificity=round(a[0][0][0]/(a[0][0][0]+a[0][0][1]),2)
    return sensitivity,specificity

'''
Question 5

F1- Score

* Return the `Macro` F1-Score calculated with the lists returned from 'actual_predicted_list' function.

* Round off to 2 decimal places
'''
def scorefunc(actual_filename,predicted_filename):
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output: f1_score_val: float 
    '''
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    
    f1_score_val=round(f1_score(data_actual_values,data_predicted_values,average='macro'),2)
    return f1_score_val

    
'''
Question 6

Precison- Score

* Find the `micro` Precision-Score with the lists returned from `actual_predicted_list` function.

* Round off to 2 decimal places

'''

def precisionfunc(actual_filename,predicted_filename):
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output: precision_val: float 
    '''
    
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    precision_val=round(precision_score(data_actual_values,data_predicted_values,average='micro'),2)
    return precision_val
    

'''

Question 7

Recall- Score

* Find `weighted` Recall-Score with the lists returned from `actual_predicted_list` function.

* Round off to 2 decimal places    

'''

def recallfunc(actual_filename,predicted_filename):
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output: recall_val: float 
    '''
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    recall_val=round(recall_score(data_actual_values,data_predicted_values,average='weighted'),2)
    return recall_val

'''
Question 8

Jaccard Score

* Find the Jaccard score for each class using the lists returned from `actual_predicted_list` function.
* Store the scores in a list and return the same in the sorted order (ascending)
* Round off the values to 2 decimal places.
'''

def jaccardfunc(actual_filename,predicted_filename):
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output:jaccard_list :list - Jaccard scores of each class in ascending order
    '''
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    jaccard_list=jaccard_score(data_actual_values,data_predicted_values,average=None).tolist()
    jaccard_list=sorted([round(i,2) for i in jaccard_list])
    return jaccard_list

'''
Question 9

Balanced Accuracy Score

* Return the Balanced Accuracy score using the lists from  `actual_predicted_list` function.

* Round off the values to 2 decimal places.

'''
def accuracyfunc(actual_filename,predicted_filename):
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output: bal_accuracy: float 
    '''
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    bal_accuracy=round(balanced_accuracy_score(data_actual_values,data_predicted_values),2)
    return bal_accuracy

'''
Question 10

Find the Matthews Correlation Coefficient for multiclass

* Use the lists returned from returned from `actual_predicted_list` function.
* Round off the value to 2 decimal places
'''
def matthewfunc(actual_filename,predicted_filename):
    
    '''
    Input:
    actual_filename: String - CSV file name containing the records with actual class labels
    predicted_filename: String -CSV file name containing the same records with predicted class labels 
    
    Output: matthew_coeff: float 
    '''
    data_actual_values, data_predicted_values = actual_predicted_list(actual_filename,predicted_filename)
    matthews_coeff=round(matthews_corrcoef(data_actual_values,data_predicted_values),2)
    return matthews_coeff

if __name__ == "__main__":
    
    actual_fname = input()
    
    predicted_fname = input()
    
    print(conf_matrix(actual_fname,predicted_fname))
    
    print(satisfactory_dictionary(actual_fname,predicted_fname))
    
    print(extract_metrics_cm(actual_fname,predicted_fname))
    
    print(sens_spec(actual_fname,predicted_fname))
    
    print(scorefunc(actual_fname,predicted_fname))
    
    print(precisionfunc(actual_fname,predicted_fname))
    
    print(recallfunc(actual_fname,predicted_fname))
    
    print(jaccardfunc(actual_fname,predicted_fname))
    
    print(accuracyfunc(actual_fname,predicted_fname))
    
    print(matthewfunc(actual_fname,predicted_fname))
