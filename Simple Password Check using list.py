#Code Praveen Acharya
pswd=input("Enter Password:")
liss=[0,0,0,0]
a=dir(str)
bol=True

for j in pswd:
        if j.isalpha():
            if j.isupper():
                liss[0]+=1
            elif j.lower():
                liss[1]+=1
        elif j.isnumeric():
            liss[2]+=1
        else:
            liss[3]+=1
total=0
for j in liss:
    if j>0:
        total+=j
        bol=True
    else:
        bol=False
        print('''•	At least 1 letter between [a-z]
•	At least 1 number between [0-9]
•	At least 1 letter between [A-Z]
•	At least 1 character from [$#@]''')
                             
if bol==True and total>5 and total<13:
    print("Password is valid")
else:
    print("Password is not valid")
