# -*- coding: utf-8 -*-
#Importing re module
import re

text = 'The Monk1 named Baba is one of the 100 Monks in Mylapore Temple'

# Seraching certain string in a text
if re.search('Murali', text):
    print('There is a Monk')
    
# findall returns all the matches

all_Monks=re.findall('Monk',text)
print(all_Monks)

# . is used to find any one character or space
all_Monks=re.findall('Monk.',text)
print(all_Monks)


#The re.split method splits the string where there is a match and returns a list of strings where the splits have occurred.
pattern = '\d+'
result = re.split(pattern, text) 
print(result)

#iterator of matching objects
for i in re.finditer('Monk.',text):
    #span returns the tuple
    locTuple=i.span()
    print(locTuple)
    print(text[locTuple[0]:locTuple[1]])
    
#Square brackets will include any of the characters between them-Casesensitive
text1='Man man Can can Gan gan Van van'
words=re.findall('[MgCv]an',text1)

#characters in range
words1=re.findall('[d-mD-M]an',text1)

#any characters other than this the characters between(^)
words2=re.findall('[^d-mD-M]an',text1)

#compile pattern and substitute with alternate words
regex=re.compile('[MCG]an')

Words_replaced=regex.sub('Mad',text1)

re.sub('[M]\w+','',text)

RandomWords="\\text duplicates Backslash has to be found"

print(re.search("\\text",RandomWords))
print(re.search("\\\\text",RandomWords)) # \\ add excess backslash
print(re.search(r"\\text",RandomWords)) # r-raw

# . represent any character \. represents periob(.)
text2 = 'U.S.A, U.A.E'
Words3=re.findall('.\..\..',text2)

#\d,\D 
text3='Note no 789654: mile id of person whose employee id 56789 is \
        example2789@gmail.com'
re.findall('\d',text3)
re.findall('\d+',text3)
re.findall('\D+',text3)
re.findall('\d{5}',text3)
re.findall('\d{5,7}',text3)

phone= 'my phone no is 653-526-635'
re.findall('\d+-\d+-\d+',phone)
re.findall('\d{3}-\d{3}-\d{3}',phone)
re.findall('\w+',phone)
re.findall('\w+@\w+\.\w{2,3}',text3)




#Search and replace special characters and spaces with '_' and capitalize each word
string='(Re) Ordering/Monitoring'
'_'.join([i.upper() for i in re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?\s]', string) if i])
