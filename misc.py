import Piece
import Board
import TestBoard

def isUpper(s):
    if s[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    return False

def getPiece(id):
    return {"p":Piece.Pawn,
     "r":Piece.Rook,
     "kn":Piece.Knight,
     "n":Piece.Knight,
     "b":Piece.Bishop,
     "q":Piece.Queen,
     "ki":Piece.King,
     "k":Piece.King}[id]

def getScore(id,colour,x,y):
    a = {"p":10,
     "r":50,
     "kn":30,
     "n":30,
     "b":30,
     "q":80,
     "ki":0,
     "k":0}
    b = getTable(id,colour)
    return a[id]+b[x][y]

def copyBoard(board):
    a = TestBoard.TestBoard()
    for i,j in zip(board.squares,range(len(board.squares))):
        for k,l in zip(i,range(len(i))):
                if k.piece != None:
                    if isinstance(k.piece,Piece.King):
                        if k.piece.colour == "white":
                            a.wKing = a.createPiece(Piece.King,j,l,k.piece.colour)
                        else:
                            a.bKing = a.createPiece(Piece.King,j,l,k.piece.colour)
                    else:
                        a.createPiece(type(k.piece),j,l,k.piece.colour)
                else:
                    a.removePiece(j,l)
    a.getKing()
    return a

def getTable(type,colour):
    a = {
    "p":[[ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
         [ 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
         [ 1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
         [ 0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
         [ 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0],
         [ 0.5,-0.5,-1.0, 0.0, 0.0,-1.0,-0.5, 0.5],
         [ 0.5, 1.0, 1.0,-2.0,-2.0, 1.0, 1.0, 0.5],
         [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
    
    "r":[[ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
         [ 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
         [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5],
         [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5],
         [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5],
         [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5],
         [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-0.5],
         [ 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]],
    
    "kn":[[-5.0,-4.0,-3.0,-3.0,-3.0,-3.0,-4.0,-5.0],
          [-4.0,-2.0, 0.0, 0.0, 0.0, 0.0,-2.0,-4.0],
          [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0,-3.0],
          [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5,-3.0],
          [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0,-3.0],
          [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0,-3.0],
          [-4.0,-2.0, 0.0, 0.5, 0.5, 0.0,-2.0,-4.0],
          [-5.0,-4.0,-3.0,-3.0,-3.0,-3.0,-4.0,-5.0]],
    
    "n":[[-5.0,-4.0,-3.0,-3.0,-3.0,-3.0,-4.0,-5.0],
         [-4.0,-2.0, 0.0, 0.0, 0.0, 0.0,-2.0,-4.0],
         [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0,-3.0],
         [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5,-3.0],
         [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0,-3.0],
         [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0,-3.0],
         [-4.0,-2.0, 0.0, 0.5, 0.5, 0.0,-2.0,-4.0],
         [-5.0,-4.0,-3.0,-3.0,-3.0,-3.0,-4.0,-5.0]],
    
    "b":[[-2.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-2.0],
         [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-1.0],
         [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0,-1.0],
         [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5,-1.0],
         [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0,-1.0],
         [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,-1.0],
         [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5,-1.0],
         [-2.0,-1.0,-1.0,-1.0,-1.0,-1.0,-1.0,-2.0]],
    
    "q":[[-2.0,-1.0,-1.0,-0.5,-0.5,-1.0,-1.0,-2.0],
         [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,-1.0],
         [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0,-1.0],
         [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0,-0.5],
         [ 0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0],
         [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0,-1.0],
         [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0,-1.0],
         [-2.0,-1.0,-1.0,-0.5,-0.5,-1.0,-1.0,-2.0]],
    
    "ki":[[-3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0],
          [-3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0],
          [-3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0],
          [-3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0],
          [-2.0,-3.0,-3.0,-4.0,-4.0,-3.0,-3.0,-2.0],
          [-1.0,-2.0,-2.0,-3.0,-3.0,-2.0,-2.0,-1.0],
          [ 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
          [ 2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]],
    
    "k":[[-3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0],
         [-3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0],
         [-3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0],
         [-3.0,-4.0,-4.0,-5.0,-5.0,-4.0,-4.0,-3.0],
         [-2.0,-3.0,-3.0,-4.0,-4.0,-3.0,-3.0,-2.0],
         [-1.0,-2.0,-2.0,-3.0,-3.0,-2.0,-2.0,-1.0],
         [ 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
         [ 2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]]
    }
    b = a[type]
    if colour == "black":
        b.reverse()
    return b


    