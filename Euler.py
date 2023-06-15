import numpy as np
from math import radians, degrees, atan2, sqrt


def Fixed_Angle(alpha, beta, gamma, order='xyz'):
    """
    input
        alpha, beta, gamma = rotation angles in rotation order (degrees)
    output
        3x3 rotation matrix (numpy array) based on Fixed-Angle (original static axis)
    """
    c_alpha = np.cos(radians(alpha))
    s_alpha = np.sin(radians(alpha))

    c_beta = np.cos(radians(beta))
    s_beta = np.sin(radians(beta))

    c_gamma = np.cos(radians(gamma))
    s_gamma = np.sin(radians(gamma))

    R_Z = np.array([[c_alpha, -s_alpha, 0],
                    [s_alpha, c_alpha, 0],
                    [0, 0, 1]]
                   )

    R_Y = np.array([[c_beta, 0, s_beta],
                    [0, 1, 0],
                    [-s_beta, 0, c_beta]]
                   )

    R_X = np.array([[1, 0, 0],
                    [0, c_gamma, -s_gamma],
                    [0, s_gamma, c_gamma]]
                   )

    if order == 'xyz':
        matrix = R_Z @ R_Y @ R_X
    elif order == 'zyx':
        matrix = R_X @ R_Y @ R_Z
    elif order == 'yzx':
        matrix = R_X @ R_Z @ R_Y
    # complete other cases
    elif order == 'xzy':
        matrix = R_Y @ R_Z @ R_X
    elif order == 'yxz':
        matrix = R_Z @ R_X @ R_Y
    elif order == 'zxy':
        matrix = R_Y @ R_X @ R_Z

    else:
        matrix = np.identity(3)

    return matrix


def Euler_Angle(alpha, beta, gamma, order='xyz'):
    """
    input
        alpha, beta, gamma = rotation angles in rotation order (degrees)
    output
        3x3 rotation matrix (numpy array) based on Euler-Angle (moving axis)
    """
    # complete the code (hint: you can just call the previous function with 1 line of code!)

    matrix = Fixed_Angle(alpha, beta, gamma, order[::-1])

    return matrix


def Euler_Angles_from_R(matrix, order='xyz'):
    """
    input
        3x3 rotation matrix (numpy array) based on Euler-Angle (moving axis)
    output
        return alpha, beta, gamma in degrees (for all 6 orders)
    """
    r11, r12, r13 = matrix[0]
    r21, r22, r23 = matrix[1]
    r31, r32, r33 = matrix[2]

    if order == 'xzy':
        alpha = atan2(-r12, sqrt(r32 ** 2 + r22 ** 2))
        beta = atan2(r13, r11)
        gamma = atan2(r32, r22)

    elif order == 'xyz':
        alpha = atan2(-r12, r11)
        beta = atan2(r13, sqrt(r11 ** 2 + r12 ** 2))
        gamma = atan2(-r23, r33)

    elif order == 'yxz':
        alpha = atan2(r21, r22)
        beta = atan2(r13, r33)
        gamma = atan2(-r23, sqrt(r21 ** 2 + r22 ** 2))

    elif order == 'yzx':
        alpha = atan2(r21, sqrt(r22 ** 2 + r23 ** 2))
        beta = atan2(-r31, r11)
        gamma = atan2(-r23, r22)

    elif order == 'zyx':
        alpha = atan2(r21, r11)
        beta = atan2(-r31, sqrt(r11 ** 2 + r21 ** 2))
        gamma = atan2(r32, r33)

    elif order == 'zxy':
        alpha = atan2(-r21, r22)
        beta = atan2(-r31, r33)
        gamma = atan2(r32, sqrt(r31 ** 2 + r33 ** 2))

    else:
        alpha, beta, gamma = 0, 0, 0

    return degrees(alpha), degrees(beta), degrees(gamma)
