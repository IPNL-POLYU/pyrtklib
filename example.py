from pyrtklib import *

if __name__ == "__main__":
    gnss_file_list = []
    gnss_file_list.append("data/20210714.2.whampoa.ublox.f9p.obs")
    gnss_file_list.append("data/hksc1950.21f")
    gnss_file_list.append("data/hksc1950.21n")
    gnss_file_list.append("data/hksc1950.21o")
    output_path = "pyexample_output.txt"

    trace_lv = 3
    stat_lv = 3

    prcopt = prcopt_default
    solopt = solopt_default
    filopt = filopt_t()
    ts = gtime_t()
    te = gtime_t()
    tint = 0.0
    es = [2000,1,1,0,0,0]
    ee = [2000,12,31,23,59,59]
    pos = [0,0,0]
    i = 0
    j = 0
    n = 0
    ret = 0
    rov = ""
    base = ""
    ts.time = 0
    te.time = 0

    n = len(gnss_file_list)
    for i in gnss_file_list:
        print(i)

    print(output_path)

    snrmask = snrmask_t()
    snrmask.ena[0] = 1
    snrmask.ena[1] = 1
    for i in range(NFREQ):
        for j in range(9):
            snrmask.mask[i,j] = 10.0

    prcopt.mode = PMODE_KINEMA
    prcopt.soltype = 2
    prcopt.nf = 3
    prcopt.navsys = SYS_ALL

    prcopt.sateph = EPHOPT_BRDC
    prcopt.modear = 3
    prcopt.glomodear = 1
    prcopt.bdsmodear = 1
    prcopt.ionoopt = IONOOPT_BRDC
    prcopt.tropopt = TROPOPT_SAAS

    prcopt.posopt[4] = 0
    prcopt.rb[0] = -2414266.9197
    prcopt.rb[1] = 5386768.9868
    prcopt.rb[2] = 2407460.0314

    solopt.posf = SOLF_LLH
    solopt.times = TIMES_GPST
    solopt.timef = 0
    solopt.timeu = 3
    solopt.degf = 0
    solopt.outhead = 1
    solopt.outopt = 1

    solopt.datum = 0
    solopt.height = 0
    solopt.geoid = 0

    solopt.sstat = stat_lv
    solopt.trace = trace_lv

    print('starting rtklib ...')
    ret = postpos(ts,te,tint,0.0,prcopt,solopt,filopt,gnss_file_list,n,output_path,rov,base)
    print("rtklib status: %d",ret)
