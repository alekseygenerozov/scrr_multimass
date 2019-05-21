from drr_multimass import DRR_Multimass
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline as IUS
import numpy as np
import sys

agrid=np.logspace(-3, 0, 100)
idx=int(sys.argv[1])
drr = DRR_Multimass(agrid[idx], gamma=[1.75, 2.0], mbh_mass=4.3e6, mass_frac=[1, 0.01], rh=2.0, star_mass=[1, 10], j_grid_size=64)
djj, djj_err = drr(l_max=5)

np.savetxt('djj_multimass_{0}'.format(idx), np.transpose([drr.j, 1.0e6*djj]))


# f.close()




