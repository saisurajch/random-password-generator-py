import random
import string
letters = list(string.ascii_letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
level = input("Enter the level of password you want. (Eazy or Hard)\n")

a = []
for i in range(nr_letters):
  a.append(random.choice(letters))
b = []
for i  in range(nr_symbols):
  b.append(random.choice(symbols))
c = []
for i in range(nr_numbers):
  c.append(random.choice(numbers))

list = [a,b,c]
hard = []
if(level == "Eazy"):
    for n in list:
      for i in n:
       print(i,end='')
elif(level == "Hard"):
    for n in list:
      for i in n:
        hard.append(i)
    random.shuffle(hard)
    password = ''
    for i in hard:
      print(i,end='')
