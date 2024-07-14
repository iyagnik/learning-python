# -------------------------------------------------Class 1 -----------------------------------------------------------



# import s4_pyfunctions

# l = [1,2,3,4,5,6,7,8,9]
# key = 7

# result = s4_pyfunctions.binary_search(l,key)
# print(result)

# ---------------------------------------------------Class 2 ----------------------------------------------------------

# Regular Expression

# import re


# . - any char
# [a-z A-Z] - char class
# [0-9] - digit class

# + - atleast one [a-z]+
# * - zero or more [a-z]*

# ^ - start of the string
# $ - end of the string
# ? - optional

# [a-z]{2,4}

# panNumber = "ACTYZ9875S"

# r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")

# l = re.findall(r,panNumber)
# print(l)



# mobileNumber = "9265348110"

# r = re.compile("^[6-9][0-9]{9}$")
# l = re.findall(r,mobileNumber)
# print(l)

# dd-mm-yyyy

# date = "31-12-1985"
# r = re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
# l = re.findall(r,date)
# print(l)

# ---------------------------------------------------Class 3 ----------------------------------------------------------

import re

# Groups

# date = "31-12-1985"
# r = re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")

# m = re.search(r,date)
# if m:
# 	print(m.group("year"))
# else:
# 	print("Not Found!!")


# mobileNumber = "+91 9265348110"

# r = re.compile("(\+91\s)?([6-9][0-9]{9})")
# m = re.search(r,mobileNumber)
# if m:
# 	print(m.group(1))
# else:
# 	print("Invalid!!")


# ShortCuts

# [0-9]   \d
# [^0-9]  \D
# [a-zA-Z0-9]  \w
# \W

# space \s
# \S

