#importing libraries
from matplotlib import pyplot as plt
import numpy as np
import math
import scipy
from scipy import interpolate
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

#importing modules
import animate
import n_steps
import one_s

#creating instance of parameters class with default values
class parameters:
    def __init__(self):
        self.g = 1 
        self.m = 0.5
        self.M = 1
        self.I = 0.02
        self.l = 1.0
        self.c = 0.5
        self.gam = 0.01
        self.pause = 0.01
        self.fps = 10

def fixedpt(z0,params):
    t0 = 0
    [z1,t1] = one_s.one_step(t0,z0,params)
    N = len(t1)-1
    #F(x0) - x0 = 0
    return z1[N,0]-z0[0], z1[N,1]-z0[1],z1[N,2]-z0[2],z1[N,3]-z0[3]


def partialder(z0,params):

    pert = 1e-5
    N = len(z0)

    J = np.zeros((N,N))
    z_temp1 = [0]*N
    z_temp2 = [0]*N
    for i in range(0,N):
        for j in range(0,N):
            z_temp1[j] = z0[j]
            z_temp2[j] = z0[j]
        z_temp1[i] = z_temp1[i]+pert
        z_temp2[i] = z_temp2[i]-pert
        [z1,t1] = one_s.one_step(0,z_temp1,params)
        [z2,t2] = one_s.one_step(0,z_temp2,params)
        for j in range(0,N):
            J[i,j] = (z1[len(t1)-1,j] - z2[len(t2)-1,j])/(2*pert)

    return J

params = parameters();

# this is the fixed point
# q1 = 0.162597833780035;
# u1 = -0.231869638058927;
# q2 = -0.325195667560070;
# u2 = 0.037978468073736;

#an initial guess
q1 = 0.2; u1 = -0.25; q2 = -0.4; u2 = 0.2;
z0 = np.array([q1,u1,q2,u2])
#dz = fixedpt(z0,params)
zstar=fsolve(fixedpt, z0,params)
print(zstar)

J = partialder(zstar,params)
eigVal,eigVec = np.linalg.eig(J)
# print(eigVal)
# print(eigVec)
print(np.abs(eigVal))

t0 = 0;
#defines number of steps that you want the walker to walk
steps = 20;
[z,t] = n_steps.n_steps(t0,zstar,params,steps)
# print(t[len(t)-1])

animate.animate(t,z,params)
