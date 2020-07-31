n = int(input())
X = list(map(float,input().split()))
W = list(map(float,input().split()))
print(round(sum([i[0]*i[1] for i in zip(X,W)])/sum(W),1))




# Faster Method with numpy libraries
import numpy as np
n = int(input())
#Converting to array and multiplication avoids iteration
X = np.array(list(map(float,input().split())))
W = np.array(list(map(float,input().split())))
W=W.transpose()
print(sum(X*W))
