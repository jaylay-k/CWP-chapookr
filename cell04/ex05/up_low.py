word = input()
result = ""

for i in range(len(word)):
    if word[i].islower() :
        result += word[i].upper()
    else :
        result += word[i].lower()
        
print(result)