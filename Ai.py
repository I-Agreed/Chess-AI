import misc
class Ai:
    def __init__(self,board):
        self.board = board
        self.colour = "black"
        self.rec = 1
    
    def evalScore(self,board=None):
        if board == None:
            board = self.board
        w = 0
        b = 0
        for i in board.pieces():
            if i.colour == "white":
                w += misc.getScore(i.type,"white",i.x,i.y)
            
            if i.colour == "black":
                b += misc.getScore(i.type,"black",i.x,i.y)
        
        white = False
        for i in board.pieces("white"):
            if i.hasMove():
                white = True
                break
        
        if not white:
            if board.wKing.underAttack():
                b += 9999
            #else:
            #    self.master.title("Stalemate")
        black = False
        for i in board.pieces("black"):
            if i.hasMove():
                black = True
                break
        
        if not black:
            if board.bKing.underAttack():
                w += 9999
        #else:
        #    self.master.title("Stalemate")
        
        return b,w
    
    def getMoves(self,board,colour="black",minimax=None):
        #set minimax to true for min and false for max
        a = []
        if minimax == None:
            for i in board.pieces(colour):
                for j in range(board.w):
                    for k in range(board.h):
                        if i.canMove(j,k):
                            b = misc.copyBoard(board)
                            b.movePiece(i.x,i.y,j,k)
                            c = self.evalScore(b)
                            a.append([c[0]-c[1],b,[i.x,i.y,j,k]])
        elif minimax:
            for i in board.pieces(colour):
                for j in range(board.w):
                    for k in range(board.h):
                        if i.canMove(j,k):
                            b = misc.copyBoard(board)
                            b.movePiece(i.x,i.y,j,k)
                            c = self.evalScore(b)
                            if len(a) == 0:
                                a = [[c[0]-c[1],b,[i.x,i.y,j,k]]]
                            if c[0]-c[1] < a[0][0]:
                                a = [[c[0]-c[1],b,[i.x,i.y,j,k]]]
        else:
            for i in board.pieces(colour):
                for j in range(board.w):
                    for k in range(board.h):
                        if i.canMove(j,k):
                            b = misc.copyBoard(board)
                            b.movePiece(i.x,i.y,j,k)
                            c = self.evalScore(b)
                            if len(a) == 0:
                                a = [[c[0]-c[1],b,[i.x,i.y,j,k]]]
                            if c[0]-c[1] > a[0][0]:
                                a = [[c[0]-c[1],b,[i.x,i.y,j,k]]]
        return a

    def minimax(self,inp):

        out = inp[2]
        a = inp
        for i in range(self.rec):
            whiteMoves = self.getMoves(a[1],"white",False)
            if len(whiteMoves) == 0:
                break
            c = whiteMoves[0]
            for j in whiteMoves:
                if j[0] > c[0]:
                    c = j
            
            blackMoves = self.getMoves(c[1],minimax=True)
            if len(blackMoves) == 0:
                break
            a = blackMoves[-1]
            for j in blackMoves:
                if j[0] < a[0]:
                    a = j
            

        return [a[0],a[1],out]

            
    def evalMove(self):
        
        a = self.getMoves(self.board)
        b = []
        for i in a:
            b.append(self.minimax(i))
            
        c = b[0]
        for i in b:
            if i[0] > c[0]:
                c = i

        return c[2]
        
            
                    