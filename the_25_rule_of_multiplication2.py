#The Rule of 25 Python code written by Kehinde Ajibade 

n = int(input('Enter a number: ')) # n must be an integer
#modulus = n % 4  # This will give the remainder of any integer divisible by 4
quotient_remainder = divmod(n,4)
quotient = quotient_remainder[0]
modulus = quotient_remainder[1]

#quotient = n // 4 # This will give the quotient of any integer
if modulus == 0:
    result = quotient * 100
    print('Answer:',result)
elif modulus == 1:
    remainder = modulus * 25
    result = quotient * 100 + remainder
    print('Answer:',result)
elif modulus == 2:
    remainder = modulus * 25
    result = quotient * 100 + remainder
    print('Answer:',result)
else:
    remainder = modulus * 25
    result = quotient * 100 + remainder
    print('Answer:',result)