
epsilon = 0.001
y = 25
guess = y/2.0
iterations = 0

while abs(guess*guess-y) >= epsilon:
	iterations += 1
	guess = guess - (((guess**2) - y)/(2*guess))

print 'the number of iterations is', iterations
print 'Square root of', y, 'is about', guess



	
	