lower = int(input("enter the min limit"))
upper = int(input("enter the max limit"))
print(f"prime numbers beetween {lower}-{upper} are")
for num in range (lower,upper+1):
    if (num > 1):
      for i in range (2,num):
        if (num % i)==0:
         break
      else :
        print (num)