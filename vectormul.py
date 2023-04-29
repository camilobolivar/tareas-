class vector:
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        respuesta = "( "+str(self.x)+" , "+str(self.y)+", "+str(self.z)+" )"
        return(respuesta) 
    
    def __add__(self, otro):
        x_1 = (self.x + otro.x)
        x_2 = (self.y + otro.y)
        z_2 = (self.z + otro.z)
        return(vector(x_1,x_2,z_2))

    def __mul__ (self,seg):    
        if type(self) == type(seg):
            return(seg.x*self.x + seg.y*self.y + seg.z*self.z)
        else:
            escalar = vector(seg*self.x, seg*self.y, seg*self.z)
            return (escalar)
        
    def _rmul_ (self,seg):
        if type(self) == type(seg):
           return(seg.x*self.x + seg.y*self.y + seg.z*self.z)
           
        else:
            respuesta = vector(self.x*seg, self.y*seg, self.z*seg)
            return(respuesta)
            

   

print("ingrese primer vector")
X_1 = float(input("coordenada en x: "))
Y_1 = float(input("coordenada en y: "))
z_1 = float(input("coordenada en z: "))
print("ingrese segundo vector")
X_2 = float(input("coordenada en x: "))
Y_2 = float(input("coordenada en y: "))
Z_2 = float(input("coordenada en z: "))
v_1 = vector(X_1,Y_1,z_1)
v_2 = vector(X_2,Y_2,Z_2)


respuestasuma = (v_1+v_2)
print(respuestasuma)

repuestamultiplicacion = (v_1*v_2)
print(repuestamultiplicacion)

respuestaescalar = (v_1*3)
print(respuestaescalar)