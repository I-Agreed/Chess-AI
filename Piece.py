import Board
import misc


def getCardinalPoints(x1,y1,x2,y2):
    a = []
    if x1 == x2:
        b = (y1-y2)/abs(y1-y2)
        a = list(range(0,abs(y1-y2)))[1:]
        for i in a:
            a[a.index(i)] = (int(x1),int(b*i+y2))
    
    elif y1 == y2:
        b = (x1-x2)/abs(x1-x2)
        
        a = list(range(0,abs(x1-x2)))[1:]
        for i in a:
            a[a.index(i)] = (int(b*i+x2),int(y1))

    return a

def getDiagonalPoints(x1,y1,x2,y2):
    a = []
    x3 = x1-x2
    x3*=-1
    y3 = y1-y2
    y3*=-1
    if x3 == 0 or y3 == 0:
        return a
    xp = x3/abs(x3)
    yp = y3/abs(y3)
    if abs(x3) == abs(y3):
        for i in range(abs(x3))[1:]:
            a.append((int(i*xp+x1),int(i*yp+y1)))
    return a

class Piece:
    def __init__(self,x,y,colour,board):
        self.board = board
        self.type = "u"
        self.x = x
        self.y = y
        self.colour = colour
        self.opColour = ["black","white"][["white","black"].index(self.colour)]
        self.hasMoved = False
        
    def getKing(self):
        if self.colour == "white":
            self.king = self.board.wKing
            
        else:
            self.king = self.board.bKing 
    
    def setPos(self,x,y):
        self.x = x
        self.y = y
        self.hasMoved = True
    
    def direction(self):
        if self.colour == "white":
            return -1
        else:
            return 1
    
    def hasMove(self):
        for i in range(len(self.board.squares)):
            for j in range(len(self.board.squares[0])):
                if self.canMove(i,j):
                    return True
    
    def underAttack(self):
        for k in self.board.pieces(self.opColour):
                if k != None and k.canMove(self.x,self.y,king=True,checkInCheck=False):
                    return True

        return False
    def canMove(self,x,y,king=False,checkInCheck=True,checkKing=True):
        if x not in range(0,8) or y not in range(0,8):
            return False

        currentPiece = self.board.squares[x][y].piece
        if checkInCheck:

            a = misc.copyBoard(self.board)
            a.movePiece(self.x,self.y,x,y)

            if self.colour == "white":
                if a.wKing.underAttack():
                    return False
            else:
                if a.bKing.underAttack():
                    return False
            del a
        
        if currentPiece != None and currentPiece.colour == self.colour:
            return False
        
        if self.type == "u":
            return True
        
        elif self.type == "p":

            if y == self.y + self.direction() and x == self.x and (currentPiece == None and not king):
                return True
            elif not self.hasMoved and y == self.y + 2*self.direction() and x == self.x and (currentPiece == None and not king):
                return True
            if y == self.y + self.direction() and abs(x-self.x) == 1 and (currentPiece != None or king):
                return True
        
        elif self.type == "r":
            if y == self.y or x == self.x:
                a = getCardinalPoints(self.x,self.y,x,y)
                for i in a:
                    if self.board.squares[i[0]][i[1]].piece != None:
                        return False
                return True
        
        elif self.type == "b":
            x2 = x-self.x
            y2 = y-self.y
            if abs(x2) == abs(y2):
                a = getDiagonalPoints(self.x,self.y,x,y)
                for i in a:
                    if self.board.squares[i[0]][i[1]].piece != None:
                        return False
                return True
        
        elif self.type == "q":
            x2 = x-self.x
            y2 = y-self.y
            if (abs(x2) == abs(y2)) or y == self.y or x == self.x:
                a = getCardinalPoints(self.x,self.y,x,y)
                for i in a:
                    if self.board.squares[i[0]][i[1]].piece != None:
                        return False
                a = getDiagonalPoints(self.x,self.y,x,y)
                for i in a:
                    if self.board.squares[i[0]][i[1]].piece != None:
                        return False
                return True
        
        elif self.type == "kn":
            a = abs(x-self.x)
            b = abs(y-self.y)
            if (a == 1 and b == 2) or (a == 2 and b == 1):
                return True
        
        elif self.type == "ki" and checkKing:
            a = abs(x-self.x)
            b = abs(y-self.y)
            if b == 0 and not self.hasMoved:
                if x == 6 and self.board.squares[x+1][y].piece != None and\
                    self.board.squares[x-1][y].piece == None and self.board.squares[x][y].piece == None \
                        and not self.board.squares[x+1][y].piece.hasMoved:
                    return True
                
                elif x == 2 and self.board.squares[x-2][y].piece != None and\
                    self.board.squares[x-1][y].piece == None and self.board.squares[x][y].piece == None \
                        and self.board.squares[x+1][y].piece == None and not self.board.squares[x-2][y].piece.hasMoved:
                    
                    return True
            if a <= 1 and b <= 1:
                d = misc.copyBoard(self.board)
                d.movePiece(self.x,self.y,x,y)
                if not d.squares[x][y].piece.underAttack():
                    return True
            
        
        return False

            
    
    def move(self,x,y):
        pass

class Pawn(Piece):
    def __init__(self,x,y,colour,board):
        Piece.__init__(self,x,y,colour,board)
        self.type = "p"

class Bishop(Piece):
    def __init__(self,x,y,colour,board):
        Piece.__init__(self,x,y,colour,board)
        self.type = "b"

class Rook(Piece):
    def __init__(self,x,y,colour,board):
        Piece.__init__(self,x,y,colour,board)
        self.type = "r"

class Queen(Piece):
    def __init__(self,x,y,colour,board):
        Piece.__init__(self,x,y,colour,board)
        self.type = "q"

class Knight(Piece):
    def __init__(self,x,y,colour,board):
        Piece.__init__(self,x,y,colour,board)
        self.type = "kn"

class King(Piece):
    def __init__(self,x,y,colour,board):
        Piece.__init__(self,x,y,colour,board)
        self.type = "ki"


