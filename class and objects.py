class myclass:
    "this is s class"
    a=10
    def func(self):
        print('hello')

print(myclass.a)
print(myclass.func)
print(myclass.__doc__)

#creating objects

obj1=myclass()
print(obj1.a)

obj2=myclass()
print(obj2.a + 5)