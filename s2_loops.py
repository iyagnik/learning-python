# --------------------------------- Class 3 ----------------------------



# break 
# continue
# enumerate

# for value in range(10) :
# 	print(value)

# l = [10,20,30,40,50,60]
# key = 60

# for index,value in enumerate (l) :
# 	print(index,value)

# 	if value == key :
# 		print("Element Found at Index",index)
# 		break
# 	else :
# 		pass
# 		print("Pass",index)
# else :
# 	print("Element Not Found!!")

# print("Statement after the Loop")




# for value in l :

# else :
# break
# continue
# pass
# enumerate

# -------------------------- Class 4 -------------------------

# While Loop

# while [condition]:
# 	[satements]
# else:

#ex. sum of 1-20

# count = 1
# sum = 0
# while count <= 20:
# 	sum += count
# 	count += 1
# print(sum)


# --------------------------- Class 5 ---------------------------

# Assignment 1

#Find those numbers divisible by 7&5 in btw 1500-2700

# list = []
# for x in range(1500,2701):
# 	if ((x%7==0) and (x%5==0)):
# 		list.append(x)
# print (list)

#WAPP to count numbers of even / odd numbers in a series

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# even = 0
# odd = 0
# for x in l:
# 	if x%2==0:
# 		even+=1
# 	else:
# 		odd+=1
# print("Even No. :",even)
# print("Odd No. :",odd)

#WAP which iterates the integers from 1 to 50. for multiple of theree print "Fizz"

# for Fizzbuzz in range(51):
#     if Fizzbuzz % 3 == 0 and Fizzbuzz % 5 == 0:
#         print("Fizzbuzz")
#         continue
#     elif Fizzbuzz % 3 == 0:
#         print("Fizz")
#         continue
#     elif Fizzbuzz % 5 == 0:
#         print("Buzz")
#         continue
#     print(Fizzbuzz)



#WAP to calculate sum n avg of n interger numbers


# sum=0

# for x in range(5):
# 	sum+=x
# 	pass
# avg=sum/5
# print("Sum is",sum)
# print("Avg is",avg)


#WAP to caculate factorial of a number

# num = 5
# factorial = 1
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)





l = [3,2,4]
print(len(l))