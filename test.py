import unittest
from funcionescomplejos import*
from operacionesmatrices import*

class TestStringMethods(unittest.TestCase):

    def testsuma(self):
        a = (4, 3)
        b = (3, 2)
        self.assertEqual(suma(a, b), 7+5j)
        
        a = (-5, 9)
        b = (7, -8)
        self.assertEqual(suma(a, b), 2+1j)

        a = (3, -9)
        b = (12, 4)
        self.assertEqual(suma(a, b), 15-5j)
        
        a = (1, 5)
        b = (0, 2)
        self.assertEqual(suma(a, b), 1+7j)
        
        a = (13, 11)
        b = (-7, -8)
        self.assertEqual(suma(a, b), 6+3j)
        
        a = (5, 9)
        b = (7, 8)
        self.assertEqual(suma(a, b), 12+17j)
        
        a = (21, 2)
        b = (2, 3)
        self.assertEqual(suma(a, b), 23+5j)
        
        a = (-2, -5)
        b = (4, 1)
        self.assertEqual(suma(a, b), 2-4j)
        
    def testresta(self):
        a = (1, 3)
        b = (2, -1)
        self.assertEqual(resta(a, b), -1+4j)

        a = (2, 3)
        b = (3, 1)
        self.assertEqual(resta(a, b), -1+2j)

        a = (1, 2)
        b = (3, 4)
        self.assertEqual(resta(a, b), -2-2j)

        a = (-5, 6)
        b = (7, -8)
        self.assertEqual(resta(a, b), -12+14j)

        a = (9, 0)
        b = (1, -2)
        self.assertEqual(resta(a, b), 8+2j)

        a = (-3, 4)
        b = (-5, 6)
        self.assertEqual(resta(a, b), 2-2j)

        a = (11, 10)
        b = (-9, -8)
        self.assertEqual(resta(a, b), 20+18j)

        a = (7, 5)
        b = (4, -6)
        self.assertEqual(resta(a, b), 3+11j)

        a = (-9, -7)
        b = (-3, -1)
        self.assertEqual(resta(a, b), -6-6j)
        
    def testproducto(self):
        a = (1, 2)
        b = (3, -4)
        self.assertEqual(producto(a, b), 11+2j)

        a = (-5, 6)
        b = (7, -8)
        self.assertEqual(producto(a, b), 13+82j)

        a = (-1, -2)
        b = (-3, -4)
        self.assertEqual(producto(a, b), -5+10j)

        a = (-2, 2)
        b = (2, -2)
        self.assertEqual(producto(a, b), 0+8j)

        a = (1, -3)
        b = (5, -9)
        self.assertEqual(producto(a, b), -22-24j)

        a = (2, -4)
        b = (-8, -6)
        self.assertEqual(producto(a, b), -40+20j)

        a = (1, -5)
        b = (-2, 6)
        self.assertEqual(producto(a, b), 28+16j)

        a = (3, 7)
        b = (-9, -1)
        self.assertEqual(producto(a, b), -20-66j)
        
    def testdivision(self):
        a = (2, 3)
        b = (3, 1)
        self.assertEqual(division(a, b), 0.9+0.7j)

        a = (1, 2)
        b = (3, 3)
        self.assertEqual(division(a, b), 0.5+0.17j)

        a = (-2, -4)
        b = (-3, 5)
        self.assertEqual(division(a, b), -0.41+0.65j)

        a = (-1, -3)
        b = (3, -1)
        self.assertEqual(division(a, b), 0-1j)

        a = (1, 3)
        b = (7, 2)
        self.assertEqual(division(a, b), 0.25+0.36j)

        a = (-1, 2)
        b = (-1, 1)
        self.assertEqual(division(a, b), 1.5-0.5j)

        a = (1, -4)
        b = (-8, 2)
        self.assertEqual(division(a, b), -0.24+0.44j)

        a = (10, -2)
        b = (-5, 1)
        self.assertEqual(division(a, b), -2+0j)
    def testmodulo(self):
        
        a = (10, -2)
        self.assertEqual(modulo(a), 10.2)

        a = (-5, 1)
        self.assertEqual(modulo(a), 5.1)

        a = (3, 5)
        self.assertEqual(modulo(a), 5.83)

        a = (2, -3)
        self.assertEqual(modulo(a), 3.61)

        a = (0, 1)
        self.assertEqual(modulo(a), 1)

        a = (-2, -9)
        self.assertEqual(modulo(a), 9.22)

        a = (-7, 8)
        self.assertEqual(modulo(a), 10.63)

        a = (6, -4)
        self.assertEqual(modulo(a), 7.21)
        
    def testconjugado(self):

        a = (10, -2)
        self.assertEqual(conjugado(a), 10+2j)

        a = (-5, 1)
        self.assertEqual(conjugado(a), -5-1j)

        a = (3, 5)
        self.assertEqual(conjugado(a), 3-5j)

        a = (2, -3)
        self.assertEqual(conjugado(a), 2+3j)

        a = (0, 1)
        self.assertEqual(conjugado(a), 0-1j)

        a = (-2, -9)
        self.assertEqual(conjugado(a), -2+9j)

        a = (-7, 8)
        self.assertEqual(conjugado(a), -7-8j)

        a = (6, -4)
        self.assertEqual(conjugado(a), 6+4j)
        
    def testconversioncap(self):
        a = (10, -2)
        self.assertEqual(conversioncap(a), (10.2, -0.2))

        a = (-5, 1)
        self.assertEqual(conversioncap(a), (5.1, -0.2))

        a = (3, 5)
        self.assertEqual(conversioncap(a), (5.83, 1.03 ))

        a = (2, -3)
        self.assertEqual(conversioncap(a), (3.61, -0.98))

        a = (2, 1)
        self.assertEqual(conversioncap(a), (2.24, 0.46))

        a = (-2, -9)
        self.assertEqual(conversioncap(a), (9.22, 1.35))

        a = (-7, 8)
        self.assertEqual(conversioncap(a), (10.63, -0.85))

        a = (6, -4)
        self.assertEqual(conversioncap(a), (7.21, -0.59))
        
    def testconversionpac(self):
        a = (10.2, -0.2)
        self.assertEqual(conversionpac(a), (10.0, -2.03))

        a = (5.1, -0.2)
        self.assertEqual(conversionpac(a), (5.0, -1.01))

        a = (5.83, 1.03 )
        self.assertEqual(conversionpac(a), (3.0,  5.0))

        a = (3.61, -0.98)
        self.assertEqual(conversionpac(a), (2.01, -3.0))

        a = (2.24, 0.46)
        self.assertEqual(conversionpac(a), (2.01, 0.99))

        a = (9.22, 1.35)
        self.assertEqual(conversionpac(a), (2.02, 9.0))

        a = (10.63, -0.85)
        self.assertEqual(conversionpac(a), (7.02, -7.99))
        
        a = (7.21, -0.59)
        self.assertEqual(conversionpac(a), (5.99, -4.01))
    def testfase(self):
        a = (10, -2)
        self.assertEqual(fase(a), -11.31)

        a = (-5, 1)
        self.assertEqual(fase(a), -11.31)

        a = (3, 5)
        self.assertEqual(fase(a), 59.04)

        a = (2, -3)
        self.assertEqual(fase(a), -56.31)

        a = (2, 1)
        self.assertEqual(fase(a), 26.57)

        a = (-2, -9)
        self.assertEqual(fase(a), 77.47)

        a = (-7, 8)
        self.assertEqual(fase(a), -48.81)

        a = (6, -4)
        self.assertEqual(fase(a),-33.69)

    def testadiveccom(self):
        a = [2+3j, 1+0j, 3-7j]
        b = [0+4j, 8+1j, 7-7j]
        self.assertEqual(adiveccom(a,b), [2+7j, 9+1j, 10-14j])

        a = [1+2j, 6+0j, 1+4j]
        b = [4+5j, 4+9j, 1-3j]
        self.assertEqual(adiveccom(a,b), [5+7j, 10+9j, 2+1j])
        
    def testinvadi(self):
        
        a = [1+2j, 6+0j, 1+4j]
        self.assertEqual(invadi(a), [-1-2j, -6-0j, -1-4j])

        a = [4+5j, 4+9j, 1-3j]
        self.assertEqual(invadi(a), [-4-5j, -4-9j, -1+3j])

    def testmultesc(self):
        a = [2+3j, 1+0j]
        b = 7-7j
        self.assertEqual(multesc(a,b), [35+7j, 7-7j])

        a = [1+2j, 6+0j]
        b = 4+9j
        self.assertEqual(multesc(a,b), [-14+17j, 24+54j])
        
    def testadimatcom(self):
        a = [[1+0j, 2-1j],[7+2j, 8-9j]]
        b = [[1+1j, 2+2j],[3+3j, 4+4j]]
        self.assertEqual(adimatcom(a,b), [[2+1j, 4+1j],[10+5j, 12-5j]])

        a = [[1+2j, 6+0j, 1+4j],[4+5j, 4+9j, 1-3j], [1+2j, 6+0j, 1+4j]]
        b = [[4+5j, 4+9j, -2-2j], [0+9j, 6+7j, 5+4j], [3+2j, 1+0j, 2+4j]]
        self.assertEqual(adimatcom(a,b), [[5+7j, 10+9j, -1+2j],[4+14j, 10+16j, 6+1j],[4+4j, 7+0j, 3+8j]])

    def testinveradimat(self):
        a = [[1+0j, 2-1j],[7+2j, 8-9j]]
        self.assertEqual(inveradimat(a), [[-1-0j, -2+1j],[-7-2j, -8+9j]])

        a = [[4+5j, 4+9j, -2-2j], [0+9j, 6+7j, 5+4j], [3+2j, 1+0j, 2+4j]]
        self.assertEqual(inveradimat(a), [[-4-5j, -4-9j, +2+2j], [-0-9j, -6-7j, -5-4j], [-3-2j, -1-0j, -2-4j]])
        
    def testmultescmat(self):
        a = [[1+0j, 2-1j],[7+2j, 8-9j]]
        b = 7-7j
        self.assertEqual(multescmat(a,b), [[7-7j, 7-21j],[63-35j, -7-119j]])

        a = [[2+3j, 1-5j],[7+6j, 2-7j]]
        b = 4+9j
        self.assertEqual(multescmat(a,b), [[-19+30j, 49-11j],[-26+87j, 71-10j]])

    def testtranspuesta(self):
        
        a = [[1+0j, 2-1j],[7+2j, 8-9j]]
        self.assertEqual(transpuesta(a), [[1+0j, 7+2j],[2-1j, 8-9j]])

        a = [[2+3j, 1-5j],[7+6j, 2-7j]]
        self.assertEqual(transpuesta(a), [[2+3j, 7+6j],[1-5j, 2-7j]])
        
    def testconjugadamatriz(self):
        
        a = [[1+0j, 2-1j],[7+2j, 8-9j]]
        self.assertEqual(conjugadamatriz(a), [[1-0j, 2+1j],[7-2j, 8+9j]])

        a = [[2+3j, 1-5j],[7+6j, 2-7j]]
        self.assertEqual(conjugadamatriz(a), [[2-3j, 1+5j],[7-6j, 2+7j]])

    def testconjugadavector(self):
        
        a = [1+2j, 6+0j, 1+4j]
        self.assertEqual(conjugadavector(a), [1-2j, 6-0j, 1-4j])

        a = [4+5j, 4+9j, 1-3j]
        self.assertEqual(conjugadavector(a), [4-5j, 4-9j, 1+3j])

    def testadjunta(self):
        
        a = [[1+0j, 2-1j],[7+2j, 8-9j]]
        self.assertEqual(adjunta(a), [[1-0j, 7-2j],[2+1j, 8+9j]])

        a = [[2+3j, 1-5j],[7+6j, 2-7j]]
        self.assertEqual(adjunta(a), [[2-3j, 7-6j],[1+5j, 2+7j]])
