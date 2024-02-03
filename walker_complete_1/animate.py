#importing libraries
from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate

def sin(angle):
    return np.sin(angle)

def cos(angle):
    return np.cos(angle)

def animate(t,z,params):    
    #interpolation so that animation is smooth
    data_pts = 1/params.fps
    t_interp = np.arange(t[0],t[len(t)-1],data_pts)
    [m,n] = np.shape(z)
    shape = (len(t_interp),n)
    z_interp = np.zeros(shape)

    for i in range(0,n):
        f = interpolate.interp1d(t, z[:,i])
        z_interp[:,i] = f(t_interp)

    l = params.l
    c = params.c

    min_xh = min(z[:,4]); max_xh = max(z[:,4]);
    dist_travelled = max_xh - min_xh;
    camera_rate = dist_travelled/len(t_interp);

    window_xmin = -1*l; window_xmax = 1*l;
    window_ymin = -0.1; window_ymax = 1.1*l;

    R1 = np.array([min_xh-l,0])
    R2 = np.array([max_xh+l,0])

    ramp, = plt.plot([R1[0], R2[0]],[R1[1], R2[1]],linewidth=5, color='black')
    #plot
    
    #animation loop
    for i in range(0,len(t_interp)):
        theta1 = z_interp[i,0];
        theta2 = z_interp[i,2];
        xh = z_interp[i,4];
        yh = z_interp[i,5];

        H = np.array([xh, yh])
        C1 = np.array([xh+l*sin(theta1), yh-l*cos(theta1)])
        G1 = np.array([xh+c*sin(theta1), yh-c*cos(theta1)])
        C2 = np.array([xh+l*sin(theta1+theta2),yh-l*cos(theta1+theta2)])
        G2 = np.array([xh+c*sin(theta1+theta2),yh-c*cos(theta1+theta2)])

        hip, = plt.plot(H[0],H[1],color='black',marker='o',markersize=10)
        leg1, = plt.plot([H[0], C1[0]],[H[1], C1[1]],linewidth=5, color='red')
        leg2, = plt.plot([H[0], C2[0]],[H[1], C2[1]],linewidth=5, color='green')
        com1, = plt.plot(G1[0],G1[1],color='black',marker='o',markersize=5)
        com2, = plt.plot(G2[0],G2[1],color='black',marker='o',markersize=5)

        window_xmin = window_xmin + camera_rate;
        window_xmax = window_xmax + camera_rate;
        plt.xlim(window_xmin,window_xmax)
        plt.ylim(window_ymin,window_ymax)
        plt.gca().set_aspect('equal')

        #pause animation, clear previous points and reiterate
        plt.pause(params.pause)
        hip.remove()
        leg1.remove()
        leg2.remove()
        com1.remove()
        com2.remove()

    plt.close()