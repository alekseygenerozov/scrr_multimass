from drr_multimass import DRR_Multimass
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as IUS
import numpy as np


agrid=np.logspace(-3, 0, 100)
# np.savetxt('a_multimass', agrid)
# f=open('t_rr_dat_ehi.csv','w')
# for ii,aa in enumerate(agrid):
idx=sys.argv[1]
drr = DRR_Multimass(agrid[idx], gamma=[1.75, 2.5], mbh_mass=4.3e6, mass_frac=[1, 0.01], rh=2.0, star_mass=[1, 10], j_grid_size=64)
djj, djj_err = drr(l_max=5)

np.savetxt('djj_multimass_{0}'.format(ii), np.transpose([drr.j, 1.0e6*djj]))


# f.close()




