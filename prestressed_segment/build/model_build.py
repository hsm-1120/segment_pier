# start date:2022/11/09 | 2022/11/21
# author:hsm
# zerolength section -> seam

import numpy as np
from openseespy.opensees import *
import pandas as pd
import os
# from analysis import *


def seg(tendon_d, rebar_d, ini_f):

    # create output folder
    storage_path = 'data/output'
    if not os.path.exists(storage_path):
        os.mkdir(storage_path)

    # log file for error
    logFile('error.log', '-noEcho')

    # start build
    print('\033[0;33;45m####<Start Building!>####\033[0m\n')

    wipe()
    model('basic', '-ndm', 3, '-ndf', 6)

    # variables for analysis
    ini_ss   = ini_f / (tendon_d ** 2 * np.pi / 4)
    ini_sn   = ini_ss / 1.95e8

#----------------------------------------build node------------------------------------------------#
    node(1, 0, 0, 0, '-mass', 0.25, 0.25, 0.25, 0, 0, 0)
    node(2, 0, 0, 0.1, '-mass', 0.25, 0.25, 0.25, 0, 0, 0)
    node(3, 0, 0, 0.6, '-mass', 0.25, 0.25, 0.25, 0, 0, 0)
    node(4, 0, 0, 1.2, '-mass', 0.25, 0.25, 0.25, 0, 0, 0)
    node(5, 0, 0, 1.8, '-mass', 0.25, 0.25, 0.25, 0, 0, 0)
    # tendon
    node(101, 0.2, 0.2, -0.5, '-mass', 0, 0, 0, 0, 0, 0)
    node(105, 0.2, 0.2, 1.8, '-mass', 0, 0, 0, 0, 0, 0)
    node(111, -0.2, 0.2, -0.5, '-mass', 0, 0, 0, 0, 0, 0)
    node(113, -0.2, 0.2, 1.8, '-mass', 0, 0, 0, 0, 0, 0)
    node(121, 0.2, -0.2, -0.5, '-mass', 0, 0, 0, 0, 0, 0)
    node(123, 0.2, -0.2, 1.8, '-mass', 0, 0, 0, 0, 0, 0)
    node(131, -0.2, -0.2, -0.5, '-mass', 0, 0, 0, 0, 0, 0)
    node(133, -0.2, -0.2, 1.8, '-mass', 0, 0, 0, 0, 0, 0)
    # rebar
    node(201, 0.3, 0.3, -0.2, '-mass', 0, 0, 0, 0, 0, 0)
    node(202, 0.3, 0.3, 0.1, '-mass', 0, 0, 0, 0, 0, 0)
    node(211, -0.3, 0.3, -0.2, '-mass', 0, 0, 0, 0, 0, 0)
    node(212, -0.3, 0.3, 0.1, '-mass', 0, 0, 0, 0, 0, 0)
    node(221, 0.3, -0.3, -0.2, '-mass', 0, 0, 0, 0, 0, 0)
    node(222, 0.3, -0.3, 0.1, '-mass', 0, 0, 0, 0, 0, 0)
    node(231, -0.3, -0.3, -0.2, '-mass', 0, 0, 0, 0, 0, 0)
    node(232, -0.3, -0.3, 0.1, '-mass', 0, 0, 0, 0, 0, 0)
    # spring
    node(301, -0.2, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(302, -0.15, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(303, -0.1, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(304, -0.05, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(305, 0.2, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(306, 0.15, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(307, 0.1, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(308, 0.05, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(311, -0.2, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(312, -0.15, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(313, -0.1, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(314, -0.05, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(315, 0.2, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(316, 0.15, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(317, 0.1, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
    node(318, 0.05, 0, 0, '-mass', 0, 0, 0, 0, 0, 0)
 
#--------------------------------------boundary-condition---------------------------------------#
    print('\033[1;31;47m####<Boundary Condition>####\033[0m\n')
    # 
    fix(101, 1, 1, 1, 1, 1, 1)
    fix(111, 1, 1, 1, 1, 1, 1)
    fix(121, 1, 1, 1, 1, 1, 1)
    fix(131, 1, 1, 1, 1, 1, 1)

    fix(201, 1, 1, 1, 1, 1, 1)
    fix(211, 1, 1, 1, 1, 1, 1)
    fix(221, 1, 1, 1, 1, 1, 1)
    fix(231, 1, 1, 1, 1, 1, 1)
    # 
    fix(301, 1, 1, 1, 1, 1, 1)
    fix(302, 1, 1, 1, 1, 1, 1)
    fix(303, 1, 1, 1, 1, 1, 1)
    fix(304, 1, 1, 1, 1, 1, 1)
    fix(305, 1, 1, 1, 1, 1, 1)
    fix(306, 1, 1, 1, 1, 1, 1)
    fix(307, 1, 1, 1, 1, 1, 1)
    fix(308, 1, 1, 1, 1, 1, 1)

    # body
    rigidLink('beam', 5, 105)
    rigidLink('beam', 5, 113)
    rigidLink('beam', 5, 123)
    rigidLink('beam', 5, 133)

    rigidLink('beam', 2, 202)
    rigidLink('beam', 2, 212)
    rigidLink('beam', 2, 222)
    rigidLink('beam', 2, 232)

    rigidLink('beam', 1, 311)
    rigidLink('beam', 1, 312)
    rigidLink('beam', 1, 313)
    rigidLink('beam', 1, 314)
    rigidLink('beam', 1, 315)
    rigidLink('beam', 1, 316)
    rigidLink('beam', 1, 317)
    rigidLink('beam', 1, 318)
    
    geomTransf('Linear', 1, 1.0, 0.0, 0.0)
#----------------------------------------material------------------------------------------------#
    print('\033[1;31;47m####<Material/Fiber Section>####\033[0m\n')
    uniaxialMaterial('Steel02', 1, 4.0e5, 2.0e8, 0.001, 10, 0.925, 0.15)
    uniaxialMaterial('ENT', 2, 1.01e6)  # spring
    uniaxialMaterial('Elastic', 3, 1e7)
    uniaxialMaterial('ElasticPP', 4, 1.95e8, .01, -.01, 0)  # tendon
    uniaxialMaterial('InitStressMaterial', 5, 4, ini_ss)

#--------------------------------------element------------------------------------------------#
    print('\033[1;31;47m####<Element>####\033[0m\n')
    # segment element
    element('Truss', 101, 101, 105, tendon_d ** 2 * np.pi / 4, 5)
    element('Truss', 111, 111, 113, tendon_d ** 2 * np.pi / 4, 5)
    element('Truss', 121, 121, 123, tendon_d ** 2 * np.pi / 4, 5)
    element('Truss', 131, 131, 133, tendon_d ** 2 * np.pi / 4, 5)

    element('Truss', 201, 201, 202, rebar_d ** 2 * np.pi / 4, 1)
    element('Truss', 211, 211, 212, rebar_d ** 2 * np.pi / 4, 1)
    element('Truss', 221, 221, 222, rebar_d ** 2 * np.pi / 4, 1)
    element('Truss', 231, 231, 232, rebar_d ** 2 * np.pi / 4, 1)

    element('elasticBeamColumn', 1, 1, 2, 0.16, 3.25e7, 6.5e6, 0.004, 0.002, 0.002, 1)
    element('elasticBeamColumn', 2, 2, 3, 0.16, 3.25e7, 6.5e6, 0.004, 0.002, 0.002, 1)
    element('elasticBeamColumn', 3, 3, 4, 0.16, 3.25e7, 6.5e6, 0.004, 0.002, 0.002, 1)
    element('elasticBeamColumn', 4, 4, 5, 0.16, 3.25e7, 6.5e6, 0.004, 0.002, 0.002, 1)

    element('zeroLength', 301, 301, 311, '-mat', 2, 3, 3, '-dir', 1, 2, 3, '-orient', 0, 0, 1, 1, 0, 0)
    element('zeroLength', 302, 302, 312, '-mat', 2, 3, 3, '-dir', 1, 2, 3, '-orient', 0, 0, 1, 1, 0, 0)
    element('zeroLength', 303, 303, 313, '-mat', 2, 3, 3, '-dir', 1, 2, 3, '-orient', 0, 0, 1, 1, 0, 0)
    element('zeroLength', 304, 304, 314, '-mat', 2, 3, 3, '-dir', 1, 2, 3, '-orient', 0, 0, 1, 1, 0, 0)
    element('zeroLength', 305, 305, 315, '-mat', 2, 3, 3, '-dir', 1, 2, 3, '-orient', 0, 0, 1, 1, 0, 0)
    element('zeroLength', 306, 306, 316, '-mat', 2, 3, 3, '-dir', 1, 2, 3, '-orient', 0, 0, 1, 1, 0, 0)
    element('zeroLength', 307, 307, 317, '-mat', 2, 3, 3, '-dir', 1, 2, 3, '-orient', 0, 0, 1, 1, 0, 0)
    element('zeroLength', 308, 308, 318, '-mat', 2, 3, 3, '-dir', 1, 2, 3, '-orient', 0, 0, 1, 1, 0, 0)

    print('\033[0;33;42m####<Finish Building!>####\033[0m\n')
