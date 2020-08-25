import funcionescomplejos

def adiveccom(a,b):
    for i in range(len(a)):
        a[i] = a[i] + b[i]
    return a
def invadi(a):
    for i in range(len(a)):
        a[i] = a[i] * -1
    return a
def multesc(a, b):
    for i in range(len(a)):
        a[i] = a[i] * b
    return a
def adimatcom(a,b):
    for i in range(len(a)):
        for k in range(len(a)):
            a[i][k] = a[i][k] + b[i][k]
    return a
def inveradimat(a):
    for i in range(len(a)):
        for k in range(len(a[0])):
            a[i][k] = complex(a[i][k].real * -1,a[i][k].imag * -1)
    return a
def multescmat(a,b):
    for i in range(len(a)):
        for k in range(len(a[0])):
            a[i][k] = a[i][k] * b
    return a
def transpuesta(a):
    lista = []
    b = []
    for i in range(len(a[0])):
        lista = []
        for k in range(len(a)):
            lista = lista + [a[k][i]]
        b = b + [lista]
    return b
def conjugadamatriz(a):
    for i in range(len(a)):
        for k in range(len(a[0])):
            a[i][k] = complex(a[i][k].real,a[i][k].imag * -1)
    return a
def conjugadavector(a):    
    for i in range(len(a)):
        a[i] = complex(a[i].real,a[i].imag * -1)
    return a
def adjunta(a):
    a = conjugadamatriz(transpuesta(a))
    return a
def produmatr(a,b):
    m = len(a[0])
    n = len(b)
    fila = []
    c = []
    for i in range(len(a[0])):
        fila = []
        for k in range(len(b)):
             fila = fila + [0]
        c = c + [fila]
    a = transpuesta(a)
    for i in range(m):
        for j in range(n):
            c[i][j] = productvec(a[i],b[j])
            c[i][j] = complex(round(c[i][j].real,0), round(c[i][j].imag, 0))
    return transpuesta(c)
## funcion de ayuda "producto de vectores 0*n * m*0"
def productvec(a,b):
    suma = 0
    for i in range(len(a)):
        c1 = (a[i] * b[i])
        suma = suma + c1
    return suma
##
def accionvecmat(a, b):
    # poner vector en modo matriz de la forma [[a, b, c]]
    m, n = len(a), len(a[0])
    m1 = len(b)
    c = m * [0]
    if n != m1:
        return False
    else:
        for i in range(len(c)):
            c[i] = productvec(a[i],b)
    return c
def normavec(a):
    # ingresar vectores de la forma [a, b, c]
    c = 0
    for i in range(len(a)):
        c = c + a[i]**2
    c = c ** 0.5
    return round(c, 2)
def distanvec(a, b):
    # ingresar vectores de la forma [a, b, c]
    for i in range(len(a)):
        a[i] = a[i] - b[i]
    c = productvec(a, a)
    c = c ** 0.5
    return round(c, 2)
def matruni(a):
    c = adjunta(a)
    d = produmatr(a, c)
    bandera = True
    for i in range(len(d)):
        for j in range(len(d[0])):
            if d[i][i] != 1:
                bandera = False
            if d[i][j] != 0 and i != j:
                bandera = False
    return bandera
    
def matrherm(a):
    if a == adjunta(a):
        return True
    else:
        return False

def productensor(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            c1 = a[i] * b [j]
            c = c + [c1]
    return c
            
            
            
        
            

    
   
            
    


    

            
        
        

