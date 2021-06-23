#binaryAdderForMultiplication.py
def binaryAdder(b1, b2):
	if(len(b1) > len(b2)):
		diff = len(b1) - len(b2)
		b2 = '0'*diff + b2
	elif(len(b1) < len(b2)):
		diff = len(b2) - len(b1)
		b1 = '0'*diff + b1
	else:
		pass
	sum = ''
	carry = 0
	for i in range(len(b1)-1, -1, -1):
		if b1[i] == '0' and b2[i] == '0':
			if (carry):
				sum = sum + '1'
				carry = 0
			else:
				sum = sum + '0'
		elif (b1[i] == '1' and b2[i] == '0'):
			if(carry):
				sum = sum + '0'
				carry = 1
			else:
				sum = sum + '1'
		elif (b1[i] == '0' and b2[i] == '1'):
			if(carry):
				sum = sum + '0'
				carry = 1
			else:
				sum = sum + '1'
		elif(b1[i] == '1' and b2[i] == '1'):
			if(carry):
				sum = sum + '1'
				carry = 1
			else:
				sum = sum + '0'
				carry = carry + 1
	if(carry):
		sum = sum + '1'
	return sum[::-1]
