import numpy as np
import pymatrix as xp

class numpyMatrix:
    def __init__(self, list):
        if len(list)==2:
            self.col1 = list[0][0]
            self.col2 = list[0][1]
            self.col3 = list[1][0]
            self.col4 = list[1][1]
        elif len(list)==3:
            self.col1 = list[0][0]
            self.col2 = list[0][1]
            self.col3 = list[0][2]
            self.col4 = list[1][0]
            self.col5 = list[1][1]
            self.col6 = list[1][2]
            self.col7 = list[2][0]
            self.col8 = list[2][1]
            self.col9 = list[2][2]
        self.list = np.matrix(list)

    def notused(self, minor):
        listku = minor
        detert1 = listku[0][0]*listku[1][1]
        detert2 = listku[0][1]*listku[1][0]
        hasil = detert1 - detert2
        return hasil

    def showMatrix(self):
        com1 = self.list
        print(com1)
    
    def tranMatrix(self):
        com1 = self.list.transpose()
        return com1

    def invMatrix(self):
        com1 = np.linalg.inv(self.list)
        return com1       

    def determine(self):
        com1 = self.list
        if len(com1) == 2:
            detert1 = self.col1*self.col4
            detert2 = self.col2*self.col3
            hasil = detert1 - detert2
            return hasil

        elif len(com1) == 3:
            detert1 = (self.col1*self.col5*self.col9) + (self.col2*self.col6*self.col7) + (self.col3*self.col4*self.col8)
            detert2 = (self.col2*self.col4*self.col9) + (self.col1*self.col6*self.col8) + (self.col3*self.col5*self.col7)
            hasil = detert1-detert2
            return hasil
    
    def minor(self):
        com1 = self.list
        if len(com1) ==2:
            hasil = 0
            return hasil
        elif len(com1) == 3:
            minora = [[self.col5, self.col6], [self.col8, self.col9]]
            minorb = [[self.col4, self.col6], [self.col7, self.col9]]
            minorc = [[self.col4, self.col5], [self.col7, self.col8]]
            minord = [[self.col2, self.col3], [self.col8, self.col9]]
            minore = [[self.col1, self.col3], [self.col7, self.col9]]
            minorf = [[self.col1, self.col2], [self.col7, self.col8]]
            minorg = [[self.col2, self.col3], [self.col5, self.col6]]
            minorh = [[self.col1, self.col3], [self.col4, self.col6]]
            minori = [[self.col1, self.col2], [self.col4, self.col5]]
            deta = numpyMatrix.notused(numpyMatrix, minora)
            detb = numpyMatrix.notused(numpyMatrix, minorb)
            detc = numpyMatrix.notused(numpyMatrix, minorc)
            detd = numpyMatrix.notused(numpyMatrix, minord)
            dete = numpyMatrix.notused(numpyMatrix, minore)
            detf = numpyMatrix.notused(numpyMatrix, minorf)
            detg = numpyMatrix.notused(numpyMatrix, minorg)
            deth = numpyMatrix.notused(numpyMatrix, minorh)
            deti = numpyMatrix.notused(numpyMatrix, minori)
            hasil = np.matrix([[deta, detb, detc], [detd,dete,detf], [detg, deth, deti]])
            return hasil

    def cofactor(self):
        com1 = self.list
        if len(com1) == 2:
            a = self.col4
            b = -1*self.col3
            c = -1*self.col2
            d = self.col1
            newList = [[a, b], [c, d]]
            newMatrix = np.matrix(newList)
            return newMatrix
        elif len(com1) == 3:
            minora = [[self.col5, self.col6], [self.col8, self.col9]]
            minorb = [[self.col4, self.col6], [self.col7, self.col9]]
            minorc = [[self.col4, self.col5], [self.col7, self.col8]]
            minord = [[self.col2, self.col3], [self.col8, self.col9]]
            minore = [[self.col1, self.col3], [self.col7, self.col9]]
            minorf = [[self.col1, self.col2], [self.col7, self.col8]]
            minorg = [[self.col2, self.col3], [self.col5, self.col6]]
            minorh = [[self.col1, self.col3], [self.col4, self.col6]]
            minori = [[self.col1, self.col2], [self.col4, self.col5]]
            deta = numpyMatrix.notused(numpyMatrix, minora)
            detb = numpyMatrix.notused(numpyMatrix, minorb)
            detc = numpyMatrix.notused(numpyMatrix, minorc)
            detd = numpyMatrix.notused(numpyMatrix, minord)
            dete = numpyMatrix.notused(numpyMatrix, minore)
            detf = numpyMatrix.notused(numpyMatrix, minorf)
            detg = numpyMatrix.notused(numpyMatrix, minorg)
            deth = numpyMatrix.notused(numpyMatrix, minorh)
            deti = numpyMatrix.notused(numpyMatrix, minori)
            detb = -1*detb
            detd = -1*detd
            detf = -1*detf
            deth = -1*deth
            hasil = np.matrix([[deta, detb, detc], [detd, dete, detf], [detg, deth, deti]])
            return hasil

    def adjoint(self):
        com1 = self.list
        if len(com1) == 2:
            a = self.col4
            b = self.col1
            self.col2 = -1*self.col2
            self.col3 = -1*self.col3
            newList = [[a, self.col2], [self.col3, b]]
            newMatrix = np.matrix(newList)
            return newMatrix
        elif len(com1) == 3:
            minora = [[self.col5, self.col6], [self.col8, self.col9]]
            minorb = [[self.col4, self.col6], [self.col7, self.col9]]
            minorc = [[self.col4, self.col5], [self.col7, self.col8]]
            minord = [[self.col2, self.col3], [self.col8, self.col9]]
            minore = [[self.col1, self.col3], [self.col7, self.col9]]
            minorf = [[self.col1, self.col2], [self.col7, self.col8]]
            minorg = [[self.col2, self.col3], [self.col5, self.col6]]
            minorh = [[self.col1, self.col3], [self.col4, self.col6]]
            minori = [[self.col1, self.col2], [self.col4, self.col5]]
            deta = numpyMatrix.notused(numpyMatrix, minora)
            detb = numpyMatrix.notused(numpyMatrix, minorb)
            detc = numpyMatrix.notused(numpyMatrix, minorc)
            detd = numpyMatrix.notused(numpyMatrix, minord)
            dete = numpyMatrix.notused(numpyMatrix, minore)
            detf = numpyMatrix.notused(numpyMatrix, minorf)
            detg = numpyMatrix.notused(numpyMatrix, minorg)
            deth = numpyMatrix.notused(numpyMatrix, minorh)
            deti = numpyMatrix.notused(numpyMatrix, minori)
            detb = -1*detb
            detd = -1*detd
            detf = -1*detf
            deth = -1*deth
            matrixBaru = np.matrix([[deta,detd,detg],[detb,dete,deth],[detc,detf,deti]])
            return matrixBaru

