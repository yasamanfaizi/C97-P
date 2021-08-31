intro = input("write about yourself: ")
wordcount = 1
letter = 0
for i in intro:
    letter = letter+1
    if i == ' ': 
        wordcount = wordcount + 1
        letter= letter -1
print(wordcount)
print(letter)