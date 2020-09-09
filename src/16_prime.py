
num = int(input('Enter a number: '))

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,'not prime') # is a whole number
           break
   else:
       print(num,'is prime')
else: # < or = 1 is not prime
   print(num,'not prime')