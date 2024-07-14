# ------------------------------------------- Class 1 -----------------------------------------

# 1 Code Reuse
# 2 Modularity

# s = "Python,HTML,CSS,Java"
# print(s.index("HTML"))

# Fun Call
# Fun Definetion

def value_rev(value):
	if type(value)==list or type(value)==str:
		rev = value[::-1]
	else:
		temp=str(value)
		rev = temp[::-1]
	# print(rev) ##
	return rev

# s = "Python"
# result = value_rev(s)
# print(result)  ##

# l = [11,22,33,44,56]
# result = value_rev(l)
# print(result)

# num = 123
# result = value_rev(num)
# print(result)



# ------------------------------------------------- Class 2 -----------------------------------

# 1 Positional Argument
# 2 Default Argument
# 3 Keyword Argument


# def linear_search(l,key):
# 	for value in l:
# 		if key == value:
# 			return True
# 	else:
# 		return False

# l = [100,222,300,444,500,666]
# key = 444
# result = linear_search(l,key)
# print(result)



# Password Generator
# 8 Char = 1 upper + 1lower + 1 special + 5 digits

# ord
# chr

# print(ord('a'),ord('z'))
# print(ord('A'),ord('Z'))
# print(chr(98))


# import random

# def gen_pass(Length=8):

# 	l = ['@','#','$','%','&','~']
# 	upper = chr(random.randint(65,90))
# 	lower = chr(random.randint(97,122))
# 	special = random.choice(l)
# 	digit = random.randint(100000,999999)
# 	password = upper + lower + special + str(digit)
# 	l = random.sample(password,Length)
# 	password = ("").join(l)
# 	return password

# reuslt = gen_pass()
# print(reuslt)


# Username/Password Check

# def validate(username,password):
# 	if username == "AIIE" and password == "AIIE@123":
# 		print("Valid Password")
# 	else:
# 		print("Invalid Username or Password!")

# validate("AIIE","AIIE@123")
# validate(password="AIIE@123",username="AIIE")

# help(print)
# print(11,12,sep=",",end="	")
# print("Hello")

# -------------------------------------------- Class 3 ----------------------------------


# 4 Variable Length Positional args
# 5 Variable Length Keyword args



# l = [100,200,300,400]
# l.append(202,300) #not works

# def add_value(*args):
# 	l = []
# 	for value in args:
# 		l.append(value)
# 	return l

# result = add_value(200,33,6666)
# print(result)



# def get_details(**kargs):
# 	print(kargs)


# get_details(name="Yagnik",email="iyagnik@pm.me",dob="Apr 20")
# get_details(name="Yagnik",contact="9265348111",dob="Apr 20")



# -------------------------------------------- Class 4 ----------------------------------

# Recursive Function----------------

# def factorial(num):
# 	if num == 1:
# 		return 1
# 	else:
# 		return num * factorial(num -1)


# numX = 6
# result = factorial(numX)
# print(result)


def binary_search(l,key):

	if len(l) == 0:
		return False
	else:
		mid = len(l) // 2

		if l[mid] == key:
			return True
		elif key < l[mid]:
			return binary_search(l[:mid],key)
		else:
			return binary_search(l[mid+1:],key)

if __name__ == '__main__':
	l = [100,200,300,400,500,600,700,800,900]
	key = 900

	result = binary_search(l,key)
	print(result)