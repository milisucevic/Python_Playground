class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		
emp_1 = Employee('Tony', 'Jackson', 50000)
emp_2 = Employee('Test', 'User', 60000)

"""
print(emp_1)
print(emp_2)

emp_1.first = 'Tony'
emp_1.last = 'Jackson'
emp_1.email = 'tony.jackson@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test.user@company.com'
emp_2.pay = 60000
"""

print(emp_1.email)
print(emp_2.email)
