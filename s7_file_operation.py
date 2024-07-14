# --------------------------------------Class 1/2-------------------------------------


# r => read
# r+
# w => write
# w+
# a => append
# a+

# fp = open("example.txt","r")
# content = fp.read()
# print(content)

# Use Position Pointer ^^^

# content = fp.read(4)
# print(content)

# content = fp.readlines()
# print(content[0])

# for c in fp:
# 	print(c)

# fp = open("example.txt","w")
# fp.write("New Line Added!!") # Delete old data and write given Data


# tell => current filePointer position
# seek(offset,position) => to change the fp position
# offset - number of char
# position - 0 => start of the file
# 		 - 1 => current position
# 		 - 2 => end of the file  # When Using 1,2 offset =0

# fp = open("example.txt","w+")
# print(fp.tell())
# fp.write("Its a Example!!")
# print(fp.tell())
# fp.seek(0,0)
# print(fp.tell())
# content = fp.read()
# print(content)


# => w+ remove old data
# => r+ keep old data
# => r,r+,w,w+ => fp  at start
# => a,a+ => fp at end

# r => fp => start, file should already exist, read
# r+ => fp => start, file should already exist, read + write

# w => fp => start, create new file, write
# w+ => fp => start, create new file, write + read

# a => fp => end, create new file, write at end
# a+ => fp => end, create new file, write at end + read



# --------------------------------------Class 3/4-------------------------------------

# JSON Proccessing/File

# import json

# handle = open("json_input.json","r")  #Make a JSON FILE FOR OUTPUT
# content = handle.read()
# print(content)
# handle.close()  => for closing
# => can save as dict
# Example
# d = json.loads(content)

# json.dums(d) => can make all conversion like tuple to dict or list to dict


# XML Files

# import xmltodict

# handle = open("input.xml","r")
# content = handle.read()
# # print(content)

# d = xmltodict.parse(content)
# d['Result']['Message'] = "cANT fOUND"
# print(d['Result']['Message'])

