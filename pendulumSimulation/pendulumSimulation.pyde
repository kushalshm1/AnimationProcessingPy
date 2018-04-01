

str_len = 0
angle = 3.14/4
angularVelocity = 0
angularAcceleration = 0


# class kushal():
#     #constructor function
#     def __init__(self,pos,rad):
#         self.positionX = pos[0];
#         self.positionY = pos[1];
#         # self.velocity = vel
#         self.radius = rad
        
        
#     def update(self,_force):
#         self.velocity += _force[0]
#     def display(self):
#         ellipse(self.positionX,self.positionY,self.radius,self.radius)
    

def setup():
    global origin,bob,str_len,newshit
    size(640,360)
    str_len = 180
    origin = [width/2,0]
    bob = [width/2,str_len]
    
def draw():
    global origin,bob,str_len,angle,angularVelocity,angularAcceleration
    origin = [width/2,0]
    bob = [width/2,str_len]
    background(100)
    bob[0] = origin[0] + str_len * sin(angle)
    bob[1] = origin[1] + str_len * cos(angle)
    line(origin[0],origin[1],bob[0],bob[1])
    ellipse(bob[0],bob[1],60,60)
    angularAcceleration = 0.01 * sin(angle)
    angle = angle + angularVelocity
    angularVelocity = angularVelocity + (-1)*angularAcceleration
    angularVelocity = angularVelocity*0.99
    
    
    # newshit = kushal([100,100],30);
    # newshit.display();
