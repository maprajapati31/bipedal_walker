import t_angles
import numpy as np

def footstrike(t, z, params):
    theta1_n,omega1_n,theta2_n,omega2_n = z

    theta1 = theta1_n + theta2_n;
    theta2 = -theta2_n;

    M = params.M
    m = params.m
    I = params.I
    l = params.l
    c = params.c
    g = params.g
    gam = params.gam

    J11 =  1
    J12 =  0
    J13 =  l*(-t_angles.cos(theta1_n) + t_angles.cos(theta1_n + theta2_n))
    J14 =  l*t_angles.cos(theta1_n + theta2_n)
    J21 =  0
    J22 =  1
    J23 =  l*(-t_angles.sin(theta1_n) + t_angles.sin(theta1_n + theta2_n))
    J24 =  l*t_angles.sin(theta1_n + theta2_n)

    J = np.array([[J11, J12, J13, J14], [J21,J22,J23,J24]])

    A11 =  1.0*M + 2.0*m
    A12 =  0
    A13 =  -1.0*M*l*t_angles.cos(theta1_n) + m*(c - l)*t_angles.t_angles.cos(theta1_n) + 1.0*m*(c*t_angles.cos(theta1_n + theta2_n) - l*t_angles.cos(theta1_n))
    A14 =  1.0*c*m*t_angles.cos(theta1_n + theta2_n)
    A21 =  0
    A22 =  1.0*M + 2.0*m
    A23 =  -1.0*M*l*t_angles.sin(theta1_n) + m*(c - l)*t_angles.sin(theta1_n) + m*(c*t_angles.sin(theta1_n + theta2_n) - l*t_angles.sin(theta1_n))
    A24 =  1.0*c*m*t_angles.sin(theta1_n + theta2_n)
    A31 =  -1.0*M*l*t_angles.cos(theta1_n) + m*(c - l)*t_angles.cos(theta1_n) + 1.0*m*(c*t_angles.cos(theta1_n + theta2_n) - l*t_angles.cos(theta1_n))
    A32 =  -1.0*M*l*t_angles.sin(theta1_n) + m*(c - l)*t_angles.sin(theta1_n) + m*(c*t_angles.sin(theta1_n + theta2_n) - l*t_angles.sin(theta1_n))
    A33 =  2.0*I + M*l**2 + m*(c - l)**2 + m*(c**2 - 2*c*l*t_angles.cos(theta2_n) + l**2)
    A34 =  1.0*I + c*m*(c - l*t_angles.cos(theta2_n))
    A41 =  1.0*c*m*t_angles.cos(theta1_n + theta2_n)
    A42 =  1.0*c*m*t_angles.sin(theta1_n + theta2_n)
    A43 =  1.0*I + c*m*(c - l*t_angles.cos(theta2_n))
    A44 =  1.0*I + c**2*m
    A_n_hs = np.array([[A11, A12, A13, A14], [A21, A22, A23, A24], [A31, A32, A33, A34], [A41, A42, A43, A44]])

    X_n_hs = np.array([0, 0, omega1_n, omega2_n])
    b_temp  = A_n_hs.dot(X_n_hs)
    b_hs = np.block([ b_temp, 0, 0 ])
    zeros_22 = np.zeros((2,2))
    A_hs = np.block([[A_n_hs, -np.transpose(J)] , [ J, zeros_22] ])
    invA_hs = np.linalg.inv(A_hs)
    X_hs = invA_hs.dot(b_hs)
    omega1 = X_hs[2] + X_hs[3]
    omega2 = -X_hs[3]

    return [theta1,omega1,theta2,omega2]
