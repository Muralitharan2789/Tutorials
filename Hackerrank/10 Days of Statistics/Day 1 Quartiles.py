# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

'''
#find median
if n%2 == 0:
    Q2 = (numbers[int(n/2)-1] + numbers[int(n/2)])/2
else:
    Q2 = numbers[int((n+1)/2)-1]
    
Q1_numbers=[]
Q3_numbers=[]
for num in numbers:
    if num < Q2:
        Q1_numbers.append(num)
    elif num > Q2:
        Q3_numbers.append(num)
n1=len(Q1_numbers)
n3=len(Q3_numbers)

if n1%2 == 0:
    Q1 = (Q1_numbers[int(n1/2)-1] + Q1_numbers[int(n1/2)])/2
else:
    Q1 = Q1_numbers[int((n1+1)/2)-1]


if n3%2 == 0:
    Q3 = (Q3_numbers[int(n3/2)-1] + Q3_numbers[int(n3/2)])/2
else:
    Q3 = Q3_numbers[int((n3+1)/2)-1]
    
print(int(Q1))
print(int(Q2))
print(int(Q3))


'''
#Function Method
def median(numbers):
    if len(numbers)%2 == 0:
        return int(sum(numbers[len(numbers)//2-1:len(numbers)//2+1])/2)
    else:
        return numbers[len(numbers)//2]

def quartiles(n,numbers):
    Q1 = median(numbers[:len(numbers)//2])
    Q2 = median(numbers)
    if n%2 == 0:
        Q3 = median(numbers[len(numbers)//2:])
    else:
        Q3 = median(numbers[len(numbers)//2+1:])
    return Q1,Q2,Q3

Q1,Q2,Q3 = quartiles(n,numbers)
print(Q1)
print(Q2)
print(Q3)



        