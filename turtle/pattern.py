import turtle


window = turtle.Screen()
window.bgcolor("red")
    
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("yellow")
t1.speed(10)
def draw_square(t1):
    for i in range(1,5):  
        t1.forward(100)
        t1.right(90)
        
   

  
    
    
for i in range(1,36): 
    draw_square(t1)
    t1.right(20)

window.exitonclick()
