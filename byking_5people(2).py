import pygame
pygame.init()
from os import path
screen= pygame.display.set_mode((1200,900))
img_dir = path.join(path.dirname(__file__), 'img')
imga_dir = path.join(path.dirname(__file__), 'imga')
imgc_dir = path.join(path.dirname(__file__), 'imgc')
imgd_dir = path.join(path.dirname(__file__), 'imgd')
imge_dir = path.join(path.dirname(__file__), 'imge')
cyclist=[0]*12
cyclist2=[0]*30
cyclist3=[0]*8
cyclist4=[0]*13
cyclist5=[0]*10

for i in range(12):
    cyclist[i]=pygame.image.load(path.join(img_dir,str(i)+'.png'))
    cyclist[i]=pygame.transform.scale(cyclist[i],(140,140))

for i in range(30):
    cyclist2[i]=pygame.image.load(path.join(imga_dir,'a'+str(i)+'.png'))
    cyclist2[i]=pygame.transform.scale(cyclist2[i],(130,130))
    
for i in range(8):
    cyclist3[i]=pygame.image.load(path.join(imgc_dir,'c'+str(i)+'.png'))
    cyclist3[i]=pygame.transform.scale(cyclist3[i],(170,150))
    
for i in range(13):
    cyclist4[i]=pygame.image.load(path.join(imgd_dir,'d'+str(i)+'.png'))
    cyclist4[i]=pygame.transform.scale(cyclist4[i],(240,180))
    
for i in range(10):
    cyclist5[i]=pygame.image.load(path.join(imge_dir,'e'+str(i)+'.png'))
    cyclist5[i]=pygame.transform.scale(cyclist5[i],(200,200))

bground=pygame.image.load('bground.png')    
class Biker():
    def __init__(self,image,y):
        self.image=image
        self.rect=self.image.get_rect(center=(0,y))
        self.k=0
        self.dx=0
    def update(self,q,dx,Q1,Q2):
        self.dx=dx
        self.k+=1
        k1=self.k//Q1
        k2=k1%Q2
        if q==1:
            self.image=cyclist[k2]
        if q==2:
            self.image=cyclist2[k2]
        if q==3:
            self.image=cyclist3[k2]
        if q==4:
            self.image=cyclist4[k2]
        if q==5:
            self.image=cyclist5[k2]
        self.rect.x += self.dx
        if self.rect.x > 1100:
            self.rect.x =-300
    def draw(self):
        screen.blit(self.image,self.rect)

clock = pygame.time.Clock()
player1=Biker(cyclist[0],100)
player2=Biker(cyclist2[0],270)
player3=Biker(cyclist3[0],450)
player4=Biker(cyclist4[0],700)
player5=Biker(cyclist5[0],800)

bground=pygame.image.load('bground1.png')  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(bground, (0, 0))
    player1.update(1,4,2,12)
    player1.draw()
    player2.update(2,6,2,12)
    player2.draw()
    player3.update(3,3,10,8)
    player3.draw()
    player4.update(4,2,10,8)
    player4.draw()
    player5.update(5,4,4,10)
    player5.draw()
    clock.tick(50)   
    pygame.display.update()
    
#pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
#path.join(img_dir, "starfield.png")    
#'img/meteor1.png'