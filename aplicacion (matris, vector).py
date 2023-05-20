class Vector:
  def __init__(self, coordenada_x, coordenada_y, coordenada_z):
    self.x = coordenada_x
    self.y = coordenada_y
    self.z = coordenada_z
    self.magnitud = (self.x**2 + self.y**2 + self.z**2)**0.5
  def __str__(self):
    respuesta = "( "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+" )"
    return(respuesta)
  
  
  def productovectorial(self, seg):
    return(self.y*seg.z-seg.y*self.z, \
                         seg.x*self.z-self.x*seg.z,  \
                         self.x*seg.y-seg.x*self.y)
  
x_1 = float(input("ingrese coordenada x_1: "))
y_1 = float(input("ingrese coordenada y_1: "))
z_1 = float(input("ingrese coordenada z_1: "))


x_2 = float(input("ingrese coordenada x_2: "))
y_2 = float(input("ingrese coordenada y_2: "))
z_2 = float(input("ingrese coordenada z_2: "))

vec_10=Vector(x_1, y_1, z_1)
vec_20=Vector(x_2, y_2, z_2)
print("posicion del vector 1:", vec_10)
print("posicion del vector 2:", vec_20)
print("magnitud del vector 1:", vec_10.magnitud)
print("magnitud del vector 2:", vec_20.magnitud)
print("vector perpendicular a los dos vectores:", \
      vec_10.productovectorial(vec_20) )




class matriz:
    def __init__(self, lista):
        self.a00=lista[0][0]
        self.a01=lista[0][1]
        self.a10=lista[1][0]
        self.a11=lista[1][1]

    def __str__(self):
        return "| {}, {} |\n| {}, {} |".format(self.a00,self.a01,self.a10,self.a11)
    
    def __add__(self,otro):
        a00 = self.a00 + otro.a00
        a01 = self.a01 + otro.a01
        a10 = self.a10 + otro.a10
        a11 = self.a11 + otro.a11
        return matriz([[a00,a01], [a10,a11]])

    def __sub__(self,otro):
        a00 = self.a00 - otro.a00
        a01 = self.a01 - otro.a01
        a10 = self.a10 - otro.a10
        a11 = self.a11 - otro.a11
        return matriz([[a00,a01], [a10,a11]])

    def __mul__(self,otro):
        if type(otro) == type(self):
            print("solo escalares por una matriz")
        else:
            a00 = self.a00 * otro
            a01 = self.a01 * otro
            a10 = self.a01 * otro
            a11 = self.a01 * otro
            return matriz([[a00,a01], [a10,a11]])
        
    def __rmul__(self,otro):
        if type(otro) == type(self):
            print("solo escalares por una matriz")
        else:
            a00 = otro* self.a00
            a01 = otro *self.a01
            a10 = otro *self.a10 
            a11 = otro *self.a11
            return matriz([[a00,a01], [a10,a11]])

a00 = float(input("ingrese coordenada a00: "))
a01 = float(input("ingrese coordenada a01: "))
a10 = float(input("ingrese coordenada a10: "))
a11 = float(input("ingrese coordenada a11: "))
otro = int(float(input("escalar:")))

ma_A = matriz([[a00,a01], [a10,a11]])
resp = ma_A * otro
print("matriz multiplicada por el escalar")
print (resp)

b00 = float(input("ingrese coordenada b00: "))
b01 = float(input("ingrese coordenada b01: "))
b10 = float(input("ingrese coordenada b10: "))
b11 = float(input("ingrese coordenada b11: "))

ma_B = matriz([[b00,b01], [b10,b11]])


resp = ma_A + ma_B
print("suma de a+b")
print (resp)


resp = ma_A - ma_B
print("resta de a-b")
print (resp)









