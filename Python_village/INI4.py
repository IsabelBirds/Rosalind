#Problem
#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.

a = 100
b = 200
c = 0

while a <= b: 
    if a % 2 == 0: 
        a = a + 1 
    else: 
        c = c + a 
        a = a + 1 
print(c)