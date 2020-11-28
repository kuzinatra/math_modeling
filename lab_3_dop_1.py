import numpy as np
N = int(input())
M = int(input())

A = np.ndarray (shape = (N,M))
for i in range(N):
  for j in range(M):
    A[i][j] = int(input())

B = np.ndarray (shape = (N,M))
for i in range(N):
  for j in range(M):
    B[i][j] = int(input())

C = np.ndarray (shape = (N,M))
for i in range(N):
  for j in range(M):
    if A[i][j] > B[i][j]:
      C[i][j] = A[i][j]
    else:
      C[i][j] = B[i][j]

print (C)
