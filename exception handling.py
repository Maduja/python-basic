import sys

randomList = ['a',0,2]

for x in randomList:
    try:
        print(x)
        r=1/int(x)
        break
    except:
        print("Ooops",sys.exc_info()[0],"occured")