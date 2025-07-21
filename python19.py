# Python OOP (Object-Oriented Programming)
# Class คือ ต้นแบบ หรือ แม่แบบ ของ Object
# Object คือ วัตถุ ที่ถูกสร้างขึ้นมาจาก Class หรืออาจะจะเรียกว่าตัวแทนของคลาส instace of class
#-------------------
class IoTSAU :
    pass
 
class Car :
    #data member
    brand = ""
    model = ""
    whell = 0
 
    #method member
    def letGo(self):
        print("ไปกันเลย......")
 
    def carStop(self):
        print("จอดแล้ว......")
 
#-------------------
obA = Car()
obB = Car()
wowA = Car()
#-------------------
obA.brand = "Toyota"
print(obB.whell + wowA.whell)
#-------------------
obA.letGo()
wowA.letGo()
obB.carStop()
#-------------------