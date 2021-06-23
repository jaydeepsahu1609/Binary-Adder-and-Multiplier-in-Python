import binaryAdderForMultiplication
#binary Adder function from another program
num2 = input("Enter first binary number : ")
num1 = input("Enter second binary number : ")
MQ = num1 + '0'*len(num1)
			#num1 to MSD and then replace LSD by 0's'
M = num2

for i in range(len(num2)):
	n = MQ[0]					#stores MSD
	MQ = MQ[1:] + '0'    #left-shift by 1
	if n == '1':
		MQ = binaryAdderForMultiplication.binaryAdder(MQ, M)
								#if shifted bit is '1', add numbers
	elif n == '0':
		MQ = binaryAdderForMultiplication.binaryAdder(MQ, '0')
						#else add 0

print("\n\nResult : ", MQ)

