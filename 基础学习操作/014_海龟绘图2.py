from turtle import *

# def DrawStars(x,y):
#     pu()
#     goto(x, y)
#     pd()
#     seth(0)
#
#     for i in range(5):
#         fd(40)
#         rt(144)
#
#
# for x in range(0, 250, 50):
#     DrawStars(x, 0)
#
# done()

pencolor('red')
for i in range(6):
    circle(50, 240)
    a = position()
    rt(180)
done()