class pymatrixMatrix():
    def __init__(self, list):
        self.list = xp.Matrix.from_list(list)
    
    def showMatrix(self):
        com1 = self,list
        return com1
    
    def tranMatrix(self):
        com1 = self.list.trans()
        return com1

    def invMatrix(self):
        com1 = self.list.inv()
        return com1       

    def cofactor(self):
        com1 = self.list.cofactors()
        return com1

    def determine(self):
        com1 = self.list.det()
        return com1
    
    def adjoint(self):
        com1 = self.list.adjoint()
        return com1

class matrixOperator():
    def __init__(self, list1, list2):
        if len(list1)==2:
            self.col11 = list1[0][0]
            self.col12 = list1[0][1]
            self.col13 = list1[1][0]
            self.col14 = list1[1][1]
        elif len(list1)==3:
            self.col11 = list1[0][0]
            self.col12 = list1[0][1]
            self.col13 = list1[0][2]
            self.col14 = list1[1][0]
            self.col15 = list1[1][1]
            self.col16 = list1[1][2]
            self.col17 = list1[2][0]
            self.col18 = list1[2][1]
            self.col19 = list1[2][2]
        
        if len(list2)==2:
            self.col21 = list2[0][0]
            self.col22 = list2[0][1]
            self.col23 = list2[1][0]
            self.col24 = list2[1][1]
        elif len(list2)==3:
            self.col21 = list2[0][0]
            self.col22 = list2[0][1]
            self.col23 = list2[0][2]
            self.col24 = list2[1][0]
            self.col25 = list2[1][1]
            self.col26 = list2[1][2]
            self.col27 = list2[2][0]
            self.col28 = list2[2][1]
            self.col29 = list2[2][2]
        self.list1 = np.matrix(list1)
        self.list2 = np.matrix(list2)
    
    def summing(self):
        com1 = self.list1
        com2 = self.list2
        if (len(com1) == 2) and (len(com2) == 2):
            a = self.col11 + self.col21
            b = self.col12 + self.col22
            c = self.col13 + self.col23
            d = self.col14 + self.col24
            hasil = np.matrix([[a,b],[c,d]])
            return hasil
        elif (len(com1) == 3) and (len(com2) == 3):
            a = self.col11 + self.col21
            b = self.col12 + self.col22
            c = self.col13 + self.col23
            d = self.col14 + self.col24
            e = self.col15 + self.col25
            f = self.col16 + self.col26
            g = self.col17 + self.col27
            h = self.col18 + self.col28
            i = self.col19 + self.col29
            hasil = np.matrix([[a, b, c], [d, e, f], [g, h, i]])
            return hasil

    def substracting(self):
        com1 = self.list1
        com2 = self.list2
        if (len(com1) == 2) and (len(com2) == 2):
            a = self.col11 - self.col21
            b = self.col12 - self.col22
            c = self.col13 - self.col23
            d = self.col14 - self.col24
            hasil = np.matrix([[a,b],[c,d]])
            return hasil
        elif (len(com1) == 3) and (len(com2) == 3):
            a = self.col11 - self.col21
            b = self.col12 - self.col22
            c = self.col13 - self.col23
            d = self.col14 - self.col24
            e = self.col15 - self.col25
            f = self.col16 - self.col26
            g = self.col17 - self.col27
            h = self.col18 - self.col28
            i = self.col19 - self.col29
            hasil = np.matrix([[a, b, c], [d, e, f], [g, h, i]])
            return hasil