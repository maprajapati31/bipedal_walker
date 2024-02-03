import numpy as np
import t_angles

def single_stance(t, z, M,m,I,l,c,g,gam):

    theta1,omega1,theta2,omega2 = z

    A11 =  2.0*I + M*l**2 + m*(c - l)**2 + m*(c**2 - 2*c*l*t_angles.cos(theta2) + l**2)
    A12 =  1.0*I + c*m*(c - l*t_angles.cos(theta2))
    A21 =  1.0*I + c*m*(c - l*t_angles.cos(theta2))
    A22 =  1.0*I + c**2*m

    b1 =  -M*g*l*t_angles.sin(gam - theta1) + c*g*m*t_angles.sin(gam - theta1) - c*g*m*t_angles.sin(-gam + theta1 + theta2) - 2*c*l*m*omega1*omega2*t_angles.sin(theta2) - c*l*m*omega2**2*t_angles.sin(theta2) - 2*g*l*m*t_angles.sin(gam - theta1)
    b2 =  1.0*c*m*(-g*t_angles.sin(-gam + theta1 + theta2) + l*omega1**2*t_angles.sin(theta2))

    A_ss = np.array([[A11, A12], [A21,A22]])
    b_ss = np.array([b1,b2])

    invA_ss = np.linalg.inv(A_ss)
    thetaddot = invA_ss.dot(b_ss)
    alpha1 = thetaddot[0]
    alpha2 = thetaddot[1]

    return [omega1,alpha1,omega2,alpha2]