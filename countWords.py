#import random
# rand=random.randint(1,10)
introstring=input("enter your introduction")
print(introstring)
charactercount=0
wordcount=1
for character in introstring:
    charactercount=charactercount+1
    if(character==" "):
        wordcount=wordcount+1
print(charactercount)
print(wordcount)

