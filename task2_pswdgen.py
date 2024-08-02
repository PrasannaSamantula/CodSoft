import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['!','@','#','$','%','&','(',')','+','^','*']
digits=['1','2','3','4','5','6','7','8','9']
n_letters=int(input("How many letters u want:"))
n_symbols=int(input("How many symbols u want:"))
n_digits=int(input("How many digits u want:"))
pswd=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    pswd += char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    pswd += char
for i in range(1,n_digits+1):
    char=random.choice(digits)
    pswd += char
random.shuffle(pswd)
pswd_list=""
for ch in pswd:
    pswd_list += ch
print(pswd_list)
