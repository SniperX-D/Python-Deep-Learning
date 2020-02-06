def matrixmult (A, B): #base function for matrix mul
    if not check_matrixs(A,B): # if statments to check if mul is possible in two ways
        if check_matrixs(B,A):
            tmp = B
            B = A
            A = tmp
        else:
            print ("Error: cant mul matrixes!")
            return
    C = []
    for row in range(A.__len__()):
        C.append([])
        for col in range(B[0].__len__()):
            C[row].append(cal(A[row],col_to_array(B,col)))

    print(C)

def cal(arr1, arr2): #calculates mul between two arrays
    sum = 0
    print ("arr1", arr1, "arr2", arr2)
    for i in range(arr1.__len__()):
        sum += (arr1[i] * arr2[i])
    print ("sum: ",sum)
    return sum

def check_matrixs(A,B): #checks if its possible to do matrix mul
    if A[0].__len__() == B.__len__():
        return True
    return False

def col_to_array(matrix, col): #converts the numbers at the matrixes colums to an array
    ret = []
    print("matrix", matrix)
    for i in matrix:
        ret.append(i[col])
    print ("ret",ret)
    return ret


A = [[1,2,3], [1,2,3], [1,2,3]]
B = [[1,2,3], [1,2,3], [1,2,3]]

matrixmult(A,B)