# funciones complejos
## autor sebastian porras
import math
def suma(a, b):
    a = list(a)
    a1, b1 = a[0], a[1]
    b = list(b)
    a2, b2 = b[0], b[1]
    suma1 =  a1 + a2
    suma2 = b1 + b2
    return complex(suma1, suma2)
def producto(a, b):
    a = list(a)
    a1, b1 = a[0], a[1]
    b = list(b)
    a2, b2 = b[0], b[1]
    producto1 = a2*a1 - b1*b2
    producto2 = b1*a2 + a1*b2
    return complex(producto1, producto2)
def resta(a, b):
    a = list(a)
    a1, b1 = a[0], a[1]
    b = list(b)
    a2, b2 = b[0], b[1]
    resta1 =  a1 - a2
    resta2 = b1 - b2
    return complex(resta1, resta2)
def division(a, b):
    a = list(a)
    a1, b1 = a[0], a[1]
    b = list(b)
    a2, b2 = b[0], b[1]
    division1 = round((a2*a1 + b1*b2) / (a2**2 + b2**2),2)
    division2 = round((b1*a2 - a1*b2) / (a2**2 + b2**2), 2)
    return complex(division1, division2)
def modulo(a):
    a = list(a)
    a1, b1 = a[0], a[1]
    modulo = (a1**2 + b1**2)**0.5
    return round(modulo, 2)
def conjugado(a):
    a = list(a)
    a1, b1 = a[0], a[1]
    b1 = -b1
    return complex(a1, b1)
def conversioncap(a):
    a = list(a)
    a1, b1 = a[0], a[1]
    r = (a1**2 + b1**2)**0.5
    angulo =math.atan(b1 / a1)
    return (round(r,2), round(angulo,2))
def conversionpac(a):
    a = list(a)
    r, angulo = a[0], a[1]
    a = round(r* math.cos(angulo),2)
    b = round(r* math.sin(angulo),2)
    return(a, b)
def fase(a):
    a = list(a)
    a, b = a[0], a[1]
    fase = math.degrees(math.atan(b/a))
    return round(fase, 2)
