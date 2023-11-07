#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "rtksrc/rtklib.h"
#include "iostream"
#include "cbind.h"
namespace py = pybind11;
std::map<void*,void*> gmap;
extern int  satsys  (int sat,Arr1D<int> Sprn){
    int *prn = Sprn.src;
    auto tmp = satsys(sat, prn);
    return tmp;
}
extern void satno2id(int sat,Arr1D<char> Sid){
    char *id = Sid.src;
    satno2id(sat, id);

}
extern double dot (Arr1D<double> Sa,Arr1D<double> Sb, int n){
    const double *a = Sa.src;
    const double *b = Sb.src;
    auto tmp = dot(a, b, n);
    return tmp;
}
extern double norm(Arr1D<double> Sa, int n){
    const double *a = Sa.src;
    auto tmp = norm(a, n);
    return tmp;
}
extern void cross3(Arr1D<double> Sa,Arr1D<double> Sb,Arr1D<double> Sc){
    const double *a = Sa.src;
    const double *b = Sb.src;
    double *c = Sc.src;
    cross3(a, b, c);

}
extern int  normv3(Arr1D<double> Sa,Arr1D<double> Sb){
    const double *a = Sa.src;
    double *b = Sb.src;
    auto tmp = normv3(a, b);
    return tmp;
}
extern void matcpy(Arr1D<double> SA,Arr1D<double> SB, int n, int m){
    double *A = SA.src;
    const double *B = SB.src;
    matcpy(A, B, n, m);

}
extern void matmul(const char *tr, int n, int k, int m, double alpha,Arr1D<double> SA,Arr1D<double> SB, double beta,Arr1D<double> SC){
    const double *A = SA.src;
    const double *B = SB.src;
    double *C = SC.src;
    matmul(tr, n, k, m, alpha, A, B, beta, C);

}
extern int  matinv(Arr1D<double> SA, int n){
    double *A = SA.src;
    auto tmp = matinv(A, n);
    return tmp;
}
extern int  solve (const char *tr,Arr1D<double> SA,Arr1D<double> SY, int n, int m,Arr1D<double> SX){
    const double *A = SA.src;
    const double *Y = SY.src;
    double *X = SX.src;
    auto tmp = solve(tr, A, Y, n, m, X);
    return tmp;
}
extern int  lsq   (Arr1D<double> SA,Arr1D<double> Sy, int n, int m,Arr1D<double> Sx,Arr1D<double> SQ){
    const double *A = SA.src;
    const double *y = Sy.src;
    double *x = Sx.src;
    double *Q = SQ.src;
    auto tmp = lsq(A, y, n, m, x, Q);
    return tmp;
}
extern int  filter(Arr1D<double> Sx,Arr1D<double> SP,Arr1D<double> SH,Arr1D<double> Sv,Arr1D<double> SR, int n, int m){
    double *x = Sx.src;
    double *P = SP.src;
    const double *H = SH.src;
    const double *v = Sv.src;
    const double *R = SR.src;
    auto tmp = filter(x, P, H, v, R, n, m);
    return tmp;
}
extern int  smoother(Arr1D<double> Sxf,Arr1D<double> SQf,Arr1D<double> Sxb,Arr1D<double> SQb, int n,Arr1D<double> Sxs,Arr1D<double> SQs){
    const double *xf = Sxf.src;
    const double *Qf = SQf.src;
    const double *xb = Sxb.src;
    const double *Qb = SQb.src;
    double *xs = Sxs.src;
    double *Qs = SQs.src;
    auto tmp = smoother(xf, Qf, xb, Qb, n, xs, Qs);
    return tmp;
}
extern void matprint (Arr1D<double> SA, int n, int m, int p, int q){
    const double *A = SA.src;
    matprint(A, n, m, p, q);

}
extern void matfprint(Arr1D<double> SA, int n, int m, int p, int q, const char *Ffp, const char *mode){
    const double *A = SA.src;
	FILE *fp = fopen(Ffp,mode);
    matfprint(A, n, m, p, q, fp);
	fclose(fp);

}
extern void    time2str(gtime_t t,Arr1D<char> Sstr, int n){
    char *str = Sstr.src;
    time2str(t, str, n);

}
extern gtime_t epoch2time(Arr1D<double> Sep){
    const double *ep = Sep.src;
    auto tmp = epoch2time(ep);
    return tmp;
}
extern void    time2epoch(gtime_t t,Arr1D<double> Sep){
    double *ep = Sep.src;
    time2epoch(t, ep);

}
extern double  time2gpst(gtime_t t,Arr1D<int> Sweek){
    int *week = Sweek.src;
    auto tmp = time2gpst(t, week);
    return tmp;
}
extern double  time2gst(gtime_t t,Arr1D<int> Sweek){
    int *week = Sweek.src;
    auto tmp = time2gst(t, week);
    return tmp;
}
extern double  time2bdt(gtime_t t,Arr1D<int> Sweek){
    int *week = Sweek.src;
    auto tmp = time2bdt(t, week);
    return tmp;
}
extern int reppath(const char *path,Arr1D<char> Srpath, gtime_t time, const char *rov, const char *base){
    char *rpath = Srpath.src;
    auto tmp = reppath(path, rpath, time, rov, base);
    return tmp;
}
extern int reppaths(const char *path,std::vector<std::string> Drpaths, int nmax, gtime_t ts, gtime_t te, const char *rov, const char *base){
    char **rpaths = convertChar(Drpaths);
    auto tmp = reppaths(path, rpaths, nmax, ts, te, rov, base);
    free(rpaths);
    return tmp;
}
extern void ecef2pos(Arr1D<double> Sr,Arr1D<double> Spos){
    const double *r = Sr.src;
    double *pos = Spos.src;
    ecef2pos(r, pos);

}
extern void pos2ecef(Arr1D<double> Spos,Arr1D<double> Sr){
    const double *pos = Spos.src;
    double *r = Sr.src;
    pos2ecef(pos, r);

}
extern void ecef2enu(Arr1D<double> Spos,Arr1D<double> Sr,Arr1D<double> Se){
    const double *pos = Spos.src;
    const double *r = Sr.src;
    double *e = Se.src;
    ecef2enu(pos, r, e);

}
extern void enu2ecef(Arr1D<double> Spos,Arr1D<double> Se,Arr1D<double> Sr){
    const double *pos = Spos.src;
    const double *e = Se.src;
    double *r = Sr.src;
    enu2ecef(pos, e, r);

}
extern void covenu  (Arr1D<double> Spos,Arr1D<double> SP,Arr1D<double> SQ){
    const double *pos = Spos.src;
    const double *P = SP.src;
    double *Q = SQ.src;
    covenu(pos, P, Q);

}
extern void covecef (Arr1D<double> Spos,Arr1D<double> SQ,Arr1D<double> SP){
    const double *pos = Spos.src;
    const double *Q = SQ.src;
    double *P = SP.src;
    covecef(pos, Q, P);

}
extern void xyz2enu (Arr1D<double> Spos,Arr1D<double> SE){
    const double *pos = Spos.src;
    double *E = SE.src;
    xyz2enu(pos, E);

}
extern void eci2ecef(gtime_t tutc,Arr1D<double> Serpv,Arr1D<double> SU,Arr1D<double> Sgmst){
    const double *erpv = Serpv.src;
    double *U = SU.src;
    double *gmst = Sgmst.src;
    eci2ecef(tutc, erpv, U, gmst);

}
extern void deg2dms (double deg,Arr1D<double> Sdms, int ndec){
    double *dms = Sdms.src;
    deg2dms(deg, dms, ndec);

}
extern double dms2deg(Arr1D<double> Sdms){
    const double *dms = Sdms.src;
    auto tmp = dms2deg(dms);
    return tmp;
}
extern void readpos(const char *file, const char *rcv,Arr1D<double> Spos){
    double *pos = Spos.src;
    readpos(file, rcv, pos);

}
extern int  readblq(const char *file, const char *sta,Arr1D<double> Sodisp){
    double *odisp = Sodisp.src;
    auto tmp = readblq(file, sta, odisp);
    return tmp;
}
extern int  geterp (const erp_t *erp, gtime_t time,Arr1D<double> Sval){
    double *val = Sval.src;
    auto tmp = geterp(erp, time, val);
    return tmp;
}
extern void tracemat (int level,Arr1D<double> SA, int n, int m, int p, int q){
    const double *A = SA.src;
    tracemat(level, A, n, m, p, q);

}
extern void traceb   (int level,Arr1D<uint8_t> Sp, int n){
    const uint8_t *p = Sp.src;
    traceb(level, p, n);

}
extern int expath (const char *path,std::vector<std::string> Dpaths, int nmax){
    char **paths = convertChar(Dpaths);
    auto tmp = expath(path, paths, nmax);
    free(paths);
    return tmp;
}
extern double satazel(Arr1D<double> Spos,Arr1D<double> Se,Arr1D<double> Sazel){
    const double *pos = Spos.src;
    const double *e = Se.src;
    double *azel = Sazel.src;
    auto tmp = satazel(pos, e, azel);
    return tmp;
}
extern double geodist(Arr1D<double> Srs,Arr1D<double> Srr,Arr1D<double> Se){
    const double *rs = Srs.src;
    const double *rr = Srr.src;
    double *e = Se.src;
    auto tmp = geodist(rs, rr, e);
    return tmp;
}
extern void dops(int ns,Arr1D<double> Sazel, double elmin,Arr1D<double> Sdop){
    const double *azel = Sazel.src;
    double *dop = Sdop.src;
    dops(ns, azel, elmin, dop);

}
extern double ionmodel(gtime_t t,Arr1D<double> Sion,Arr1D<double> Spos,Arr1D<double> Sazel){
    const double *ion = Sion.src;
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    auto tmp = ionmodel(t, ion, pos, azel);
    return tmp;
}
extern double ionmapf(Arr1D<double> Spos,Arr1D<double> Sazel){
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    auto tmp = ionmapf(pos, azel);
    return tmp;
}
extern double ionppp(Arr1D<double> Spos,Arr1D<double> Sazel, double re, double hion,Arr1D<double> Spppos){
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    double *pppos = Spppos.src;
    auto tmp = ionppp(pos, azel, re, hion, pppos);
    return tmp;
}
extern double tropmodel(gtime_t time,Arr1D<double> Spos,Arr1D<double> Sazel, double humi){
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    auto tmp = tropmodel(time, pos, azel, humi);
    return tmp;
}
extern double tropmapf(gtime_t time,Arr1D<double> Spos,Arr1D<double> Sazel,Arr1D<double> Smapfw){
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    double *mapfw = Smapfw.src;
    auto tmp = tropmapf(time, pos, azel, mapfw);
    return tmp;
}
extern int iontec(gtime_t time, const nav_t *nav,Arr1D<double> Spos,Arr1D<double> Sazel, int opt,Arr1D<double> Sdelay,Arr1D<double> Svar){
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    double *delay = Sdelay.src;
    double *var = Svar.src;
    auto tmp = iontec(time, nav, pos, azel, opt, delay, var);
    return tmp;
}
extern int ionocorr(gtime_t time, const nav_t *nav, int sat,Arr1D<double> Spos,Arr1D<double> Sazel, int ionoopt,Arr1D<double> Sion,Arr1D<double> Svar){
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    double *ion = Sion.src;
    double *var = Svar.src;
    auto tmp = ionocorr(time, nav, sat, pos, azel, ionoopt, ion, var);
    return tmp;
}
extern int tropcorr(gtime_t time, const nav_t *nav,Arr1D<double> Spos,Arr1D<double> Sazel, int tropopt,Arr1D<double> Strp,Arr1D<double> Svar){
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    double *trp = Strp.src;
    double *var = Svar.src;
    auto tmp = tropcorr(time, nav, pos, azel, tropopt, trp, var);
    return tmp;
}
extern void antmodel(const pcv_t *pcv,Arr1D<double> Sdel,Arr1D<double> Sazel, int opt,Arr1D<double> Sdant){
    const double *del = Sdel.src;
    const double *azel = Sazel.src;
    double *dant = Sdant.src;
    antmodel(pcv, del, azel, opt, dant);

}
extern void antmodel_s(const pcv_t *pcv, double nadir,Arr1D<double> Sdant){
    double *dant = Sdant.src;
    antmodel_s(pcv, nadir, dant);

}
extern void sunmoonpos(gtime_t tutc,Arr1D<double> Serpv,Arr1D<double> Srsun,Arr1D<double> Srmoon,Arr1D<double> Sgmst){
    const double *erpv = Serpv.src;
    double *rsun = Srsun.src;
    double *rmoon = Srmoon.src;
    double *gmst = Sgmst.src;
    sunmoonpos(tutc, erpv, rsun, rmoon, gmst);

}
extern void tidedisp(gtime_t tutc,Arr1D<double> Srr, int opt, const erp_t *erp,Arr1D<double> Sodisp,Arr1D<double> Sdr){
    const double *rr = Srr.src;
    const double *odisp = Sodisp.src;
    double *dr = Sdr.src;
    tidedisp(tutc, rr, opt, erp, odisp, dr);

}
extern double geoidh(Arr1D<double> Spos){
    const double *pos = Spos.src;
    auto tmp = geoidh(pos);
    return tmp;
}
extern int tokyo2jgd(Arr1D<double> Spos){
    double *pos = Spos.src;
    auto tmp = tokyo2jgd(pos);
    return tmp;
}
extern int jgd2tokyo(Arr1D<double> Spos){
    double *pos = Spos.src;
    auto tmp = jgd2tokyo(pos);
    return tmp;
}
extern int outrnxobsh(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxobsh(fp, opt, nav);
	fclose(fp);
    return tmp;
}
extern int outrnxobsb(const char *Ffp, const char *mode, const rnxopt_t *opt, const obsd_t *obs, int n, int epflag){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxobsb(fp, opt, obs, n, epflag);
	fclose(fp);
    return tmp;
}
extern int outrnxnavh (const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxnavh(fp, opt, nav);
	fclose(fp);
    return tmp;
}
extern int outrnxgnavh(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxgnavh(fp, opt, nav);
	fclose(fp);
    return tmp;
}
extern int outrnxhnavh(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxhnavh(fp, opt, nav);
	fclose(fp);
    return tmp;
}
extern int outrnxlnavh(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxlnavh(fp, opt, nav);
	fclose(fp);
    return tmp;
}
extern int outrnxqnavh(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxqnavh(fp, opt, nav);
	fclose(fp);
    return tmp;
}
extern int outrnxcnavh(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxcnavh(fp, opt, nav);
	fclose(fp);
    return tmp;
}
extern int outrnxinavh(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxinavh(fp, opt, nav);
	fclose(fp);
    return tmp;
}
extern int outrnxnavb (const char *Ffp, const char *mode, const rnxopt_t *opt, const eph_t *eph){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxnavb(fp, opt, eph);
	fclose(fp);
    return tmp;
}
extern int outrnxgnavb(const char *Ffp, const char *mode, const rnxopt_t *opt, const geph_t *geph){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxgnavb(fp, opt, geph);
	fclose(fp);
    return tmp;
}
extern int outrnxhnavb(const char *Ffp, const char *mode, const rnxopt_t *opt, const seph_t *seph){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = outrnxhnavb(fp, opt, seph);
	fclose(fp);
    return tmp;
}
extern int rtk_uncompress(const char *file,Arr1D<char> Suncfile){
    char *uncfile = Suncfile.src;
    auto tmp = rtk_uncompress(file, uncfile);
    return tmp;
}
extern int convrnx(int format, rnxopt_t *opt, const char *file,std::vector<std::string> Dofile){
    char **ofile = convertChar(Dofile);
    auto tmp = convrnx(format, opt, file, ofile);
    free(ofile);
    return tmp;
}
extern int  open_rnxctr (rnxctr_t *rnx, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = open_rnxctr(rnx, fp);
	fclose(fp);
    return tmp;
}
extern int  input_rnxctr(rnxctr_t *rnx, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_rnxctr(rnx, fp);
	fclose(fp);
    return tmp;
}
extern void eph2pos (gtime_t time, const eph_t  *eph,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar){
    double *rs = Srs.src;
    double *dts = Sdts.src;
    double *var = Svar.src;
    eph2pos(time, eph, rs, dts, var);

}
extern void geph2pos(gtime_t time, const geph_t *geph,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar){
    double *rs = Srs.src;
    double *dts = Sdts.src;
    double *var = Svar.src;
    geph2pos(time, geph, rs, dts, var);

}
extern void seph2pos(gtime_t time, const seph_t *seph,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar){
    double *rs = Srs.src;
    double *dts = Sdts.src;
    double *var = Svar.src;
    seph2pos(time, seph, rs, dts, var);

}
extern int  peph2pos(gtime_t time, int sat, const nav_t *nav, int opt,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar){
    double *rs = Srs.src;
    double *dts = Sdts.src;
    double *var = Svar.src;
    auto tmp = peph2pos(time, sat, nav, opt, rs, dts, var);
    return tmp;
}
extern void satantoff(gtime_t time,Arr1D<double> Srs, int sat, const nav_t *nav,Arr1D<double> Sdant){
    const double *rs = Srs.src;
    double *dant = Sdant.src;
    satantoff(time, rs, sat, nav, dant);

}
extern int  satpos(gtime_t time, gtime_t teph, int sat, int ephopt, const nav_t *nav,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar,Arr1D<int> Ssvh){
    double *rs = Srs.src;
    double *dts = Sdts.src;
    double *var = Svar.src;
    int *svh = Ssvh.src;
    auto tmp = satpos(time, teph, sat, ephopt, nav, rs, dts, var, svh);
    return tmp;
}
extern void satposs(gtime_t time, const obsd_t *obs, int n, const nav_t *nav, int sateph,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar,Arr1D<int> Ssvh){
    double *rs = Srs.src;
    double *dts = Sdts.src;
    double *var = Svar.src;
    int *svh = Ssvh.src;
    satposs(time, obs, n, nav, sateph, rs, dts, var, svh);

}
extern void alm2pos(gtime_t time, const alm_t *alm,Arr1D<double> Srs,Arr1D<double> Sdts){
    double *rs = Srs.src;
    double *dts = Sdts.src;
    alm2pos(time, alm, rs, dts);

}
extern int tle_pos(gtime_t time, const char *name, const char *satno, const char *desig, const tle_t *tle, const erp_t *erp,Arr1D<double> Srs){
    double *rs = Srs.src;
    auto tmp = tle_pos(time, name, satno, desig, tle, erp, rs);
    return tmp;
}
extern uint32_t getbitu(Arr1D<uint8_t> Sbuff, int pos, int len){
    const uint8_t *buff = Sbuff.src;
    auto tmp = getbitu(buff, pos, len);
    return tmp;
}
extern int32_t  getbits(Arr1D<uint8_t> Sbuff, int pos, int len){
    const uint8_t *buff = Sbuff.src;
    auto tmp = getbits(buff, pos, len);
    return tmp;
}
extern void setbitu(Arr1D<uint8_t> Sbuff, int pos, int len, uint32_t data){
    uint8_t *buff = Sbuff.src;
    setbitu(buff, pos, len, data);

}
extern void setbits(Arr1D<uint8_t> Sbuff, int pos, int len, int32_t  data){
    uint8_t *buff = Sbuff.src;
    setbits(buff, pos, len, data);

}
extern uint32_t rtk_crc32 (Arr1D<uint8_t> Sbuff, int len){
    const uint8_t *buff = Sbuff.src;
    auto tmp = rtk_crc32(buff, len);
    return tmp;
}
extern uint32_t rtk_crc24q(Arr1D<uint8_t> Sbuff, int len){
    const uint8_t *buff = Sbuff.src;
    auto tmp = rtk_crc24q(buff, len);
    return tmp;
}
extern uint16_t rtk_crc16 (Arr1D<uint8_t> Sbuff, int len){
    const uint8_t *buff = Sbuff.src;
    auto tmp = rtk_crc16(buff, len);
    return tmp;
}
extern int decode_word (uint32_t word,Arr1D<uint8_t> Sdata){
    uint8_t *data = Sdata.src;
    auto tmp = decode_word(word, data);
    return tmp;
}
extern int decode_frame(Arr1D<uint8_t> Sbuff, eph_t *eph, alm_t *alm,Arr1D<double> Sion,Arr1D<double> Sutc){
    const uint8_t *buff = Sbuff.src;
    double *ion = Sion.src;
    double *utc = Sutc.src;
    auto tmp = decode_frame(buff, eph, alm, ion, utc);
    return tmp;
}
extern int test_glostr(Arr1D<uint8_t> Sbuff){
    const uint8_t *buff = Sbuff.src;
    auto tmp = test_glostr(buff);
    return tmp;
}
extern int decode_glostr(Arr1D<uint8_t> Sbuff, geph_t *geph,Arr1D<double> Sutc){
    const uint8_t *buff = Sbuff.src;
    double *utc = Sutc.src;
    auto tmp = decode_glostr(buff, geph, utc);
    return tmp;
}
extern int decode_bds_d1(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sion,Arr1D<double> Sutc){
    const uint8_t *buff = Sbuff.src;
    double *ion = Sion.src;
    double *utc = Sutc.src;
    auto tmp = decode_bds_d1(buff, eph, ion, utc);
    return tmp;
}
extern int decode_bds_d2(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sutc){
    const uint8_t *buff = Sbuff.src;
    double *utc = Sutc.src;
    auto tmp = decode_bds_d2(buff, eph, utc);
    return tmp;
}
extern int decode_gal_inav(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sion,Arr1D<double> Sutc){
    const uint8_t *buff = Sbuff.src;
    double *ion = Sion.src;
    double *utc = Sutc.src;
    auto tmp = decode_gal_inav(buff, eph, ion, utc);
    return tmp;
}
extern int decode_gal_fnav(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sion,Arr1D<double> Sutc){
    const uint8_t *buff = Sbuff.src;
    double *ion = Sion.src;
    double *utc = Sutc.src;
    auto tmp = decode_gal_fnav(buff, eph, ion, utc);
    return tmp;
}
extern int decode_irn_nav(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sion,Arr1D<double> Sutc){
    const uint8_t *buff = Sbuff.src;
    double *ion = Sion.src;
    double *utc = Sutc.src;
    auto tmp = decode_irn_nav(buff, eph, ion, utc);
    return tmp;
}
extern int input_rawf (raw_t *raw, int format, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_rawf(raw, format, fp);
	fclose(fp);
    return tmp;
}
extern int input_oem4f (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_oem4f(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_oem3f (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_oem3f(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_ubxf  (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_ubxf(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_ss2f  (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_ss2f(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_cresf (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_cresf(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_stqf  (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_stqf(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_javadf(raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_javadf(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_nvsf  (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_nvsf(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_bnxf  (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_bnxf(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_rt17f (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_rt17f(raw, fp);
	fclose(fp);
    return tmp;
}
extern int input_sbff  (raw_t *raw, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_sbff(raw, fp);
	fclose(fp);
    return tmp;
}
extern int gen_ubx (const char *msg,Arr1D<uint8_t> Sbuff){
    uint8_t *buff = Sbuff.src;
    auto tmp = gen_ubx(msg, buff);
    return tmp;
}
extern int gen_stq (const char *msg,Arr1D<uint8_t> Sbuff){
    uint8_t *buff = Sbuff.src;
    auto tmp = gen_stq(msg, buff);
    return tmp;
}
extern int gen_nvs (const char *msg,Arr1D<uint8_t> Sbuff){
    uint8_t *buff = Sbuff.src;
    auto tmp = gen_nvs(msg, buff);
    return tmp;
}
extern int input_rtcm2f(rtcm_t *rtcm, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_rtcm2f(rtcm, fp);
	fclose(fp);
    return tmp;
}
extern int input_rtcm3f(rtcm_t *rtcm, const char *Ffp, const char *mode){
	FILE *fp = fopen(Ffp,mode);
    auto tmp = input_rtcm3f(rtcm, fp);
	fclose(fp);
    return tmp;
}
extern int readsol (std::vector<std::string> Dfiles, int nfile, solbuf_t *sol){
    char **files = convertChar(Dfiles);
    auto tmp = readsol(files, nfile, sol);
    free(files);
    return tmp;
}
extern int readsolt(std::vector<std::string> Dfiles, int nfile, gtime_t ts, gtime_t te, double tint, int qflag, solbuf_t *sol){
    char **files = convertChar(Dfiles);
    auto tmp = readsolt(files, nfile, ts, te, tint, qflag, sol);
    free(files);
    return tmp;
}
extern int readsolstat(std::vector<std::string> Dfiles, int nfile, solstatbuf_t *statbuf){
    char **files = convertChar(Dfiles);
    auto tmp = readsolstat(files, nfile, statbuf);
    free(files);
    return tmp;
}
extern int readsolstatt(std::vector<std::string> Dfiles, int nfile, gtime_t ts, gtime_t te, double tint, solstatbuf_t *statbuf){
    char **files = convertChar(Dfiles);
    auto tmp = readsolstatt(files, nfile, ts, te, tint, statbuf);
    free(files);
    return tmp;
}
extern int outprcopts(Arr1D<uint8_t> Sbuff, const prcopt_t *opt){
    uint8_t *buff = Sbuff.src;
    auto tmp = outprcopts(buff, opt);
    return tmp;
}
extern int outsolheads(Arr1D<uint8_t> Sbuff, const solopt_t *opt){
    uint8_t *buff = Sbuff.src;
    auto tmp = outsolheads(buff, opt);
    return tmp;
}
extern int outsols  (Arr1D<uint8_t> Sbuff, const sol_t *sol,Arr1D<double> Srb, const solopt_t *opt){
    uint8_t *buff = Sbuff.src;
    const double *rb = Srb.src;
    auto tmp = outsols(buff, sol, rb, opt);
    return tmp;
}
extern int outsolexs(Arr1D<uint8_t> Sbuff, const sol_t *sol, const ssat_t *ssat, const solopt_t *opt){
    uint8_t *buff = Sbuff.src;
    auto tmp = outsolexs(buff, sol, ssat, opt);
    return tmp;
}
extern void outprcopt(const char *Ffp, const char *mode, const prcopt_t *opt){
	FILE *fp = fopen(Ffp,mode);
    outprcopt(fp, opt);
	fclose(fp);

}
extern void outsolhead(const char *Ffp, const char *mode, const solopt_t *opt){
	FILE *fp = fopen(Ffp,mode);
    outsolhead(fp, opt);
	fclose(fp);

}
extern void outsol  (const char *Ffp, const char *mode, const sol_t *sol,Arr1D<double> Srb, const solopt_t *opt){
    const double *rb = Srb.src;
	FILE *fp = fopen(Ffp,mode);
    outsol(fp, sol, rb, opt);
	fclose(fp);

}
extern void outsolex(const char *Ffp, const char *mode, const sol_t *sol, const ssat_t *ssat, const solopt_t *opt){
	FILE *fp = fopen(Ffp,mode);
    outsolex(fp, sol, ssat, opt);
	fclose(fp);

}
extern int outnmea_rmc(Arr1D<uint8_t> Sbuff, const sol_t *sol){
    uint8_t *buff = Sbuff.src;
    auto tmp = outnmea_rmc(buff, sol);
    return tmp;
}
extern int outnmea_gga(Arr1D<uint8_t> Sbuff, const sol_t *sol){
    uint8_t *buff = Sbuff.src;
    auto tmp = outnmea_gga(buff, sol);
    return tmp;
}
extern int outnmea_gsa(Arr1D<uint8_t> Sbuff, const sol_t *sol, const ssat_t *ssat){
    uint8_t *buff = Sbuff.src;
    auto tmp = outnmea_gsa(buff, sol, ssat);
    return tmp;
}
extern int outnmea_gsv(Arr1D<uint8_t> Sbuff, const sol_t *sol, const ssat_t *ssat){
    uint8_t *buff = Sbuff.src;
    auto tmp = outnmea_gsv(buff, sol, ssat);
    return tmp;
}
extern int convkml(const char *infile, const char *outfile, gtime_t ts, gtime_t te, double tint, int qflg,Arr1D<double> Soffset, int tcolor, int pcolor, int outalt, int outtime){
    double *offset = Soffset.src;
    auto tmp = convkml(infile, outfile, ts, te, tint, qflg, offset, tcolor, pcolor, outalt, outtime);
    return tmp;
}
extern int convgpx(const char *infile, const char *outfile, gtime_t ts, gtime_t te, double tint, int qflg,Arr1D<double> Soffset, int outtrk, int outpnt, int outalt, int outtime){
    double *offset = Soffset.src;
    auto tmp = convgpx(infile, outfile, ts, te, tint, qflg, offset, outtrk, outpnt, outalt, outtime);
    return tmp;
}
extern void sbsoutmsg(const char *Ffp, const char *mode, sbsmsg_t *sbsmsg){
	FILE *fp = fopen(Ffp,mode);
    sbsoutmsg(fp, sbsmsg);
	fclose(fp);

}
extern int  sbsdecodemsg(gtime_t time, int prn,Arr1D<uint32_t> Swords, sbsmsg_t *sbsmsg){
    const uint32_t *words = Swords.src;
    auto tmp = sbsdecodemsg(time, prn, words, sbsmsg);
    return tmp;
}
extern int sbssatcorr(gtime_t time, int sat, const nav_t *nav,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar){
    double *rs = Srs.src;
    double *dts = Sdts.src;
    double *var = Svar.src;
    auto tmp = sbssatcorr(time, sat, nav, rs, dts, var);
    return tmp;
}
extern int sbsioncorr(gtime_t time, const nav_t *nav,Arr1D<double> Spos,Arr1D<double> Sazel,Arr1D<double> Sdelay,Arr1D<double> Svar){
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    double *delay = Sdelay.src;
    double *var = Svar.src;
    auto tmp = sbsioncorr(time, nav, pos, azel, delay, var);
    return tmp;
}
extern double sbstropcorr(gtime_t time,Arr1D<double> Spos,Arr1D<double> Sazel,Arr1D<double> Svar){
    const double *pos = Spos.src;
    const double *azel = Sazel.src;
    double *var = Svar.src;
    auto tmp = sbstropcorr(time, pos, azel, var);
    return tmp;
}
extern int opt2str(const opt_t *opt,Arr1D<char> Sstr){
    char *str = Sstr.src;
    auto tmp = opt2str(opt, str);
    return tmp;
}
extern int opt2buf(const opt_t *opt,Arr1D<char> Sbuff){
    char *buff = Sbuff.src;
    auto tmp = opt2buf(opt, buff);
    return tmp;
}
extern int  strread  (stream_t *stream,Arr1D<uint8_t> Sbuff, int n){
    uint8_t *buff = Sbuff.src;
    auto tmp = strread(stream, buff, n);
    return tmp;
}
extern int  strwrite (stream_t *stream,Arr1D<uint8_t> Sbuff, int n){
    uint8_t *buff = Sbuff.src;
    auto tmp = strwrite(stream, buff, n);
    return tmp;
}
extern int  strstat  (stream_t *stream,Arr1D<char> Smsg){
    char *msg = Smsg.src;
    auto tmp = strstat(stream, msg);
    return tmp;
}
extern int  strstatx (stream_t *stream,Arr1D<char> Smsg){
    char *msg = Smsg.src;
    auto tmp = strstatx(stream, msg);
    return tmp;
}
extern void strsum   (stream_t *stream,Arr1D<int> Sinb,Arr1D<int> Sinr,Arr1D<int> Soutb,Arr1D<int> Soutr){
    int *inb = Sinb.src;
    int *inr = Sinr.src;
    int *outb = Soutb.src;
    int *outr = Soutr.src;
    strsum(stream, inb, inr, outb, outr);

}
extern void strsetopt(Arr1D<int> Sopt){
    const int *opt = Sopt.src;
    strsetopt(opt);

}
extern int lambda(int n, int m,Arr1D<double> Sa,Arr1D<double> SQ,Arr1D<double> SF,Arr1D<double> Ss){
    const double *a = Sa.src;
    const double *Q = SQ.src;
    double *F = SF.src;
    double *s = Ss.src;
    auto tmp = lambda(n, m, a, Q, F, s);
    return tmp;
}
extern int lambda_reduction(int n,Arr1D<double> SQ,Arr1D<double> SZ){
    const double *Q = SQ.src;
    double *Z = SZ.src;
    auto tmp = lambda_reduction(n, Q, Z);
    return tmp;
}
extern int lambda_search(int n, int m,Arr1D<double> Sa,Arr1D<double> SQ,Arr1D<double> SF,Arr1D<double> Ss){
    const double *a = Sa.src;
    const double *Q = SQ.src;
    double *F = SF.src;
    double *s = Ss.src;
    auto tmp = lambda_search(n, m, a, Q, F, s);
    return tmp;
}
extern int pntpos(const obsd_t *obs, int n, const nav_t *nav, const prcopt_t *opt, sol_t *sol,Arr1D<double> Sazel, ssat_t *ssat,Arr1D<char> Smsg){
    double *azel = Sazel.src;
    char *msg = Smsg.src;
    auto tmp = pntpos(obs, n, nav, opt, sol, azel, ssat, msg);
    return tmp;
}
extern int  rtkoutstat(rtk_t *rtk,Arr1D<char> Sbuff){
    char *buff = Sbuff.src;
    auto tmp = rtkoutstat(rtk, buff);
    return tmp;
}
extern int pppoutstat(rtk_t *rtk,Arr1D<char> Sbuff){
    char *buff = Sbuff.src;
    auto tmp = pppoutstat(rtk, buff);
    return tmp;
}
extern int ppp_ar(rtk_t *rtk, const obsd_t *obs, int n,Arr1D<int> Sexc, const nav_t *nav,Arr1D<double> Sazel,Arr1D<double> Sx,Arr1D<double> SP){
    int *exc = Sexc.src;
    const double *azel = Sazel.src;
    double *x = Sx.src;
    double *P = SP.src;
    auto tmp = ppp_ar(rtk, obs, n, exc, nav, azel, x, P);
    return tmp;
}
extern int postpos(gtime_t ts, gtime_t te, double ti, double tu, const prcopt_t *popt, const solopt_t *sopt, const filopt_t *fopt,std::vector<std::string> Dinfile, int n,Arr1D<char> Soutfile, const char *rov, const char *base){
    char **infile = convertChar(Dinfile);
    char *outfile = Soutfile.src;
    auto tmp = postpos(ts, te, ti, tu, popt, sopt, fopt, infile, n, outfile, rov, base);
    free(infile);
    return tmp;
}
extern int  strsvrstart(strsvr_t *svr,Arr1D<int> Sopts,Arr1D<int> Sstrs,std::vector<std::string> Dpaths,std::vector<std::string> Dlogs,std::vector<std::vector<strconv_t>> Dconv,std::vector<std::string> Dcmds,std::vector<std::string> Dcmds_priodic,Arr1D<double> Snmeapos){
    char **paths = convertChar(Dpaths);
    char **logs = convertChar(Dlogs);
    strconv_t **conv = convertType(Dconv);
    char **cmds = convertChar(Dcmds);
    char **cmds_priodic = convertChar(Dcmds_priodic);
    int *opts = Sopts.src;
    int *strs = Sstrs.src;
    const double *nmeapos = Snmeapos.src;
    auto tmp = strsvrstart(svr, opts, strs, paths, logs, conv, cmds, cmds_priodic, nmeapos);
    free(paths);
    free(logs);
    free(conv);
    free(cmds);
    free(cmds_priodic);
    return tmp;
}
extern void strsvrstop (strsvr_t *svr,std::vector<std::string> Dcmds){
    char **cmds = convertChar(Dcmds);
    strsvrstop(svr, cmds);
    free(cmds);

}
extern void strsvrstat (strsvr_t *svr,Arr1D<int> Sstat,Arr1D<int> Slog_stat,Arr1D<int> Sbyte,Arr1D<int> Sbps,Arr1D<char> Smsg){
    int *stat = Sstat.src;
    int *log_stat = Slog_stat.src;
    int *byte = Sbyte.src;
    int *bps = Sbps.src;
    char *msg = Smsg.src;
    strsvrstat(svr, stat, log_stat, byte, bps, msg);

}
extern int  rtksvrstart (rtksvr_t *svr, int cycle, int buffsize,Arr1D<int> Sstrs,std::vector<std::string> Dpaths,Arr1D<int> Sformats, int navsel,std::vector<std::string> Dcmds,std::vector<std::string> Dcmds_periodic,std::vector<std::string> Drcvopts, int nmeacycle, int nmeareq,Arr1D<double> Snmeapos, prcopt_t *prcopt, solopt_t *solopt, stream_t *moni,Arr1D<char> Serrmsg){
    char **paths = convertChar(Dpaths);
    char **cmds = convertChar(Dcmds);
    char **cmds_periodic = convertChar(Dcmds_periodic);
    char **rcvopts = convertChar(Drcvopts);
    int *strs = Sstrs.src;
    int *formats = Sformats.src;
    const double *nmeapos = Snmeapos.src;
    char *errmsg = Serrmsg.src;
    auto tmp = rtksvrstart(svr, cycle, buffsize, strs, paths, formats, navsel, cmds, cmds_periodic, rcvopts, nmeacycle, nmeareq, nmeapos, prcopt, solopt, moni, errmsg);
    free(paths);
    free(cmds);
    free(cmds_periodic);
    free(rcvopts);
    return tmp;
}
extern void rtksvrstop  (rtksvr_t *svr,std::vector<std::string> Dcmds){
    char **cmds = convertChar(Dcmds);
    rtksvrstop(svr, cmds);
    free(cmds);

}
extern int  rtksvrostat (rtksvr_t *svr, int type, gtime_t *time,Arr1D<int> Ssat,Arr1D<double> Saz,Arr1D<double> Sel,std::vector<std::vector<int>> Dsnr,Arr1D<int> Svsat){
    int **snr = convertType(Dsnr);
    int *sat = Ssat.src;
    double *az = Saz.src;
    double *el = Sel.src;
    int *vsat = Svsat.src;
    auto tmp = rtksvrostat(svr, type, time, sat, az, el, snr, vsat);
    free(snr);
    return tmp;
}
extern void rtksvrsstat (rtksvr_t *svr,Arr1D<int> Ssstat,Arr1D<char> Smsg){
    int *sstat = Ssstat.src;
    char *msg = Smsg.src;
    rtksvrsstat(svr, sstat, msg);

}
extern int dl_readurls(const char *file,std::vector<std::string> Dtypes, int ntype, url_t *urls, int nmax){
    char **types = convertChar(Dtypes);
    auto tmp = dl_readurls(file, types, ntype, urls, nmax);
    free(types);
    return tmp;
}
extern int dl_readstas(const char *file,std::vector<std::string> Dstas, int nmax){
    char **stas = convertChar(Dstas);
    auto tmp = dl_readstas(file, stas, nmax);
    free(stas);
    return tmp;
}
extern int dl_exec(gtime_t ts, gtime_t te, double ti, int seqnos, int seqnoe, const url_t *urls, int nurl,std::vector<std::string> Dstas, int nsta, const char *dir, const char *usr, const char *pwd, const char *proxy, int opts,Arr1D<char> Smsg, const char *Ffp, const char *mode){
    char **stas = convertChar(Dstas);
    char *msg = Smsg.src;
	FILE *fp = fopen(Ffp,mode);
    auto tmp = dl_exec(ts, te, ti, seqnos, seqnoe, urls, nurl, stas, nsta, dir, usr, pwd, proxy, opts, msg, fp);
    free(stas);
	fclose(fp);
    return tmp;
}
extern void dl_test(gtime_t ts, gtime_t te, double ti, const url_t *urls, int nurl,std::vector<std::string> Dstas, int nsta, const char *dir, int ncol, int datefmt, const char *Ffp, const char *mode){
    char **stas = convertChar(Dstas);
	FILE *fp = fopen(Ffp,mode);
    dl_test(ts, te, ti, urls, nurl, stas, nsta, dir, ncol, datefmt, fp);
    free(stas);
	fclose(fp);

}
PYBIND11_MODULE(pyrtklib, m) {
    m.doc() = "rtklib python interface by pybind11";
	m.attr("NULL") = __null;
    m.attr("PI")=3.1415926535897932;
    m.attr("D2R")=(PI/180.0);
    m.attr("R2D")=(180.0/PI);
    m.attr("CLIGHT")=299792458.0;
    m.attr("SC2RAD")=3.1415926535898;
    m.attr("AU")=149597870691.0;
    m.attr("AS2R")=(D2R/3600.0);
    m.attr("OMGE")=7.2921151467E-5;
    m.attr("RE_WGS84")=6378137.0;
    m.attr("FE_WGS84")=(1.0/298.257223563);
    m.attr("HION")=350000.0;
    m.attr("MAXFREQ")=7;
    m.attr("FREQ1")=1.57542E9;
    m.attr("FREQ2")=1.22760E9;
    m.attr("FREQ5")=1.17645E9;
    m.attr("FREQ6")=1.27875E9;
    m.attr("FREQ7")=1.20714E9;
    m.attr("FREQ8")=1.191795E9;
    m.attr("FREQ9")=2.492028E9;
    m.attr("FREQ1_GLO")=1.60200E9;
    m.attr("DFRQ1_GLO")=0.56250E6;
    m.attr("FREQ2_GLO")=1.24600E9;
    m.attr("DFRQ2_GLO")=0.43750E6;
    m.attr("FREQ3_GLO")=1.202025E9;
    m.attr("FREQ1a_GLO")=1.600995E9;
    m.attr("FREQ2a_GLO")=1.248060E9;
    m.attr("FREQ1_CMP")=1.561098E9;
    m.attr("FREQ2_CMP")=1.20714E9;
    m.attr("FREQ3_CMP")=1.26852E9;
    m.attr("EFACT_GPS")=1.0;
    m.attr("EFACT_GLO")=1.5;
    m.attr("EFACT_GAL")=1.0;
    m.attr("EFACT_QZS")=1.0;
    m.attr("EFACT_CMP")=1.0;
    m.attr("EFACT_IRN")=1.5;
    m.attr("EFACT_SBS")=3.0;
    m.attr("SYS_NONE")=0x00;
    m.attr("SYS_GPS")=0x01;
    m.attr("SYS_SBS")=0x02;
    m.attr("SYS_GLO")=0x04;
    m.attr("SYS_GAL")=0x08;
    m.attr("SYS_QZS")=0x10;
    m.attr("SYS_CMP")=0x20;
    m.attr("SYS_IRN")=0x40;
    m.attr("SYS_LEO")=0x80;
    m.attr("SYS_ALL")=0xFF;
    m.attr("TSYS_GPS")=0;
    m.attr("TSYS_UTC")=1;
    m.attr("TSYS_GLO")=2;
    m.attr("TSYS_GAL")=3;
    m.attr("TSYS_QZS")=4;
    m.attr("TSYS_CMP")=5;
    m.attr("TSYS_IRN")=6;
    m.attr("NFREQ")=3;
    m.attr("NFREQGLO")=2;
    m.attr("NEXOBS")=0;
    m.attr("SNR_UNIT")=0.001;
    m.attr("MINPRNGPS")=1;
    m.attr("MAXPRNGPS")=32;
    m.attr("NSATGPS")=(MAXPRNGPS-MINPRNGPS+1);
    m.attr("NSYSGPS")=1;
    m.attr("MINPRNGLO")=1;
    m.attr("MAXPRNGLO")=27;
    m.attr("NSATGLO")=(MAXPRNGLO-MINPRNGLO+1);
    m.attr("NSYSGLO")=1;
    m.attr("MINPRNGAL")=1;
    m.attr("MAXPRNGAL")=36;
    m.attr("NSATGAL")=(MAXPRNGAL-MINPRNGAL+1);
    m.attr("NSYSGAL")=1;
    m.attr("MINPRNQZS")=0;
    m.attr("MAXPRNQZS")=0;
    m.attr("MINPRNQZS_S")=0;
    m.attr("MAXPRNQZS_S")=0;
    m.attr("NSATQZS")=0;
    m.attr("NSYSQZS")=0;
    m.attr("MINPRNCMP")=1;
    m.attr("MAXPRNCMP")=63;
    m.attr("NSATCMP")=(MAXPRNCMP-MINPRNCMP+1);
    m.attr("NSYSCMP")=1;
    m.attr("MINPRNIRN")=0;
    m.attr("MAXPRNIRN")=0;
    m.attr("NSATIRN")=0;
    m.attr("NSYSIRN")=0;
    m.attr("MINPRNLEO")=0;
    m.attr("MAXPRNLEO")=0;
    m.attr("NSATLEO")=0;
    m.attr("NSYSLEO")=0;
    m.attr("NSYS")=(NSYSGPS+NSYSGLO+NSYSGAL+NSYSQZS+NSYSCMP+NSYSIRN+NSYSLEO);
    m.attr("MINPRNSBS")=120;
    m.attr("MAXPRNSBS")=158;
    m.attr("NSATSBS")=(MAXPRNSBS-MINPRNSBS+1);
    m.attr("MAXSAT")=(NSATGPS+NSATGLO+NSATGAL+NSATQZS+NSATCMP+NSATIRN+NSATSBS+NSATLEO);
    m.attr("MAXSTA")=255;
    m.attr("MAXOBS")=96;
    m.attr("MAXRCV")=64;
    m.attr("MAXOBSTYPE")=64;
    m.attr("DTTOL")=0.025;
    m.attr("MAXDTOE")=7200.0;
    m.attr("MAXDTOE_QZS")=7200.0;
    m.attr("MAXDTOE_GAL")=14400.0;
    m.attr("MAXDTOE_CMP")=21600.0;
    m.attr("MAXDTOE_GLO")=1800.0;
    m.attr("MAXDTOE_IRN")=7200.0;
    m.attr("MAXDTOE_SBS")=360.0;
    m.attr("MAXDTOE_S")=86400.0;
    m.attr("MAXGDOP")=300.0;
    m.attr("INT_SWAP_TRAC")=86400.0;
    m.attr("INT_SWAP_STAT")=86400.0;
    m.attr("MAXEXFILE")=1024;
    m.attr("MAXSBSAGEF")=30.0;
    m.attr("MAXSBSAGEL")=1800.0;
    m.attr("MAXSBSURA")=8;
    m.attr("MAXBAND")=10;
    m.attr("MAXNIGP")=201;
    m.attr("MAXNGEO")=4;
    m.attr("MAXCOMMENT")=100;
    m.attr("MAXSTRPATH")=1024;
    m.attr("MAXSTRMSG")=1024;
    m.attr("MAXSTRRTK")=8;
    m.attr("MAXSBSMSG")=32;
    m.attr("MAXSOLMSG")=8191;
    m.attr("MAXRAWLEN")=16384;
    m.attr("MAXERRMSG")=4096;
    m.attr("MAXANT")=64;
    m.attr("MAXSOLBUF")=256;
    m.attr("MAXOBSBUF")=128;
    m.attr("MAXNRPOS")=16;
    m.attr("MAXLEAPS")=64;
    m.attr("MAXGISLAYER")=32;
    m.attr("MAXRCVCMD")=4096;
    m.attr("RNX2VER")=2.10;
    m.attr("RNX3VER")=3.00;
    m.attr("OBSTYPE_PR")=0x01;
    m.attr("OBSTYPE_CP")=0x02;
    m.attr("OBSTYPE_DOP")=0x04;
    m.attr("OBSTYPE_SNR")=0x08;
    m.attr("OBSTYPE_ALL")=0xFF;
    m.attr("FREQTYPE_L1")=0x01;
    m.attr("FREQTYPE_L2")=0x02;
    m.attr("FREQTYPE_L3")=0x04;
    m.attr("FREQTYPE_L4")=0x08;
    m.attr("FREQTYPE_L5")=0x10;
    m.attr("FREQTYPE_ALL")=0xFF;
    m.attr("CODE_NONE")=0;
    m.attr("CODE_L1C")=1;
    m.attr("CODE_L1P")=2;
    m.attr("CODE_L1W")=3;
    m.attr("CODE_L1Y")=4;
    m.attr("CODE_L1M")=5;
    m.attr("CODE_L1N")=6;
    m.attr("CODE_L1S")=7;
    m.attr("CODE_L1L")=8;
    m.attr("CODE_L1E")=9;
    m.attr("CODE_L1A")=10;
    m.attr("CODE_L1B")=11;
    m.attr("CODE_L1X")=12;
    m.attr("CODE_L1Z")=13;
    m.attr("CODE_L2C")=14;
    m.attr("CODE_L2D")=15;
    m.attr("CODE_L2S")=16;
    m.attr("CODE_L2L")=17;
    m.attr("CODE_L2X")=18;
    m.attr("CODE_L2P")=19;
    m.attr("CODE_L2W")=20;
    m.attr("CODE_L2Y")=21;
    m.attr("CODE_L2M")=22;
    m.attr("CODE_L2N")=23;
    m.attr("CODE_L5I")=24;
    m.attr("CODE_L5Q")=25;
    m.attr("CODE_L5X")=26;
    m.attr("CODE_L7I")=27;
    m.attr("CODE_L7Q")=28;
    m.attr("CODE_L7X")=29;
    m.attr("CODE_L6A")=30;
    m.attr("CODE_L6B")=31;
    m.attr("CODE_L6C")=32;
    m.attr("CODE_L6X")=33;
    m.attr("CODE_L6Z")=34;
    m.attr("CODE_L6S")=35;
    m.attr("CODE_L6L")=36;
    m.attr("CODE_L8I")=37;
    m.attr("CODE_L8Q")=38;
    m.attr("CODE_L8X")=39;
    m.attr("CODE_L2I")=40;
    m.attr("CODE_L2Q")=41;
    m.attr("CODE_L6I")=42;
    m.attr("CODE_L6Q")=43;
    m.attr("CODE_L3I")=44;
    m.attr("CODE_L3Q")=45;
    m.attr("CODE_L3X")=46;
    m.attr("CODE_L1I")=47;
    m.attr("CODE_L1Q")=48;
    m.attr("CODE_L5A")=49;
    m.attr("CODE_L5B")=50;
    m.attr("CODE_L5C")=51;
    m.attr("CODE_L9A")=52;
    m.attr("CODE_L9B")=53;
    m.attr("CODE_L9C")=54;
    m.attr("CODE_L9X")=55;
    m.attr("CODE_L1D")=56;
    m.attr("CODE_L5D")=57;
    m.attr("CODE_L5P")=58;
    m.attr("CODE_L5Z")=59;
    m.attr("CODE_L6E")=60;
    m.attr("CODE_L7D")=61;
    m.attr("CODE_L7P")=62;
    m.attr("CODE_L7Z")=63;
    m.attr("CODE_L8D")=64;
    m.attr("CODE_L8P")=65;
    m.attr("CODE_L4A")=66;
    m.attr("CODE_L4B")=67;
    m.attr("CODE_L4X")=68;
    m.attr("MAXCODE")=68;
    m.attr("PMODE_SINGLE")=0;
    m.attr("PMODE_DGPS")=1;
    m.attr("PMODE_KINEMA")=2;
    m.attr("PMODE_STATIC")=3;
    m.attr("PMODE_MOVEB")=4;
    m.attr("PMODE_FIXED")=5;
    m.attr("PMODE_PPP_KINEMA")=6;
    m.attr("PMODE_PPP_STATIC")=7;
    m.attr("PMODE_PPP_FIXED")=8;
    m.attr("SOLF_LLH")=0;
    m.attr("SOLF_XYZ")=1;
    m.attr("SOLF_ENU")=2;
    m.attr("SOLF_NMEA")=3;
    m.attr("SOLF_STAT")=4;
    m.attr("SOLF_GSIF")=5;
    m.attr("SOLQ_NONE")=0;
    m.attr("SOLQ_FIX")=1;
    m.attr("SOLQ_FLOAT")=2;
    m.attr("SOLQ_SBAS")=3;
    m.attr("SOLQ_DGPS")=4;
    m.attr("SOLQ_SINGLE")=5;
    m.attr("SOLQ_PPP")=6;
    m.attr("SOLQ_DR")=7;
    m.attr("MAXSOLQ")=7;
    m.attr("TIMES_GPST")=0;
    m.attr("TIMES_UTC")=1;
    m.attr("TIMES_JST")=2;
    m.attr("IONOOPT_OFF")=0;
    m.attr("IONOOPT_BRDC")=1;
    m.attr("IONOOPT_SBAS")=2;
    m.attr("IONOOPT_IFLC")=3;
    m.attr("IONOOPT_EST")=4;
    m.attr("IONOOPT_TEC")=5;
    m.attr("IONOOPT_QZS")=6;
    m.attr("IONOOPT_STEC")=8;
    m.attr("TROPOPT_OFF")=0;
    m.attr("TROPOPT_SAAS")=1;
    m.attr("TROPOPT_SBAS")=2;
    m.attr("TROPOPT_EST")=3;
    m.attr("TROPOPT_ESTG")=4;
    m.attr("TROPOPT_ZTD")=5;
    m.attr("EPHOPT_BRDC")=0;
    m.attr("EPHOPT_PREC")=1;
    m.attr("EPHOPT_SBAS")=2;
    m.attr("EPHOPT_SSRAPC")=3;
    m.attr("EPHOPT_SSRCOM")=4;
    m.attr("ARMODE_OFF")=0;
    m.attr("ARMODE_CONT")=1;
    m.attr("ARMODE_INST")=2;
    m.attr("ARMODE_FIXHOLD")=3;
    m.attr("ARMODE_WLNL")=4;
    m.attr("ARMODE_TCAR")=5;
    m.attr("SBSOPT_LCORR")=1;
    m.attr("SBSOPT_FCORR")=2;
    m.attr("SBSOPT_ICORR")=4;
    m.attr("SBSOPT_RANGE")=8;
    m.attr("POSOPT_POS")=0;
    m.attr("POSOPT_SINGLE")=1;
    m.attr("POSOPT_FILE")=2;
    m.attr("POSOPT_RINEX")=3;
    m.attr("POSOPT_RTCM")=4;
    m.attr("STR_NONE")=0;
    m.attr("STR_SERIAL")=1;
    m.attr("STR_FILE")=2;
    m.attr("STR_TCPSVR")=3;
    m.attr("STR_TCPCLI")=4;
    m.attr("STR_NTRIPSVR")=5;
    m.attr("STR_NTRIPCLI")=6;
    m.attr("STR_FTP")=7;
    m.attr("STR_HTTP")=8;
    m.attr("STR_NTRIPCAS")=9;
    m.attr("STR_UDPSVR")=10;
    m.attr("STR_UDPCLI")=11;
    m.attr("STR_MEMBUF")=12;
    m.attr("STRFMT_RTCM2")=0;
    m.attr("STRFMT_RTCM3")=1;
    m.attr("STRFMT_OEM4")=2;
    m.attr("STRFMT_OEM3")=3;
    m.attr("STRFMT_UBX")=4;
    m.attr("STRFMT_SS2")=5;
    m.attr("STRFMT_CRES")=6;
    m.attr("STRFMT_STQ")=7;
    m.attr("STRFMT_JAVAD")=8;
    m.attr("STRFMT_NVS")=9;
    m.attr("STRFMT_BINEX")=10;
    m.attr("STRFMT_RT17")=11;
    m.attr("STRFMT_SEPT")=12;
    m.attr("STRFMT_RINEX")=13;
    m.attr("STRFMT_SP3")=14;
    m.attr("STRFMT_RNXCLK")=15;
    m.attr("STRFMT_SBAS")=16;
    m.attr("STRFMT_NMEA")=17;
    m.attr("MAXRCVFMT")=12;
    m.attr("STR_MODE_R")=0x1;
    m.attr("STR_MODE_W")=0x2;
    m.attr("STR_MODE_RW")=0x3;
    m.attr("GEOID_EMBEDDED")=0;
    m.attr("GEOID_EGM96_M150")=1;
    m.attr("GEOID_EGM2008_M25")=2;
    m.attr("GEOID_EGM2008_M10")=3;
    m.attr("GEOID_GSI2000_M15")=4;
    m.attr("GEOID_RAF09")=5;
    m.attr("DLOPT_FORCE")=0x01;
    m.attr("DLOPT_KEEPCMP")=0x02;
    m.attr("DLOPT_HOLDERR")=0x04;
    m.attr("DLOPT_HOLDLST")=0x08;
    m.attr("LLI_SLIP")=0x01;
    m.attr("LLI_HALFC")=0x02;
    m.attr("LLI_BOCTRK")=0x04;
    m.attr("LLI_HALFA")=0x40;
    m.attr("LLI_HALFS")=0x80;
    m.attr("P2_5")=0.03125;
    m.attr("P2_6")=0.015625;
    m.attr("P2_11")=4.882812500000000E-04;
    m.attr("P2_15")=3.051757812500000E-05;
    m.attr("P2_17")=7.629394531250000E-06;
    m.attr("P2_19")=1.907348632812500E-06;
    m.attr("P2_20")=9.536743164062500E-07;
    m.attr("P2_21")=4.768371582031250E-07;
    m.attr("P2_23")=1.192092895507810E-07;
    m.attr("P2_24")=5.960464477539063E-08;
    m.attr("P2_27")=7.450580596923828E-09;
    m.attr("P2_29")=1.862645149230957E-09;
    m.attr("P2_30")=9.313225746154785E-10;
    m.attr("P2_31")=4.656612873077393E-10;
    m.attr("P2_32")=2.328306436538696E-10;
    m.attr("P2_33")=1.164153218269348E-10;
    m.attr("P2_35")=2.910383045673370E-11;
    m.attr("P2_38")=3.637978807091710E-12;
    m.attr("P2_39")=1.818989403545856E-12;
    m.attr("P2_40")=9.094947017729280E-13;
    m.attr("P2_43")=1.136868377216160E-13;
    m.attr("P2_48")=3.552713678800501E-15;
    m.attr("P2_50")=8.881784197001252E-16;
    m.attr("P2_55")=2.775557561562891E-17;
    m.attr("VER_RTKLIB")="2.4.3";
    m.attr("PATCH_LEVEL")="b34";
    bindArr1D<gtime_t>(m,"gtime_t");
    bindArr2D<gtime_t>(m,"gtime_t");
    bindArr1D<obsd_t>(m,"obsd_t");
    bindArr2D<obsd_t>(m,"obsd_t");
    bindArr1D<obs_t>(m,"obs_t");
    bindArr2D<obs_t>(m,"obs_t");
    bindArr1D<erpd_t>(m,"erpd_t");
    bindArr2D<erpd_t>(m,"erpd_t");
    bindArr1D<erp_t>(m,"erp_t");
    bindArr2D<erp_t>(m,"erp_t");
    bindArr1D<pcv_t>(m,"pcv_t");
    bindArr2D<pcv_t>(m,"pcv_t");
    bindArr1D<pcvs_t>(m,"pcvs_t");
    bindArr2D<pcvs_t>(m,"pcvs_t");
    bindArr1D<alm_t>(m,"alm_t");
    bindArr2D<alm_t>(m,"alm_t");
    bindArr1D<eph_t>(m,"eph_t");
    bindArr2D<eph_t>(m,"eph_t");
    bindArr1D<geph_t>(m,"geph_t");
    bindArr2D<geph_t>(m,"geph_t");
    bindArr1D<peph_t>(m,"peph_t");
    bindArr2D<peph_t>(m,"peph_t");
    bindArr1D<pclk_t>(m,"pclk_t");
    bindArr2D<pclk_t>(m,"pclk_t");
    bindArr1D<seph_t>(m,"seph_t");
    bindArr2D<seph_t>(m,"seph_t");
    bindArr1D<tled_t>(m,"tled_t");
    bindArr2D<tled_t>(m,"tled_t");
    bindArr1D<tle_t>(m,"tle_t");
    bindArr2D<tle_t>(m,"tle_t");
    bindArr1D<tec_t>(m,"tec_t");
    bindArr2D<tec_t>(m,"tec_t");
    bindArr1D<sbsmsg_t>(m,"sbsmsg_t");
    bindArr2D<sbsmsg_t>(m,"sbsmsg_t");
    bindArr1D<sbs_t>(m,"sbs_t");
    bindArr2D<sbs_t>(m,"sbs_t");
    bindArr1D<sbsfcorr_t>(m,"sbsfcorr_t");
    bindArr2D<sbsfcorr_t>(m,"sbsfcorr_t");
    bindArr1D<sbslcorr_t>(m,"sbslcorr_t");
    bindArr2D<sbslcorr_t>(m,"sbslcorr_t");
    bindArr1D<sbssatp_t>(m,"sbssatp_t");
    bindArr2D<sbssatp_t>(m,"sbssatp_t");
    bindArr1D<sbssat_t>(m,"sbssat_t");
    bindArr2D<sbssat_t>(m,"sbssat_t");
    bindArr1D<sbsigp_t>(m,"sbsigp_t");
    bindArr2D<sbsigp_t>(m,"sbsigp_t");
    bindArr1D<sbsigpband_t>(m,"sbsigpband_t");
    bindArr2D<sbsigpband_t>(m,"sbsigpband_t");
    bindArr1D<sbsion_t>(m,"sbsion_t");
    bindArr2D<sbsion_t>(m,"sbsion_t");
    bindArr1D<dgps_t>(m,"dgps_t");
    bindArr2D<dgps_t>(m,"dgps_t");
    bindArr1D<ssr_t>(m,"ssr_t");
    bindArr2D<ssr_t>(m,"ssr_t");
    bindArr1D<nav_t>(m,"nav_t");
    bindArr2D<nav_t>(m,"nav_t");
    bindArr1D<sta_t>(m,"sta_t");
    bindArr2D<sta_t>(m,"sta_t");
    bindArr1D<sol_t>(m,"sol_t");
    bindArr2D<sol_t>(m,"sol_t");
    bindArr1D<solbuf_t>(m,"solbuf_t");
    bindArr2D<solbuf_t>(m,"solbuf_t");
    bindArr1D<solstat_t>(m,"solstat_t");
    bindArr2D<solstat_t>(m,"solstat_t");
    bindArr1D<solstatbuf_t>(m,"solstatbuf_t");
    bindArr2D<solstatbuf_t>(m,"solstatbuf_t");
    bindArr1D<rtcm_t>(m,"rtcm_t");
    bindArr2D<rtcm_t>(m,"rtcm_t");
    bindArr1D<rnxctr_t>(m,"rnxctr_t");
    bindArr2D<rnxctr_t>(m,"rnxctr_t");
    bindArr1D<url_t>(m,"url_t");
    bindArr2D<url_t>(m,"url_t");
    bindArr1D<opt_t>(m,"opt_t");
    bindArr2D<opt_t>(m,"opt_t");
    bindArr1D<snrmask_t>(m,"snrmask_t");
    bindArr2D<snrmask_t>(m,"snrmask_t");
    bindArr1D<prcopt_t>(m,"prcopt_t");
    bindArr2D<prcopt_t>(m,"prcopt_t");
    bindArr1D<solopt_t>(m,"solopt_t");
    bindArr2D<solopt_t>(m,"solopt_t");
    bindArr1D<filopt_t>(m,"filopt_t");
    bindArr2D<filopt_t>(m,"filopt_t");
    bindArr1D<rnxopt_t>(m,"rnxopt_t");
    bindArr2D<rnxopt_t>(m,"rnxopt_t");
    bindArr1D<ssat_t>(m,"ssat_t");
    bindArr2D<ssat_t>(m,"ssat_t");
    bindArr1D<ambc_t>(m,"ambc_t");
    bindArr2D<ambc_t>(m,"ambc_t");
    bindArr1D<rtk_t>(m,"rtk_t");
    bindArr2D<rtk_t>(m,"rtk_t");
    bindArr1D<raw_t>(m,"raw_t");
    bindArr2D<raw_t>(m,"raw_t");
    bindArr1D<stream_t>(m,"stream_t");
    bindArr2D<stream_t>(m,"stream_t");
    bindArr1D<strconv_t>(m,"strconv_t");
    bindArr2D<strconv_t>(m,"strconv_t");
    bindArr1D<strsvr_t>(m,"strsvr_t");
    bindArr2D<strsvr_t>(m,"strsvr_t");
    bindArr1D<rtksvr_t>(m,"rtksvr_t");
    bindArr2D<rtksvr_t>(m,"rtksvr_t");
    bindArr1D<gis_pnt_t>(m,"gis_pnt_t");
    bindArr2D<gis_pnt_t>(m,"gis_pnt_t");
    bindArr1D<gis_poly_t>(m,"gis_poly_t");
    bindArr2D<gis_poly_t>(m,"gis_poly_t");
    bindArr1D<gis_polygon_t>(m,"gis_polygon_t");
    bindArr2D<gis_polygon_t>(m,"gis_polygon_t");
    bindArr1D<gisd_t>(m,"gisd_t");
    bindArr2D<gisd_t>(m,"gisd_t");
    bindArr1D<gis_t>(m,"gis_t");
    bindArr2D<gis_t>(m,"gis_t");
    bindArr1D<long double>(m,"long double");
    bindArr2D<long double>(m,"long double");
    bindArr1D<double>(m,"double");
    bindArr2D<double>(m,"double");
    bindArr1D<float>(m,"float");
    bindArr2D<float>(m,"float");
    bindArr1D<char>(m,"char");
    bindArr2D<char>(m,"char");
    bindArr1D<unsigned char>(m,"unsigned char");
    bindArr2D<unsigned char>(m,"unsigned char");
    bindArr1D<int>(m,"int");
    bindArr2D<int>(m,"int");
    bindArr1D<unsigned int>(m,"unsigned int");
    bindArr2D<unsigned int>(m,"unsigned int");
    bindArr1D<short>(m,"short");
    bindArr2D<short>(m,"short");
    bindArr1D<unsigned short>(m,"unsigned short");
    bindArr2D<unsigned short>(m,"unsigned short");
    bindArr1D<long>(m,"long");
    bindArr2D<long>(m,"long");
    bindArr1D<unsigned long>(m,"unsigned long");
    bindArr2D<unsigned long>(m,"unsigned long");
    py::class_<gtime_t>(m,"gtime_t").def(py::init())
        .def_readwrite("time",&gtime_t::time)
        .def_readwrite("sec",&gtime_t::sec)
        .def_property_readonly("ptr",[](gtime_t& o){return &o;},py::return_value_policy::reference);

    py::class_<obsd_t>(m,"obsd_t").def(py::init())
        .def_readwrite("time",&obsd_t::time)
        .def_readwrite("sat",&obsd_t::sat)
        .def_readwrite("rcv",&obsd_t::rcv)
        .def_property_readonly("SNR",[](obsd_t& o) {Arr1D<uint16_t>* tmp = new Arr1D<uint16_t>(o.SNR,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("LLI",[](obsd_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.LLI,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("code",[](obsd_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.code,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("L",[](obsd_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.L,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("P",[](obsd_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.P,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("D",[](obsd_t& o) {Arr1D<float>* tmp = new Arr1D<float>(o.D,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](obsd_t& o){return &o;},py::return_value_policy::reference);

    py::class_<obs_t>(m,"obs_t").def(py::init())
        .def_readwrite("n",&obs_t::n)
        .def_readwrite("nmax",&obs_t::nmax)
        .def_property("data",[](obs_t& o) {Arr1D<obsd_t>* tmp = new Arr1D<obsd_t>(o.data,-1);return tmp;},[](obs_t& o,Arr1D<obsd_t>arr){o.data=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](obs_t& o){return &o;},py::return_value_policy::reference);

    py::class_<erpd_t>(m,"erpd_t").def(py::init())
        .def_readwrite("mjd",&erpd_t::mjd)
        .def_readwrite("xp",&erpd_t::xp)
        .def_readwrite("yp",&erpd_t::yp)
        .def_readwrite("xpr",&erpd_t::xpr)
        .def_readwrite("ypr",&erpd_t::ypr)
        .def_readwrite("ut1_utc",&erpd_t::ut1_utc)
        .def_readwrite("lod",&erpd_t::lod)
        .def_property_readonly("ptr",[](erpd_t& o){return &o;},py::return_value_policy::reference);

    py::class_<erp_t>(m,"erp_t").def(py::init())
        .def_readwrite("n",&erp_t::n)
        .def_readwrite("nmax",&erp_t::nmax)
        .def_property("data",[](erp_t& o) {Arr1D<erpd_t>* tmp = new Arr1D<erpd_t>(o.data,-1);return tmp;},[](erp_t& o,Arr1D<erpd_t>arr){o.data=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](erp_t& o){return &o;},py::return_value_policy::reference);

    py::class_<pcv_t>(m,"pcv_t").def(py::init())
        .def_readwrite("sat",&pcv_t::sat)
        .def_readwrite("ts",&pcv_t::ts)
        .def_readwrite("te",&pcv_t::te)
        .def_property_readonly("type",[](pcv_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.type,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("code",[](pcv_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.code,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("off",[](pcv_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.off,NFREQ, 3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("var",[](pcv_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.var,NFREQ,19);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](pcv_t& o){return &o;},py::return_value_policy::reference);

    py::class_<pcvs_t>(m,"pcvs_t").def(py::init())
        .def_readwrite("n",&pcvs_t::n)
        .def_readwrite("nmax",&pcvs_t::nmax)
        .def_property("pcv",[](pcvs_t& o) {Arr1D<pcv_t>* tmp = new Arr1D<pcv_t>(o.pcv,-1);return tmp;},[](pcvs_t& o,Arr1D<pcv_t>arr){o.pcv=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](pcvs_t& o){return &o;},py::return_value_policy::reference);

    py::class_<alm_t>(m,"alm_t").def(py::init())
        .def_readwrite("sat",&alm_t::sat)
        .def_readwrite("svh",&alm_t::svh)
        .def_readwrite("svconf",&alm_t::svconf)
        .def_readwrite("week",&alm_t::week)
        .def_readwrite("toa",&alm_t::toa)
        .def_readwrite("A",&alm_t::A)
        .def_readwrite("e",&alm_t::e)
        .def_readwrite("i0",&alm_t::i0)
        .def_readwrite("OMG0",&alm_t::OMG0)
        .def_readwrite("omg",&alm_t::omg)
        .def_readwrite("M0",&alm_t::M0)
        .def_readwrite("OMGd",&alm_t::OMGd)
        .def_readwrite("toas",&alm_t::toas)
        .def_readwrite("f0",&alm_t::f0)
        .def_readwrite("f1",&alm_t::f1)
        .def_property_readonly("ptr",[](alm_t& o){return &o;},py::return_value_policy::reference);

    py::class_<eph_t>(m,"eph_t").def(py::init())
        .def_readwrite("sat",&eph_t::sat)
        .def_readwrite("iode",&eph_t::iode)
        .def_readwrite("iodc",&eph_t::iodc)
        .def_readwrite("sva",&eph_t::sva)
        .def_readwrite("svh",&eph_t::svh)
        .def_readwrite("week",&eph_t::week)
        .def_readwrite("code",&eph_t::code)
        .def_readwrite("flag",&eph_t::flag)
        .def_readwrite("toe",&eph_t::toe)
        .def_readwrite("toc",&eph_t::toc)
        .def_readwrite("ttr",&eph_t::ttr)
        .def_readwrite("A",&eph_t::A)
        .def_readwrite("e",&eph_t::e)
        .def_readwrite("i0",&eph_t::i0)
        .def_readwrite("OMG0",&eph_t::OMG0)
        .def_readwrite("omg",&eph_t::omg)
        .def_readwrite("M0",&eph_t::M0)
        .def_readwrite("deln",&eph_t::deln)
        .def_readwrite("OMGd",&eph_t::OMGd)
        .def_readwrite("idot",&eph_t::idot)
        .def_readwrite("crc",&eph_t::crc)
        .def_readwrite("crs",&eph_t::crs)
        .def_readwrite("cuc",&eph_t::cuc)
        .def_readwrite("cus",&eph_t::cus)
        .def_readwrite("cic",&eph_t::cic)
        .def_readwrite("cis",&eph_t::cis)
        .def_readwrite("toes",&eph_t::toes)
        .def_readwrite("fit",&eph_t::fit)
        .def_readwrite("f0",&eph_t::f0)
        .def_readwrite("f1",&eph_t::f1)
        .def_readwrite("f2",&eph_t::f2)
        .def_readwrite("Adot",&eph_t::Adot)
        .def_readwrite("ndot",&eph_t::ndot)
        .def_property_readonly("tgd",[](eph_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.tgd,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](eph_t& o){return &o;},py::return_value_policy::reference);

    py::class_<geph_t>(m,"geph_t").def(py::init())
        .def_readwrite("sat",&geph_t::sat)
        .def_readwrite("iode",&geph_t::iode)
        .def_readwrite("frq",&geph_t::frq)
        .def_readwrite("svh",&geph_t::svh)
        .def_readwrite("sva",&geph_t::sva)
        .def_readwrite("age",&geph_t::age)
        .def_readwrite("toe",&geph_t::toe)
        .def_readwrite("tof",&geph_t::tof)
        .def_readwrite("taun",&geph_t::taun)
        .def_readwrite("gamn",&geph_t::gamn)
        .def_readwrite("dtaun",&geph_t::dtaun)
        .def_property_readonly("pos",[](geph_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.pos,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("vel",[](geph_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.vel,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("acc",[](geph_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.acc,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](geph_t& o){return &o;},py::return_value_policy::reference);

    py::class_<peph_t>(m,"peph_t").def(py::init())
        .def_readwrite("time",&peph_t::time)
        .def_readwrite("index",&peph_t::index)
        .def_property_readonly("pos",[](peph_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.pos,MAXSAT,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("std",[](peph_t& o) {Arr2D<float>* tmp = new Arr2D<float>(o.std,MAXSAT,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("vel",[](peph_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.vel,MAXSAT,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("vst",[](peph_t& o) {Arr2D<float>* tmp = new Arr2D<float>(o.vst,MAXSAT,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("cov",[](peph_t& o) {Arr2D<float>* tmp = new Arr2D<float>(o.cov,MAXSAT,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("vco",[](peph_t& o) {Arr2D<float>* tmp = new Arr2D<float>(o.vco,MAXSAT,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](peph_t& o){return &o;},py::return_value_policy::reference);

    py::class_<pclk_t>(m,"pclk_t").def(py::init())
        .def_readwrite("time",&pclk_t::time)
        .def_readwrite("index",&pclk_t::index)
        .def_property_readonly("clk",[](pclk_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.clk,MAXSAT,1);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("std",[](pclk_t& o) {Arr2D<float>* tmp = new Arr2D<float>(o.std,MAXSAT,1);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](pclk_t& o){return &o;},py::return_value_policy::reference);

    py::class_<seph_t>(m,"seph_t").def(py::init())
        .def_readwrite("sat",&seph_t::sat)
        .def_readwrite("t0",&seph_t::t0)
        .def_readwrite("tof",&seph_t::tof)
        .def_readwrite("sva",&seph_t::sva)
        .def_readwrite("svh",&seph_t::svh)
        .def_readwrite("af0",&seph_t::af0)
        .def_readwrite("af1",&seph_t::af1)
        .def_property_readonly("pos",[](seph_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.pos,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("vel",[](seph_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.vel,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("acc",[](seph_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.acc,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](seph_t& o){return &o;},py::return_value_policy::reference);

    py::class_<tled_t>(m,"tled_t").def(py::init())
        .def_readwrite("satclass",&tled_t::satclass)
        .def_readwrite("epoch",&tled_t::epoch)
        .def_readwrite("ndot",&tled_t::ndot)
        .def_readwrite("nddot",&tled_t::nddot)
        .def_readwrite("bstar",&tled_t::bstar)
        .def_readwrite("etype",&tled_t::etype)
        .def_readwrite("eleno",&tled_t::eleno)
        .def_readwrite("inc",&tled_t::inc)
        .def_readwrite("OMG",&tled_t::OMG)
        .def_readwrite("ecc",&tled_t::ecc)
        .def_readwrite("omg",&tled_t::omg)
        .def_readwrite("M",&tled_t::M)
        .def_readwrite("n",&tled_t::n)
        .def_readwrite("rev",&tled_t::rev)
        .def_property_readonly("name",[](tled_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.name,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("alias",[](tled_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.alias,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("satno",[](tled_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.satno,16);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("desig",[](tled_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.desig,16);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](tled_t& o){return &o;},py::return_value_policy::reference);

    py::class_<tle_t>(m,"tle_t").def(py::init())
        .def_readwrite("n",&tle_t::n)
        .def_readwrite("nmax",&tle_t::nmax)
        .def_property("data",[](tle_t& o) {Arr1D<tled_t>* tmp = new Arr1D<tled_t>(o.data,-1);return tmp;},[](tle_t& o,Arr1D<tled_t>arr){o.data=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](tle_t& o){return &o;},py::return_value_policy::reference);

    py::class_<tec_t>(m,"tec_t").def(py::init())
        .def_readwrite("time",&tec_t::time)
        .def_readwrite("rb",&tec_t::rb)
        .def_property_readonly("ndata",[](tec_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.ndata,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("lats",[](tec_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.lats,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("lons",[](tec_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.lons,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("hgts",[](tec_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.hgts,3);return tmp;},py::return_value_policy::reference)
        .def_property("data",[](tec_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.data,-1);return tmp;},[](tec_t& o,Arr1D<double>arr){o.data=arr.src;},py::return_value_policy::reference)
        .def_property("rms",[](tec_t& o) {Arr1D<float>* tmp = new Arr1D<float>(o.rms,-1);return tmp;},[](tec_t& o,Arr1D<float>arr){o.rms=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](tec_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sbsmsg_t>(m,"sbsmsg_t").def(py::init())
        .def_readwrite("week",&sbsmsg_t::week)
        .def_readwrite("tow",&sbsmsg_t::tow)
        .def_readwrite("prn",&sbsmsg_t::prn)
        .def_readwrite("rcv",&sbsmsg_t::rcv)
        .def_property_readonly("msg",[](sbsmsg_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.msg,29);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](sbsmsg_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sbs_t>(m,"sbs_t").def(py::init())
        .def_readwrite("n",&sbs_t::n)
        .def_readwrite("nmax",&sbs_t::nmax)
        .def_property("msgs",[](sbs_t& o) {Arr1D<sbsmsg_t>* tmp = new Arr1D<sbsmsg_t>(o.msgs,-1);return tmp;},[](sbs_t& o,Arr1D<sbsmsg_t>arr){o.msgs=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](sbs_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sbsfcorr_t>(m,"sbsfcorr_t").def(py::init())
        .def_readwrite("t0",&sbsfcorr_t::t0)
        .def_readwrite("prc",&sbsfcorr_t::prc)
        .def_readwrite("rrc",&sbsfcorr_t::rrc)
        .def_readwrite("dt",&sbsfcorr_t::dt)
        .def_readwrite("iodf",&sbsfcorr_t::iodf)
        .def_readwrite("udre",&sbsfcorr_t::udre)
        .def_readwrite("ai",&sbsfcorr_t::ai)
        .def_property_readonly("ptr",[](sbsfcorr_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sbslcorr_t>(m,"sbslcorr_t").def(py::init())
        .def_readwrite("t0",&sbslcorr_t::t0)
        .def_readwrite("iode",&sbslcorr_t::iode)
        .def_readwrite("daf0",&sbslcorr_t::daf0)
        .def_readwrite("daf1",&sbslcorr_t::daf1)
        .def_property_readonly("dpos",[](sbslcorr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.dpos,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("dvel",[](sbslcorr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.dvel,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](sbslcorr_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sbssatp_t>(m,"sbssatp_t").def(py::init())
        .def_readwrite("sat",&sbssatp_t::sat)
        .def_readwrite("fcorr",&sbssatp_t::fcorr)
        .def_readwrite("lcorr",&sbssatp_t::lcorr)
        .def_property_readonly("ptr",[](sbssatp_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sbssat_t>(m,"sbssat_t").def(py::init())
        .def_readwrite("iodp",&sbssat_t::iodp)
        .def_readwrite("nsat",&sbssat_t::nsat)
        .def_readwrite("tlat",&sbssat_t::tlat)
        .def_property_readonly("sat",[](sbssat_t& o) {Arr1D<sbssatp_t>* tmp = new Arr1D<sbssatp_t>(o.sat,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](sbssat_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sbsigp_t>(m,"sbsigp_t").def(py::init())
        .def_readwrite("t0",&sbsigp_t::t0)
        .def_readwrite("lat",&sbsigp_t::lat)
        .def_readwrite("lon",&sbsigp_t::lon)
        .def_readwrite("give",&sbsigp_t::give)
        .def_readwrite("delay",&sbsigp_t::delay)
        .def_property_readonly("ptr",[](sbsigp_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sbsigpband_t>(m,"sbsigpband_t").def(py::init())
        .def_readwrite("x",&sbsigpband_t::x)
        .def_readwrite("bits",&sbsigpband_t::bits)
        .def_readwrite("bite",&sbsigpband_t::bite)
        .def_property("y",[](sbsigpband_t& o) {Arr1D<int16_t>* tmp = new Arr1D<int16_t>(const_cast<int16_t*>(o.y),-1);return tmp;},[](sbsigpband_t& o,Arr1D<int16_t>arr){o.y=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](sbsigpband_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sbsion_t>(m,"sbsion_t").def(py::init())
        .def_readwrite("iodi",&sbsion_t::iodi)
        .def_readwrite("nigp",&sbsion_t::nigp)
        .def_property_readonly("igp",[](sbsion_t& o) {Arr1D<sbsigp_t>* tmp = new Arr1D<sbsigp_t>(o.igp,MAXNIGP);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](sbsion_t& o){return &o;},py::return_value_policy::reference);

    py::class_<dgps_t>(m,"dgps_t").def(py::init())
        .def_readwrite("t0",&dgps_t::t0)
        .def_readwrite("prc",&dgps_t::prc)
        .def_readwrite("rrc",&dgps_t::rrc)
        .def_readwrite("iod",&dgps_t::iod)
        .def_readwrite("udre",&dgps_t::udre)
        .def_property_readonly("ptr",[](dgps_t& o){return &o;},py::return_value_policy::reference);

    py::class_<ssr_t>(m,"ssr_t").def(py::init())
        .def_readwrite("iode",&ssr_t::iode)
        .def_readwrite("iodcrc",&ssr_t::iodcrc)
        .def_readwrite("ura",&ssr_t::ura)
        .def_readwrite("refd",&ssr_t::refd)
        .def_readwrite("hrclk",&ssr_t::hrclk)
        .def_readwrite("yaw_ang",&ssr_t::yaw_ang)
        .def_readwrite("yaw_rate",&ssr_t::yaw_rate)
        .def_readwrite("update",&ssr_t::update)
        .def_property_readonly("t0",[](ssr_t& o) {Arr1D<gtime_t>* tmp = new Arr1D<gtime_t>(o.t0,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("udi",[](ssr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.udi,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("iod",[](ssr_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.iod,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("deph",[](ssr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.deph,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ddeph",[](ssr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.ddeph,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("dclk",[](ssr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.dclk,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("cbias",[](ssr_t& o) {Arr1D<float>* tmp = new Arr1D<float>(o.cbias,MAXCODE);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("pbias",[](ssr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.pbias,MAXCODE);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("stdpb",[](ssr_t& o) {Arr1D<float>* tmp = new Arr1D<float>(o.stdpb,MAXCODE);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](ssr_t& o){return &o;},py::return_value_policy::reference);

    py::class_<nav_t>(m,"nav_t").def(py::init())
        .def_readwrite("n",&nav_t::n)
        .def_readwrite("nmax",&nav_t::nmax)
        .def_readwrite("ng",&nav_t::ng)
        .def_readwrite("ngmax",&nav_t::ngmax)
        .def_readwrite("ns",&nav_t::ns)
        .def_readwrite("nsmax",&nav_t::nsmax)
        .def_readwrite("ne",&nav_t::ne)
        .def_readwrite("nemax",&nav_t::nemax)
        .def_readwrite("nc",&nav_t::nc)
        .def_readwrite("ncmax",&nav_t::ncmax)
        .def_readwrite("na",&nav_t::na)
        .def_readwrite("namax",&nav_t::namax)
        .def_readwrite("nt",&nav_t::nt)
        .def_readwrite("ntmax",&nav_t::ntmax)
        .def_readwrite("erp",&nav_t::erp)
        .def_readwrite("sbssat",&nav_t::sbssat)
        .def_property("eph",[](nav_t& o) {Arr1D<eph_t>* tmp = new Arr1D<eph_t>(o.eph,-1);return tmp;},[](nav_t& o,Arr1D<eph_t>arr){o.eph=arr.src;},py::return_value_policy::reference)
        .def_property("geph",[](nav_t& o) {Arr1D<geph_t>* tmp = new Arr1D<geph_t>(o.geph,-1);return tmp;},[](nav_t& o,Arr1D<geph_t>arr){o.geph=arr.src;},py::return_value_policy::reference)
        .def_property("seph",[](nav_t& o) {Arr1D<seph_t>* tmp = new Arr1D<seph_t>(o.seph,-1);return tmp;},[](nav_t& o,Arr1D<seph_t>arr){o.seph=arr.src;},py::return_value_policy::reference)
        .def_property("peph",[](nav_t& o) {Arr1D<peph_t>* tmp = new Arr1D<peph_t>(o.peph,-1);return tmp;},[](nav_t& o,Arr1D<peph_t>arr){o.peph=arr.src;},py::return_value_policy::reference)
        .def_property("pclk",[](nav_t& o) {Arr1D<pclk_t>* tmp = new Arr1D<pclk_t>(o.pclk,-1);return tmp;},[](nav_t& o,Arr1D<pclk_t>arr){o.pclk=arr.src;},py::return_value_policy::reference)
        .def_property("alm",[](nav_t& o) {Arr1D<alm_t>* tmp = new Arr1D<alm_t>(o.alm,-1);return tmp;},[](nav_t& o,Arr1D<alm_t>arr){o.alm=arr.src;},py::return_value_policy::reference)
        .def_property("tec",[](nav_t& o) {Arr1D<tec_t>* tmp = new Arr1D<tec_t>(o.tec,-1);return tmp;},[](nav_t& o,Arr1D<tec_t>arr){o.tec=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("utc_gps",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.utc_gps,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("utc_glo",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.utc_glo,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("utc_gal",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.utc_gal,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("utc_qzs",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.utc_qzs,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("utc_cmp",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.utc_cmp,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("utc_irn",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.utc_irn,9);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("utc_sbs",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.utc_sbs,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ion_gps",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.ion_gps,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ion_gal",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.ion_gal,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ion_qzs",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.ion_qzs,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ion_cmp",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.ion_cmp,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ion_irn",[](nav_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.ion_irn,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("glo_fcn",[](nav_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.glo_fcn,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("cbias",[](nav_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.cbias,MAXSAT,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("rbias",[](nav_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.rbias,MAXRCV,2);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("pcvs",[](nav_t& o) {Arr1D<pcv_t>* tmp = new Arr1D<pcv_t>(o.pcvs,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("sbsion",[](nav_t& o) {Arr1D<sbsion_t>* tmp = new Arr1D<sbsion_t>(o.sbsion,MAXBAND+1);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("dgps",[](nav_t& o) {Arr1D<dgps_t>* tmp = new Arr1D<dgps_t>(o.dgps,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ssr",[](nav_t& o) {Arr1D<ssr_t>* tmp = new Arr1D<ssr_t>(o.ssr,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](nav_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sta_t>(m,"sta_t").def(py::init())
        .def_readwrite("antsetup",&sta_t::antsetup)
        .def_readwrite("itrf",&sta_t::itrf)
        .def_readwrite("deltype",&sta_t::deltype)
        .def_readwrite("hgt",&sta_t::hgt)
        .def_readwrite("glo_cp_align",&sta_t::glo_cp_align)
        .def_property_readonly("name",[](sta_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.name,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("marker",[](sta_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.marker,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("antdes",[](sta_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.antdes,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("antsno",[](sta_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.antsno,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("rectype",[](sta_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.rectype,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("recver",[](sta_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.recver,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("recsno",[](sta_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.recsno,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("pos",[](sta_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.pos,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("del",[](sta_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.del,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("glo_cp_bias",[](sta_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.glo_cp_bias,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](sta_t& o){return &o;},py::return_value_policy::reference);

    py::class_<sol_t>(m,"sol_t").def(py::init())
        .def_readwrite("time",&sol_t::time)
        .def_readwrite("type",&sol_t::type)
        .def_readwrite("stat",&sol_t::stat)
        .def_readwrite("ns",&sol_t::ns)
        .def_readwrite("age",&sol_t::age)
        .def_readwrite("ratio",&sol_t::ratio)
        .def_readwrite("thres",&sol_t::thres)
        .def_property_readonly("rr",[](sol_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.rr,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("qr",[](sol_t& o) {Arr1D<float>* tmp = new Arr1D<float>(o.qr,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("qv",[](sol_t& o) {Arr1D<float>* tmp = new Arr1D<float>(o.qv,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("dtr",[](sol_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.dtr,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](sol_t& o){return &o;},py::return_value_policy::reference);

    py::class_<solbuf_t>(m,"solbuf_t").def(py::init())
        .def_readwrite("n",&solbuf_t::n)
        .def_readwrite("nmax",&solbuf_t::nmax)
        .def_readwrite("cyclic",&solbuf_t::cyclic)
        .def_readwrite("start",&solbuf_t::start)
        .def_readwrite("end",&solbuf_t::end)
        .def_readwrite("time",&solbuf_t::time)
        .def_readwrite("nb",&solbuf_t::nb)
        .def_property("data",[](solbuf_t& o) {Arr1D<sol_t>* tmp = new Arr1D<sol_t>(o.data,-1);return tmp;},[](solbuf_t& o,Arr1D<sol_t>arr){o.data=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("rb",[](solbuf_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.rb,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("buff",[](solbuf_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.buff,MAXSOLMSG+1);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](solbuf_t& o){return &o;},py::return_value_policy::reference);

    py::class_<solstat_t>(m,"solstat_t").def(py::init())
        .def_readwrite("time",&solstat_t::time)
        .def_readwrite("sat",&solstat_t::sat)
        .def_readwrite("frq",&solstat_t::frq)
        .def_readwrite("az",&solstat_t::az)
        .def_readwrite("el",&solstat_t::el)
        .def_readwrite("resp",&solstat_t::resp)
        .def_readwrite("resc",&solstat_t::resc)
        .def_readwrite("flag",&solstat_t::flag)
        .def_readwrite("snr",&solstat_t::snr)
        .def_readwrite("lock",&solstat_t::lock)
        .def_readwrite("outc",&solstat_t::outc)
        .def_readwrite("slipc",&solstat_t::slipc)
        .def_readwrite("rejc",&solstat_t::rejc)
        .def_property_readonly("ptr",[](solstat_t& o){return &o;},py::return_value_policy::reference);

    py::class_<solstatbuf_t>(m,"solstatbuf_t").def(py::init())
        .def_readwrite("n",&solstatbuf_t::n)
        .def_readwrite("nmax",&solstatbuf_t::nmax)
        .def_property("data",[](solstatbuf_t& o) {Arr1D<solstat_t>* tmp = new Arr1D<solstat_t>(o.data,-1);return tmp;},[](solstatbuf_t& o,Arr1D<solstat_t>arr){o.data=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](solstatbuf_t& o){return &o;},py::return_value_policy::reference);

    py::class_<rtcm_t>(m,"rtcm_t").def(py::init())
        .def_readwrite("staid",&rtcm_t::staid)
        .def_readwrite("stah",&rtcm_t::stah)
        .def_readwrite("seqno",&rtcm_t::seqno)
        .def_readwrite("outtype",&rtcm_t::outtype)
        .def_readwrite("time",&rtcm_t::time)
        .def_readwrite("time_s",&rtcm_t::time_s)
        .def_readwrite("obs",&rtcm_t::obs)
        .def_readwrite("nav",&rtcm_t::nav)
        .def_readwrite("sta",&rtcm_t::sta)
        .def_readwrite("obsflag",&rtcm_t::obsflag)
        .def_readwrite("ephsat",&rtcm_t::ephsat)
        .def_readwrite("ephset",&rtcm_t::ephset)
        .def_readwrite("nbyte",&rtcm_t::nbyte)
        .def_readwrite("nbit",&rtcm_t::nbit)
        .def_readwrite("len",&rtcm_t::len)
        .def_readwrite("word",&rtcm_t::word)
        .def_property("dgps",[](rtcm_t& o) {Arr1D<dgps_t>* tmp = new Arr1D<dgps_t>(o.dgps,-1);return tmp;},[](rtcm_t& o,Arr1D<dgps_t>arr){o.dgps=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ssr",[](rtcm_t& o) {Arr1D<ssr_t>* tmp = new Arr1D<ssr_t>(o.ssr,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("msg",[](rtcm_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.msg,128);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("msgtype",[](rtcm_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.msgtype,256);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("msmtype",[](rtcm_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.msmtype,7,128);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("cp",[](rtcm_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.cp,MAXSAT,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("lock",[](rtcm_t& o) {Arr2D<uint16_t>* tmp = new Arr2D<uint16_t>(o.lock,MAXSAT,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("loss",[](rtcm_t& o) {Arr2D<uint16_t>* tmp = new Arr2D<uint16_t>(o.loss,MAXSAT,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("lltime",[](rtcm_t& o) {Arr2D<gtime_t>* tmp = new Arr2D<gtime_t>(o.lltime,MAXSAT,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("buff",[](rtcm_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.buff,1200);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("nmsg2",[](rtcm_t& o) {Arr1D<uint32_t>* tmp = new Arr1D<uint32_t>(o.nmsg2,100);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("nmsg3",[](rtcm_t& o) {Arr1D<uint32_t>* tmp = new Arr1D<uint32_t>(o.nmsg3,400);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("opt",[](rtcm_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.opt,256);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](rtcm_t& o){return &o;},py::return_value_policy::reference);

    py::class_<rnxctr_t>(m,"rnxctr_t").def(py::init())
        .def_readwrite("time",&rnxctr_t::time)
        .def_readwrite("ver",&rnxctr_t::ver)
        .def_readwrite("type",&rnxctr_t::type)
        .def_readwrite("sys",&rnxctr_t::sys)
        .def_readwrite("tsys",&rnxctr_t::tsys)
        .def_readwrite("obs",&rnxctr_t::obs)
        .def_readwrite("nav",&rnxctr_t::nav)
        .def_readwrite("sta",&rnxctr_t::sta)
        .def_readwrite("ephsat",&rnxctr_t::ephsat)
        .def_readwrite("ephset",&rnxctr_t::ephset)
        .def_property_readonly("tobs",[](rnxctr_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.tobs,8,MAXOBSTYPE);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("opt",[](rnxctr_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.opt,256);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](rnxctr_t& o){return &o;},py::return_value_policy::reference);

    py::class_<url_t>(m,"url_t").def(py::init())
        .def_readwrite("tint",&url_t::tint)
        .def_property_readonly("type",[](url_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.type,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("path",[](url_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.path,1024);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("dir",[](url_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.dir,1024);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](url_t& o){return &o;},py::return_value_policy::reference);

    py::class_<opt_t>(m,"opt_t").def(py::init())
        .def_readwrite("format",&opt_t::format)
        .def_property("name",[](opt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(const_cast<char*>(o.name),-1);return tmp;},[](opt_t& o,Arr1D<char>arr){o.name=arr.src;},py::return_value_policy::reference)
        .def_property("var",[](opt_t& o) {Arr1D<void>* tmp = new Arr1D<void>(o.var,-1);return tmp;},[](opt_t& o,Arr1D<void>arr){o.var=arr.src;},py::return_value_policy::reference)
        .def_property("comment",[](opt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(const_cast<char*>(o.comment),-1);return tmp;},[](opt_t& o,Arr1D<char>arr){o.comment=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](opt_t& o){return &o;},py::return_value_policy::reference);

    py::class_<snrmask_t>(m,"snrmask_t").def(py::init())
        .def_property_readonly("ena",[](snrmask_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.ena,2);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("mask",[](snrmask_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.mask,NFREQ,9);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](snrmask_t& o){return &o;},py::return_value_policy::reference);

    py::class_<prcopt_t>(m,"prcopt_t").def(py::init())
        .def_readwrite("mode",&prcopt_t::mode)
        .def_readwrite("soltype",&prcopt_t::soltype)
        .def_readwrite("nf",&prcopt_t::nf)
        .def_readwrite("navsys",&prcopt_t::navsys)
        .def_readwrite("elmin",&prcopt_t::elmin)
        .def_readwrite("snrmask",&prcopt_t::snrmask)
        .def_readwrite("sateph",&prcopt_t::sateph)
        .def_readwrite("modear",&prcopt_t::modear)
        .def_readwrite("glomodear",&prcopt_t::glomodear)
        .def_readwrite("bdsmodear",&prcopt_t::bdsmodear)
        .def_readwrite("maxout",&prcopt_t::maxout)
        .def_readwrite("minlock",&prcopt_t::minlock)
        .def_readwrite("minfix",&prcopt_t::minfix)
        .def_readwrite("armaxiter",&prcopt_t::armaxiter)
        .def_readwrite("ionoopt",&prcopt_t::ionoopt)
        .def_readwrite("tropopt",&prcopt_t::tropopt)
        .def_readwrite("dynamics",&prcopt_t::dynamics)
        .def_readwrite("tidecorr",&prcopt_t::tidecorr)
        .def_readwrite("niter",&prcopt_t::niter)
        .def_readwrite("codesmooth",&prcopt_t::codesmooth)
        .def_readwrite("intpref",&prcopt_t::intpref)
        .def_readwrite("sbascorr",&prcopt_t::sbascorr)
        .def_readwrite("sbassatsel",&prcopt_t::sbassatsel)
        .def_readwrite("rovpos",&prcopt_t::rovpos)
        .def_readwrite("refpos",&prcopt_t::refpos)
        .def_readwrite("sclkstab",&prcopt_t::sclkstab)
        .def_readwrite("elmaskar",&prcopt_t::elmaskar)
        .def_readwrite("elmaskhold",&prcopt_t::elmaskhold)
        .def_readwrite("thresslip",&prcopt_t::thresslip)
        .def_readwrite("maxtdiff",&prcopt_t::maxtdiff)
        .def_readwrite("maxinno",&prcopt_t::maxinno)
        .def_readwrite("maxgdop",&prcopt_t::maxgdop)
        .def_readwrite("maxaveep",&prcopt_t::maxaveep)
        .def_readwrite("initrst",&prcopt_t::initrst)
        .def_readwrite("outsingle",&prcopt_t::outsingle)
        .def_readwrite("syncsol",&prcopt_t::syncsol)
        .def_readwrite("freqopt",&prcopt_t::freqopt)
        .def_property_readonly("eratio",[](prcopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.eratio,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("err",[](prcopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.err,5);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("std",[](prcopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.std,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("prn",[](prcopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.prn,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("thresar",[](prcopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.thresar,8);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("baseline",[](prcopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.baseline,2);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ru",[](prcopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.ru,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("rb",[](prcopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.rb,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("anttype",[](prcopt_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.anttype,2,MAXANT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("antdel",[](prcopt_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.antdel,2,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("pcvr",[](prcopt_t& o) {Arr1D<pcv_t>* tmp = new Arr1D<pcv_t>(o.pcvr,2);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("exsats",[](prcopt_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.exsats,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("rnxopt",[](prcopt_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.rnxopt,2,256);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("posopt",[](prcopt_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.posopt,6);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("odisp",[](prcopt_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.odisp,2,6*11);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("pppopt",[](prcopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.pppopt,256);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](prcopt_t& o){return &o;},py::return_value_policy::reference);

    py::class_<solopt_t>(m,"solopt_t").def(py::init())
        .def_readwrite("posf",&solopt_t::posf)
        .def_readwrite("times",&solopt_t::times)
        .def_readwrite("timef",&solopt_t::timef)
        .def_readwrite("timeu",&solopt_t::timeu)
        .def_readwrite("degf",&solopt_t::degf)
        .def_readwrite("outhead",&solopt_t::outhead)
        .def_readwrite("outopt",&solopt_t::outopt)
        .def_readwrite("outvel",&solopt_t::outvel)
        .def_readwrite("datum",&solopt_t::datum)
        .def_readwrite("height",&solopt_t::height)
        .def_readwrite("geoid",&solopt_t::geoid)
        .def_readwrite("solstatic",&solopt_t::solstatic)
        .def_readwrite("sstat",&solopt_t::sstat)
        .def_readwrite("trace",&solopt_t::trace)
        .def_readwrite("maxsolstd",&solopt_t::maxsolstd)
        .def_property_readonly("nmeaintv",[](solopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.nmeaintv,2);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("sep",[](solopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.sep,64);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("prog",[](solopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.prog,64);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](solopt_t& o){return &o;},py::return_value_policy::reference);

    py::class_<filopt_t>(m,"filopt_t").def(py::init())
        .def_property_readonly("satantp",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.satantp,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("rcvantp",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.rcvantp,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("stapos",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.stapos,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("geoid",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.geoid,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("iono",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.iono,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("dcb",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.dcb,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("eop",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.eop,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("blq",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.blq,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("tempdir",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.tempdir,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("geexe",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.geexe,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("solstat",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.solstat,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("trace",[](filopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.trace,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](filopt_t& o){return &o;},py::return_value_policy::reference);

    py::class_<rnxopt_t>(m,"rnxopt_t").def(py::init())
        .def_readwrite("ts",&rnxopt_t::ts)
        .def_readwrite("te",&rnxopt_t::te)
        .def_readwrite("tint",&rnxopt_t::tint)
        .def_readwrite("ttol",&rnxopt_t::ttol)
        .def_readwrite("tunit",&rnxopt_t::tunit)
        .def_readwrite("rnxver",&rnxopt_t::rnxver)
        .def_readwrite("navsys",&rnxopt_t::navsys)
        .def_readwrite("obstype",&rnxopt_t::obstype)
        .def_readwrite("freqtype",&rnxopt_t::freqtype)
        .def_readwrite("outiono",&rnxopt_t::outiono)
        .def_readwrite("outtime",&rnxopt_t::outtime)
        .def_readwrite("outleaps",&rnxopt_t::outleaps)
        .def_readwrite("autopos",&rnxopt_t::autopos)
        .def_readwrite("phshift",&rnxopt_t::phshift)
        .def_readwrite("halfcyc",&rnxopt_t::halfcyc)
        .def_readwrite("sep_nav",&rnxopt_t::sep_nav)
        .def_readwrite("tstart",&rnxopt_t::tstart)
        .def_readwrite("tend",&rnxopt_t::tend)
        .def_readwrite("trtcm",&rnxopt_t::trtcm)
        .def_property_readonly("mask",[](rnxopt_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.mask,7,64);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("staid",[](rnxopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.staid,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("prog",[](rnxopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.prog,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("runby",[](rnxopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.runby,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("marker",[](rnxopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.marker,64);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("markerno",[](rnxopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.markerno,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("markertype",[](rnxopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.markertype,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("name",[](rnxopt_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.name,2,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("rec",[](rnxopt_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.rec,3,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ant",[](rnxopt_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.ant,3,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("apppos",[](rnxopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.apppos,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("antdel",[](rnxopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.antdel,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("glo_cp_bias",[](rnxopt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.glo_cp_bias,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("comment",[](rnxopt_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.comment,MAXCOMMENT,64);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("rcvopt",[](rnxopt_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.rcvopt,256);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("exsats",[](rnxopt_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.exsats,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("glofcn",[](rnxopt_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.glofcn,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("tobs",[](rnxopt_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.tobs,7,MAXOBSTYPE);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("shift",[](rnxopt_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.shift,7,MAXOBSTYPE);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("nobs",[](rnxopt_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.nobs,7);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](rnxopt_t& o){return &o;},py::return_value_policy::reference);

    py::class_<ssat_t>(m,"ssat_t").def(py::init())
        .def_readwrite("sys",&ssat_t::sys)
        .def_readwrite("vs",&ssat_t::vs)
        .def_readwrite("phw",&ssat_t::phw)
        .def_property_readonly("azel",[](ssat_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.azel,2);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("resp",[](ssat_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.resp,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("resc",[](ssat_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.resc,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("vsat",[](ssat_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.vsat,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("snr",[](ssat_t& o) {Arr1D<uint16_t>* tmp = new Arr1D<uint16_t>(o.snr,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("fix",[](ssat_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.fix,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("slip",[](ssat_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.slip,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("half",[](ssat_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.half,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("lock",[](ssat_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.lock,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("outc",[](ssat_t& o) {Arr1D<uint32_t>* tmp = new Arr1D<uint32_t>(o.outc,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("slipc",[](ssat_t& o) {Arr1D<uint32_t>* tmp = new Arr1D<uint32_t>(o.slipc,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("rejc",[](ssat_t& o) {Arr1D<uint32_t>* tmp = new Arr1D<uint32_t>(o.rejc,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("gf",[](ssat_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.gf,NFREQ-1);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("mw",[](ssat_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.mw,NFREQ-1);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("pt",[](ssat_t& o) {Arr2D<gtime_t>* tmp = new Arr2D<gtime_t>(o.pt,2,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ph",[](ssat_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.ph,2,NFREQ);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](ssat_t& o){return &o;},py::return_value_policy::reference);

    py::class_<ambc_t>(m,"ambc_t").def(py::init())
        .def_readwrite("fixcnt",&ambc_t::fixcnt)
        .def_property_readonly("epoch",[](ambc_t& o) {Arr1D<gtime_t>* tmp = new Arr1D<gtime_t>(o.epoch,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("n",[](ambc_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.n,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("LC",[](ambc_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.LC,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("LCv",[](ambc_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.LCv,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("flags",[](ambc_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.flags,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](ambc_t& o){return &o;},py::return_value_policy::reference);

    py::class_<rtk_t>(m,"rtk_t").def(py::init())
        .def_readwrite("sol",&rtk_t::sol)
        .def_readwrite("nx",&rtk_t::nx)
        .def_readwrite("na",&rtk_t::na)
        .def_readwrite("tt",&rtk_t::tt)
        .def_readwrite("nfix",&rtk_t::nfix)
        .def_readwrite("neb",&rtk_t::neb)
        .def_readwrite("opt",&rtk_t::opt)
        .def_property_readonly("rb",[](rtk_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.rb,6);return tmp;},py::return_value_policy::reference)
        .def_property("x",[](rtk_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.x,-1);return tmp;},[](rtk_t& o,Arr1D<double>arr){o.x=arr.src;},py::return_value_policy::reference)
        .def_property("P",[](rtk_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.P,-1);return tmp;},[](rtk_t& o,Arr1D<double>arr){o.P=arr.src;},py::return_value_policy::reference)
        .def_property("xa",[](rtk_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.xa,-1);return tmp;},[](rtk_t& o,Arr1D<double>arr){o.xa=arr.src;},py::return_value_policy::reference)
        .def_property("Pa",[](rtk_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.Pa,-1);return tmp;},[](rtk_t& o,Arr1D<double>arr){o.Pa=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ambc",[](rtk_t& o) {Arr1D<ambc_t>* tmp = new Arr1D<ambc_t>(o.ambc,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ssat",[](rtk_t& o) {Arr1D<ssat_t>* tmp = new Arr1D<ssat_t>(o.ssat,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("errbuf",[](rtk_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.errbuf,MAXERRMSG);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](rtk_t& o){return &o;},py::return_value_policy::reference);

    py::class_<raw_t>(m,"raw_t").def(py::init())
        .def_readwrite("time",&raw_t::time)
        .def_readwrite("obs",&raw_t::obs)
        .def_readwrite("obuf",&raw_t::obuf)
        .def_readwrite("nav",&raw_t::nav)
        .def_readwrite("sta",&raw_t::sta)
        .def_readwrite("ephsat",&raw_t::ephsat)
        .def_readwrite("ephset",&raw_t::ephset)
        .def_readwrite("sbsmsg",&raw_t::sbsmsg)
        .def_readwrite("icpc",&raw_t::icpc)
        .def_readwrite("nbyte",&raw_t::nbyte)
        .def_readwrite("len",&raw_t::len)
        .def_readwrite("iod",&raw_t::iod)
        .def_readwrite("tod",&raw_t::tod)
        .def_readwrite("tbase",&raw_t::tbase)
        .def_readwrite("flag",&raw_t::flag)
        .def_readwrite("outtype",&raw_t::outtype)
        .def_readwrite("format",&raw_t::format)
        .def_property_readonly("tobs",[](raw_t& o) {Arr2D<gtime_t>* tmp = new Arr2D<gtime_t>(o.tobs,MAXSAT,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("msgtype",[](raw_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.msgtype,256);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("subfrm",[](raw_t& o) {Arr2D<uint8_t>* tmp = new Arr2D<uint8_t>(o.subfrm,MAXSAT,380);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("lockt",[](raw_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.lockt,MAXSAT,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("icpp",[](raw_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.icpp,MAXSAT,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("off",[](raw_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.off,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("prCA",[](raw_t& o) {Arr2D<double>* tmp = new Arr2D<double>(o.prCA,MAXSAT,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("dpCA",[](raw_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.dpCA,MAXSAT);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("halfc",[](raw_t& o) {Arr2D<uint8_t>* tmp = new Arr2D<uint8_t>(o.halfc,MAXSAT,NFREQ+NEXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("freqn",[](raw_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.freqn,MAXOBS);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("buff",[](raw_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.buff,MAXRAWLEN);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("opt",[](raw_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.opt,256);return tmp;},py::return_value_policy::reference)
        .def_property("rcv_data",[](raw_t& o) {Arr1D<void>* tmp = new Arr1D<void>(o.rcv_data,-1);return tmp;},[](raw_t& o,Arr1D<void>arr){o.rcv_data=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](raw_t& o){return &o;},py::return_value_policy::reference);

    py::class_<stream_t>(m,"stream_t").def(py::init())
        .def_readwrite("type",&stream_t::type)
        .def_readwrite("mode",&stream_t::mode)
        .def_readwrite("state",&stream_t::state)
        .def_readwrite("inb",&stream_t::inb)
        .def_readwrite("inr",&stream_t::inr)
        .def_readwrite("outb",&stream_t::outb)
        .def_readwrite("outr",&stream_t::outr)
        .def_readwrite("tick_i",&stream_t::tick_i)
        .def_readwrite("tick_o",&stream_t::tick_o)
        .def_readwrite("tact",&stream_t::tact)
        .def_readwrite("inbt",&stream_t::inbt)
        .def_readwrite("outbt",&stream_t::outbt)
        .def_readwrite("lock",&stream_t::lock)
        .def_property("port",[](stream_t& o) {Arr1D<void>* tmp = new Arr1D<void>(o.port,-1);return tmp;},[](stream_t& o,Arr1D<void>arr){o.port=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("path",[](stream_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.path,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("msg",[](stream_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.msg,MAXSTRMSG);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](stream_t& o){return &o;},py::return_value_policy::reference);

    py::class_<strconv_t>(m,"strconv_t").def(py::init())
        .def_readwrite("itype",&strconv_t::itype)
        .def_readwrite("otype",&strconv_t::otype)
        .def_readwrite("nmsg",&strconv_t::nmsg)
        .def_readwrite("stasel",&strconv_t::stasel)
        .def_readwrite("rtcm",&strconv_t::rtcm)
        .def_readwrite("raw",&strconv_t::raw)
        .def_readwrite("out",&strconv_t::out)
        .def_property_readonly("msgs",[](strconv_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.msgs,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("tint",[](strconv_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.tint,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("tick",[](strconv_t& o) {Arr1D<uint32_t>* tmp = new Arr1D<uint32_t>(o.tick,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ephsat",[](strconv_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.ephsat,32);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](strconv_t& o){return &o;},py::return_value_policy::reference);

    py::class_<strsvr_t>(m,"strsvr_t").def(py::init())
        .def_readwrite("state",&strsvr_t::state)
        .def_readwrite("cycle",&strsvr_t::cycle)
        .def_readwrite("buffsize",&strsvr_t::buffsize)
        .def_readwrite("nmeacycle",&strsvr_t::nmeacycle)
        .def_readwrite("relayback",&strsvr_t::relayback)
        .def_readwrite("nstr",&strsvr_t::nstr)
        .def_readwrite("npb",&strsvr_t::npb)
        .def_readwrite("tick",&strsvr_t::tick)
        .def_readwrite("thread",&strsvr_t::thread)
        .def_readwrite("lock",&strsvr_t::lock)
        .def_property_readonly("cmds_periodic",[](strsvr_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.cmds_periodic,16,MAXRCVCMD);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("nmeapos",[](strsvr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.nmeapos,3);return tmp;},py::return_value_policy::reference)
        .def_property("buff",[](strsvr_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.buff,-1);return tmp;},[](strsvr_t& o,Arr1D<uint8_t>arr){o.buff=arr.src;},py::return_value_policy::reference)
        .def_property("pbuf",[](strsvr_t& o) {Arr1D<uint8_t>* tmp = new Arr1D<uint8_t>(o.pbuf,-1);return tmp;},[](strsvr_t& o,Arr1D<uint8_t>arr){o.pbuf=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("stream",[](strsvr_t& o) {Arr1D<stream_t>* tmp = new Arr1D<stream_t>(o.stream,16);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("strlog",[](strsvr_t& o) {Arr1D<stream_t>* tmp = new Arr1D<stream_t>(o.strlog,16);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("conv",[](strsvr_t& o) {Arr2D<strconv_t>* tmp = new Arr2D<strconv_t>(o.conv,-1,16);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](strsvr_t& o){return &o;},py::return_value_policy::reference);

    py::class_<rtksvr_t>(m,"rtksvr_t").def(py::init())
        .def_readwrite("state",&rtksvr_t::state)
        .def_readwrite("cycle",&rtksvr_t::cycle)
        .def_readwrite("nmeacycle",&rtksvr_t::nmeacycle)
        .def_readwrite("nmeareq",&rtksvr_t::nmeareq)
        .def_readwrite("buffsize",&rtksvr_t::buffsize)
        .def_readwrite("navsel",&rtksvr_t::navsel)
        .def_readwrite("nsbs",&rtksvr_t::nsbs)
        .def_readwrite("nsol",&rtksvr_t::nsol)
        .def_readwrite("rtk",&rtksvr_t::rtk)
        .def_readwrite("nav",&rtksvr_t::nav)
        .def_readwrite("tick",&rtksvr_t::tick)
        .def_readwrite("thread",&rtksvr_t::thread)
        .def_readwrite("cputime",&rtksvr_t::cputime)
        .def_readwrite("prcout",&rtksvr_t::prcout)
        .def_readwrite("nave",&rtksvr_t::nave)
        .def_readwrite("bl_reset",&rtksvr_t::bl_reset)
        .def_readwrite("lock",&rtksvr_t::lock)
        .def_property_readonly("nmeapos",[](rtksvr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.nmeapos,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("format",[](rtksvr_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.format,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("solopt",[](rtksvr_t& o) {Arr1D<solopt_t>* tmp = new Arr1D<solopt_t>(o.solopt,2);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("nb",[](rtksvr_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.nb,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("nsb",[](rtksvr_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.nsb,2);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("npb",[](rtksvr_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.npb,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("buff",[](rtksvr_t& o) {Arr2D<uint8_t>* tmp = new Arr2D<uint8_t>(o.buff,-1,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("sbuf",[](rtksvr_t& o) {Arr2D<uint8_t>* tmp = new Arr2D<uint8_t>(o.sbuf,-1,2);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("pbuf",[](rtksvr_t& o) {Arr2D<uint8_t>* tmp = new Arr2D<uint8_t>(o.pbuf,-1,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("solbuf",[](rtksvr_t& o) {Arr1D<sol_t>* tmp = new Arr1D<sol_t>(o.solbuf,MAXSOLBUF);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("nmsg",[](rtksvr_t& o) {Arr2D<uint32_t>* tmp = new Arr2D<uint32_t>(o.nmsg,3,10);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("raw",[](rtksvr_t& o) {Arr1D<raw_t>* tmp = new Arr1D<raw_t>(o.raw,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("rtcm",[](rtksvr_t& o) {Arr1D<rtcm_t>* tmp = new Arr1D<rtcm_t>(o.rtcm,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ftime",[](rtksvr_t& o) {Arr1D<gtime_t>* tmp = new Arr1D<gtime_t>(o.ftime,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("files",[](rtksvr_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.files,3,MAXSTRPATH);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("obs",[](rtksvr_t& o) {Arr2D<obs_t>* tmp = new Arr2D<obs_t>(o.obs,3,MAXOBSBUF);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("sbsmsg",[](rtksvr_t& o) {Arr1D<sbsmsg_t>* tmp = new Arr1D<sbsmsg_t>(o.sbsmsg,MAXSBSMSG);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("stream",[](rtksvr_t& o) {Arr1D<stream_t>* tmp = new Arr1D<stream_t>(o.stream,8);return tmp;},py::return_value_policy::reference)
        .def_property("moni",[](rtksvr_t& o) {Arr1D<stream_t>* tmp = new Arr1D<stream_t>(o.moni,-1);return tmp;},[](rtksvr_t& o,Arr1D<stream_t>arr){o.moni=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("rb_ave",[](rtksvr_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.rb_ave,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("cmds_periodic",[](rtksvr_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.cmds_periodic,3,MAXRCVCMD);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("cmd_reset",[](rtksvr_t& o) {Arr1D<char>* tmp = new Arr1D<char>(o.cmd_reset,MAXRCVCMD);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](rtksvr_t& o){return &o;},py::return_value_policy::reference);

    py::class_<gis_pnt_t>(m,"gis_pnt_t").def(py::init())
        .def_property_readonly("pos",[](gis_pnt_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.pos,3);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](gis_pnt_t& o){return &o;},py::return_value_policy::reference);

    py::class_<gis_poly_t>(m,"gis_poly_t").def(py::init())
        .def_readwrite("npnt",&gis_poly_t::npnt)
        .def_property_readonly("bound",[](gis_poly_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.bound,4);return tmp;},py::return_value_policy::reference)
        .def_property("pos",[](gis_poly_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.pos,-1);return tmp;},[](gis_poly_t& o,Arr1D<double>arr){o.pos=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](gis_poly_t& o){return &o;},py::return_value_policy::reference);

    py::class_<gis_polygon_t>(m,"gis_polygon_t").def(py::init())
        .def_readwrite("npnt",&gis_polygon_t::npnt)
        .def_property_readonly("bound",[](gis_polygon_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.bound,4);return tmp;},py::return_value_policy::reference)
        .def_property("pos",[](gis_polygon_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.pos,-1);return tmp;},[](gis_polygon_t& o,Arr1D<double>arr){o.pos=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](gis_polygon_t& o){return &o;},py::return_value_policy::reference);

    py::class_<gisd_t>(m,"gisd_t").def(py::init())
        .def_readwrite("type",&gisd_t::type)
        .def_property("data",[](gisd_t& o) {Arr1D<void>* tmp = new Arr1D<void>(o.data,-1);return tmp;},[](gisd_t& o,Arr1D<void>arr){o.data=arr.src;},py::return_value_policy::reference)
        .def_property("next",[](gisd_t& o) {Arr1D<gisd_t>* tmp = new Arr1D<gisd_t>(o.next,-1);return tmp;},[](gisd_t& o,Arr1D<gisd_t>arr){o.next=arr.src;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](gisd_t& o){return &o;},py::return_value_policy::reference);

    py::class_<gis_t>(m,"gis_t").def(py::init())
        .def_property_readonly("name",[](gis_t& o) {Arr2D<char>* tmp = new Arr2D<char>(o.name,MAXGISLAYER,256);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("flag",[](gis_t& o) {Arr1D<int>* tmp = new Arr1D<int>(o.flag,MAXGISLAYER);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("data",[](gis_t& o) {Arr2D<gisd_t>* tmp = new Arr2D<gisd_t>(o.data,-1,MAXGISLAYER);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("bound",[](gis_t& o) {Arr1D<double>* tmp = new Arr1D<double>(o.bound,4);return tmp;},py::return_value_policy::reference)
        .def_property_readonly("ptr",[](gis_t& o){return &o;},py::return_value_policy::reference);

    m.attr("chisqr") = new Arr1D<double>((void*)chisqr,-1);
    m.attr("igpband1") = new Arr2D<sbsigpband_t>((void*)igpband1,9,8);
    m.attr("igpband2") = new Arr2D<sbsigpband_t>((void*)igpband2,2,5);
    m.attr("formatstrs") = new Arr2D<char>((void*)formatstrs,-1,-1);
    m.attr("sysopts") = new Arr1D<opt_t>((void*)sysopts,-1);
    m.attr("prcopt_default") = new prcopt_t(prcopt_default);
    m.attr("solopt_default") = new solopt_t(solopt_default);
    m.def("satsys",static_cast<int(*)(int sat,Arr1D<int> Sprn)>(&satsys),"rtklib satsys");
    m.def("satno2id",static_cast<void(*)(int sat,Arr1D<char> Sid)>(&satno2id),"rtklib satno2id");
    m.def("dot",static_cast<double(*)(Arr1D<double> Sa,Arr1D<double> Sb, int n)>(&dot),"rtklib dot");
    m.def("norm",static_cast<double(*)(Arr1D<double> Sa, int n)>(&norm),"rtklib norm");
    m.def("cross3",static_cast<void(*)(Arr1D<double> Sa,Arr1D<double> Sb,Arr1D<double> Sc)>(&cross3),"rtklib cross3");
    m.def("normv3",static_cast<int(*)(Arr1D<double> Sa,Arr1D<double> Sb)>(&normv3),"rtklib normv3");
    m.def("matcpy",static_cast<void(*)(Arr1D<double> SA,Arr1D<double> SB, int n, int m)>(&matcpy),"rtklib matcpy");
    m.def("matmul",static_cast<void(*)(const char *tr, int n, int k, int m, double alpha,Arr1D<double> SA,Arr1D<double> SB, double beta,Arr1D<double> SC)>(&matmul),"rtklib matmul");
    m.def("matinv",static_cast<int(*)(Arr1D<double> SA, int n)>(&matinv),"rtklib matinv");
    m.def("solve",static_cast<int(*)(const char *tr,Arr1D<double> SA,Arr1D<double> SY, int n, int m,Arr1D<double> SX)>(&solve),"rtklib solve");
    m.def("lsq",static_cast<int(*)(Arr1D<double> SA,Arr1D<double> Sy, int n, int m,Arr1D<double> Sx,Arr1D<double> SQ)>(&lsq),"rtklib lsq");
    m.def("filter",static_cast<int(*)(Arr1D<double> Sx,Arr1D<double> SP,Arr1D<double> SH,Arr1D<double> Sv,Arr1D<double> SR, int n, int m)>(&filter),"rtklib filter");
    m.def("smoother",static_cast<int(*)(Arr1D<double> Sxf,Arr1D<double> SQf,Arr1D<double> Sxb,Arr1D<double> SQb, int n,Arr1D<double> Sxs,Arr1D<double> SQs)>(&smoother),"rtklib smoother");
    m.def("matprint",static_cast<void(*)(Arr1D<double> SA, int n, int m, int p, int q)>(&matprint),"rtklib matprint");
    m.def("matfprint",static_cast<void(*)(Arr1D<double> SA, int n, int m, int p, int q, const char *Ffp, const char *mode)>(&matfprint),"rtklib matfprint");
    m.def("time2str",static_cast<void(*)(gtime_t t,Arr1D<char> Sstr, int n)>(&time2str),"rtklib time2str");
    m.def("epoch2time",static_cast<gtime_t(*)(Arr1D<double> Sep)>(&epoch2time),"rtklib epoch2time");
    m.def("time2epoch",static_cast<void(*)(gtime_t t,Arr1D<double> Sep)>(&time2epoch),"rtklib time2epoch");
    m.def("time2gpst",static_cast<double(*)(gtime_t t,Arr1D<int> Sweek)>(&time2gpst),"rtklib time2gpst");
    m.def("time2gst",static_cast<double(*)(gtime_t t,Arr1D<int> Sweek)>(&time2gst),"rtklib time2gst");
    m.def("time2bdt",static_cast<double(*)(gtime_t t,Arr1D<int> Sweek)>(&time2bdt),"rtklib time2bdt");
    m.def("reppath",static_cast<int(*)(const char *path,Arr1D<char> Srpath, gtime_t time, const char *rov, const char *base)>(&reppath),"rtklib reppath");
    m.def("reppaths",static_cast<int(*)(const char *path,std::vector<std::string> Drpaths, int nmax, gtime_t ts, gtime_t te, const char *rov, const char *base)>(&reppaths),"rtklib reppaths");
    m.def("ecef2pos",static_cast<void(*)(Arr1D<double> Sr,Arr1D<double> Spos)>(&ecef2pos),"rtklib ecef2pos");
    m.def("pos2ecef",static_cast<void(*)(Arr1D<double> Spos,Arr1D<double> Sr)>(&pos2ecef),"rtklib pos2ecef");
    m.def("ecef2enu",static_cast<void(*)(Arr1D<double> Spos,Arr1D<double> Sr,Arr1D<double> Se)>(&ecef2enu),"rtklib ecef2enu");
    m.def("enu2ecef",static_cast<void(*)(Arr1D<double> Spos,Arr1D<double> Se,Arr1D<double> Sr)>(&enu2ecef),"rtklib enu2ecef");
    m.def("covenu",static_cast<void(*)(Arr1D<double> Spos,Arr1D<double> SP,Arr1D<double> SQ)>(&covenu),"rtklib covenu");
    m.def("covecef",static_cast<void(*)(Arr1D<double> Spos,Arr1D<double> SQ,Arr1D<double> SP)>(&covecef),"rtklib covecef");
    m.def("xyz2enu",static_cast<void(*)(Arr1D<double> Spos,Arr1D<double> SE)>(&xyz2enu),"rtklib xyz2enu");
    m.def("eci2ecef",static_cast<void(*)(gtime_t tutc,Arr1D<double> Serpv,Arr1D<double> SU,Arr1D<double> Sgmst)>(&eci2ecef),"rtklib eci2ecef");
    m.def("deg2dms",static_cast<void(*)(double deg,Arr1D<double> Sdms, int ndec)>(&deg2dms),"rtklib deg2dms");
    m.def("dms2deg",static_cast<double(*)(Arr1D<double> Sdms)>(&dms2deg),"rtklib dms2deg");
    m.def("readpos",static_cast<void(*)(const char *file, const char *rcv,Arr1D<double> Spos)>(&readpos),"rtklib readpos");
    m.def("readblq",static_cast<int(*)(const char *file, const char *sta,Arr1D<double> Sodisp)>(&readblq),"rtklib readblq");
    m.def("geterp",static_cast<int(*)(const erp_t *erp, gtime_t time,Arr1D<double> Sval)>(&geterp),"rtklib geterp");
    m.def("tracemat",static_cast<void(*)(int level,Arr1D<double> SA, int n, int m, int p, int q)>(&tracemat),"rtklib tracemat");
    m.def("traceb",static_cast<void(*)(int level,Arr1D<uint8_t> Sp, int n)>(&traceb),"rtklib traceb");
    m.def("expath",static_cast<int(*)(const char *path,std::vector<std::string> Dpaths, int nmax)>(&expath),"rtklib expath");
    m.def("satazel",static_cast<double(*)(Arr1D<double> Spos,Arr1D<double> Se,Arr1D<double> Sazel)>(&satazel),"rtklib satazel");
    m.def("geodist",static_cast<double(*)(Arr1D<double> Srs,Arr1D<double> Srr,Arr1D<double> Se)>(&geodist),"rtklib geodist");
    m.def("dops",static_cast<void(*)(int ns,Arr1D<double> Sazel, double elmin,Arr1D<double> Sdop)>(&dops),"rtklib dops");
    m.def("ionmodel",static_cast<double(*)(gtime_t t,Arr1D<double> Sion,Arr1D<double> Spos,Arr1D<double> Sazel)>(&ionmodel),"rtklib ionmodel");
    m.def("ionmapf",static_cast<double(*)(Arr1D<double> Spos,Arr1D<double> Sazel)>(&ionmapf),"rtklib ionmapf");
    m.def("ionppp",static_cast<double(*)(Arr1D<double> Spos,Arr1D<double> Sazel, double re, double hion,Arr1D<double> Spppos)>(&ionppp),"rtklib ionppp");
    m.def("tropmodel",static_cast<double(*)(gtime_t time,Arr1D<double> Spos,Arr1D<double> Sazel, double humi)>(&tropmodel),"rtklib tropmodel");
    m.def("tropmapf",static_cast<double(*)(gtime_t time,Arr1D<double> Spos,Arr1D<double> Sazel,Arr1D<double> Smapfw)>(&tropmapf),"rtklib tropmapf");
    m.def("iontec",static_cast<int(*)(gtime_t time, const nav_t *nav,Arr1D<double> Spos,Arr1D<double> Sazel, int opt,Arr1D<double> Sdelay,Arr1D<double> Svar)>(&iontec),"rtklib iontec");
    m.def("ionocorr",static_cast<int(*)(gtime_t time, const nav_t *nav, int sat,Arr1D<double> Spos,Arr1D<double> Sazel, int ionoopt,Arr1D<double> Sion,Arr1D<double> Svar)>(&ionocorr),"rtklib ionocorr");
    m.def("tropcorr",static_cast<int(*)(gtime_t time, const nav_t *nav,Arr1D<double> Spos,Arr1D<double> Sazel, int tropopt,Arr1D<double> Strp,Arr1D<double> Svar)>(&tropcorr),"rtklib tropcorr");
    m.def("antmodel",static_cast<void(*)(const pcv_t *pcv,Arr1D<double> Sdel,Arr1D<double> Sazel, int opt,Arr1D<double> Sdant)>(&antmodel),"rtklib antmodel");
    m.def("antmodel_s",static_cast<void(*)(const pcv_t *pcv, double nadir,Arr1D<double> Sdant)>(&antmodel_s),"rtklib antmodel_s");
    m.def("sunmoonpos",static_cast<void(*)(gtime_t tutc,Arr1D<double> Serpv,Arr1D<double> Srsun,Arr1D<double> Srmoon,Arr1D<double> Sgmst)>(&sunmoonpos),"rtklib sunmoonpos");
    m.def("tidedisp",static_cast<void(*)(gtime_t tutc,Arr1D<double> Srr, int opt, const erp_t *erp,Arr1D<double> Sodisp,Arr1D<double> Sdr)>(&tidedisp),"rtklib tidedisp");
    m.def("geoidh",static_cast<double(*)(Arr1D<double> Spos)>(&geoidh),"rtklib geoidh");
    m.def("tokyo2jgd",static_cast<int(*)(Arr1D<double> Spos)>(&tokyo2jgd),"rtklib tokyo2jgd");
    m.def("jgd2tokyo",static_cast<int(*)(Arr1D<double> Spos)>(&jgd2tokyo),"rtklib jgd2tokyo");
    m.def("outrnxobsh",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav)>(&outrnxobsh),"rtklib outrnxobsh");
    m.def("outrnxobsb",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const obsd_t *obs, int n, int epflag)>(&outrnxobsb),"rtklib outrnxobsb");
    m.def("outrnxnavh",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav)>(&outrnxnavh),"rtklib outrnxnavh");
    m.def("outrnxgnavh",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav)>(&outrnxgnavh),"rtklib outrnxgnavh");
    m.def("outrnxhnavh",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav)>(&outrnxhnavh),"rtklib outrnxhnavh");
    m.def("outrnxlnavh",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav)>(&outrnxlnavh),"rtklib outrnxlnavh");
    m.def("outrnxqnavh",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav)>(&outrnxqnavh),"rtklib outrnxqnavh");
    m.def("outrnxcnavh",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav)>(&outrnxcnavh),"rtklib outrnxcnavh");
    m.def("outrnxinavh",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const nav_t *nav)>(&outrnxinavh),"rtklib outrnxinavh");
    m.def("outrnxnavb",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const eph_t *eph)>(&outrnxnavb),"rtklib outrnxnavb");
    m.def("outrnxgnavb",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const geph_t *geph)>(&outrnxgnavb),"rtklib outrnxgnavb");
    m.def("outrnxhnavb",static_cast<int(*)(const char *Ffp, const char *mode, const rnxopt_t *opt, const seph_t *seph)>(&outrnxhnavb),"rtklib outrnxhnavb");
    m.def("rtk_uncompress",static_cast<int(*)(const char *file,Arr1D<char> Suncfile)>(&rtk_uncompress),"rtklib rtk_uncompress");
    m.def("convrnx",static_cast<int(*)(int format, rnxopt_t *opt, const char *file,std::vector<std::string> Dofile)>(&convrnx),"rtklib convrnx");
    m.def("open_rnxctr",static_cast<int(*)(rnxctr_t *rnx, const char *Ffp, const char *mode)>(&open_rnxctr),"rtklib open_rnxctr");
    m.def("input_rnxctr",static_cast<int(*)(rnxctr_t *rnx, const char *Ffp, const char *mode)>(&input_rnxctr),"rtklib input_rnxctr");
    m.def("eph2pos",static_cast<void(*)(gtime_t time, const eph_t  *eph,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar)>(&eph2pos),"rtklib eph2pos");
    m.def("geph2pos",static_cast<void(*)(gtime_t time, const geph_t *geph,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar)>(&geph2pos),"rtklib geph2pos");
    m.def("seph2pos",static_cast<void(*)(gtime_t time, const seph_t *seph,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar)>(&seph2pos),"rtklib seph2pos");
    m.def("peph2pos",static_cast<int(*)(gtime_t time, int sat, const nav_t *nav, int opt,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar)>(&peph2pos),"rtklib peph2pos");
    m.def("satantoff",static_cast<void(*)(gtime_t time,Arr1D<double> Srs, int sat, const nav_t *nav,Arr1D<double> Sdant)>(&satantoff),"rtklib satantoff");
    m.def("satpos",static_cast<int(*)(gtime_t time, gtime_t teph, int sat, int ephopt, const nav_t *nav,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar,Arr1D<int> Ssvh)>(&satpos),"rtklib satpos");
    m.def("satposs",static_cast<void(*)(gtime_t time, const obsd_t *obs, int n, const nav_t *nav, int sateph,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar,Arr1D<int> Ssvh)>(&satposs),"rtklib satposs");
    m.def("alm2pos",static_cast<void(*)(gtime_t time, const alm_t *alm,Arr1D<double> Srs,Arr1D<double> Sdts)>(&alm2pos),"rtklib alm2pos");
    m.def("tle_pos",static_cast<int(*)(gtime_t time, const char *name, const char *satno, const char *desig, const tle_t *tle, const erp_t *erp,Arr1D<double> Srs)>(&tle_pos),"rtklib tle_pos");
    m.def("getbitu",static_cast<uint32_t(*)(Arr1D<uint8_t> Sbuff, int pos, int len)>(&getbitu),"rtklib getbitu");
    m.def("getbits",static_cast<int32_t(*)(Arr1D<uint8_t> Sbuff, int pos, int len)>(&getbits),"rtklib getbits");
    m.def("setbitu",static_cast<void(*)(Arr1D<uint8_t> Sbuff, int pos, int len, uint32_t data)>(&setbitu),"rtklib setbitu");
    m.def("setbits",static_cast<void(*)(Arr1D<uint8_t> Sbuff, int pos, int len, int32_t  data)>(&setbits),"rtklib setbits");
    m.def("rtk_crc32",static_cast<uint32_t(*)(Arr1D<uint8_t> Sbuff, int len)>(&rtk_crc32),"rtklib rtk_crc32");
    m.def("rtk_crc24q",static_cast<uint32_t(*)(Arr1D<uint8_t> Sbuff, int len)>(&rtk_crc24q),"rtklib rtk_crc24q");
    m.def("rtk_crc16",static_cast<uint16_t(*)(Arr1D<uint8_t> Sbuff, int len)>(&rtk_crc16),"rtklib rtk_crc16");
    m.def("decode_word",static_cast<int(*)(uint32_t word,Arr1D<uint8_t> Sdata)>(&decode_word),"rtklib decode_word");
    m.def("decode_frame",static_cast<int(*)(Arr1D<uint8_t> Sbuff, eph_t *eph, alm_t *alm,Arr1D<double> Sion,Arr1D<double> Sutc)>(&decode_frame),"rtklib decode_frame");
    m.def("test_glostr",static_cast<int(*)(Arr1D<uint8_t> Sbuff)>(&test_glostr),"rtklib test_glostr");
    m.def("decode_glostr",static_cast<int(*)(Arr1D<uint8_t> Sbuff, geph_t *geph,Arr1D<double> Sutc)>(&decode_glostr),"rtklib decode_glostr");
    m.def("decode_bds_d1",static_cast<int(*)(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sion,Arr1D<double> Sutc)>(&decode_bds_d1),"rtklib decode_bds_d1");
    m.def("decode_bds_d2",static_cast<int(*)(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sutc)>(&decode_bds_d2),"rtklib decode_bds_d2");
    m.def("decode_gal_inav",static_cast<int(*)(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sion,Arr1D<double> Sutc)>(&decode_gal_inav),"rtklib decode_gal_inav");
    m.def("decode_gal_fnav",static_cast<int(*)(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sion,Arr1D<double> Sutc)>(&decode_gal_fnav),"rtklib decode_gal_fnav");
    m.def("decode_irn_nav",static_cast<int(*)(Arr1D<uint8_t> Sbuff, eph_t *eph,Arr1D<double> Sion,Arr1D<double> Sutc)>(&decode_irn_nav),"rtklib decode_irn_nav");
    m.def("input_rawf",static_cast<int(*)(raw_t *raw, int format, const char *Ffp, const char *mode)>(&input_rawf),"rtklib input_rawf");
    m.def("input_oem4f",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_oem4f),"rtklib input_oem4f");
    m.def("input_oem3f",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_oem3f),"rtklib input_oem3f");
    m.def("input_ubxf",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_ubxf),"rtklib input_ubxf");
    m.def("input_ss2f",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_ss2f),"rtklib input_ss2f");
    m.def("input_cresf",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_cresf),"rtklib input_cresf");
    m.def("input_stqf",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_stqf),"rtklib input_stqf");
    m.def("input_javadf",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_javadf),"rtklib input_javadf");
    m.def("input_nvsf",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_nvsf),"rtklib input_nvsf");
    m.def("input_bnxf",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_bnxf),"rtklib input_bnxf");
    m.def("input_rt17f",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_rt17f),"rtklib input_rt17f");
    m.def("input_sbff",static_cast<int(*)(raw_t *raw, const char *Ffp, const char *mode)>(&input_sbff),"rtklib input_sbff");
    m.def("gen_ubx",static_cast<int(*)(const char *msg,Arr1D<uint8_t> Sbuff)>(&gen_ubx),"rtklib gen_ubx");
    m.def("gen_stq",static_cast<int(*)(const char *msg,Arr1D<uint8_t> Sbuff)>(&gen_stq),"rtklib gen_stq");
    m.def("gen_nvs",static_cast<int(*)(const char *msg,Arr1D<uint8_t> Sbuff)>(&gen_nvs),"rtklib gen_nvs");
    m.def("input_rtcm2f",static_cast<int(*)(rtcm_t *rtcm, const char *Ffp, const char *mode)>(&input_rtcm2f),"rtklib input_rtcm2f");
    m.def("input_rtcm3f",static_cast<int(*)(rtcm_t *rtcm, const char *Ffp, const char *mode)>(&input_rtcm3f),"rtklib input_rtcm3f");
    m.def("readsol",static_cast<int(*)(std::vector<std::string> Dfiles, int nfile, solbuf_t *sol)>(&readsol),"rtklib readsol");
    m.def("readsolt",static_cast<int(*)(std::vector<std::string> Dfiles, int nfile, gtime_t ts, gtime_t te, double tint, int qflag, solbuf_t *sol)>(&readsolt),"rtklib readsolt");
    m.def("readsolstat",static_cast<int(*)(std::vector<std::string> Dfiles, int nfile, solstatbuf_t *statbuf)>(&readsolstat),"rtklib readsolstat");
    m.def("readsolstatt",static_cast<int(*)(std::vector<std::string> Dfiles, int nfile, gtime_t ts, gtime_t te, double tint, solstatbuf_t *statbuf)>(&readsolstatt),"rtklib readsolstatt");
    m.def("outprcopts",static_cast<int(*)(Arr1D<uint8_t> Sbuff, const prcopt_t *opt)>(&outprcopts),"rtklib outprcopts");
    m.def("outsolheads",static_cast<int(*)(Arr1D<uint8_t> Sbuff, const solopt_t *opt)>(&outsolheads),"rtklib outsolheads");
    m.def("outsols",static_cast<int(*)(Arr1D<uint8_t> Sbuff, const sol_t *sol,Arr1D<double> Srb, const solopt_t *opt)>(&outsols),"rtklib outsols");
    m.def("outsolexs",static_cast<int(*)(Arr1D<uint8_t> Sbuff, const sol_t *sol, const ssat_t *ssat, const solopt_t *opt)>(&outsolexs),"rtklib outsolexs");
    m.def("outprcopt",static_cast<void(*)(const char *Ffp, const char *mode, const prcopt_t *opt)>(&outprcopt),"rtklib outprcopt");
    m.def("outsolhead",static_cast<void(*)(const char *Ffp, const char *mode, const solopt_t *opt)>(&outsolhead),"rtklib outsolhead");
    m.def("outsol",static_cast<void(*)(const char *Ffp, const char *mode, const sol_t *sol,Arr1D<double> Srb, const solopt_t *opt)>(&outsol),"rtklib outsol");
    m.def("outsolex",static_cast<void(*)(const char *Ffp, const char *mode, const sol_t *sol, const ssat_t *ssat, const solopt_t *opt)>(&outsolex),"rtklib outsolex");
    m.def("outnmea_rmc",static_cast<int(*)(Arr1D<uint8_t> Sbuff, const sol_t *sol)>(&outnmea_rmc),"rtklib outnmea_rmc");
    m.def("outnmea_gga",static_cast<int(*)(Arr1D<uint8_t> Sbuff, const sol_t *sol)>(&outnmea_gga),"rtklib outnmea_gga");
    m.def("outnmea_gsa",static_cast<int(*)(Arr1D<uint8_t> Sbuff, const sol_t *sol, const ssat_t *ssat)>(&outnmea_gsa),"rtklib outnmea_gsa");
    m.def("outnmea_gsv",static_cast<int(*)(Arr1D<uint8_t> Sbuff, const sol_t *sol, const ssat_t *ssat)>(&outnmea_gsv),"rtklib outnmea_gsv");
    m.def("convkml",static_cast<int(*)(const char *infile, const char *outfile, gtime_t ts, gtime_t te, double tint, int qflg,Arr1D<double> Soffset, int tcolor, int pcolor, int outalt, int outtime)>(&convkml),"rtklib convkml");
    m.def("convgpx",static_cast<int(*)(const char *infile, const char *outfile, gtime_t ts, gtime_t te, double tint, int qflg,Arr1D<double> Soffset, int outtrk, int outpnt, int outalt, int outtime)>(&convgpx),"rtklib convgpx");
    m.def("sbsoutmsg",static_cast<void(*)(const char *Ffp, const char *mode, sbsmsg_t *sbsmsg)>(&sbsoutmsg),"rtklib sbsoutmsg");
    m.def("sbsdecodemsg",static_cast<int(*)(gtime_t time, int prn,Arr1D<uint32_t> Swords, sbsmsg_t *sbsmsg)>(&sbsdecodemsg),"rtklib sbsdecodemsg");
    m.def("sbssatcorr",static_cast<int(*)(gtime_t time, int sat, const nav_t *nav,Arr1D<double> Srs,Arr1D<double> Sdts,Arr1D<double> Svar)>(&sbssatcorr),"rtklib sbssatcorr");
    m.def("sbsioncorr",static_cast<int(*)(gtime_t time, const nav_t *nav,Arr1D<double> Spos,Arr1D<double> Sazel,Arr1D<double> Sdelay,Arr1D<double> Svar)>(&sbsioncorr),"rtklib sbsioncorr");
    m.def("sbstropcorr",static_cast<double(*)(gtime_t time,Arr1D<double> Spos,Arr1D<double> Sazel,Arr1D<double> Svar)>(&sbstropcorr),"rtklib sbstropcorr");
    m.def("opt2str",static_cast<int(*)(const opt_t *opt,Arr1D<char> Sstr)>(&opt2str),"rtklib opt2str");
    m.def("opt2buf",static_cast<int(*)(const opt_t *opt,Arr1D<char> Sbuff)>(&opt2buf),"rtklib opt2buf");
    m.def("strread",static_cast<int(*)(stream_t *stream,Arr1D<uint8_t> Sbuff, int n)>(&strread),"rtklib strread");
    m.def("strwrite",static_cast<int(*)(stream_t *stream,Arr1D<uint8_t> Sbuff, int n)>(&strwrite),"rtklib strwrite");
    m.def("strstat",static_cast<int(*)(stream_t *stream,Arr1D<char> Smsg)>(&strstat),"rtklib strstat");
    m.def("strstatx",static_cast<int(*)(stream_t *stream,Arr1D<char> Smsg)>(&strstatx),"rtklib strstatx");
    m.def("strsum",static_cast<void(*)(stream_t *stream,Arr1D<int> Sinb,Arr1D<int> Sinr,Arr1D<int> Soutb,Arr1D<int> Soutr)>(&strsum),"rtklib strsum");
    m.def("strsetopt",static_cast<void(*)(Arr1D<int> Sopt)>(&strsetopt),"rtklib strsetopt");
    m.def("lambda",static_cast<int(*)(int n, int m,Arr1D<double> Sa,Arr1D<double> SQ,Arr1D<double> SF,Arr1D<double> Ss)>(&lambda),"rtklib lambda");
    m.def("lambda_reduction",static_cast<int(*)(int n,Arr1D<double> SQ,Arr1D<double> SZ)>(&lambda_reduction),"rtklib lambda_reduction");
    m.def("lambda_search",static_cast<int(*)(int n, int m,Arr1D<double> Sa,Arr1D<double> SQ,Arr1D<double> SF,Arr1D<double> Ss)>(&lambda_search),"rtklib lambda_search");
    m.def("pntpos",static_cast<int(*)(const obsd_t *obs, int n, const nav_t *nav, const prcopt_t *opt, sol_t *sol,Arr1D<double> Sazel, ssat_t *ssat,Arr1D<char> Smsg)>(&pntpos),"rtklib pntpos");
    m.def("rtkoutstat",static_cast<int(*)(rtk_t *rtk,Arr1D<char> Sbuff)>(&rtkoutstat),"rtklib rtkoutstat");
    m.def("pppoutstat",static_cast<int(*)(rtk_t *rtk,Arr1D<char> Sbuff)>(&pppoutstat),"rtklib pppoutstat");
    m.def("ppp_ar",static_cast<int(*)(rtk_t *rtk, const obsd_t *obs, int n,Arr1D<int> Sexc, const nav_t *nav,Arr1D<double> Sazel,Arr1D<double> Sx,Arr1D<double> SP)>(&ppp_ar),"rtklib ppp_ar");
    m.def("postpos",static_cast<int(*)(gtime_t ts, gtime_t te, double ti, double tu, const prcopt_t *popt, const solopt_t *sopt, const filopt_t *fopt,std::vector<std::string> Dinfile, int n,Arr1D<char> Soutfile, const char *rov, const char *base)>(&postpos),"rtklib postpos");
    m.def("strsvrstart",static_cast<int(*)(strsvr_t *svr,Arr1D<int> Sopts,Arr1D<int> Sstrs,std::vector<std::string> Dpaths,std::vector<std::string> Dlogs,std::vector<std::vector<strconv_t>> Dconv,std::vector<std::string> Dcmds,std::vector<std::string> Dcmds_priodic,Arr1D<double> Snmeapos)>(&strsvrstart),"rtklib strsvrstart");
    m.def("strsvrstop",static_cast<void(*)(strsvr_t *svr,std::vector<std::string> Dcmds)>(&strsvrstop),"rtklib strsvrstop");
    m.def("strsvrstat",static_cast<void(*)(strsvr_t *svr,Arr1D<int> Sstat,Arr1D<int> Slog_stat,Arr1D<int> Sbyte,Arr1D<int> Sbps,Arr1D<char> Smsg)>(&strsvrstat),"rtklib strsvrstat");
    m.def("rtksvrstart",static_cast<int(*)(rtksvr_t *svr, int cycle, int buffsize,Arr1D<int> Sstrs,std::vector<std::string> Dpaths,Arr1D<int> Sformats, int navsel,std::vector<std::string> Dcmds,std::vector<std::string> Dcmds_periodic,std::vector<std::string> Drcvopts, int nmeacycle, int nmeareq,Arr1D<double> Snmeapos, prcopt_t *prcopt, solopt_t *solopt, stream_t *moni,Arr1D<char> Serrmsg)>(&rtksvrstart),"rtklib rtksvrstart");
    m.def("rtksvrstop",static_cast<void(*)(rtksvr_t *svr,std::vector<std::string> Dcmds)>(&rtksvrstop),"rtklib rtksvrstop");
    m.def("rtksvrostat",static_cast<int(*)(rtksvr_t *svr, int type, gtime_t *time,Arr1D<int> Ssat,Arr1D<double> Saz,Arr1D<double> Sel,std::vector<std::vector<int>> Dsnr,Arr1D<int> Svsat)>(&rtksvrostat),"rtklib rtksvrostat");
    m.def("rtksvrsstat",static_cast<void(*)(rtksvr_t *svr,Arr1D<int> Ssstat,Arr1D<char> Smsg)>(&rtksvrsstat),"rtklib rtksvrsstat");
    m.def("dl_readurls",static_cast<int(*)(const char *file,std::vector<std::string> Dtypes, int ntype, url_t *urls, int nmax)>(&dl_readurls),"rtklib dl_readurls");
    m.def("dl_readstas",static_cast<int(*)(const char *file,std::vector<std::string> Dstas, int nmax)>(&dl_readstas),"rtklib dl_readstas");
    m.def("dl_exec",static_cast<int(*)(gtime_t ts, gtime_t te, double ti, int seqnos, int seqnoe, const url_t *urls, int nurl,std::vector<std::string> Dstas, int nsta, const char *dir, const char *usr, const char *pwd, const char *proxy, int opts,Arr1D<char> Smsg, const char *Ffp, const char *mode)>(&dl_exec),"rtklib dl_exec");
    m.def("dl_test",static_cast<void(*)(gtime_t ts, gtime_t te, double ti, const url_t *urls, int nurl,std::vector<std::string> Dstas, int nsta, const char *dir, int ncol, int datefmt, const char *Ffp, const char *mode)>(&dl_test),"rtklib dl_test");
    m.def("satno",&satno,"rtklib satno");
    m.def("satid2no",&satid2no,"rtklib satid2no");
    m.def("obs2code",&obs2code,"rtklib obs2code");
    m.def("code2obs",&code2obs,"rtklib code2obs");
    m.def("code2freq",&code2freq,"rtklib code2freq");
    m.def("sat2freq",&sat2freq,"rtklib sat2freq");
    m.def("code2idx",&code2idx,"rtklib code2idx");
    m.def("satexclude",&satexclude,"rtklib satexclude");
    m.def("testsnr",&testsnr,"rtklib testsnr");
    m.def("setcodepri",&setcodepri,"rtklib setcodepri");
    m.def("getcodepri",&getcodepri,"rtklib getcodepri");
    m.def("mat",&mat,"rtklib mat");
    m.def("imat",&imat,"rtklib imat");
    m.def("zeros",&zeros,"rtklib zeros");
    m.def("eye",&eye,"rtklib eye");
    m.def("str2num",&str2num,"rtklib str2num");
    m.def("str2time",&str2time,"rtklib str2time");
    m.def("gpst2time",&gpst2time,"rtklib gpst2time");
    m.def("gst2time",&gst2time,"rtklib gst2time");
    m.def("bdt2time",&bdt2time,"rtklib bdt2time");
    m.def("time_str",&time_str,"rtklib time_str");
    m.def("timeadd",&timeadd,"rtklib timeadd");
    m.def("timediff",&timediff,"rtklib timediff");
    m.def("gpst2utc",&gpst2utc,"rtklib gpst2utc");
    m.def("utc2gpst",&utc2gpst,"rtklib utc2gpst");
    m.def("gpst2bdt",&gpst2bdt,"rtklib gpst2bdt");
    m.def("bdt2gpst",&bdt2gpst,"rtklib bdt2gpst");
    m.def("timeget",&timeget,"rtklib timeget");
    m.def("timeset",&timeset,"rtklib timeset");
    m.def("timereset",&timereset,"rtklib timereset");
    m.def("time2doy",&time2doy,"rtklib time2doy");
    m.def("utc2gmst",&utc2gmst,"rtklib utc2gmst");
    m.def("read_leaps",&read_leaps,"rtklib read_leaps");
    m.def("adjgpsweek",&adjgpsweek,"rtklib adjgpsweek");
    m.def("tickget",&tickget,"rtklib tickget");
    m.def("sleepms",&sleepms,"rtklib sleepms");
    m.def("sortobs",&sortobs,"rtklib sortobs");
    m.def("uniqnav",&uniqnav,"rtklib uniqnav");
    m.def("screent",&screent,"rtklib screent");
    m.def("readnav",&readnav,"rtklib readnav");
    m.def("savenav",&savenav,"rtklib savenav");
    m.def("freeobs",&freeobs,"rtklib freeobs");
    m.def("freenav",&freenav,"rtklib freenav");
    m.def("readerp",&readerp,"rtklib readerp");
    m.def("traceopen",&traceopen,"rtklib traceopen");
    m.def("traceclose",&traceclose,"rtklib traceclose");
    m.def("tracelevel",&tracelevel,"rtklib tracelevel");
    m.def("traceobs",&traceobs,"rtklib traceobs");
    m.def("tracenav",&tracenav,"rtklib tracenav");
    m.def("tracegnav",&tracegnav,"rtklib tracegnav");
    m.def("tracehnav",&tracehnav,"rtklib tracehnav");
    m.def("tracepeph",&tracepeph,"rtklib tracepeph");
    m.def("tracepclk",&tracepclk,"rtklib tracepclk");
    m.def("execcmd",&execcmd,"rtklib execcmd");
    m.def("createdir",&createdir,"rtklib createdir");
    m.def("readtec",&readtec,"rtklib readtec");
    m.def("readpcv",&readpcv,"rtklib readpcv");
    m.def("searchpcv",&searchpcv,"rtklib searchpcv");
    m.def("opengeoid",&opengeoid,"rtklib opengeoid");
    m.def("closegeoid",&closegeoid,"rtklib closegeoid");
    m.def("loaddatump",&loaddatump,"rtklib loaddatump");
    m.def("readrnx",&readrnx,"rtklib readrnx");
    m.def("readrnxt",&readrnxt,"rtklib readrnxt");
    m.def("readrnxc",&readrnxc,"rtklib readrnxc");
    m.def("init_rnxctr",&init_rnxctr,"rtklib init_rnxctr");
    m.def("free_rnxctr",&free_rnxctr,"rtklib free_rnxctr");
    m.def("eph2clk",&eph2clk,"rtklib eph2clk");
    m.def("geph2clk",&geph2clk,"rtklib geph2clk");
    m.def("seph2clk",&seph2clk,"rtklib seph2clk");
    m.def("setseleph",&setseleph,"rtklib setseleph");
    m.def("getseleph",&getseleph,"rtklib getseleph");
    m.def("readsp3",&readsp3,"rtklib readsp3");
    m.def("readsap",&readsap,"rtklib readsap");
    m.def("readdcb",&readdcb,"rtklib readdcb");
    //m.def("readfcb",&readfcb,"rtklib readfcb");
    m.def("tle_read",&tle_read,"rtklib tle_read");
    m.def("tle_name_read",&tle_name_read,"rtklib tle_name_read");
    m.def("init_raw",&init_raw,"rtklib init_raw");
    m.def("free_raw",&free_raw,"rtklib free_raw");
    m.def("input_raw",&input_raw,"rtklib input_raw");
    m.def("init_rt17",&init_rt17,"rtklib init_rt17");
    //m.def("init_cmr",&init_cmr,"rtklib init_cmr");
    m.def("free_rt17",&free_rt17,"rtklib free_rt17");
    //m.def("free_cmr",&free_cmr,"rtklib free_cmr");
    //m.def("update_cmr",&update_cmr,"rtklib update_cmr");
    m.def("input_oem4",&input_oem4,"rtklib input_oem4");
    m.def("input_oem3",&input_oem3,"rtklib input_oem3");
    m.def("input_ubx",&input_ubx,"rtklib input_ubx");
    m.def("input_ss2",&input_ss2,"rtklib input_ss2");
    m.def("input_cres",&input_cres,"rtklib input_cres");
    m.def("input_stq",&input_stq,"rtklib input_stq");
    m.def("input_javad",&input_javad,"rtklib input_javad");
    m.def("input_nvs",&input_nvs,"rtklib input_nvs");
    m.def("input_bnx",&input_bnx,"rtklib input_bnx");
    m.def("input_rt17",&input_rt17,"rtklib input_rt17");
    m.def("input_sbf",&input_sbf,"rtklib input_sbf");
    m.def("init_rtcm",&init_rtcm,"rtklib init_rtcm");
    m.def("free_rtcm",&free_rtcm,"rtklib free_rtcm");
    m.def("input_rtcm2",&input_rtcm2,"rtklib input_rtcm2");
    m.def("input_rtcm3",&input_rtcm3,"rtklib input_rtcm3");
    m.def("gen_rtcm2",&gen_rtcm2,"rtklib gen_rtcm2");
    m.def("gen_rtcm3",&gen_rtcm3,"rtklib gen_rtcm3");
    m.def("initsolbuf",&initsolbuf,"rtklib initsolbuf");
    m.def("freesolbuf",&freesolbuf,"rtklib freesolbuf");
    m.def("freesolstatbuf",&freesolstatbuf,"rtklib freesolstatbuf");
    m.def("getsol",&getsol,"rtklib getsol");
    m.def("addsol",&addsol,"rtklib addsol");
    m.def("inputsol",&inputsol,"rtklib inputsol");
    m.def("sbsreadmsg",&sbsreadmsg,"rtklib sbsreadmsg");
    m.def("sbsreadmsgt",&sbsreadmsgt,"rtklib sbsreadmsgt");
    m.def("sbsupdatecorr",&sbsupdatecorr,"rtklib sbsupdatecorr");
    m.def("searchopt",&searchopt,"rtklib searchopt");
    m.def("str2opt",&str2opt,"rtklib str2opt");
    m.def("loadopts",&loadopts,"rtklib loadopts");
    m.def("saveopts",&saveopts,"rtklib saveopts");
    m.def("resetsysopts",&resetsysopts,"rtklib resetsysopts");
    m.def("getsysopts",&getsysopts,"rtklib getsysopts");
    m.def("setsysopts",&setsysopts,"rtklib setsysopts");
    m.def("strinitcom",&strinitcom,"rtklib strinitcom");
    m.def("strinit",&strinit,"rtklib strinit");
    m.def("strlock",&strlock,"rtklib strlock");
    m.def("strunlock",&strunlock,"rtklib strunlock");
    m.def("stropen",&stropen,"rtklib stropen");
    m.def("strclose",&strclose,"rtklib strclose");
    m.def("strsync",&strsync,"rtklib strsync");
    m.def("strgettime",&strgettime,"rtklib strgettime");
    m.def("strsendnmea",&strsendnmea,"rtklib strsendnmea");
    m.def("strsendcmd",&strsendcmd,"rtklib strsendcmd");
    m.def("strsettimeout",&strsettimeout,"rtklib strsettimeout");
    m.def("strsetdir",&strsetdir,"rtklib strsetdir");
    m.def("strsetproxy",&strsetproxy,"rtklib strsetproxy");
    m.def("rtkinit",&rtkinit,"rtklib rtkinit");
    m.def("rtkfree",&rtkfree,"rtklib rtkfree");
    m.def("rtkpos",&rtkpos,"rtklib rtkpos");
    m.def("rtkopenstat",&rtkopenstat,"rtklib rtkopenstat");
    m.def("rtkclosestat",&rtkclosestat,"rtklib rtkclosestat");
    m.def("pppos",&pppos,"rtklib pppos");
    m.def("pppnx",&pppnx,"rtklib pppnx");
    m.def("strsvrinit",&strsvrinit,"rtklib strsvrinit");
    m.def("strconvnew",&strconvnew,"rtklib strconvnew");
    m.def("strconvfree",&strconvfree,"rtklib strconvfree");
    m.def("rtksvrinit",&rtksvrinit,"rtklib rtksvrinit");
    m.def("rtksvrfree",&rtksvrfree,"rtklib rtksvrfree");
    m.def("rtksvropenstr",&rtksvropenstr,"rtklib rtksvropenstr");
    m.def("rtksvrclosestr",&rtksvrclosestr,"rtklib rtksvrclosestr");
    m.def("rtksvrlock",&rtksvrlock,"rtklib rtksvrlock");
    m.def("rtksvrunlock",&rtksvrunlock,"rtklib rtksvrunlock");
    m.def("rtksvrmark",&rtksvrmark,"rtklib rtksvrmark");
    m.def("gis_read",&gis_read,"rtklib gis_read");
    m.def("gis_free",&gis_free,"rtklib gis_free");
    m.def("settspan",&settspan,"rtklib settspan");
    m.def("settime",&settime,"rtklib settime");

}
