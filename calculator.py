class addition:
	def _init_(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	def add(num1, num2):
		return num1 + num2
addition()
class subtraction:
	def _init_(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	def sub(num1, num2):
		return num1 + num2
subtraction()
class multiplication:
	def _init_(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	def mult(num1, num2):
		return num1 * num2
multiplication()
class division:
	def _init_(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	def div(num1, num2):
		return num1 / num2
division()
input = input('Enter your calculation: ')
strLengthIndex = 0
temp = 0
while strLengthIndex < len(input):
	if(isinstance(input[strLengthIndex], int)):
		strLengthIndex += 1
	else:
		if "+" in input:
			result = addition.add(int(input[:input.find('+')]), int(input[input.find('+'):plusOne])) 
			temp += int(result)
		if "-" is input[strLengthIndex]:
			plusOne = int(strLengthIndex + 2)
			result = subtraction.sub(int(input[:input.find('-')]), int(input[input.find('-'):plusOne])) 
			print(str(result))
		if "*" in input:
			result = multiplication.mult(int(input[:input.find('*')]), int(input[input.find('*'):])) 
			print(str(result))
		if "/" in input:
			result = division.div(int(input[:input.find('/')]), int(input[input.find('/'):])) 
			print(str(result))
		strLengthIndex += 1