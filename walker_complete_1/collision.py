
def collision(t, z, M,m,I,l,c,g,gam):
    #z is a vector that represents the state of the system
    theta1,omega1,theta2,omega2 = z

    if (theta1>-0.05): 
        #allow legs to pass through for small hip angles (taken care in real walker using stepping stones)
        gstop = 1
    else:
        gstop = theta2 + 2*theta1

    #value returned by gstop is used by numerical simulations solver to detect event occurence, in this case, collision
    return gstop
    