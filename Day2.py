# Python program to print prime factors

import math
# a given number n





def primeFactors(n):
	
	# Print the number of two's that divide n
	while n % 2 == 0:
		print (2)
		n = n / 2





	# so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(math.sqrt(n))+1,2):
		
		# while i divides n , print i and divide n
		while n % i== 0:
			print (i)
			n = n / i
			



	if n > 2:
		print (n)
		
# Driver Program to test above function

n = int(input("enter the number to test"))
primeFactors(n)
