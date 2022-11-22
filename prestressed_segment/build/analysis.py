
import numpy as np
from openseespy.opensees import *
import pandas as pd
import os


def recorder_define(folder, item, tag):

    if item == 'node':
        recorder('Node', '-file', folder, '-time', '-node', int(tag), '-dof', 1, 2, 3, 'disp')

    if item == 'truss':
        recorder('Element', '-file', forder, '-time', '-ele', int(tag), 'axialForce')

    if item == 'zeroLength':
        recorder('Element', '-file', forder, '-time', '-ele', int(tag), 'force')


def quasi_static(axial_load, step):

    folder = 'data/output/quasi_static'
    if not os.path.exists(folder):
        os.mkdir(folder)

    wipeAnalysis()
    timeSeries('Linear', 1)
    pattern('Plain', 1, 1)
    load(5, 0, 0, axial_load, 0, 0, 0)
    integrator('LoadControl', 0.1)
    system('SparseGeneral')
    test('NormDispIncr', 1.0e-4, 100, 0)
    numberer('RCM')
    constraints('Transformation')
    algorithm('KrylovNewton')
    analysis('Static')
    ok = analyze(10)
    if ok != 0:
        print('\033[1;37;41m####<axial load Failed!>####\033[0m\n')
    else:
        print('\033[1;37;42m####<axial load Succeed!>####\033[0m\n')

    loadConst('-time', 0.0)
    #############################################################
    rcl = pd.read_excel('data/input/model_infor/7_recorder.xlsx')
    for tag, item in zip(rcl.iloc[:, 0], rcl.iloc[:, 1]):
        savepath = folder + f'/{item}_{tag}.out'
        recorder_define(savepath, item, tag)
    record()
    #############################################################
    ##########################################>-->analysis module
    # cyclic load
    ##########################################>-|->lateral load
    timeSeries('Linear', 2)
    pattern('Plain', 2, 2)
    load(5, 1, 0, 0, 0, 0, 0)
    system('SparseGeneral', '-piv')
    test('NormDispIncr', 1.0e-4, 100, 0)
    numberer('RCM')
    constraints('Transformation')
    algorithm('KrylovNewton')
    analysis('Static')
    for i in range(step):
        integrator('DisplacementControl', 5, 1, 0.001)
        ok1=analyze(10 * (i + 1))
        integrator('DisplacementControl', 5, 1, -0.001)
        ok2=analyze(10 * (i + 1))
        integrator('DisplacementControl', 5, 1, -0.001)
        ok3=analyze(10 * (i + 1))
        integrator('DisplacementControl', 5, 1, 0.001)
        ok4=analyze(10 * (i + 1))
        if (ok1 + ok2 + ok3 + ok4) != 0:
        # if ok1 != 0:
            print('\033[1;37;41m####<No.{} step Failed!>####\033[0m\n'.format(i + 1))
        else:
            print('\033[1;37;42m####<No.{} step Succeed!>####\033[0m\n'.format(i + 1))
    ##########################################>-|->analysis module


def seismic(tag, dt, npt, pga):

    folder = 'data/output/seismic'
    if not os.path.exists(folder):
        os.mkdir(folder)

    sub_folder = f'data/output/seismic/{tag}'
    if not os.path.exists(folder):
        os.mkdir(folder)

    print(tag)
    
    wipeAnalysis()
    setTime(0.0)

    damp = 0.05
    mpropswitch = 1.0
    kcurrswitch = 0.0
    kcommswitch = 1.0
    kinitswitch = 0.0
    i = 1
    j = 2
    lambdan = eigen(j)
    lambdai = lambdan[i - 1]
    lambdaj = lambdan[j - 1]
    omegai = np.sqrt(lambdai)
    omegaj = np.sqrt(lambdaj)
    alpham = mpropswitch * damp * (2 * omegai * omegaj) / (omegai + omegaj)
    betakcurr = kcurrswitch * 2. * damp / (omegai + omegaj)
    betakcomm = kcommswitch * 2. * damp / (omegai + omegaj)
    betakinit = kinitswitch * 2. * damp / (omegai + omegaj)
    rayleigh(alpham, betakcurr, betakcomm, betakinit)

    factor = 980
    filepath = f'data/input/ground_motion/{tag}.txt'
    timeSeries('Path', 2, '-dt', dt, '-filePath', filepath, '-factor', factor, '-prependZero')
    pattern('UniformExcitation', 2, 1, '-accel', 2)
    
    # rcl = pd.read_excel('data/input/model_infor/7_recorder.xlsx')
    # for tag, item in zip(rcl.iloc[:, 0], rcl.iloc[:, 1]):
    #     savepath = folder + f'/{item}_{tag}.out'
    #     recorder_define(savepath, item, tag)
    # recorder('Node', '-file', node_his, '-timeSeries', 2, '-dt', )
    # record()
    
    system("BandGeneral")
    constraints('Transformation')
    numberer('RCM')
    test('NormDispIncr', 1.0e-4, 100, 0)
    algorithm('KrylovNewton')
    integrator('Newmark', 0.5, 0.25)
    analysis('Transient')
    record()
    ok = analyze(npt, dt)
    if ok == 0:
        print(f'\033[1;37;42mFinish {tag} Analysis\033[0m\n')
    else:
        print(f'\033[1;37;41mFailed {tag} Analysis\033[0m\n')