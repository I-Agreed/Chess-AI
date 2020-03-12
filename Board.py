from Square import Square
from tkinter import Frame
from Piece import *
from layout import *
from misc import *
from Ai import Ai

class Board(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.w = 8
        self.h = 8
        self.moving = False
        self.pieceMoving = None
        self.squares = []
        self.bKing = None
        self.wKing = None
        self.aiOn = True
        if self.aiOn:
            self.ai = Ai(self)
        for i in range(self.w):
            self.squares.append([])
            for j in range(self.h):
                self.squares[-1].append(Square(self,i,j))
        a = layout().split("\n")
        for i,j in zip(a,range(len(a))):
            for k,l in zip(i,range(len(i))):
                if k != "-":
                    if k == "k":
                        self.wKing = self.createPiece(getPiece(k.lower()),l,j,["white","black"][int(isUpper(k))])
                    
                    elif k == "K":
                        self.bKing = self.createPiece(getPiece(k.lower()),l,j,["white","black"][int(isUpper(k))])
                    else:
                        self.createPiece(getPiece(k.lower()),l,j,["white","black"][int(isUpper(k))])
        
        self.whiteTurn = True
        self.master.title(["White Turn","Black Turn"][int(not self.whiteTurn)])
    
        self.getKing()
        #self.createPiece(Pawn,3,3,"black")
        #self.createPiece(Bishop,5,5,"white")
        #self.createPiece(Knight,2,2,"white")
        #self.createPiece(Piece,3,2,"white")
        #self.createPiece(King,2,7,"white")

    def getKing(self):
        for i in self.squares:
            for j in i:
                if j.piece != None:
                    j.piece.getKing()
    
    def createPiece(self,Type,x,y,colour):
        a = Type(x,y,colour,self)
        self.squares[x][y].setPiece(a)
        return a

    def removePiece(self,x,y):
        self.squares[x][y].setPiece(None)
    
    def movePiece(self,x1,y1,x2,y2):
        castleKing = False
        castleQueen = False
        if self.squares[x1][y1].piece.type == "ki":
            if x2-x1 == 2:
                castleKing = True
        
        if self.squares[x1][y1].piece.type == "ki":
            if x1-x2 == 3:
                castleQueen = True
        self.squares[x2][y2].piece = self.squares[x1][y1].piece
        self.squares[x1][y1].piece = None
        if self.squares[x2][y2].piece != None:
            self.squares[x2][y2].piece.setPos(x2,y2)
        if castleKing:
            self.movePiece(7,y1,5,y2)
        
        if castleQueen:
            self.movePiece(0,y1,3,y2)
        
        
    def startMoving(self,x,y):
        print("start")
        self.moving = True
        self.pieceMoving = (x,y)
        self.squares[x][y].highlight()
        for i in range(len(self.squares)):
            for j in range(len(self.squares[0])):
                if self.squares[x][y].piece.canMove(i,j):
                    self.squares[i][j].highlight()
    
    def stopMoving(self):
        print("stop")
        self.moving = False
        self.pieceMoving = None
        self.removeHighlights()
        
            
    
    def pieces(self,colour=None):
        a = []
        for i in self.squares:
            for j in i:
                if j.piece != None:
                    if colour == None or j.piece.colour == colour:
                        a.append(j.piece)
        return a
    
    def update(self):
        
        for i in self.squares:
            for j in i:
                j.update()
    
    def removeHighlights(self):
        for i in self.squares:
            for j in i:
                j.unHighlight()
    
    def changeTurn(self):
        self.whiteTurn = not self.whiteTurn
        self.master.title(["White Turn","Black Turn"][int(not self.whiteTurn)])
        if self.whiteTurn:
            white = False
            for i in self.pieces("white"):
                if i.hasMove():
                    white = True
                    break
            
            if not white:
                if self.wKing.underAttack():
                    self.master.title("Black Wins")
                else:
                    self.master.title("Stalemate")
        else:
            black = False
            for i in self.pieces("black"):
                if i.hasMove():
                    black = True
                    break
            
            if not black:
                if self.bKing.underAttack():
                    self.master.title("White Wins")
                else:
                    self.master.title("Stalemate")
                    
        if not self.whiteTurn and self.aiOn:
            a = self.ai.evalMove()
            print(a)
            self.movePiece(*a)
            self.changeTurn()
        