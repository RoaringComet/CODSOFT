# generating passwords #
import random as r
import string as s
# special characters
n = int(input(" enter the length of your desired password"))

spl = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', ':', ';', ',', '.']

# password difficulty
def easy_pass (n):
    p = r.sample(s.ascii_letters,n)
    p = "".join(p)
    print (' password is : ',{p})

def medium_pass (n):
    p = r.sample((s.ascii_letters),n)
    p = "".join(p)
    print (' password is : ',{p})

def hard_pass (n):
    p = r.sample((s.ascii_letters+  r.sample[spl,5]),k=n)
    p = "".join(p)
    print (' password is : ',{p})

while True:
    print(""" Easy Password : 1
     Medium Password : 2
     Hard Password : 3
      Exit : <else>""")

    x = int(input("enter your choice : "))

    if x == 1:
        easy_pass(n)
    elif x == 2:
        medium_pass(n)
    elif x == 3:
        hard_pass(n)
    else :
        break



