#Ch 2

print'''
Chapter 2
'''

print'''
Write a program that examines three variables 
\t*x
\t*y
\t*z
and prints the largest odd number among them. 
If none are odd, print a message to that effect.
'''

odd_list = list() #add list that we will put odd numbers into

#define parameters: x, y, and z
def odd_numbers(x,y,z):
	variables = x, y, z #put our parameters in a variable
	for i in (variables): 
		if i % 2 == 1: #check to see if there is a remainder
			print i, "is odd"
			odd_list.insert(0,i) #if odd, add to the "odd_list"
		else:
			print i, "is even"
	if len(odd_list) == 0:
		print "There are no odd numbers"
	else:
		print max(odd_list), "is the largest odd number"
			
odd_numbers(20,6,4)
		
#type conversions
n = int(raw_input('Enter an int: '))
print type(n)

#iteration

x = 3
ans = 0
itersLeft = x

while (itersLeft != 0): #itersLeft = 3 for now
	ans = ans + x #increment ans by 3 in each iteration
	itersLeft = itersLeft - 1 #3 iters and goes down from there
print str(x) + '*' + str(x) + ' = ' + str(ans)


print '''
Write a program that asks the user 
to input 10 integers, and then prints
the largest odd number that was entered.
If no odd number was entered, it 
should print a message to that effect
'''

while True: #continue until the code is false
	try: #try to run this code+if error is encountered to go the except block
		parameters = [] #container for our values
		for i in xrange(1,10):
			#append the raw integer values to the list parameters
			parameters.append(int(raw_input('Enter an integer: ')))
		break
	except ValueError: #if there is an error execute this block
		print "Oops! That was not a valid number. Let's try that again..."

print parameters

def odd_numbers(parameters):
	for i in (parameters): 
		if i % 2 == 1: #check to see if there is a remainder
			#print i, "is odd"
			odd_list.insert(0,i) #if odd, add to the "odd_list"
	if len(odd_list) == 0:
		print "There are no odd numbers"
	else:
		print max(odd_list), "is the largest odd number"
			
odd_numbers(parameters)




























