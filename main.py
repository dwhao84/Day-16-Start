from turtle import Turtle, Screen
import another_module

print(another_module.another_module) # Should be 12

# Constructing the OBJECT:
timmy = Turtle() # 建立turtle module，並建立Turtle的型別，叫Timmy。
print(timmy)            # 印出的是Object。

# Object -> Attribute
# car.speed

my_screen = Screen()
# 這個時候，my_screen就是一個物件(Object)，而canvheight是屬性(Attribute)
print(my_screen.canvheight) # Show 300.

