# ----------------------------------Class 1-------------------------------------

# OOP

# class Account:
# 	def __init__(self,cust_id,name,bal=0,):
# 		self.id = cust_id
# 		self.name = name
# 		self.bal = bal

# 	def get_bal(self):
# 		return self.bal

# 	def deposite(self,ammount):
# 		self.bal = self.bal + ammount
# 		return self.bal

# 	def withdraw(self,ammount):
# 		if ammount > self.bal:
# 			return "Insuffiecient Bal"
# 		else:
# 			self.bal = self.bal - ammount
# 			return self.bal

# customer1 = Account("100","Yagnik")
# print(customer1.bal)
# customer1.withdraw(100)
# print(customer1)

# print(customer1.id,customer1.name,customer1.bal)
# customer1.deposite(50000)
# print(customer1.get_bal())

# ----------------------------------Class 2-------------------------------------


# privet var => __varName
# Var Outside of Method => Class Variable

# Class Method => Decorater
# @classmethod 
# def function(cls):
# 	cls.var += 1

# Static Method => Intance Method
# @staticmethod
# def function():
# 	print("Hello")

# ----------------------------------Class 3-------------------------------------

# Inheritance

# class SecondMethod(firstMethod):
# 	pass
# class A:
# 	pass
# class B:
# 	pass
# class C(B,A):
# 	pass

# obj = C()
# help(obj)