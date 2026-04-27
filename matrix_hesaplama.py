

M1=[[1,3],[2,-2]]
M2=[[-2,5],[7,14]]
M3=[[0,0],[0,0]]
M4=[[0,0],[0,0]]
matrix_length=len(M1)
for i in range(matrix_length):
    for j in range(matrix_length):
        M3[i][j]=M1[i][j]+M2[i][j]
        M4[i][j]=M1[i][j]-M2[i][j]
print("m1=",M1)
print("m2=",M2)
print("m3=",M3)
print("m4=",M4)



