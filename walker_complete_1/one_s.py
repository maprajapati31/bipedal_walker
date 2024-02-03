
import numpy as np
import footstrike
import collision
#import main_walker
import ss
from scipy.integrate import solve_ivp

def one_step(t0,z0,params):

    tf = t0+4;
    t = np.linspace(t0, tf, 1001)
    collision.collision.terminal = True
    # contact.direction = -1
    # sol = solve_ivp(ss.single_stance,[t0, tf],z0,method='RK45', t_eval=t, dense_output=True, \
    #         args=(params.M,params.m,params.I,params.l,params.c,params.g,params.gam))
    sol = solve_ivp(ss.single_stance,[t0, tf],z0,method='RK45', t_eval=t, dense_output=True, \
                    events=collision.collision, atol = 1e-13,rtol = 1e-12, args=(params.M,params.m,params.I,params.l,params.c,params.g,params.gam))


    #get solution at different time steps from sol.y
    [m,n] = np.shape(sol.y)
    shape = (n,m)
    t = sol.t
    z = np.zeros(shape)

    #get event from sol.y_events and exact time sol.t_events
    [mm,nn,pp] = np.shape(sol.y_events)
    tt_last_event = sol.t_events[mm-1]
    yy_last_event = sol.y_events[mm-1]

    #save data in z
    for i in range(0,m):
        z[:,i] = sol.y[i,:]

    #get state before footstrike using events
    t_end = tt_last_event[0]
    theta1 = yy_last_event[0,0]
    omega1 = yy_last_event[0,1]
    theta2 = yy_last_event[0,2]
    omega2 = yy_last_event[0,3]

    zminus = np.array([theta1, omega1, theta2, omega2 ])

    #return state after footstrike
    zplus = footstrike.footstrike
    (t_end,zminus,params)

    #replace last entry in z and t
    t[n-1] = t_end
    z[n-1,0] = zplus[0];
    z[n-1,1] = zplus[1];
    z[n-1,2] = zplus[2];
    z[n-1,3] = zplus[3];


    return z,t

