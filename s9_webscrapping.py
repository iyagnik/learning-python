# ----------------------------------Class 1-------------------------------------

# BeautifulSoup

# import requests
# from bs4 import BeautifulSoup

# r = requests.get("https://kayoanime.com/")
# print(r.status_code)

# soup = BeautifulSoup(r.content,"html.parser")
# print(soup.prettify())

# find('a')
# find_all('div')
# find_parent('a')
# find_next_sibligs("a")

# card = soup.find("li",attrs={"class":"post-item"})
# print(card.prettify())



# ----------------------------------Class 2-------------------------------------

# FOR DBMS

# import sqlite3

# conn = sqlite3.connect("example2.db")
# c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY,NAME TEXT)""")

# # c.execute("INSERT INTO EMP(ID,NAME) VALUES(77,'YAGNIK')")
# # conn.execute("COMMIT")

# c.execute("""SELECT * FROM EMP""")
# print(next(c))