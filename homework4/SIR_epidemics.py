import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N  = 130                   # total number of individuals
I0 = 1                      # initial number of infectives
S0 = N-I0                   # initial number of susceptibles
R0 = 0                      # initial number of recovered individuals
z0 = [S0,I0,R0]             # initial condition
r  = 0.1693                 # infection rate [1/(ind*day)]
a  = 0.125                  # removal rate of infectives [1/day]
ti = 0                      # initial time
tf = 20                     # final time
nt = 101                    # number of time points
t  = np.linspace(ti,tf,nt)  # time points

# function that returns dy/dt
def model(z,t,r,a):
    S = z[0]
    I = z[1]
    R = z[2]
    dSdt = -r*S*I
    dIdt = +r*S*I - a*I
    dRdt = +a*I
    dzdt = [dSdt,dIdt,dRdt]
    return dzdt

# Time evolution
z = odeint(model,z0,t,args=(r,a))
S = z[:,0]
I = z[:,1]
R = z[:,2]

# plot timeseries
plt.plot(t,S,'--b',label='S')
plt.plot(t,I,'r',label='I')
plt.plot(t,R,'-.k',label='R')
ax = plt.gca()
plt.xlabel('time [days]')
plt.ylabel('number of individuals')
plt.legend(loc='best')
plt.axis((t[0],t[-1],0,1.02*np.max(z)))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.savefig('./SIR.png')
plt.show()

# State diagrams
# plt.figure
# for i in range(1,10):
#     zi = odeint(model,[(10-i)*N/10,i*N/10,0],t,args=(r,a))
#     plt.plot(zi[:,0],zi[:,1],'b')
# plt.plot([0,N],[N,0],'b')
# plt.plot([a/r,a/r],[0,N-a/r],'--b')
# plt.axis((0,N,0,N))
# plt.xlabel('S')
# plt.ylabel('I')
# ax = plt.gca()
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# plt.savefig('./SIR_state.png')
# plt.show()
