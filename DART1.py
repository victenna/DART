import pygame,math
pygame.init()
parameters=pygame.image.load('Parameters.png')
screen = pygame.display.set_mode((1200, 800)) 
clock=pygame.time.Clock()
font = pygame.font.Font(None, 50)
txt_surface = font.render('Double Asteroid Redirection Test(DART)', True, 'white')


X0=600
Y0=300
xRadius = 450
yRadius = 200
X1=580
Y1=320
x1Radius = 420
y1Radius = 170

ellipse1 = pygame.Rect(X0-xRadius,Y0-yRadius,2*xRadius,2*yRadius)
ellipse2 = pygame.Rect(X1-x1Radius,Y1-y1Radius,2*x1Radius,2*y1Radius)
z=0
class Asteroids():
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
        #self.image=pygame.transform.scale(self.image ,(225,195))
        
    def settings(self,scale_x,scale_y,X0,Y0):
        self.image=pygame.transform.scale(self.image ,(scale_x,scale_y))
        self.X0 = X0
        self.Y0= Y0
        #self.rect=self.image.get_rect(center=(X0,Y0))
        self.rect=self.image.get_rect(center=(self.X0,self.Y0))
        self.degree=0
        self.deltax=0
        self.deltay=0
     
    def settings1(self,scale_x,scale_y):#,X0,Y0):
        self.image=pygame.transform.scale(self.image ,(scale_x,scale_y))
        self.rect=self.image.get_rect(center=(600,300))
        self.degree=0
        self.deltax=0#!!!!!!!!!!!!!!!!
        self.deltay=0#!!!!!!!!!!!!!!!!!!

    def update(self,xRadius,yRadius):
        self.xRadius=xRadius
        self.yRadius=yRadius
        self.degree+=0.25
        phase=self.degree* 2* math.pi/360
        x = int(math.cos(phase) * self.xRadius)+600
        y = int(math.sin(-phase) * self.yRadius)+300
        self.rect.centerx = x
        self.rect.centery = y
        
    def update1(self,xRadius,yRadius):
        self.xRadius=xRadius
        self.yRadius=yRadius
        self.degree+=0.2
        phase=self.degree* 2* math.pi/360
        x = int(math.cos(phase) * self.xRadius)+580
        y = int(math.sin(-phase) * self.yRadius)+320
        self.rect.centerx = x
        self.rect.centery = y
    def draw(self):
        screen.blit(self.image,self.rect)
        
class Dart():
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
        
    def settings(self,scale_x,scale_y,x0,y0):
        self.image=pygame.transform.scale(self.image ,(scale_x,scale_y))
        self.x0 = x0
        self.y0= y0
        self.rect=self.image.get_rect(center=(self.x0,self.y0))
        #self.image.get_rect()
        self.dx,self.dy=4.8,2.4
        
    def update(self):
        self.x0-=self.dx
        self.y0-=self.dy
        self.rect=self.image.get_rect(center=(self.x0,self.y0))
        
    def draw(self):
        screen.blit(self.image,self.rect)
 
didymos=[0]*4
for i in range(4):
    name='Didymos'+str(i)+'.png'
    didymos[i]=Asteroids(name)
    didymos[i].settings(225,195,600,300)
    
dimo=[0]*2
dimo[0]=Asteroids('Dimo0.png')
dimo[0].settings1(80,72)
dimo[1]=Asteroids('Dimo12.png')
dimo[1].settings1(80,72)

dart=Dart('spacecraft1.png')
dart.settings(50,50,800,700)
point=Dart('point.png')
point.settings(5,5,800,700)

collision=0
i0=-1
q=-1
z=0
while(True):

    i0=i0+1
    i1=round(i0/10)
    i=i1%4
    i2=i0%5
    screen.fill((0, 0, 0))
    didymos[i].draw()
    collision=dart.rect.colliderect(dimo[0].rect)
    if collision==0 and z==0:
        dimo[0].update(450,200)
        dimo[1].update(450,200)
        dimo[0].draw()
        dart.draw()
        point.draw()
        if dimo[0].degree>170:
            dart.update()
            point.update()
    
    if collision==1:
        z=1
    if z==1:
        q=q+1
        if q<=50:
            dimo[0].update1(420,170)
            dimo[1].update1(420,170)
            dimo[1].draw()
        if q>50:
            dimo[0].update1(420,170)
            dimo[0].draw()

    pygame.draw.ellipse(screen,(255,255,255),ellipse1,1)
    pygame.draw.ellipse(screen,(255,0,255),ellipse2,1)
    screen.blit(parameters,(0,550))
    screen.blit(txt_surface, (270,30))
    pygame.display.flip()
    clock.tick(60)
    
