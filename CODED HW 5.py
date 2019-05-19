"REPLACE THE BOTTOM WITH YOUR Matrix CLASS "

class Matrix:
    
    def __init__(self, rowSpace = [[0]]):
        self.rowSpace = rowSpace
        self.colSpace = []
        column = []
        i = 0
        z = 0
        
        while(z < len(rowSpace[0])):
            for x in rowSpace:
                column.append(x[i])
            self.colSpace = self.colSpace + [column]
            column = []
            z = 1 + z
            i = 1 + i
            if(i >= len(rowSpace[0])):
                break

    def __add__(self, other):
        if(len(self.rowSpace) == len(other.rowSpace) and len(self.colSpace) == len(other.colSpace)):
            solutionRows = []
            oneRow = []
            i = 0
            j = 0
            for x in self.rowSpace:
                for y in x:
                    oneRow.append(y + other.rowSpace[i][j])
                    j = j +1
                solutionRows = solutionRows + [oneRow]
                j = 0
                i = i + 1
                oneRow = []          
            return Matrix(solutionRows)
        else:
            print('ERROR: Dimension mismatch.')
    
    def __sub__(self, other):
        if(len(self.rowSpace) == len(other.rowSpace) and len(self.colSpace) == len(other.colSpace)):
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
        
        if type(other) == float:
            for x in self.rowSpace:
                for y in x:
                    oneRow.append(y * other)
                    j = j + 1
                j = 0
                i = i + 1
                solutionRows = solutionRows + [oneRow]
                oneRow = []
            return Matrix(solutionRows)
        
        elif type(other) == Matrix:
            for x in self.rowSpace:
                z = 0
                i = 0
                while(z < len(other.colSpace)):
                    total = 0
                    for y in x:
                        total = total + (y * other.colSpace[i][j])
                        j = j + 1
                    oneRow.append(total)
                    z = z + 1
                    i = i + 1
                    j = 0
                solutionRows = solutionRows + [oneRow]
                oneRow = []
            return Matrix(solutionRows)
        
        elif type(other) == Vec:
            for x in self.rowSpace:
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
        while(i != len(A.rowSpace)):
            lowerDiagonal = A.getdiag(z) + lowerDiagonal
            z = z - 1
            i = i + 1
        for x in lowerDiagonal:
            if x != 0:
                isUpper = False
        if(isUpper == True):
            revA = list(reversed(A.rowSpace))
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

    def getdiag(self, k):
        returnList = []
        if k == 0:
            i = k
            for x in self.rowSpace:
                if(i < len(self.colSpace)):
                    returnList += [x[i]]
                i = i + 1
        if k >= 1:
            i = k
            for x in self.rowSpace:
                if(i < len(self.colSpace)):
                    returnList += [x[i]]
                i = i + 1
        if k <= -1:
            i = -1 * k
            for x in self.colSpace:
                if(i < len(self.rowSpace)):
                    returnList += [x[i]]
                i = i +1

        return returnList
    
    def __str__(self):
        matrix = ''
        for x in self.rowSpace:
            for y in x:
                if y >= 0 and y < 10:
                    matrix += str(y) + '     '
                if y < 0 or y >= 10:
                    matrix += str(y) + '    '

            matrix += '\n'
        return str(matrix)
    
    def dim(self):
        """returns the dimensions of this Matrix object
        OUTPUT: tuple (m, n) where m is the number of rows 
        of this matrix and n is the number of columns of this matrix
        """    
        m = len(self.rowSpace)
        n = len(self.colSpace)
        return (m, n)
            
    def swapRows(self, i, j):
        """swaps the i-th and j-th rows of this matrix
        INPUT: i, j - integer index of the rows to swap
        OUTPUT: None
        """
        temp = self.rowSpace[i]
        self.rowSpace[i] = self.rowSpace[j]
        self.rowSpace[j] = temp
         
        columnChange = []
        k = 0
        for x in self.rowSpace:
            m = 0
            for y in x:
                self.colSpace[m][k] = y
                m = m + 1
            k = k + 1
    
    def swapCols(self, i, j):
        """swaps the i-th and j-th columns of this matrix
        INPUT: i, j - integer index of the columns to swap
        OUTPUT: None
        """
        
        temp = self.colSpace[j]
        self.colSpace[j] = self.colSpace[i]
        self.colSpace[i] = temp
                
        rowChange = []
        k = 0
        for x in self.colSpace:
            m = 0
            for y in x:
                self.rowSpace[m][k] = y
                m = m + 1
            k = k + 1
    
    def rank(self):
        """returns the rank form of matrix A
        INPUT: A - n X m matrix
        OUTPUT: rank of A as an integer
        """
        bases = []
        lastRow = []
        lastCol = []
        finalMatrix = A
        
        for x in A.rowSpace:
            lastRow = x
        for x in A.colSpace:
            lastCol = x
            
        j= 0
        if(len(finalMatrix.rowSpace) > len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.colSpace)):
                k = j + 1
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in finalMatrix.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        
                        k = k + 1
                j = j + 1
        
        elif(len(finalMatrix.rowSpace) < len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.rowSpace)):
                k = j + 1
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in A.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l]):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        k = k + 1
                j = j + 1
        
        elif(len(finalMatrix.rowSpace) == len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.rowSpace)):
                k = j + 1
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in A.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l]):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        k = k + 1
                j = j + 1
        i = 0
        compareRow = []
        
        while(i < len(finalMatrix.rowSpace[0])):
            compareRow.append(0.0)
            i = i + 1
            
        for x in finalMatrix.rowSpace:
            if(x != compareRow):
                bases.append(x)
                
        rank = len(bases)
        return (rank)
    
