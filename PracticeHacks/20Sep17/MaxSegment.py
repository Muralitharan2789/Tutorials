def MaxSegment(badNumbers,lower,upper):
    a=[]
    c=[]
    for i in range(lower,upper+1):
        if i in badNumbers:
            a.append(i+1)
            c.append(i-1)
        else:
            continue
        
    pairs=[]
    
    for i in range(len(a)):
        pairs.append(c[i]-lower)
        lower=a[i]
    
    return max((max(pairs),upper-lower))+1

# Test Case1:
lower=1
upper=10
badNumbers=[5, 4, 2, 15]
MaxSegment(badNumbers,lower,upper)

# Test Case2:
lower=3
upper=48
badNumbers=[3,7,13, 24,37,49,60]
MaxSegment(badNumbers,lower,upper)
