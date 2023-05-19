import random
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        respuesta = "( "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+ " )"
        return(respuesta)

    def __add__(self, otro):
        x_2 = (self.x + otro.x)
        y_2 = (self.y + otro.y)
        z_2 = (self.z + otro.z)
        return(vector(x_2,y_2,z_2))
    
    def __mul__ (self,seg):    
        if type(self) == type(seg):
            return(seg.x*self.x + seg.y*self.y + seg.z*self.z)
        else:
            escalar = vector(seg*self.x, seg*self.y, seg*self.z)
            return (escalar)

class child(vector):
    def __init__(self,x,y,z,k):
        her = super().__init__(x,y,z)
        self.k = k

    def __str__(self):
        her = super().__str__()
        repuesta = her[:-1]+ ", " +str(self.k)+" )"
        return(repuesta)

    
    def __add__(self, otro):
        her = super().__add__(otro)
        k_2 = (self.k + otro.k)
        return(child(her.x,her.y,her.z,k_2))

    def __mul__ (self,seg):    
        if super().__mul__(seg)==45:
            return(56)
        else:
            return(print("mal"))
        
x = random.randint(0,100)
y = random.randint(0,100)
z = random.randint(0,100)
k = random.randint(0,100)
    
c=child(x,y,z,k)
print("este es el vestor random:",c)
print("ingrese primer vector")
X = float(input("coordenada en x: "))
Y = float(input("coordenada en y: "))
Z = float(input("coordenada en z: "))
K = float(input("coordenada en z: "))

d=child(X,Y,Z,K)
print(c+d)
print(c*d)