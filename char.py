string = (input ("enter a word "))
char = (input("enter the letter you want to check "))
i = 0
count = 0
while (i < len(string)):
    if (string[i]  == char):
       count = count + 1
    i = i + 1
print(f" the occurence of the letter {char} is {count} times ")   