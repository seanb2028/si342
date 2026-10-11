# Sean Beckford
class Pos:
    def __init__(self,row,col):
        self.row = row
        self.col = col

    def __str__(self):
        return Pos.disp(self.row,self.col)

    def __repr__(self):
        return Pos.disp(self.row,self.col)

    def __eq__(self,other):
        return self.row == other.row and self.col == other.col

    def len(self):
        return self.row + self.col
    
    sep = ":"

    def disp(v1,v2):
        return f"({v1}{Pos.sep}{v2})";

    def step(self,dir):
        directions = {
            "N" : (-1,0),
            "E" : (0,1),
            "S" : (1,0),
            "W" : (0,-1)
        }

        self.row += directions[dir][0]
        self.col += directions[dir][1]

class LabPos(Pos): # means LabPos extends Pos
    def __init__(self,row,col,lab):
        Pos.__init__(self,row,col)  # calls the constructor from Pos 
        self.lab = lab
    
    def __str__(self):  # override the __str__(self) from class Pos 
        return Pos.__str__(self) + ":" + self.lab

    def labMerge(A):
        return "".join(p[2] for p in A)