class MatrixSolvers:
    
    def RREF(A):
        """returns the reduced-row echelon form of matrix A
        INPUT: A - m X n Matrix object
        OUTPUT: m X n Matrix object that is the reduced row echelon form of A
        """
        lastRow = []
        lastCol = []
        finalMatrix = A
        for x in A.rowSpace:
            lastRow = x
        for x in A.colSpace:
            lastCol = x
        j= 0
        if(len(finalMatrix.rowSpace) > len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.colSpace)):
                k = j + 1
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in finalMatrix.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        
                        k = k + 1
                j = j + 1
            return(finalMatrix)
        
        elif(len(finalMatrix.rowSpace) < len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.rowSpace)):
                k = j + 1
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in A.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        k = k + 1
                j = j + 1
            return(finalMatrix)
        
        elif(len(finalMatrix.rowSpace) == len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.rowSpace)):
                k = j + 1
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in A.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        k = k + 1
                j = j + 1
            return(finalMatrix)
    
    def gaussianElimination(A,b):
        """uses Gaussian Elimination without pivoting to return the solution to the system Ax = b,
        for m X n Matrix A, and m-dimensional Vec b.  Prints `No solution` if no solution exists, 
        or `Infinitely many solutions` if there are infinitely solutions.
        INPUT: Matrix object A, Vec object b
        OUTPUT: m- dimensional Vec object x, if a unique solution exists, None otherwise 
        """
        workMatrix = A
        i = 0
        for x in workMatrix.rowSpace:
            x.append(b.vec[i])
            i = i + 1
        workMatrix.colSpace.append(b.vec)
        workMatrix = MatrixSolvers.RREF(workMatrix)
        print(workMatrix)
        rank = workMatrix.rank()
        if(rank == len(workMatrix.colSpace)-1):
            print('unique solution')
            i = 0
            compareRow = []
            bases = []
            while(i < len(workMatrix.rowSpace[0])):
                compareRow.append(0.0)
                i = i + 1
            for x in workMatrix.rowSpace:
                if(x != compareRow):
                    bases.append(x)
            bBar = []
            aMat = []
            bVal = 0
            for x in bases:
                for y in x:
                    bVal = y
                bBar.append(bVal)
            
            for x in bases:
                i = 0
                oneRow = []
                while(i < len(bases[0])-1):
                    oneRow.append(x[i])
                    i = i +1
                aMat.append(oneRow)
            finalMatrix = Matrix(aMat)
            finalVec = Vec(bBar)
            solution = Matrix.solve(finalMatrix, finalVec)
            return(Vec(solution))
        else:
            lastRow = []
            aMat = []
            bBar = 0
            for x in workMatrix.rowSpace:
                lastRow = x
            for x in lastRow:
                if(x == lastRow[len(lastRow) - 1]):
                    bBar = x
                else:
                    aMat.append(x)
            allZeroA = False
            zerob = False
            for x in aMat:
                if(x == 0):
                    allZeroA = True
                if(x != 0):
                    allZeroA = False
                    break
            if(allZeroA and bBar != 0):
                print('no solution')
            if(allZeroA == False):
                print('infinitely many solutions')              
            
    def gaussianElim_PP(A,b):
        """uses Gaussian Elimination with partial pivoting to return the solution to the system Ax = b,
        for m X n Matrix A, and m-dimensional Vec b.  Prints `No solution` if no solution exists, 
        or `Infinitely many solutions` if there are infinitely solutions.
        INPUT: Matrix object A, Vec object b
        OUTPUT: m- dimensional Vec object x, if a unique solution exists, None otherwise 
        """
        workMatrix = A
        i = 0
        for x in workMatrix.rowSpace:
            x.append(b.vec[i])
            i = i + 1
        workMatrix.colSpace.append(b.vec)
        lastRow = []
        lastCol = []
        finalMatrix = A
        for x in A.rowSpace:
            lastRow = x
        for x in A.colSpace:
            lastCol = x
        j= 0
        if(len(finalMatrix.rowSpace) > len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.colSpace)):
                k = j + 1
                l = j
                while(l < len(finalMatrix.rowSpace)-j):
                    if(finalMatrix.rowSpace[j][j] < finalMatrix.rowSpace[l][j]):
                        Matrix.swapRows(finalMatrix, j, l)
                    l = l +1
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in finalMatrix.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        
                        k = k + 1
                j = j + 1
        
        elif(len(finalMatrix.rowSpace) < len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.rowSpace)):
                k = j + 1
                l = j
                while(l < len(finalMatrix.rowSpace)-j):
                    if(finalMatrix.rowSpace[j][j] < finalMatrix.rowSpace[l][j]):
                        Matrix.swapRows(finalMatrix, j, l)
                    l = l +1
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in A.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        k = k + 1
                j = j + 1
        
        elif(len(finalMatrix.rowSpace) == len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.rowSpace)):
                k = j + 1
                l = j
                while(l < len(finalMatrix.rowSpace)-j):
                    if(finalMatrix.rowSpace[j][j] < finalMatrix.rowSpace[l][j]):
                        Matrix.swapRows(finalMatrix, j, l)
                    l = l +1
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in A.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        k = k + 1
                j = j + 1
        print(workMatrix)
        compareRow = []
        bases = []
        while(i < len(finalMatrix.rowSpace[0])):
            compareRow.append(0.0)
            i = i + 1
        for x in finalMatrix.rowSpace:
            if(x != compareRow):
                bases.append(x)
        rank = len(bases)
        if(rank == len(workMatrix.colSpace)-1):
            print('unique solution')
            i = 0
            compareRow = []
            bases = []
            while(i < len(workMatrix.rowSpace[0])):
                compareRow.append(0.0)
                i = i + 1
            for x in workMatrix.rowSpace:
                if(x != compareRow):
                    bases.append(x)
            bBar = []
            aMat = []
            bVal = 0
            for x in bases:
                for y in x:
                    bVal = y
                bBar.append(bVal)
            
            for x in bases:
                i = 0
                oneRow = []
                while(i < len(bases[0])-1):
                    oneRow.append(x[i])
                    i = i +1
                aMat.append(oneRow)
            finalMatrix = Matrix(aMat)
            finalVec = Vec(bBar)
            solution = Matrix.solve(finalMatrix, finalVec)
            return(Vec(solution))
        else:
            lastRow = []
            aMat = []
            bBar = 0
            for x in workMatrix.rowSpace:
                lastRow = x
            for x in lastRow:
                if(x == lastRow[len(lastRow) - 1]):
                    bBar = x
                else:
                    aMat.append(x)
            allZeroA = False
            zerob = False
            for x in aMat:
                if(x == 0):
                    allZeroA = True
                if(x != 0):
                    allZeroA = False
                    break
            if(allZeroA and bBar != 0):
                print('no solution')
            if(allZeroA == False):
                print('infinitely many solutions')
    
    def gaussianElim_TP(A,b):
        """uses Gaussian Elimination with total pivoting to return the solution to the system Ax = b,
        for m X n Matrix A, and m-dimensional Vec b.  Prints `No solution` if no solution exists, 
        or `Infinitely many solutions` if there are infinitely solutions.
        INPUT: Matrix object A, Vec object b
        OUTPUT: m- dimensional Vec object x, if a unique solution exists, None otherwise 
        """
        
        workMatrix = A
        i = 0
        for x in workMatrix.rowSpace:
            x.append(b.vec[i])
            i = i + 1
        workMatrix.colSpace.append(b.vec)
        lastRow = []
        lastCol = []
        finalMatrix = A
        for x in A.rowSpace:
            lastRow = x
        for x in A.colSpace:
            lastCol = x
        j= 0
        if(len(finalMatrix.rowSpace) > len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.colSpace)):
                k = j + 1
                greatestNum = 0
                row = 0
                trueRow = 0
                trueCol = 0
                for x in finalMatrix.rowSpace:
                    col = 0
                    for y in x:
                        if(finalMatrix.rowSpace.index(x) < finalMatrix.rowSpace.index(finalMatrix.rowSpace[j])):
                            pass
                        elif(x.index(y) == len(finalMatrix.rowSpace[0])-1):
                            pass
                        elif(abs(y) > greatestNum):
                            greatestNum = abs(y)
                            trueRow = row
                            trueCol = col
                        col = col + 1
                    row = row + 1
                Matrix.swapRows(finalMatrix, j, trueRow)
                Matrix.swapCols(finalMatrix, j, trueCol)
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in finalMatrix.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        
                        k = k + 1
                j = j + 1
        
        elif(len(finalMatrix.rowSpace) < len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.rowSpace)):
                k = j + 1
                greatestNum = 0
                row = 0
                trueRow = 0
                trueCol = 0
                for x in finalMatrix.rowSpace:
                    col = 0
                    for y in x:
                        if(finalMatrix.rowSpace.index(x) < finalMatrix.rowSpace.index(finalMatrix.rowSpace[j])):
                            pass
                        elif(x.index(y) == len(finalMatrix.rowSpace[0])-1):
                            pass
                        elif(abs(y) > greatestNum):
                            greatestNum = abs(y)
                            trueRow = row
                            trueCol = col
                        col = col + 1
                    row = row + 1
                Matrix.swapRows(finalMatrix, j, trueRow)
                Matrix.swapCols(finalMatrix, j, trueCol)
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in A.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        k = k + 1
                j = j + 1
        
        elif(len(finalMatrix.rowSpace) == len(finalMatrix.colSpace)):
            while(j < len(finalMatrix.rowSpace)):
                k = j + 1
                greatestNum = 0
                row = 0
                trueRow = 0
                trueCol = 0
                for x in finalMatrix.rowSpace:
                    col = 0
                    for y in x:
                        if(finalMatrix.rowSpace.index(x) < finalMatrix.rowSpace.index(finalMatrix.rowSpace[j])):
                            pass
                        elif(x.index(y) == len(finalMatrix.rowSpace[0])-1):
                            pass
                        elif(abs(y) > greatestNum):
                            greatestNum = abs(y)
                            trueRow = row
                            trueCol = col
                        col = col + 1
                    row = row + 1
                Matrix.swapRows(finalMatrix, j, trueRow)
                Matrix.swapCols(finalMatrix, j, trueCol)
                while(k < len(finalMatrix.rowSpace)):
                    if(finalMatrix.rowSpace[j][j] == 0):
                        k = k + 1
                    else:
                        alpha = finalMatrix.rowSpace[k][j]/finalMatrix.rowSpace[j][j]
                        finalRow = []
                        l = 0
                        for x in A.rowSpace[k]:
                            if(finalMatrix.rowSpace[j][l] == 0):
                                finalRow.append(0.0)
                                l = l + 1
                            else:
                                value = x - (alpha * finalMatrix.rowSpace[j][l])
                                finalRow.append(value)
                                l = l + 1
                        finalMatrix.rowSpace[k] = finalRow
                        k = k + 1
                j = j + 1
        print(workMatrix)
        compareRow = []
        bases = []
        while(i < len(finalMatrix.rowSpace[0])):
            compareRow.append(0.0)
            i = i + 1
        for x in finalMatrix.rowSpace:
            if(x != compareRow):
                bases.append(x)
        rank = len(bases)
        if(rank == len(workMatrix.colSpace)-1):
            print('unique solution')
            i = 0
            compareRow = []
            bases = []
            while(i < len(workMatrix.rowSpace[0])):
                compareRow.append(0.0)
                i = i + 1
            for x in workMatrix.rowSpace:
                if(x != compareRow):
                    bases.append(x)
            bBar = []
            aMat = []
            bVal = 0
            for x in bases:
                for y in x:
                    bVal = y
                bBar.append(bVal)
            
            for x in bases:
                i = 0
                oneRow = []
                while(i < len(bases[0])-1):
                    oneRow.append(x[i])
                    i = i +1
                aMat.append(oneRow)
            finalMatrix = Matrix(aMat)
            finalVec = Vec(bBar)
            solution = Matrix.solve(finalMatrix, finalVec)
            return(Vec(solution))
        else:
            lastRow = []
            aMat = []
            bBar = 0
            for x in workMatrix.rowSpace:
                lastRow = x
            for x in lastRow:
                if(x == lastRow[len(lastRow) - 1]):
                    bBar = x
                else:
                    aMat.append(x)
            allZeroA = False
            zerob = False
            for x in aMat:
                if(x == 0):
                    allZeroA = True
                if(x != 0):
                    allZeroA = False
                    break
            if(allZeroA and bBar != 0):
                print('no solution')
            if(allZeroA == False):
                print('infinitely many solutions')
        
    
   
#-------------TESTER CELL-------------------    
A = Matrix([[1, 2],[3, 4],[5, 6]])

print("Matrix A")           
print(A)
print()

print("The dimensions of the matrix are: ")
print(A.dim())
print()

print("The rank of the matrix is: ")
print(A.rank())
print()        