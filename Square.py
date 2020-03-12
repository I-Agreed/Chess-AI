from tkinter import *
import images
class Square(Canvas):
    def __init__(self,master,x,y):
        Canvas.__init__(self,master)
        self.board = master
        self.x = x
        self.y = y
        self.piece = None
        self.colour = ["white","black"][(x+y)%2]
        self.textColour = ["white","black"][(x+y+1)%2]
        self.rect,self.text,self.image = None,None,None
        if self.piece != None:
            self.delete("all")
            self.rect = self.create_rectangle(10,10,78,78,fill=self.piece.colour,outlineborder=self.piece.opColour)
            self.text = self.create_text(45,45,text=self.piece.type.upper(),fill=self.piece.opColour,font=("Arial", 18, "bold"))
        self.config(bg=self.colour,width=90,height=90,borderwidth=0,highlightthickness=0)
        self.grid(column=x,row=y)
        self.bind("<Button-1>",self.click)
    
    def setPiece(self,piece):
        self.piece = piece
        self.update()
    
    def update(self):
        self.delete("all")
        self.colour = ["white","black"][(self.x+self.y)%2]
        self.textColour = ["white","black"][(self.x+self.y+1)%2]
        self.rect,self.text,self.image = None,None,None
        if self.piece != None:

            self.rect = self.create_rectangle(10,10,78,78,fill=self.piece.colour,outline=self.piece.opColour)
            self.text = self.create_text(45,45,text=self.piece.type.upper(),fill=self.piece.opColour,font=("Arial", 18, "bold"))
    def click(self,event=None):
        if not self.board.moving and self.piece != None and (self.piece.colour == "white") == self.board.whiteTurn:
            self.board.startMoving(self.x,self.y)
            self.board.update()
        
        
        
        elif self.board.moving:
            x,y = self.board.pieceMoving
            if x == self.x and y == self.y:
                self.board.stopMoving()
                
            elif self.board.squares[x][y].piece.canMove(self.x,self.y):
                self.board.movePiece(x,y,self.x,self.y)
                self.board.changeTurn()
                self.board.stopMoving()
            
        
            self.board.update()
            
    
    def getPieceType(self):
        if self.piece != None:
            return self.piece.type
        else:
            return " "
    
    def highlight(self):
        if self.colour == "black":
            self.config(bg="#005500")
        
        elif self.colour == "white":
            self.config(bg="#44cc44")
    
    def unHighlight(self):
        if self.colour == "black":
            self.config(bg="#000000")
        
        elif self.colour == "white":
            self.config(bg="#ffffff")
        