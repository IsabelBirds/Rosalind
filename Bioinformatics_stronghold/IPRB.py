#Problem

#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing 
# a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate. 
# AA, Aa, aa

k = 27 
m = 19
n = 26

def dominant_allele(k,m,n):
    tot = k + m + n
    P_kk = (k/tot)*((k-1)/(tot-1))
    P_mm = (m/tot)*((m-1)/(tot-1))
    P_km = (k*m)/(tot * (tot - 1) / 2)
    P_kn = (k*n)/(tot * (tot - 1) / 2)
    P_mn = (m*n)/(tot * (tot - 1) / 2)
    Prob = P_kk + P_km + P_kn + (P_mm * .75) + (P_mn * .5)
    return(Prob)

prob = dominant_allele(k,m,n)

print(prob)