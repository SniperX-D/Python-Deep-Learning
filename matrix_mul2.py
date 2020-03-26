import numpy as np

def matrixmult (A, B):
	res = []
	for i in range(B.__len__()):
		sum = 0
		for j in range(B[i].__len__()):
			sum += A[i][j] * B[i][j]
		res.append(sum)

	f_res = 0
	for i in range(res.__len__()):
		f_res += res[i]

	return f_res

def matrix_mul2(A,B):
	try:
		res = []
		for i in range(A.__len__() - B.__len__() + 1):
			tmp_arr = []
			for j in range(A[i].__len__() - B[0].__len__() + 1):
				cal_matrix = [] # matrix to calculate with B
				for k in range(B.__len__()):
					tmp = []
					for h in range(B[k].__len__()):
						tmp.append(A[i+k][j+h])
					cal_matrix.append(tmp)
				tmp_arr.append(matrixmult(cal_matrix, B))
		
			res.append(tmp_arr)
		
		return res
	except():
		return 0

A = [[0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0], [0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0], [0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0], [0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0], [0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0], [0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0], [0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0], [0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0]]
B = [[0.0,1.0,0.0], [0.0,1.0,0.0], [0.0,1.0,0.0]]

print(matrix_mul2(A,B))
print("----------------------------------------------------------------------------")
B = np.random.rand(3,3)

res = matrix_mul2(A,B)
while (res != []):
	print(res)
	res = matrix_mul2(res,B)
	