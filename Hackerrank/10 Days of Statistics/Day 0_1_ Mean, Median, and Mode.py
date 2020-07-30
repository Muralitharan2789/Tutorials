# Enter your code here. Read input from STDIN. Print output to STDOUT

# By using Python standard Libraries
'''
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))
'''

#Source Code 
n = int(input())
dictionary = {}
numbers = list(map(int, input().split()))
numbers.sort()
total = 0
#create dictionary with numbers:frequency
for num in numbers:
    if num not in dictionary:
        dictionary[num] = 1
    else:
        dictionary[num] = dictionary[num] + 1
#find total and mean
total = 0
for num in numbers:
    total += num
mean = total/n
#find median
if n%2 == 0:
    median = (numbers[int(n/2)-1] + numbers[int(n/2)])/2
else:
    median = numbers[int((n+1)/2)-1]
#find mode
freq = 0
mode = 0
for key in dictionary.keys():
    if dictionary[key] >= freq:
        if dictionary[key] == freq:
            if int(key) < mode:
                mode = key
                freq = dictionary[key]
        else:
            mode = key
            freq = dictionary[key]

print (mean)
print (median)
print (mode)

'''
#Other Codes
for key, value in dictionary.items():
    total = total + (key*value)
mean = total/n
print(mean)
'''
