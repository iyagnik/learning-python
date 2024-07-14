#--------------------- Class 1 -----------------------
#1 String

# s = ' ' , "", """", """


# 1 String are immutable
# 2 string is ordered data Structure

# s = "PYTHON JAVA ETC"
# print(s[100])
# print(s[:9])
# print(s[::2])
# print(s[::-1])
# for value in s:
#     print(value)
# for value in s[::2]:
#     print(value)

#---------------------- Class 2 ------------------------
# help(str)
# print(dir(str))
# a=100
# b=111
# print("Value of a is",a)
#format
# print("Value of a is {val2} & b is {val1}".format(val1=a,val2=b))

# s = "python sttring sample"

# s = s.capitalize()
# print(s,id(s))

# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.isupper()) #istitle #islower

# s = "HTML,CSS,JAVA,PYTHON"
# l = s.split(",")
# print(l)
# s1 = (" ").join(l)
# print(s1)


# s1 = "ABCD"
# s2 = "1234"
# s3 = "Python is ABCD"

# table = str.maketrans(s1,s2)
# result = s3.translate(table)
# print(result)

# index
# find
# rfing function 

# s = "HTML,CSS,JAVA"
# print("PYTHON" in s)
# print(s.index("CSS"))
# print(s.rfind("Css"))

# s = "************to much spaceeee**********"
# s1 = s.strip("*")
# print(s1)

# s = "Python"
# s1 = s.ljust(20,"*") #center
# print(s1)

# s = "html,css,java"

# s2 = s.replace("html","HTML5")
# print(s2)


#----------------------------Class 3-----------------------

# List

# 1 list are mutable (can add and delete)
# 2 ordered indexing/slicing
# 3 heterogrneous datatype 

# l = [10,20,30,44,"Python","CSS",[100,222,"HTML5"]]
# print(l,type(l))

# print(l[-1][0])
# print(l[::-1])

# l = [100,200,300,444,555]

# for value in l[::2]:
#     print(value)

# l.append(667)
# print(l)

# a=200
# print(id(a))
# b=200
# print(id(b))
# print(id(l[1]))

# l.extend([777,888])
# print(l)

# l.insert(0,1000)
# print(l)

# l = [11,22,33]

# l2 = l.copy()
# print(l,l2)
# print(id(l),id(l2))

#---------------------------Class 4------------------------------

# l = [11,22,33,44,55]
# l[2] = 333
# print(l)

# pop remove clear del 

# r = l.pop()
# print(l,r)
# l.remove(22)
# print(l)

# l.clear()
# print(l)

# del l
# print(l)

# l = [22,22,11,55,44]
# l2 = [33]
# l.sort()
# print(l)
# l.reverse()
# print(l)

# l3 = sorted(l)
# print(l3)

# print(l.index(44))
# print(l.count(22))

# print(l + l2)
# print(l * 2)

#------------------- Class 5 -------------------------
# Tuple
# immutable data structure
# ordered indexing slicing

# t = (10,20,33,44,44,44)
# print(t,type(t))
# print(t.count(44))

# l = [10,20,30,40,50]

# for t in enumerate(l):
#     print(t)

# t = tuple(l)
# print(t)

# t = ("a","b","c",777)
# l = list(t)
# print(l,type(l))

#---------------------------- Class 6 ----------------------------------
# dict
# mutable
# unordered
# key should be unique
# keys should be immutable
# int str float tuple 

# d = {"sid":77,"name":"Yagnik","mail":"00yagnik@gmail.com"}
# print(d)
# d["contact"] = 9265348110
# print(d)
# print(d["sid"])

# print(d.get("sid","Not Found"))
# print(d.setdefault("age",19))
# print(d)

# for key in d:
#     print(key,d[key])


# d = {}
# for value in range(1,11):
#     d[value] = value * value
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

# for t in d.items():
#     print(t)



#---------------------------- Class 7 ---------------------------------

# l1 = [1,2,3,4,5]
# l2 = [1,4,5,7,8,9]

# d = dict(zip(l1,l2))
# print(d)

# d = dict.fromkeys(l1,0)
# print(d)

# d1 = {1:1,2:3,4:6}
# d2 = {5:25,7:49}

# d1.update(d2)
# print(d1)

# pop popiteam clear del 

# r = d1.pop(2)
# print(d1,r)

# r = d1.popitem()
# print(d1,r)

# d1.clear()
# print(d1)

# del d1
# print(d1)


#-----------------------------Class 8 ---------------------------------
# SET DATA Type

# 1 sets are mutable
# 2 all the elements should be unique
# 3 immutable elements in the set - int float tuple str
# 4 unordered


# s = {10,20,30,44,44,44,44}
# print(s,type(s))

# s = {111,222,333}
# s.add(444)
# print(s)

# s2 = {555,600,111}

# s3 = s.union(s2)
# print(s3)

# s3 = s.intersection(s2)
# print(s3)

# s3 = s2.difference(s)
# print(s3)

# s3 = s.symmetric_difference(s2)
# print(s3)
# print(s)
# s.update(s2)
# print(s)

# s.intersection_update(s2)
# print(s)

# s.difference_update(s2)
# print(s)

# s.symmetric_difference_update(s2)
# print(s)

# s1 = {100,200,300,400,500}
# s2 = {100,200,500}

# print(s2.issubset(s1))
# print(s1.issuperset(s2))

# l = [100,200,300,444,444]
# s = set(l)
# print(s)

# l1 = [100,200,300,400,500]
# l2 = [50,100,150,200,15,30,45,75,105]

# s1 = set(l1)
# s2 = set(l2)

# s3 = s1.union(s2)
# print(s3)

# l3 = sorted(s3)
# print(l3)

# l3 = list(s3)

# l3.sort()
# print(l3)

# pop remove discard clear del 

# s = {100,222,333,444,500,666}
# r = s.pop()
# print(s,r)

# s.remove(100)
# print(s)

# s.discard(10000)
# print(s)

# s.clear()
# print(s)

# del s



#---------------------------------------- Class 9 -------------------------------------------------

# l = [100,200,300,400,500]
# print(sum(l))
# print(max(l))
# print(min(l))

# num = 29.36584
# print(round(num))

# help(__builtins__)

# -------------------- Math ------------------

# import math

# l = [0.2] * 10
# print(l)
# print(sum(l))

# print(math.fsum(l))

# num2 = 19.8889
# print(math.floor(num2), math.ceil(num2))

# print(math.sqrt(64))
# print(math.factorial(5))

# print(math.modf(num2))

# d, i = math.modf(num2)
# print(i,d)

# print(math.pow(5,2))

# print(math.log(10,2))
# print(math.log10(3))
# print(math.log2(10))

# print(math.sin(math.radians(30)))
# print(math.cos(math.radians(30)))
# print(math.tan(math.radians(30)))

# help(math)

# -------------------Random-----------------------

# import random

# Random Numbers Between 0-1

# print(random.random()) 

# l = [1,2,3,4,5,6]
# print(random.choice(l))

# print(random.randint(1,3))
# print(random.randrange(1,3)) #excluding 3

# print(random.uniform(1,7))

