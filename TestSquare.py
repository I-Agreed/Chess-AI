
class TestSquare:
    def __init__(self,master,x,y):
        self.board = master
        self.x = x
        self.y = y
        self.piece = None

    
    def setPiece(self,piece):
        self.piece = piece
        self.update()
    
    def update(self):
        pass
    
    
    def getPieceType(self):
        if self.piece != None:
            return self.piece.type
        else:
            return " "
    
    def highlight(self):
        pass

    
    def unHighlight(self):
        pass