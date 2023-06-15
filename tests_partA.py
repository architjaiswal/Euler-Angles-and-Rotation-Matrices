import numpy as np
from Euler import Euler_Angle, Euler_Angles_from_R, Fixed_Angle

######## Part A #######################

R_YXZ = Euler_Angle(60, 30, 60, 'yxz')
print("Rotation Matrix R_YXZ (alpha: 60, beta: 30, gamma: 60, order='yxz') is")
print(R_YXZ)


R_XYZ = Euler_Angle(30, 45, 60, 'xyz')
print("\nRotation Matrix R_XYZ = ")
print(R_XYZ)

## check your code
alpha, beta, gamma = Euler_Angles_from_R(R_YXZ, 'yxz')
print ("\nalpha, beta, gamma = ")
print (alpha, beta, gamma)

## Find the axis of rotation
Eval, Evec = np.linalg.eig(R_XYZ)
print ("\nEigen Values = ")
print (Eval)
print ("\nEigen Vectors = ")
print (Evec)

print("\nAxis of rotation is the vector who's eigenvalue is 1")
print("The axis of rotation is: ", Evec[:,0])
