Summary of changes from single component version

Cusp
1. Multimass-cusp (cusp_multimass.py): initialized with list of power law slopes (gammas), stellar masses (star_mass), and the mass fraction of each component (mass_frac). By default initialize a single component with the same defaults as cusp.py. We assume each component is described by a power law density profile. 

2. Methods total_stellar_mass, total_number_of_stars, stellar_mass, inverse_cumulative_a, _nu_mass0, _g, and _gp now take a positional argument corresponding to the index of one of the components. 
3. Method nu_mass returns the precession frequency due to the total enclosed mass by summing over all of the components. 
Diffusion coefficients (drr_mulitmass.py)

DRR

1. _drr and _drr_lnnp take the component number as one of their arguments. The diffusion coefficients are computed component by component, and then summed together in __call__.  Note that the key in _drr_lnnp_cache includes the component number.


    Examples
1. Example_multimass.py: saves diffusion coefficients for a grid of semi-major axes to files (djj_multimass_*.csv: each file corresponds to a different semi-major axis and contains two columns: j and the diffusion coefficient). 
Currently we have the default BW cusp with an r^-2.5 BH cusp with 1% of the mass inside of rh on top. 

1. Example_multimass_analysis.py: Computes j-averaged scalar resonant relaxation time (as described in Bar-Or and Fouvry 2018).
