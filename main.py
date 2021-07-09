print("Welcome to Love Calculator")
your_name = input("Your Name:\n").lower()
their_name = input("Their Name:\n").lower()
name = your_name + their_name
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = t+r+u+e
# print(true)
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
love = l+o+v+e
# print(love)
total = (true * 10) + love
# print(f'Your Score is: {total}')
if total < 10 or total > 90:
    print(f'Your Score is: {total}, you go together like Coke and Mentos.')
elif 40 < total < 50:
    print(f'Your Score is: {total}, you are alright together.')
else:
    print(f'Your Score is: {total}.')
