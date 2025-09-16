class Demo:
    a=4

o= Demo()
print(o.a) # print the class artribute because the instance attribute is not present

o.a=0
print(o.a)  #inastance attribute is present so instannce attribute is present but it doesn't mean class attribute is changed 

print(Demo.a)

