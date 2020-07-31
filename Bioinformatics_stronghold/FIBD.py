#Problem

#Given: Positive integers n≤100 and m≤20.
#Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

n = 85
m = 16


#Fn = Fn-2 + Fn-1 - Fn-m
1,1,2,2,3,4, 

def relation(n,m):
    seq = [1,1]
    for i in range(2, n):
        if i < m:
            x = seq[i - 2] + seq[i - 1]
            seq.append(x)
        else:
            x = sum(seq[i-m:i-1])
            seq.append(x)
    return(seq)

print(' '.join(map(str,relation(n,m))))
