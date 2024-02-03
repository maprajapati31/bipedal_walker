
def sin(angle):
    return np.sin(angle)

def cos(angle):
    return np.cos(angle)

import numpy as np
import one_s

def n_steps(t0,z0,params,steps):

    z = z0
    t = t0

    #initialise walker's position variables
    theta1 = z0[0];
    l = params.l
    xh = 0
    yh = l*cos(theta1)
    xh_start = xh
    

    zz = np.append(z0,np.array([xh,yh]))
    for i in range(0,steps):
        [z_temp,t_temp] = one_s.one_step(t0,z0,params)
        [mm,nn] = np.shape(z_temp)
        zz_temp = np.zeros( (mm,6))
        for j in range(0,mm):
            xh = xh_start + l*sin(z_temp[0,0])-l*sin(z_temp[j,0]);
            yh = l*cos(z_temp[j,0]);
            zz_temp[j,:] = np.append(z_temp[j,:],np.array([xh,yh]))
        xh_start = zz_temp[mm-2,4]
        if i==0:
            #z = np.concatenate(([z], z_temp[1:mm-1,:]), axis=0)
            t = np.concatenate(([t], t_temp[1:mm-1]), axis=0)
            zz = np.concatenate(([zz], zz_temp[1:mm-1,:]), axis=0)
        else:
            #z = np.concatenate((z, z_temp[1:mm-1,:]), axis=0)
            t = np.concatenate((t, t_temp[1:mm-1]), axis=0)
            zz = np.concatenate((zz, zz_temp[1:mm-1,:]), axis=0)
        theta1 = z_temp[mm-1,0]
        omega1 = z_temp[mm-1,1]
        theta2 = z_temp[mm-1,2]
        omega2 = z_temp[mm-1,3]
        z0 = np.array([theta1, omega1, theta2, omega2])
        t0 = t_temp[mm-1]

    return zz,t