#
    def testprodumatr(self):
        
        a = [[2+3j, 7+6j],[1-5j, 2-7j]]
        b = [[1-0j, 7-2j],[2+1j, 8+9j]]
        self.assertEqual(produmatr(a,b), [[-1-34j, 7-47j],[54-23j, 87-19j]])

        a = [[4+5j, 4+9j, 1-3j], [1-0j, 7-2j, 2+1j]]
        b = [[2+3j, 5-4j],[1+7j, -2-5j],[2+3j, -2-2j]]
        self.assertEqual(produmatr(a,b), [[-2+18j, 8-8j, 25-6j], [-33+28j, -83+6j, 23-8j], [-9+20j, -37+20j, 9-9j]])

    def testmatrherm(self):
        
        a = [[7+0j, 6-5j],[6+5j, -3+0j]]
        self.assertEqual(matrherm(a), True)

        a = [[2+0j, 3-5j],[3+7j, 5+0j]]
        self.assertEqual(matrherm(a), False)

    def testmatruni(self):
        
        a = [[0+1j, 0+0j],[0+0j, 0+1j]]
        self.assertEqual(matruni(a), True)

        a = [[2+0j, 3-5j],[3+7j, 5+0j]]
        self.assertEqual(matruni(a), False)

    def testproductotensor(self):
        a = [2+1j, 1+3j]
        b = [3+2j, 7+5j, -3+2j]
        self.assertEqual(productensor(a, b), [4+7j, 9+17j, -8+1j, -3+11j, -8+26j, -9-7j])

        
if __name__ == '__main__':
    unittest.main()
