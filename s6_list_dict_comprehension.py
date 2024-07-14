# ------------------------------------Class 1------------------------------
# l = [100,200,300,400,500]

# l2 = [value*value for value in l]
# print(l2)

# for value in l:
# 	l2.append(value*value)

# print(l2)

# l = [10,15,20,25,30,35,40,45,50]

# l2 = [value for value in l if value%2 != 0]
# print(l2)


# l = ["ABC","ABCD","ABCDE","YZYZYZYZ"]
# l2 = [len(value) for value in l ]
# print(l2)


# l3 = [(value1,value2) for value1 in range(1,3) for value2 in range(99,101)]
# print(l3)

# l = [[1,2,3],[4,5,6],[8,7,9]]
# l2 = [val2 for val in l for val2 in val]
# print(l2)

# l = [100,105,110,115,120]

# l2 = ["Even" if value%2 == 0 else "Odd" for value in l]
# print(l2)

# d = {x:x**2 for x in range(1,8)}
# print(d)


# d = {chr(x):x for x in range(97,123)}
# print(d)

# d2 = {value:key for key,value in d.items()}
# print(d2)


# ------------------------------------Class 2------------------------------

# Map
# Filter 
# Lambda 
# They are Fast/

# Map---------------


# def sqr(num):
# 	return num**2


# l = [10,20,30,40,50]
# result = list(map(sqr,l))
# print(result)


# def add(num1,num2):
# 	return num1 + num2

# l1 = [100,200,300,400,500]
# l2 = [10,20,30,40,50]

# result = list(map(add,l1,l2))
# print(result)

# Filter-----------

# def num_check(num):
# 	if num%2 == 0:
# 		return 1
# 	else:
# 		return 0


# l = [10,15,20,25,30,35,40]

# result = list(filter(num_check,l))
# print(result)


# Lambda-------------------if Function is Small



# l = [10,20,30,40,50]
# result = list(map(lambda num1:num1**2,l))
# print(result)

# l = [10,15,20,25,30,35,40]

# result = list(filter(lambda num:num%2==0,l))
# print(result)

# d = {2:30,1:20,3:10}

# l = sorted(d.items(),key=lambda x:x[1])
# print(l)


# ------------------------------------Class 3------------------------------

# GENERATORS-----------------

# def printVal(l):
# 	for value in l:
# 		print(value)

# l = [10,20,30,40,50]

# printVal(l)

# def fibonacci():
# 	first_num = 0
# 	second_num = 1
# 	yield first_num
# 	yield second_num
# 	while(True):
# 		next_val = first_num + second_num
# 		yield next_val
# 		first_num,second_num = second_num,next_val


# gen = fibonacci()

# for value in range(10):
# 	print(next(gen),end=",")


#IGNORE>>>>>>>
# for value in range(5):
# 	for x in range(value):
# 		print("*",end = " ")
# 	print()


# ------------------------------------Class 3------------------------------

# INTERTOOLS IN PYTHON

# l = [100,200,300,400,500,600]

# i = iter(l)
# print(i)

# for value in i:
# 	print(value)

import itertools

# l1 = [10,20,30,40,50]
# l2 = [100,200,300,400,500]
# l3 = [1000,2000,3000,4000,5000]

# i = itertools.chain(l1,l2,l3)
# print(i)

# for x in itertools.islice(i,0,8):
# 	print(x)

# count = 0
# for x in itertools.repeat(l1):   #Can use cycle instead of repeat
# 	if count < 20:
# 		print(x)
# 	else:

# 		break
# 	count+=1


# i = iter(l1)
# t = itertools.tee(i)
# print(t)
# for x in t[0]:
# 	print(x)
# for value in t[1]:
# 	print(value)



# count = 0
# for x in itertools.count(50,5):
# 	if count > 21:
# 		break
# 	else:
# 		print(x)
# 	count+=1


# l = [1,2,3,4,5]
# print(list(itertools.permutations(l,2)))
# print(list(itertools.combinations(l,2)))