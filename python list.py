myclass=["snake","lion","monkey"]
print(myclass[1])
print(len(myclass))
myclass[0]="cheetah"
print(myclass)

myclass[1:2]=("lion","monkey")
print(myclass)

specialclass=["lion","monkey"]
print(specialclass)
specialclass.append("donkey")
print(specialclass.append)

specialclass=["lion","monkey"]
specialclass.insert(0, "donkey")
print(specialclass)

myclass.extend(specialclass)
print(myclass)