#Chapter 3: Simple Numerical Programs

raw_input_marker = '>> '

print '''
example 1
'''

print "Enter an integer: ",
x = int(raw_input(raw_input_marker))
ans = 0 #sets ans to 0

while ans**3 < abs(x): #abs(x) - ans**3 is a decrementing function
	print 'Value of the decrementing function, abs(x)-ans**3, =',\
			abs(x) - ans**3
	ans = ans + 1
	print ans
if ans ** 3 != abs(x):
	print x, 'is not a perfect cube'
else:
	if x < 0:
		ans = -ans
	print 'Cube root of ' + str(x) + ' is ' + str(ans)
	

print '''
example 2
'''

#this function will take in a positive integer and set i to 0.
#then it will continue to iterate as long as i is less than max
#if we enter 100, we will continue to iterate until i = 99.
#then i will get passed through, we will add 1 to i, reassign the value, and print it
max = int(raw_input('Enter a positive integer: '))
i = 0
while i < max: #max - i is known as our decrementing function
	i = i + 1 
print i

print '''
example 3:
write a program that asks the user to enter an integer and
prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to
the integer entered by the user. If no such pair of integers exists, it should print
a message to that effect
'''

base = int(raw_input('Enter an integer: '))
x = 0
factor_list = list()

while x < base:
	for i in range(1,5):
		if x ** i == base:
			print x, i
			factors = x,i
			factor_list.insert(0,factors)
	x = x + 1

if len(factor_list) == 0:
	print 'There are no exponential factors between 1 and 5 for %r' % base
else:
	print factor_list
	

print '''
example 4
Let s be a string that contains a sequence of decimal numbers
separated by commas, e.g. s='1.23, 2.4, 3.123'. Write a program
that prints the sum of the numbers in s.
'''

s = '1.23, 2.4, 3.123, 4.234'

#this function splits the string wherever there is a ','
#then it applies the function float to each piece of the string using map
#after converting to a number, we sum all the numbers and print
sum_s = sum(map(float,s.split(',')))
print sum_s


print '''
example 5
exhaustive enumeration
'''

#initial parameters
x = -25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
	ans += step
	numGuesses += 1
print 'numGuesses =', numGuesses
if abs(ans**2 - x) >= epsilon:
	print 'Failed on square root of', x
else:
	print ans, 'is close to square root of', x


print '''
example 6
bisection search
'''
#initial parameters
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
	print 'low =', low, 'high =', high, 'ans =', ans
	numGuesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x


print '''
example 7
issues with floating points
'''

x = 0.0

for i in range(10):
	x = x + 0.1
if x == 1.0:
	print x, '= 1.0'
else:
	print x, 'is not 1.0'


print '''
example 8
Newton Raphson method
'''

epsilon = 0.001
y = 25
guess = y/2.0
iterations = 0

while abs(guess*guess-y) >= epsilon:
	iterations += 1
	guess = guess - (((guess**2) - y)/(2*guess))

print 'the number of iterations is', iterations
print 'Square root of', y, 'is about', guess














	

