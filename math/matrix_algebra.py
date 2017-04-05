# Matrix Algebra

import math
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])
rng = [A,B,C,D,u,w]
j = 1
for i in rng:
	print('1.'+str(j), 'dimension', i.shape)
	j += 1

alpha = 6
print('2.1', u+v)
print('2.2', u-v)
print('2.3', alpha*u)
print('2.4', np.sum(u*v))

dot = np.dot(u, v)
u_modulus = np.sqrt((u*u).sum())
v_modulus = np.sqrt((v*v).sum())
cos_angle = dot / u_modulus / v_modulus
angle = np.arccos(cos_angle)

print('2.5', angle*360 / 2 / np.pi)
print('2.5', u_modulus)

print('3.1 not defined')
print('3.2', A-np.matrix.transpose(C))
print('3.3', np.matrix.transpose(C)+ 3*D)
print('3.4', np.dot(B, A))
print('3.5 not defined')
print('3.6 not defined')
print('3.7', np.dot(C, B))
print('3.8', B**4)
print('3.9', np.dot(A, np.matrix.transpose(A)))
print('3.10', np.dot(np.matrix.transpose(D), D))
