#Thomas Jansen
#thomas@ronmix.com

from guizero import App, Waffle, Picture, Box, Text
import os


white = (0, 0, 0)
black = (255,255,255)
bg_grey = (40, 36, 44)

King_Black = r"Chess_Pieces\King_B.png"
King_White = r"Chess_Pieces\King_W.png"
Queen_Black = r"Chess_Pieces\Queen_B.png"
Queen_White = r"Chess_Pieces\Queen_W.png"
Bischop_Black = r"Chess_Pieces\Bischop_B.png"
Bischop_White = r"Chess_Pieces\Bischop_W.png"
Horse_Black = r"Chess_Pieces\Horse_B.png"
Horse_White = r"Chess_Pieces\Horse_W.png"
Rook_Black = r"Chess_Pieces\Rook_B.png"
Rook_White = r"Chess_Pieces\Rook_W.png"
Pawn_Black = r"Chess_Pieces\Pawn_B.png"
Pawn_White = r"Chess_Pieces\Pawn_W.png"


app = App(title="Chess", bg=bg_grey, height=685, width=685, layout="grid")

#Does not work
#board = Waffle(app, height=8, width=8, dim=80, bg="grey", grid=[0,0])

#Make the board checkered
'''
for q in range (0,8,2):
    for i in range(0,8,2):
        board[i,q].color = black
for q in range (1,8,2):
    for i in range(1,8,2):
        board[i,q].color = black

for q in range (0,8,2):
    for i in range(1,8,2):
        board[i,q].color = white
for q in range (1,8,2):
    for i in range(0,8,2):
        board[i,q].color = white
'''

box0_0 = Box(app, layout='grid', grid=[0,0], border=1) 
box0_1 = Box(app, layout='grid', grid=[0,1], border=1) 
box0_2 = Box(app, layout='grid', grid=[0,2], border=1) 
box0_3 = Box(app, layout='grid', grid=[0,3], border=1) 
box0_4 = Box(app, layout='grid', grid=[0,4], border=1) 
box0_5 = Box(app, layout='grid', grid=[0,5], border=1) 
box0_6 = Box(app, layout='grid', grid=[0,6], border=1) 
box0_7 = Box(app, layout='grid', grid=[0,7], border=1) 
box1_0 = Box(app, layout='grid', grid=[1,0], border=1) 
box1_1 = Box(app, layout='grid', grid=[1,1], border=1) 
box1_2 = Box(app, layout='grid', grid=[1,2], border=1) 
box1_3 = Box(app, layout='grid', grid=[1,3], border=1) 
box1_4 = Box(app, layout='grid', grid=[1,4], border=1) 
box1_5 = Box(app, layout='grid', grid=[1,5], border=1) 
box1_6 = Box(app, layout='grid', grid=[1,6], border=1) 
box1_7 = Box(app, layout='grid', grid=[1,7], border=1) 
box2_0 = Box(app, layout='grid', grid=[2,0], border=1) 
box2_1 = Box(app, layout='grid', grid=[2,1], border=1) 
box2_2 = Box(app, layout='grid', grid=[2,2], border=1) 
box2_3 = Box(app, layout='grid', grid=[2,3], border=1) 
box2_4 = Box(app, layout='grid', grid=[2,4], border=1) 
box2_5 = Box(app, layout='grid', grid=[2,5], border=1) 
box2_6 = Box(app, layout='grid', grid=[2,6], border=1) 
box2_7 = Box(app, layout='grid', grid=[2,7], border=1) 
box3_0 = Box(app, layout='grid', grid=[3,0], border=1) 
box3_1 = Box(app, layout='grid', grid=[3,1], border=1) 
box3_2 = Box(app, layout='grid', grid=[3,2], border=1) 
box3_3 = Box(app, layout='grid', grid=[3,3], border=1) 
box3_4 = Box(app, layout='grid', grid=[3,4], border=1) 
box3_5 = Box(app, layout='grid', grid=[3,5], border=1) 
box3_6 = Box(app, layout='grid', grid=[3,6], border=1) 
box3_7 = Box(app, layout='grid', grid=[3,7], border=1) 
box4_0 = Box(app, layout='grid', grid=[4,0], border=1) 
box4_1 = Box(app, layout='grid', grid=[4,1], border=1) 
box4_2 = Box(app, layout='grid', grid=[4,2], border=1) 
box4_3 = Box(app, layout='grid', grid=[4,3], border=1) 
box4_4 = Box(app, layout='grid', grid=[4,4], border=1) 
box4_5 = Box(app, layout='grid', grid=[4,5], border=1) 
box4_6 = Box(app, layout='grid', grid=[4,6], border=1) 
box4_7 = Box(app, layout='grid', grid=[4,7], border=1) 
box5_0 = Box(app, layout='grid', grid=[5,0], border=1) 
box5_1 = Box(app, layout='grid', grid=[5,1], border=1) 
box5_2 = Box(app, layout='grid', grid=[5,2], border=1) 
box5_3 = Box(app, layout='grid', grid=[5,3], border=1) 
box5_4 = Box(app, layout='grid', grid=[5,4], border=1) 
box5_5 = Box(app, layout='grid', grid=[5,5], border=1) 
box5_6 = Box(app, layout='grid', grid=[5,6], border=1) 
box5_7 = Box(app, layout='grid', grid=[5,7], border=1) 
box6_0 = Box(app, layout='grid', grid=[6,0], border=1) 
box6_1 = Box(app, layout='grid', grid=[6,1], border=1) 
box6_2 = Box(app, layout='grid', grid=[6,2], border=1) 
box6_3 = Box(app, layout='grid', grid=[6,3], border=1) 
box6_4 = Box(app, layout='grid', grid=[6,4], border=1) 
box6_5 = Box(app, layout='grid', grid=[6,5], border=1) 
box6_6 = Box(app, layout='grid', grid=[6,6], border=1) 
box6_7 = Box(app, layout='grid', grid=[6,7], border=1) 
box7_0 = Box(app, layout='grid', grid=[7,0], border=1) 
box7_1 = Box(app, layout='grid', grid=[7,1], border=1) 
box7_2 = Box(app, layout='grid', grid=[7,2], border=1) 
box7_3 = Box(app, layout='grid', grid=[7,3], border=1) 
box7_4 = Box(app, layout='grid', grid=[7,4], border=1) 
box7_5 = Box(app, layout='grid', grid=[7,5], border=1) 
box7_6 = Box(app, layout='grid', grid=[7,6], border=1) 
box7_7 = Box(app, layout='grid', grid=[7,7], border=1) 


picture = Picture(box0_0, image=King_Black, grid=[0,0])
picture = Picture(box0_1, image=King_White, grid=[0,0])


app.display()