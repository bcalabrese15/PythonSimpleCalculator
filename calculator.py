class addition:
	def _init_(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	def add(num1, num2):
		return num1 + num2
input = input('Enter your calculation: ')
if "+" in input:
	result = addition.add(int(input[:input.find('+')]), int(input[input.find('+'):])) 
	print(str(result))