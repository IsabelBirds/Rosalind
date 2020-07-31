#Problem
#Given: A file containing at most 1000 lines.
#Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

a = 0
b = len(open('Python_village/INI5.txt').readlines()) 

while a < b: 
    f = open('Python_village/INI5.txt','r')   
    if a % 2 == 1: 
        print(f.readlines()[a]) 
        a = a + 1 
    else: 
        a  = a + 1
    f.close()