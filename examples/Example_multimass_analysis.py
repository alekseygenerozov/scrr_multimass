# from scrrpy import DRR
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as IUS
import numpy as np
import sys


agrid=np.logspace(-3, 0, 100)
times=np.empty_like(agrid)
times2=np.empty_like(agrid)
loc=sys.argv[1]

jo=(1.0-float(sys.argv[2])**2.0)**0.5
fig,ax=plt.subplots(figsize=(10,9))
for ii,aa in enumerate(agrid):
	dat=np.genfromtxt(loc+'/djj_multimass_{0}'.format(ii))
	print(dat[-1,0])
	times[ii]=(IUS(dat[:,0], 2*dat[:,0]*dat[:,1]).integral(dat[0,0],dat[-1,0]))**-1.0
	times2[ii]=IUS(dat[:,0], 2*dat[:,0]/dat[:,1]).integral(jo,dat[-1,0])

np.savetxt(loc+'/t_rr_dat_multimass.csv', np.transpose([agrid, times]))
np.savetxt(loc+'/t_rr_dat_multimass_ecc{0}.csv'.format(sys.argv[2]), np.transpose([agrid, times2]))

ax.loglog(agrid, times)
ax.loglog(agrid, times2)
fig.savefig(loc+'/trr_multimass.pdf')

# for ii,aa in enumerate(agrid):
# 	dat=np.genfromtxt('djj_multimass_{0}'.format(ii))

# 	times[ii]=IUS(dat[:,0], 2*dat[:,0]*dat[:,1]).integral(dat[0,0],dat[-1,0])**-1.0






