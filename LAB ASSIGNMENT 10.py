#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:46:50 2018

@author: Pir8
"""

class Vec:
    
    def __init__(self, contents = []):
        self.vec = contents
        return
    
    def add(self, element, *positions): # *positions - this allows the user to enter as many elements as desired and 
        #the inputs get stored into a list called positions
        """
        adds the given element at the given positions
        INPUT: element - the new element
               positions - a list of integers
        """
        if len(positions) == 0:
            self.vec.append(element)
        else:
            k = 0
            for p in positions:
                self.vec.insert(p+k, element)
                k += 1
        return
    
    def remove(self, *positions):
        """
        removes the elements at the given positions
        INPUT: positions - list of integers
        """
        k = 0
        for p in positions:
            del self.vec[p - k]
            k += 1
            
    def __add__(self, other):
        if type(self) == Vec and type(other) == Vec:
            if len(self.vec) == len(other.vec):
                return Vec([self.vec[i] + other.vec[i] for i in range(len(self.vec))])
            else:
                print("ERROR: Incompatible vector lengths.")
            return Vec()
        return
    
    def __mul__(self, other):
        if type(self) == Vec and type(other) == Vec:
            if len(self.vec) == len(other.vec):
                return sum([self.vec[i] * other.vec[i] for i in range(len(self.vec))])
            else:
                print("ERROR: Incompatible vector lengths.")
                return None
        elif type(self) == Vec and (type(other) == float or type(other) == int):
            return Vec([other * self.vec[i] for i in range(len(self.vec))])
        return
    
    def __rmul__(self, other):
        if type(self) == Vec and (type(other) == float or type(other) == int):
            return Vec([other * self.vec[i] for i in range(len(self.vec))])             
        return None
    
    def __str__(self):
        return str(self.vec)
        

class Matrix:
    
    def __init__(self, rowsp = [[0]]):
        self.rowsp = rowsp
        self.colsp = []
        column = []
        i = 0
        j = 0
        z = 0
        while(z < len(rowsp[0])):
            for x in rowsp:
                column.append(x[i])
            self.colsp += [column]
        
            z = 1 + z
            i = 1 + i
            if(i >= len(rowsp[0])):
                break
            oneColumn = [] 
    
    def setCol(self,j, u):
        if(len(self.colsp[j])==len(u)):
            self.colsp[j] = u
            i = 0
            if(self.rowsp == [[0]]):
                for x in self.colsp:
                    for y in x:
                        if(len(x) != len(self.rowsp)):
                            self.rowsp += [[0]]
            for x in self.rowsp:
                x[j] = u[i]
                i = i + 1
        else:
            return print('ERROR: Incompatible column space.')
            
    def setRow(self,i, v):
        if(len(self.rowsp[i])==len(v)):
            self.rowsp[i] = v
            j = 0
            if(self.rowsp == [[0]]):
                for x in self.rowsp:
                    for y in x:
                        if(len(x) != len(self.colsp)):
                            self.colsp += [[0]]
            for x in self.colsp:
                x[i] = v[j]
                j = j + 1
        else:
            return print('ERROR: Incompatible row length.')
    
    def setEntry(self,i, j, a):
        self.rowsp[i][j] = a
        self.colsp[j][i] = a
        
    def getCol(self, j):
        return self.colsp[j]
    
    def getRow(self, i):
        return self.rowsp[i]
    
    def getEntry(self, i, j):
        return self.colsp[j][i]
    
    def getColSpace(self):
        return self.colsp
    
    def getRowSpace(self):
        return self.rowsp
    
    def getdiag(self, k):
        diagList = []
        if k == 0:
            i = k
            for x in self.rowsp:
                if(i < len(self.colsp)):
                    diagList += [x[i]]
                i = i + 1
        if k >= 1:
            i = k
            for x in self.rowsp:
                if(i < len(self.colsp)):
                    diagList += [x[i]]
                i = i + 1
        if k <= -1:
            i = -1 * k
            for x in self.colsp:
                if(i < len(self.rowsp)):
                    diagList += [x[i]]
                i = i +1

        return diagList
        
    def __str__(self):
        matrix = ''
        for x in self.rowsp:
            for y in x:
                if y >= 0 and y < 10:
                    matrix += str(y) + '     '
                if y < 0 or y >= 10:
                    matrix += str(y) + '    '

            matrix += '\n'
        return str(matrix)
    
    
    def __add__(self, other):
        if(len(self.rowsp) == len(other.rowsp) and len(self.colsp) == len(other.colsp)):
            solutionRows = []
            oneRow = []
            i = 0
            j = 0
            for x in self.rowsp:
                for y in x:
                    oneRow.append(y + other.rowsp[i][j])
                    j = j +1
                solutionRows = solutionRows + [oneRow]
                j = 0
                i = i + 1
                oneRow = []          
            return Matrix(solutionRows)
        else:
            print('ERROR: Dimension mismatch.')
    
    def __sub__(self, other):
        if(len(self.rowsp) == len(other.rowsp) and len(self.colsp) == len(other.colsp)):
            solutionRows = []
            oneRow = []
            i = 0
            j = 0
            for x in self.rowsp:
                for y in x:
                    oneRow.append(y - other.rowsp[i][j])
                    j = j +1
                solutionRows = solutionRows + [oneRow]
                j = 0
                i = i + 1
                oneRow = []
            
            return Matrix(solutionRows)
        else:
            print('ERROR: Dimension mismatch.')
        
    def __mul__(self, other):
        solutionRows = []
        oneRow = []
        i = 0
        j = 0
        k = 0
        if type(other) == float:
            for x in self.rowsp:
                for y in x:
                    oneRow.append(y * other)
                    j = j + 1
                j = 0
                i = i + 1
                solutionRows = solutionRows + [oneRow]
                oneRow = []
            return Matrix(solutionRows)
        elif type(other) == Matrix:
            for x in self.rowsp:
                z = 0
                i = 0
                while(z < len(other.colsp)):
                    total = 0
                    for y in x:
                        total = total + (y * other.colsp[i][j])
                        j = j + 1
                    oneRow.append(total)
                    z = z + 1
                    i = i + 1
                    j = 0
                solutionRows = solutionRows + [oneRow]
                oneRow = []
            return Matrix(solutionRows)
        elif type(other) == Vec:
            for x in self.rowsp:
                i = 0
                total = 0
                for y in x:
                    total = total + (y * other.vec[j])
                    j = j + 1
                oneRow.append(total)
                j = 0
                solutionRows = solutionRows + [oneRow]
                oneRow = []
            return Matrix(solutionRows)
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __rmul__(self, other): 
        solutionRows = []
        oneRow = []
        i = 0
        j = 0
        k = 0
        if type(other) == float:
            for x in self.rowsp:
                for y in x:
                    oneRow.append(y * other)
                    j = j + 1
                j = 0
                i = i + 1
                solutionRows = solutionRows + [oneRow]
                oneRow = []
            return Matrix(solutionRows)
        else:
            print("ERROR: Unsupported Type.")

    def solve(A,b):
        lowerDiagonal = []
        isUpper = True
        z = -1
        i = 0
        solutionSet = []
        while(i != len(A.rowsp)):
            lowerDiagonal = A.getdiag(z) + lowerDiagonal
            z = z - 1
            i = i + 1
        for x in lowerDiagonal:
            if x != 0:
                isUpper = False
        if(isUpper == True):
            revA = list(reversed(A.rowsp))
            revb = list(reversed(b.vec))
            xBar = []
            z = 0
            while(z < len(revA)):
                xBar.append(1)
                z = z + 1
            i = 0
            solutionSet = []
            for x in revA:
                subNum = 0
                k = 0
                reversedRow = list(reversed(x))
                divisor = reversedRow[i]
                for y in reversed(x):
                    if y == divisor:
                        k = k + 1
                    elif y == 0:
                        k = k + 1
                    else:
                        subNum = subNum + (y * xBar[k])
                        k = k + 1
                xBar[i] = (revb[i] - subNum)/divisor
                solutionSet.append((revb[i] - subNum)/divisor)
                i = i + 1
                
            solutionSet = list(reversed(solutionSet))
            print(solutionSet)
        else:
            print('ERROR: Unsupported matrix type.')
#            
#"""-----------------------------------TESTER CELL------------------------------------------------"""
#"TESTING OPERATOR + "
#
#A = Matrix([[1, 2],[3, 4],[5, 6]])
#B = Matrix([[1, 2],[1, 2]])
#C = Matrix([[10, 20],[30, 40],[50, 60]])
#
#P = A + B # dimension mismatch
#Q = A + C 
#
#print("Matrix A")           
#print(A)
#print()
#
#print("Matrix C")           
#print(C)
#print()
#
#print("Matrix Q = A + C")           
#print(Q)
#print()
#
#"TESTING OPERATOR * "
## TESTING SCALAR-MATRIX MULTIPLICATION
#T = -0.5 * B     
#print("Matrix B")
#print(B)
#print()
#
#print("Matrix T = -0.5 * B")
#print(T)
#print()
#
#
## TESTING MATRIX-MATRIX MULTIPLICATION
#U = A * B
#print("Matrix U = A * B")
#print(U)
#print()
#
#
## TESTING MATRIX-VECTOR MULTIPLICATION
#x = Vec([0, 1])  # Vec object
#b = A * x   # b is a Vec data type
#print("Vector b = A * x")
#print(b) 
 

from image import file2image
from image import isgray
from image import image2file
from image import image2display
from image import color2gray
from image import rgbsplit

def png2graymatrix(filename):
    T = file2image(filename)
    if isgray(T):                  
        pts = []
        rows = []
        for x in T:
            for y in x: 
                pts.append(y[0])
            rows.append(pts)
            pts = []
        image_data = rows 
    else:
        color2gray(T)
        pts = []
        rows = []
        for x in T:
            for y in x:
                pts.append(y[0])
            rows.append(pts)
            pts = []
        image_data = rows
    return Matrix(image_data)       

def graymatrix2png(img_matrix, path):
    image2file(img_matrix.rowsp, path)
    
def get100pics():
    M = png2graymatrix("male12.png")  
    F = png2graymatrix("female00.png")  
    i = 0
    while(i < 100):
        C = M * (i/100) + F * ((100 - i)/100)  
        i = i + 1
        graymatrix2png(C, "mixedfaces" + str(i) + ".png") 
        
def get400pics():
    A = png2graymatrix("male03.png")  
    B = png2graymatrix("female04.png")  
    C = png2graymatrix("male04.png")  
    D = png2graymatrix("female00.png")  
    E = png2graymatrix("male12.png")
    i = 0
    while(i < 100):
        F = B * (i/100) + A * ((100 - i)/100)
        i = i + 1
        graymatrix2png(F, "1stmixedfaces" + str(i) + ".png") 
    i = 0
    while(i < 100):
        F = C * (i/100) + B * ((100 - i)/100)
        i = i + 1
        graymatrix2png(F, "2ndmixedfaces" + str(i) + ".png")
    i = 0
    while(i < 100):
        F = D * (i/100) + C * ((100 - i)/100)
        i = i + 1
        graymatrix2png(F, "3rdmixedfaces" + str(i) + ".png")
    i = 0
    while(i < 100):
        F = E * (i/100) + D * ((100 - i)/100)
        i = i + 1
        graymatrix2png(F, "4thmixedfaces" + str(i) + ".png")
        
"""------------------TESTER FOR FUNCTIONS png2graymatrix() AND graymatrix2png()-------------------------"""
#M = png2graymatrix("male12.png")
#F = png2graymatrix("female00.png")  
#C = M * 0.5 + F * 0.5 
#graymatrix2png(C, "mixedfaces.png")
get400pics()

#
#"""
#EXTRA CREDIT
#""" 
#
#"""------------------EXTRA CREDIT: SEE TASK 4"""
#
#def make_video(images, outimg=None, fps=5, size=None,
#               is_color=True, format="XVID"):
#    """
#    Create a video from a list of images.
# 
#    @param      outvid      output video
#    @param      images      list of images to use in the video
#    @param      fps         frame per second
#    @param      size        size of each frame
#    @param      is_color    color
#    @param      format      see http://www.fourcc.org/codecs.php
#    @return                 see http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
# 
#    The function relies on http://opencv-python-tutroals.readthedocs.org/en/latest/.
#    By default, the video will have the size of the first image.
#    It will resize every image to this size before adding them to the video.
#    """
#    from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
#    fourcc = VideoWriter_fourcc(*format)
#    vid = None
#    for image in images:
#        if not os.path.exists(image):
#            raise FileNotFoundError(image)
#        img = imread(image)
#        if vid is None:
#            if size is None:
#                size = img.shape[1], img.shape[0]
#            vid = VideoWriter(outvid, fourcc, float(fps), size, is_color)
#        if size[0] != img.shape[1] and size[1] != img.shape[0]:
#            img = resize(img, size)
#        vid.write(img)
#    vid.release()
#    return vid
#
#"""------------------------SAMPLE USAGE-------------------"""
#images = []  
#
#for i in range(10):  
#    file = ("male0%i.png" % i)
#    images.append(file)
#    
#for i in range(10, 15): 
#    file = ("male%i.png" % i)
#    images.append(file)
#    
#print(images)  
#make_video(images, format = "MPEG4")  