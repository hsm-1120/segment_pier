import numpy as np
from openseespy.opensees import *
import pandas as pd
import os
from build.model_build import seg
from build.analysis import *


# initial parameters
r_d = 0.02
t_d = 0.01
i_f = 80
i_p = -220
# model
seg(t_d, r_d, i_f)
# static recorder
# node_disp = f'data/output/quasi_static/{r_d}_{t_d}_{i_f}_{i_p}_5disp.out'
# joint_open = f'data/output/quasi_static/{r_d}_{t_d}_{i_f}_{i_p}_311disp.out'
# tendon_force = f'data/output/quasi_static/{r_d}_{t_d}_{i_f}_{i_p}_101force.out'
# rebar_force = f'data/output/quasi_static/{r_d}_{t_d}_{i_f}_{i_p}_201force.out'

# recorder('Node', '-file', node_disp, '-time', '-node', 5, '-dof', 1, 'disp')
# recorder('Node', '-file', joint_open, '-time', '-node', 311, '-dof', 3, 'disp')
# recorder('Element', '-file', tendon_force, '-time', '-ele', 101, 'axialForce')
# recorder('Element', '-file', rebar_force, '-time', '-ele', 201, 'axialForce')

# quasi_static(i_p, 6)

# seismic recorder
tag = 'RSN944_NORTHR_WBA000'
dt = 0.01
npt = 3499
pga = 0.074
node_his = f'data/output/quasi_static/{tag}_311disp.out'
# recorder('Node', '-file', node_his, '-time', '-node', 5, '-dof', 1, 'disp')
recorder('Element', '-file', node_his, '-time', '-ele', 201, 'axialForce')
seismic(tag, dt, npt, pga)