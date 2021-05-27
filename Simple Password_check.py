print('''•	At least 1 letter between [a-z]
•	At least 1 number between [0-9]
•	At least 1 letter between [A-Z]
•	At least 1 character from [$#@]''')
pswd=input("Enter a passowrd:")
bol=True
d={"loweralpha":0,"upperalpha":0,"Number":0,"Symbol":0}
for i in pswd:
        if i.isalpha():
           if i.islower():
               d["loweralpha"]+=1
           if i.isupper():
               d["upperalpha"]+=1
        elif i.isnumeric():
            d["Number"]+=1
        else:
            d["Symbol"]+=1
total_length=0
for i in d.keys():
    if d[i]>0:
        total_length+=d[i]
    else:
        total_length+=d[i]
        bol=False
        print("At least 1 letter should be",i)
if bol==True and total_length>5 and total_length<13:
        print("Password is Valid")
else:
     print("Password length should be inbetween 6 to 12")
