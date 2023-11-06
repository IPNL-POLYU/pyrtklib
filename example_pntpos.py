from pyrtklib import *
import pandas as pd
import numpy as np


def nextobsf(obs,i):
    n = 0
    while i+n < obs.n:
        tt = timediff(obs.data[i+n].time,obs.data[i].time)
        if tt > 0.05:
            break
        n+=1
    return n

def get_sat_cnt(obs,i,m,rcv):
    cnt = 0
    for k in range(i,i+m):
        if obs.data[k].rcv == rcv:
            cnt+=1
    return cnt

def get_sat_pos(obsd,n,nav):
    svh = Arr1Dint(MAXOBS)
    rs = Arr1Ddouble(6*n)
    dts = Arr1Ddouble(2*n)
    var = Arr1Ddouble(1*n)
    satposs(obsd[0].time,obsd.ptr,n,nav,0,rs,dts,var,svh)
    noeph = []
    for i in range(n):
        if rs[6*i] == 0:
            noeph.append(i)
    nrs = Arr1Ddouble(6*(n-len(noeph)))
    j = 0
    for i in range(6*n):
        if rs[i]!=0:
            nrs[j] = rs[i]
            j+=1
    return nrs,noeph

def split_obs(obs):
    i = 0
    m = nextobsf(obs,i)
    obss = []
    while m!=0:
        tmp_obs = obs_t()
        tmp_obs.data = obs.data[i:i+m]
        tmp_obs.n = m
        tmp_obs.nmax = m
        i+=m
        obss.append(tmp_obs)
        m = nextobsf(obs,i)
    return obss
    
def get_obs_pnt(obs,nav,prcopt):
    m = obs.n
    sol = sol_t()
    sat = Arr1Dssat_t(MAXSAT)
    sol.time = obs.data[0].time
    msg = Arr1Dchar(100)
    azel = Arr1Ddouble(m*2)
    pntpos(obs.data.ptr,obs.n,nav,prcopt,sol,azel,sat.ptr,msg)
    return sol,sat,azel,msg

traceopen('test.log')
tracelevel(4)



files = [
    '/home/hrz/project/rtk/v_rtk/data/KLB/F9P_211203_061807.obs',
    "/home/hrz/project/rtk/v_rtk/data/KLB/BRDC00IGS_R_20213370000_01D_MN.rnx"
]
obs = obs_t()
nav = nav_t()
sta = sta_t()
prcopt = prcopt_default
solopt = solopt_default
readrnx(files[0],1,"",obs,nav,sta)
for i in files[1:]:
    readrnx(i,1,"",obs,nav,sta)
sortobs(obs)
uniqnav(nav)


data = []
obss = split_obs(obs)
prcopt.mode = PMODE_KINEMA
prcopt.navsys = SYS_ALL
prcopt.soltype = 0
prcopt.elmin = 0#15.0*D2R
prcopt.tidecorr = 0
prcopt.posopt[4] = 0
prcopt.tropopt = TROPOPT_SBAS
prcopt.ionoopt = IONOOPT_BRDC
prcopt.sateph = EPHOPT_BRDC
prcopt.modear = 3 #fix and hold

index = 0
for o in obss:
    sol,sat,azel,msg = get_obs_pnt(o,nav,prcopt)
    if msg[0] == "no observation data":
        break
    ecef = Arr1Ddouble(3)
    ecef[0] = sol.rr[0]
    ecef[1] = sol.rr[1]
    ecef[2] = sol.rr[2]
    pos = Arr1Ddouble(3)
    ecef2pos(ecef,pos)
    print(sol.time.time,*(np.array(pos[:2])*R2D),pos[2])
print('done')