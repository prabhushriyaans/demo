class M:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.m=[]
        self.a=[]
        self.s=[]
    def mul(self):
        for i in range(len(self.x)):
            row=[]
            for j in range(len(self.y[0])):
                sm=0
                for k in range(len(self.y)):
                    sm +=self.x[i][k] *self.y[k][j]
                row.append(sm)
            self.m.append(row)
        return self.m
    def addition(self):
        for i in range(len(self.x)):
            sm=0
            row=[]
            for j in range(len(self.y)):
                sm =self.x[i][j]+self.y[i][j]
                row.append(sm)
            self.a.append(row)
        return self.a
    def subtraction(self):
            for i in range(len(self.x)):
                sm=0
                row=[]
                for j in range(len(self.y)):
                    sm =self.x[i][j]-self.y[i][j]
                    row.append(sm)
                self.s.append(row)
            return self.s

            


