from scrr_multimass.drr_multimass import DRR_Multimass
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as IUS
import numpy as np
import sys

agrid=np.logspace(-3, 0, 100)
idx=int(sys.argv[1])
# for idx in range(len(agrid)):
drr = DRR_Multimass(agrid[idx], gamma=[1.43, 1.8], mbh_mass=4.0e6, mass_frac=[1, 0.4], rh=7.0, star_mass=[1.0, 50], j_grid_size=64)
djj, djj_err = drr(l_max=5, neval=1e4)

np.savetxt('djj_multimass_{0}'.format(idx), np.transpose([drr.j, 1.0e6*djj]))


# f.close()




