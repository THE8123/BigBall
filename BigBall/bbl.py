import pygame
import os
import webbrowser
import time
import math

class Platform:
    def __init__(self):
        self.img = pygame.image.load('pl.png')
        self.speed = 0
        self.x = 362
        self.y = 572
    def upd(self):
        screen.blit(self.img, (self.x,self.y))
        if self.x <=0: self.speed = speed
        elif self.x >= 702: self.speed = -speed
        self.x += self.speed

class Block:
    def __init__(self,hp,x,y):
        self.img = pygame.image.load('block.png')
        self.hp = hp
        self.x = x
        self.y = y
        self.x2 = x+10
        self.y2 = y+10


class Ball:
    def __init__(self,speedx,speedy,x,y):
        self.speedx = speedx
        self.speedy = speedy
        self.x = x
        self.y = y
        self.img = pygame.image.load('ball.png')

    def logic(self):
        if self.x <= 0 or self.x >= 771: self.speedx = -self.speedx
        # if self.y <= 0 or self.y >= 571: self.speedy = -self.speedy
        if self.y <= 0: self.speedy = -self.speedy
        if abs(self.y+29-572)<=2 and platform.x-28 <= self.x <= platform.x+97:
            self.speedy = -self.speedy
            self.y += self.speedy
        for i in blocks:
            if min(i.x2,self.x+29) >= max(i.x,self.x) and min(i.y2,self.y+29) >= max(i.y,self.y):
                i.hp -=1
                self.speedy = -self.speedy
                self.y += self.speedy

    def upd(self):
        screen.blit(self.img,(self.x,self.y))
        self.x += self.speedx
        self.y += self.speedy


def blocksupd():
    global blocks
    blocks.sort(key=lambda x:-x.hp)
    end = -1
    for i in range(len(blocks)):
        if blocks[i].hp == 0:
            end = i

            break
    if end != -1:
        blocks = blocks[:end]


def frame():
    blocksupd()
    platform.upd()
    ball.logic()
    ball.upd()
    for block in blocks:
        screen.blit(block.img,(block.x,block.y))



blocks = []
for y in range(5,250,25):
    for x in range(5,786,25):
        blocks.append(Block(1,x,y))
for x in range(0,310,9):
    blocks.append(Block(999, x, 290))
for x in range(490,800,9):
    blocks.append(Block(999, x, 290))

speed = 0.75
def game():
    global platform, ball, screen
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("bara bara bara")
    bg = (0,0,0)
    platform = Platform()
    ball = Ball(0.4,0.4,400,300)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # webbrowser.open('https://vk.com/im?peers=594802001_c32_-21092922&sel=498757294&z=photo498757294_457248966%2Fmail3571288')
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    platform.speed = speed
                if event.key == pygame.K_a:
                    platform.speed = -speed
                if event.key == pygame.K_SPACE:
                    time.sleep(3)
                if event.key == pygame.K_8:
                    os.startfile(__file__)
                    exit()

        screen.fill(bg)
        frame()
        pygame.display.flip()
        if len(blocks) == 0:
            print('maladec!1!1')

game()

'''
         *%%.                                                                                               %%%!
        $BBBBBBBBBB$**!                                                                                  @BBBBBBS*
          *&#####SBBBBBB&****!                        !.                                                 BBB&%@BBB#!
                   .!@SBBBBBBBBBBS%!!!.              @BB!                                                 .     $BBB!
                       .....%SSSBBBBBBBBB@!          @BBB                                                        @BBB
                                 ...!&#SBBBBS@        #BB@       !!@BB&.                      !!!!!.              #BB.
                                       @BBBBB#        *BBB    %SBBBBBBB.                 .%#SBBBBBBB*             &BBB
                               ..%#BBBBBBBB&.          #BB$ *BBBBS$!!                 !&BBBBBBB$!!!!               SBB
                            !&BBBBBBS$*!                BBB!BBB@                    .&BBBB&*                       SBB
                        .@SBBBBB&**                     #BBBBB.                    %BBB#!                          SBB
                     %#BBBBB#%.                         *BBBB                     $BBB*                            #BB
                   %BBBBB$*                           $BBBBBB                   .BBBB.                            %BBB
               .@SBBBB@                            %BBBBB!&BB#!                 @BB@                              #BB%
            %&BBBBB#.                           !SBBBB@%   &BBB                %BB#                              *BBB
       *@BBBBBBS$!                           %&BBBB&.       BBB               .BBB%                             !BBB!
    !#BBBBS$$!                           .@BBBBBS@!         %BBB              *BB&                              &BB@
   !BBBBS$*!!*%%%%*                      &BBB&*              %BBS             BBS!                             $BBB.
    $#BBBBBBBBBBBBBBBBBBBB&%%%*                               BBB&           &BB#                             %BBB*
                 %######SBBBBBBBBBBS%******!                  .BBB*          BBB!                            *BBB%
                          .  %##SSBBBBBBBBBBBBBB$              @BB&          BB#                            .BBB$
                                   ........$SSSB@                .           BB#                           &BBB@
                                                                             BBB!                          &BS%
                                                                             &BBB!
                                                                              &BBBBBSSSSS@
                                                                               .*#BBBBBBBS
                                                                                                          *&&!
                                                                                                        !#BBBB.
          @BB                                                                    %&%                    BBBBBB#
          SBB                                                                 *SBBBBBB*                 BBBBBB.
          #BB                       *BBBBBBBS@@$! !BB*    .%!     %BBBBBBBBS .BBB@%@BBBB                #BBB#.
         %BBB                       .$@$SBBBBBBB# %BB$   @BBB    *BB#$@@@@@% .BBB!   SBB
         #BBBBBB&.                      &BB       *BB*   BBB*    *BB*         $BBB% !BBB
         #BBB@SBBB@  !SS!   *!         *BBB       *BB&%%*BBB     !BB*          $BBBBBBB%
         #BB   %BBB  $BB! %BBB         #BB$       %BBBBBBBBB     #BBBBBBBS      !BBBBBB.
         #BB**!BBB#  $BB$&BBBB         #BB       !BBB%   BBB    !BB#@####&     *BBB##BBB.
         &BBBBBBBB   %BBBBBBB$         #BB.      *BB@   #BBB    *BB%          @BBS.  @BBB
          . *#S$.      .. SBB          *#&       .&#!   BBB    .BBB*         BBBB% .!&BBB
                         .BBB                           SBB    !BBBBBBBB&    &BBBBBBBBBB.
                     .&@*BBB&                            !.     .!&BBBBBS      !!&SS#!!.
                     $BBBBB#
                      !!!!.
'''









































