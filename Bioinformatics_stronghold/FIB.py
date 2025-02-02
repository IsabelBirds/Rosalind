#Problem

#A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. 
# In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were 
# alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month 
# is equal to the number of rabbits that were alive two months prior. As a result, if Fn represents the number of 
# rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined 
# by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears 
# Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

#When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation 
# to generate terms for progressively larger values of n. This problem introduces us to the computational technique of 
# dynamic programming, which successively builds up solutions by using the answers to smaller cases.

#Given: Positive integers n≤40 and k≤5.

#Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each 
# generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

n = 5 
k = 2

#Fn = 3*Fn-2 + Fn-1
# 1, 1, 4, 7, 19 

def relation(n,k):
    seq = [1,1]
    for i in range(2, n):
        x = k*seq[i - 2] + seq[i - 1]
        seq.append(x)
    return(seq)


n = 35 
k = 2

print(' '.join(map(str,relation(n,k))))