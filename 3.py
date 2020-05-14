def longestWord(l):
    l1=sorted(l,key=lambda x:len(x))
    return l1[len(l1)-1]
l=list(map(str,input().split(',')))
print(longestWord(l))
