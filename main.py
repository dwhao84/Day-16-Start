from turtle import Turtle, Screen
import another_module

print(another_module.another_module) # Should be 12

# Constructing the OBJECT:
timmy = Turtle()        # 建立turtle module，並建立Turtle的型別，叫Timmy。
print(timmy)            # 印出的是Object。

# Calling Method.
timmy.shape("turtle")   # 可以在 docs.python.org/3/library/turtle.html，看到完整的功能。
timmy.color("red")      # 將Turtle顏色改成紅色
timmy.forward(100)      # 將Turtle往前100

# Object -> Attribute
# car.speed
my_screen = Screen()
# 這個時候，my_screen就是一個物件(Object)，而canvheight是屬性(Attribute)
print(my_screen.canvheight) # Show 300.

# exitonclick是一個method。
# 點擊畫面之後，畫面就是消逝。
my_screen.exitonclick()