"""
rtklib python interface by pybind11
"""
from __future__ import annotations
import typing
__all__ = ['ARMODE_CONT', 'ARMODE_FIXHOLD', 'ARMODE_INST', 'ARMODE_OFF', 'ARMODE_TCAR', 'ARMODE_WLNL', 'AS2R', 'AU', 'Arr1Dalm_t', 'Arr1Dambc_t', 'Arr1Dchar', 'Arr1Ddgps_t', 'Arr1Ddouble', 'Arr1Deph_t', 'Arr1Derp_t', 'Arr1Derpd_t', 'Arr1Dfilopt_t', 'Arr1Dfloat', 'Arr1Dgeph_t', 'Arr1Dgis_pnt_t', 'Arr1Dgis_poly_t', 'Arr1Dgis_polygon_t', 'Arr1Dgis_t', 'Arr1Dgisd_t', 'Arr1Dgtime_t', 'Arr1Dint', 'Arr1Dlong', 'Arr1Dnav_t', 'Arr1Dobs_t', 'Arr1Dobsd_t', 'Arr1Dopt_t', 'Arr1Dpclk_t', 'Arr1Dpcv_t', 'Arr1Dpcvs_t', 'Arr1Dpeph_t', 'Arr1Dprcopt_t', 'Arr1Draw_t', 'Arr1Drnxctr_t', 'Arr1Drnxopt_t', 'Arr1Drtcm_t', 'Arr1Drtk_t', 'Arr1Drtksvr_t', 'Arr1Dsbs_t', 'Arr1Dsbsfcorr_t', 'Arr1Dsbsigp_t', 'Arr1Dsbsigpband_t', 'Arr1Dsbsion_t', 'Arr1Dsbslcorr_t', 'Arr1Dsbsmsg_t', 'Arr1Dsbssat_t', 'Arr1Dsbssatp_t', 'Arr1Dseph_t', 'Arr1Dshort', 'Arr1Dsnrmask_t', 'Arr1Dsol_t', 'Arr1Dsolbuf_t', 'Arr1Dsolopt_t', 'Arr1Dsolstat_t', 'Arr1Dsolstatbuf_t', 'Arr1Dssat_t', 'Arr1Dssr_t', 'Arr1Dsta_t', 'Arr1Dstrconv_t', 'Arr1Dstream_t', 'Arr1Dstrsvr_t', 'Arr1Dtec_t', 'Arr1Dtle_t', 'Arr1Dtled_t', 'Arr1Durl_t', 'Arr2Dalm_t', 'Arr2Dambc_t', 'Arr2Dchar', 'Arr2Ddgps_t', 'Arr2Ddouble', 'Arr2Deph_t', 'Arr2Derp_t', 'Arr2Derpd_t', 'Arr2Dfilopt_t', 'Arr2Dfloat', 'Arr2Dgeph_t', 'Arr2Dgis_pnt_t', 'Arr2Dgis_poly_t', 'Arr2Dgis_polygon_t', 'Arr2Dgis_t', 'Arr2Dgisd_t', 'Arr2Dgtime_t', 'Arr2Dint', 'Arr2Dlong', 'Arr2Dnav_t', 'Arr2Dobs_t', 'Arr2Dobsd_t', 'Arr2Dopt_t', 'Arr2Dpclk_t', 'Arr2Dpcv_t', 'Arr2Dpcvs_t', 'Arr2Dpeph_t', 'Arr2Dprcopt_t', 'Arr2Draw_t', 'Arr2Drnxctr_t', 'Arr2Drnxopt_t', 'Arr2Drtcm_t', 'Arr2Drtk_t', 'Arr2Drtksvr_t', 'Arr2Dsbs_t', 'Arr2Dsbsfcorr_t', 'Arr2Dsbsigp_t', 'Arr2Dsbsigpband_t', 'Arr2Dsbsion_t', 'Arr2Dsbslcorr_t', 'Arr2Dsbsmsg_t', 'Arr2Dsbssat_t', 'Arr2Dsbssatp_t', 'Arr2Dseph_t', 'Arr2Dshort', 'Arr2Dsnrmask_t', 'Arr2Dsol_t', 'Arr2Dsolbuf_t', 'Arr2Dsolopt_t', 'Arr2Dsolstat_t', 'Arr2Dsolstatbuf_t', 'Arr2Dssat_t', 'Arr2Dssr_t', 'Arr2Dsta_t', 'Arr2Dstrconv_t', 'Arr2Dstream_t', 'Arr2Dstrsvr_t', 'Arr2Dtec_t', 'Arr2Dtle_t', 'Arr2Dtled_t', 'Arr2Durl_t', 'CLIGHT', 'CODE_L1A', 'CODE_L1B', 'CODE_L1C', 'CODE_L1D', 'CODE_L1E', 'CODE_L1I', 'CODE_L1L', 'CODE_L1M', 'CODE_L1N', 'CODE_L1P', 'CODE_L1Q', 'CODE_L1S', 'CODE_L1W', 'CODE_L1X', 'CODE_L1Y', 'CODE_L1Z', 'CODE_L2C', 'CODE_L2D', 'CODE_L2I', 'CODE_L2L', 'CODE_L2M', 'CODE_L2N', 'CODE_L2P', 'CODE_L2Q', 'CODE_L2S', 'CODE_L2W', 'CODE_L2X', 'CODE_L2Y', 'CODE_L3I', 'CODE_L3Q', 'CODE_L3X', 'CODE_L4A', 'CODE_L4B', 'CODE_L4X', 'CODE_L5A', 'CODE_L5B', 'CODE_L5C', 'CODE_L5D', 'CODE_L5I', 'CODE_L5P', 'CODE_L5Q', 'CODE_L5X', 'CODE_L5Z', 'CODE_L6A', 'CODE_L6B', 'CODE_L6C', 'CODE_L6E', 'CODE_L6I', 'CODE_L6L', 'CODE_L6Q', 'CODE_L6S', 'CODE_L6X', 'CODE_L6Z', 'CODE_L7D', 'CODE_L7I', 'CODE_L7P', 'CODE_L7Q', 'CODE_L7X', 'CODE_L7Z', 'CODE_L8D', 'CODE_L8I', 'CODE_L8P', 'CODE_L8Q', 'CODE_L8X', 'CODE_L9A', 'CODE_L9B', 'CODE_L9C', 'CODE_L9X', 'CODE_NONE', 'D2R', 'DFRQ1_GLO', 'DFRQ2_GLO', 'DLOPT_FORCE', 'DLOPT_HOLDERR', 'DLOPT_HOLDLST', 'DLOPT_KEEPCMP', 'DTTOL', 'EFACT_CMP', 'EFACT_GAL', 'EFACT_GLO', 'EFACT_GPS', 'EFACT_IRN', 'EFACT_QZS', 'EFACT_SBS', 'EPHOPT_BRDC', 'EPHOPT_PREC', 'EPHOPT_SBAS', 'EPHOPT_SSRAPC', 'EPHOPT_SSRCOM', 'FE_WGS84', 'FREQ1', 'FREQ1_CMP', 'FREQ1_GLO', 'FREQ1a_GLO', 'FREQ2', 'FREQ2_CMP', 'FREQ2_GLO', 'FREQ2a_GLO', 'FREQ3_CMP', 'FREQ3_GLO', 'FREQ5', 'FREQ6', 'FREQ7', 'FREQ8', 'FREQ9', 'FREQTYPE_ALL', 'FREQTYPE_L1', 'FREQTYPE_L2', 'FREQTYPE_L3', 'FREQTYPE_L4', 'FREQTYPE_L5', 'GEOID_EGM2008_M10', 'GEOID_EGM2008_M25', 'GEOID_EGM96_M150', 'GEOID_EMBEDDED', 'GEOID_GSI2000_M15', 'GEOID_RAF09', 'HION', 'INT_SWAP_STAT', 'INT_SWAP_TRAC', 'IONOOPT_BRDC', 'IONOOPT_EST', 'IONOOPT_IFLC', 'IONOOPT_OFF', 'IONOOPT_QZS', 'IONOOPT_SBAS', 'IONOOPT_STEC', 'IONOOPT_TEC', 'LLI_BOCTRK', 'LLI_HALFA', 'LLI_HALFC', 'LLI_HALFS', 'LLI_SLIP', 'MAXANT', 'MAXBAND', 'MAXCODE', 'MAXCOMMENT', 'MAXDTOE', 'MAXDTOE_CMP', 'MAXDTOE_GAL', 'MAXDTOE_GLO', 'MAXDTOE_IRN', 'MAXDTOE_QZS', 'MAXDTOE_S', 'MAXDTOE_SBS', 'MAXERRMSG', 'MAXEXFILE', 'MAXFREQ', 'MAXGDOP', 'MAXGISLAYER', 'MAXLEAPS', 'MAXNGEO', 'MAXNIGP', 'MAXNRPOS', 'MAXOBS', 'MAXOBSBUF', 'MAXOBSTYPE', 'MAXPRNCMP', 'MAXPRNGAL', 'MAXPRNGLO', 'MAXPRNGPS', 'MAXPRNIRN', 'MAXPRNLEO', 'MAXPRNQZS', 'MAXPRNQZS_S', 'MAXPRNSBS', 'MAXRAWLEN', 'MAXRCV', 'MAXRCVCMD', 'MAXRCVFMT', 'MAXSAT', 'MAXSBSAGEF', 'MAXSBSAGEL', 'MAXSBSMSG', 'MAXSBSURA', 'MAXSOLBUF', 'MAXSOLMSG', 'MAXSOLQ', 'MAXSTA', 'MAXSTRMSG', 'MAXSTRPATH', 'MAXSTRRTK', 'MINPRNCMP', 'MINPRNGAL', 'MINPRNGLO', 'MINPRNGPS', 'MINPRNIRN', 'MINPRNLEO', 'MINPRNQZS', 'MINPRNQZS_S', 'MINPRNSBS', 'NEXOBS', 'NFREQ', 'NFREQGLO', 'NSATCMP', 'NSATGAL', 'NSATGLO', 'NSATGPS', 'NSATIRN', 'NSATLEO', 'NSATQZS', 'NSATSBS', 'NSYS', 'NSYSCMP', 'NSYSGAL', 'NSYSGLO', 'NSYSGPS', 'NSYSIRN', 'NSYSLEO', 'NSYSQZS', 'NULL', 'OBSTYPE_ALL', 'OBSTYPE_CP', 'OBSTYPE_DOP', 'OBSTYPE_PR', 'OBSTYPE_SNR', 'OMGE', 'P2_11', 'P2_15', 'P2_17', 'P2_19', 'P2_20', 'P2_21', 'P2_23', 'P2_24', 'P2_27', 'P2_29', 'P2_30', 'P2_31', 'P2_32', 'P2_33', 'P2_35', 'P2_38', 'P2_39', 'P2_40', 'P2_43', 'P2_48', 'P2_5', 'P2_50', 'P2_55', 'P2_6', 'PATCH_LEVEL', 'PI', 'PMODE_DGPS', 'PMODE_FIXED', 'PMODE_KINEMA', 'PMODE_MOVEB', 'PMODE_PPP_FIXED', 'PMODE_PPP_KINEMA', 'PMODE_PPP_STATIC', 'PMODE_SINGLE', 'PMODE_STATIC', 'POSOPT_FILE', 'POSOPT_POS', 'POSOPT_RINEX', 'POSOPT_RTCM', 'POSOPT_SINGLE', 'R2D', 'RE_WGS84', 'RNX2VER', 'RNX3VER', 'SBSOPT_FCORR', 'SBSOPT_ICORR', 'SBSOPT_LCORR', 'SBSOPT_RANGE', 'SC2RAD', 'SNR_UNIT', 'SOLF_ENU', 'SOLF_GSIF', 'SOLF_LLH', 'SOLF_NMEA', 'SOLF_STAT', 'SOLF_XYZ', 'SOLQ_DGPS', 'SOLQ_DR', 'SOLQ_FIX', 'SOLQ_FLOAT', 'SOLQ_NONE', 'SOLQ_PPP', 'SOLQ_SBAS', 'SOLQ_SINGLE', 'STRFMT_BINEX', 'STRFMT_CRES', 'STRFMT_JAVAD', 'STRFMT_NMEA', 'STRFMT_NVS', 'STRFMT_OEM3', 'STRFMT_OEM4', 'STRFMT_RINEX', 'STRFMT_RNXCLK', 'STRFMT_RT17', 'STRFMT_RTCM2', 'STRFMT_RTCM3', 'STRFMT_SBAS', 'STRFMT_SEPT', 'STRFMT_SP3', 'STRFMT_SS2', 'STRFMT_STQ', 'STRFMT_UBX', 'STR_FILE', 'STR_FTP', 'STR_HTTP', 'STR_MEMBUF', 'STR_MODE_R', 'STR_MODE_RW', 'STR_MODE_W', 'STR_NONE', 'STR_NTRIPCAS', 'STR_NTRIPCLI', 'STR_NTRIPSVR', 'STR_SERIAL', 'STR_TCPCLI', 'STR_TCPSVR', 'STR_UDPCLI', 'STR_UDPSVR', 'SYS_ALL', 'SYS_CMP', 'SYS_GAL', 'SYS_GLO', 'SYS_GPS', 'SYS_IRN', 'SYS_LEO', 'SYS_NONE', 'SYS_QZS', 'SYS_SBS', 'TIMES_GPST', 'TIMES_JST', 'TIMES_UTC', 'TROPOPT_EST', 'TROPOPT_ESTG', 'TROPOPT_OFF', 'TROPOPT_SAAS', 'TROPOPT_SBAS', 'TROPOPT_ZTD', 'TSYS_CMP', 'TSYS_GAL', 'TSYS_GLO', 'TSYS_GPS', 'TSYS_IRN', 'TSYS_QZS', 'TSYS_UTC', 'VER_RTKLIB', 'addsol', 'adjgpsweek', 'alm2pos', 'alm_t', 'ambc_t', 'antmodel', 'antmodel_s', 'bdt2gpst', 'bdt2time', 'chisqr', 'closegeoid', 'code2freq', 'code2idx', 'code2obs', 'convgpx', 'convkml', 'convrnx', 'covecef', 'covenu', 'createdir', 'cross3', 'decode_bds_d1', 'decode_bds_d2', 'decode_frame', 'decode_gal_fnav', 'decode_gal_inav', 'decode_glostr', 'decode_irn_nav', 'decode_word', 'deg2dms', 'dgps_t', 'dl_exec', 'dl_readstas', 'dl_readurls', 'dl_test', 'dms2deg', 'dops', 'dot', 'ecef2enu', 'ecef2pos', 'eci2ecef', 'enu2ecef', 'eph2clk', 'eph2pos', 'eph_t', 'epoch2time', 'erp_t', 'erpd_t', 'execcmd', 'expath', 'eye', 'filopt_t', 'filter', 'formatstrs', 'free_raw', 'free_rnxctr', 'free_rt17', 'free_rtcm', 'freenav', 'freeobs', 'freesolbuf', 'freesolstatbuf', 'gen_nvs', 'gen_rtcm2', 'gen_rtcm3', 'gen_stq', 'gen_ubx', 'geodist', 'geoidh', 'geph2clk', 'geph2pos', 'geph_t', 'getbits', 'getbitu', 'getcodepri', 'geterp', 'getseleph', 'getsol', 'getsysopts', 'gis_free', 'gis_pnt_t', 'gis_poly_t', 'gis_polygon_t', 'gis_read', 'gis_t', 'gisd_t', 'gpst2bdt', 'gpst2time', 'gpst2utc', 'gst2time', 'gtime_t', 'igpband1', 'igpband2', 'imat', 'init_raw', 'init_rnxctr', 'init_rt17', 'init_rtcm', 'initsolbuf', 'input_bnx', 'input_bnxf', 'input_cres', 'input_cresf', 'input_javad', 'input_javadf', 'input_nvs', 'input_nvsf', 'input_oem3', 'input_oem3f', 'input_oem4', 'input_oem4f', 'input_raw', 'input_rawf', 'input_rnxctr', 'input_rt17', 'input_rt17f', 'input_rtcm2', 'input_rtcm2f', 'input_rtcm3', 'input_rtcm3f', 'input_sbf', 'input_sbff', 'input_ss2', 'input_ss2f', 'input_stq', 'input_stqf', 'input_ubx', 'input_ubxf', 'inputsol', 'ionmapf', 'ionmodel', 'ionocorr', 'ionppp', 'iontec', 'jgd2tokyo', 'lambda', 'lambda_reduction', 'lambda_search', 'loaddatump', 'loadopts', 'lsq', 'mat', 'matcpy', 'matfprint', 'matinv', 'matmul', 'matprint', 'nav_t', 'norm', 'normv3', 'obs2code', 'obs_t', 'obsd_t', 'open_rnxctr', 'opengeoid', 'opt2buf', 'opt2str', 'opt_t', 'outnmea_gga', 'outnmea_gsa', 'outnmea_gsv', 'outnmea_rmc', 'outprcopt', 'outprcopts', 'outrnxcnavh', 'outrnxgnavb', 'outrnxgnavh', 'outrnxhnavb', 'outrnxhnavh', 'outrnxinavh', 'outrnxlnavh', 'outrnxnavb', 'outrnxnavh', 'outrnxobsb', 'outrnxobsh', 'outrnxqnavh', 'outsol', 'outsolex', 'outsolexs', 'outsolhead', 'outsolheads', 'outsols', 'pclk_t', 'pcv_t', 'pcvs_t', 'peph2pos', 'peph_t', 'pntpos', 'pos2ecef', 'postpos', 'ppp_ar', 'pppnx', 'pppos', 'pppoutstat', 'prcopt_default', 'prcopt_t', 'raw_t', 'read_leaps', 'readblq', 'readdcb', 'readerp', 'readnav', 'readpcv', 'readpos', 'readrnx', 'readrnxc', 'readrnxt', 'readsap', 'readsol', 'readsolstat', 'readsolstatt', 'readsolt', 'readsp3', 'readtec', 'reppath', 'reppaths', 'resetsysopts', 'rnxctr_t', 'rnxopt_t', 'rtcm_t', 'rtk_crc16', 'rtk_crc24q', 'rtk_crc32', 'rtk_t', 'rtk_uncompress', 'rtkclosestat', 'rtkfree', 'rtkinit', 'rtkopenstat', 'rtkoutstat', 'rtkpos', 'rtksvr_t', 'rtksvrclosestr', 'rtksvrfree', 'rtksvrinit', 'rtksvrlock', 'rtksvrmark', 'rtksvropenstr', 'rtksvrostat', 'rtksvrsstat', 'rtksvrstart', 'rtksvrstop', 'rtksvrunlock', 'sat2freq', 'satantoff', 'satazel', 'satexclude', 'satid2no', 'satno', 'satno2id', 'satpos', 'satposs', 'satsys', 'savenav', 'saveopts', 'sbs_t', 'sbsdecodemsg', 'sbsfcorr_t', 'sbsigp_t', 'sbsigpband_t', 'sbsion_t', 'sbsioncorr', 'sbslcorr_t', 'sbsmsg_t', 'sbsoutmsg', 'sbsreadmsg', 'sbsreadmsgt', 'sbssat_t', 'sbssatcorr', 'sbssatp_t', 'sbstropcorr', 'sbsupdatecorr', 'screent', 'searchopt', 'searchpcv', 'seph2clk', 'seph2pos', 'seph_t', 'setbits', 'setbitu', 'setcodepri', 'setseleph', 'setsysopts', 'settime', 'settspan', 'sleepms', 'smoother', 'snrmask_t', 'sol_t', 'solbuf_t', 'solopt_default', 'solopt_t', 'solstat_t', 'solstatbuf_t', 'solve', 'sortobs', 'ssat_t', 'ssr_t', 'sta_t', 'str2num', 'str2opt', 'str2time', 'strclose', 'strconv_t', 'strconvfree', 'strconvnew', 'stream_t', 'strgettime', 'strinit', 'strinitcom', 'strlock', 'stropen', 'strread', 'strsendcmd', 'strsendnmea', 'strsetdir', 'strsetopt', 'strsetproxy', 'strsettimeout', 'strstat', 'strstatx', 'strsum', 'strsvr_t', 'strsvrinit', 'strsvrstart', 'strsvrstat', 'strsvrstop', 'strsync', 'strunlock', 'strwrite', 'sunmoonpos', 'sysopts', 'tec_t', 'test_glostr', 'testsnr', 'tickget', 'tidedisp', 'time2bdt', 'time2doy', 'time2epoch', 'time2gpst', 'time2gst', 'time2str', 'time_str', 'timeadd', 'timediff', 'timeget', 'timereset', 'timeset', 'tle_name_read', 'tle_pos', 'tle_read', 'tle_t', 'tled_t', 'tokyo2jgd', 'traceb', 'traceclose', 'tracegnav', 'tracehnav', 'tracelevel', 'tracemat', 'tracenav', 'traceobs', 'traceopen', 'tracepclk', 'tracepeph', 'tropcorr', 'tropmapf', 'tropmodel', 'uniqnav', 'url_t', 'utc2gmst', 'utc2gpst', 'xyz2enu', 'zeros']
class Arr1Dalm_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> alm_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dalm_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: alm_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: alm_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dalm_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dalm_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dalm_t) -> None:
        ...
    @property
    def ptr(self) -> alm_t:
        ...
class Arr1Dambc_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> ambc_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dambc_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ambc_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ambc_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dambc_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dambc_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dambc_t) -> None:
        ...
    @property
    def ptr(self) -> ambc_t:
        ...
class Arr1Dchar:
    @typing.overload
    def __getitem__(self, arg0: int) -> str:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dchar:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, s: str) -> None:
        """
        Constructor from Python str
        """
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: str) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dchar:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dchar:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dchar) -> None:
        ...
    @property
    def ptr(self) -> str:
        ...
class Arr1Ddgps_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> dgps_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Ddgps_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: dgps_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: dgps_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Ddgps_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Ddgps_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Ddgps_t) -> None:
        ...
    @property
    def ptr(self) -> dgps_t:
        ...
class Arr1Ddouble:
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Ddouble:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Ddouble:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Ddouble:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Ddouble) -> None:
        ...
    @property
    def ptr(self) -> float:
        ...
class Arr1Deph_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> eph_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Deph_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: eph_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: eph_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Deph_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Deph_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Deph_t) -> None:
        ...
    @property
    def ptr(self) -> eph_t:
        ...
class Arr1Derp_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> erp_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Derp_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: erp_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: erp_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Derp_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Derp_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Derp_t) -> None:
        ...
    @property
    def ptr(self) -> erp_t:
        ...
class Arr1Derpd_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> erpd_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Derpd_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: erpd_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: erpd_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Derpd_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Derpd_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Derpd_t) -> None:
        ...
    @property
    def ptr(self) -> erpd_t:
        ...
class Arr1Dfilopt_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> filopt_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dfilopt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: filopt_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: filopt_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dfilopt_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dfilopt_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dfilopt_t) -> None:
        ...
    @property
    def ptr(self) -> filopt_t:
        ...
class Arr1Dfloat:
    @typing.overload
    def __getitem__(self, arg0: int) -> float:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dfloat:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: float) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dfloat:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dfloat:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dfloat) -> None:
        ...
    @property
    def ptr(self) -> float:
        ...
class Arr1Dgeph_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> geph_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dgeph_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: geph_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: geph_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dgeph_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dgeph_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dgeph_t) -> None:
        ...
    @property
    def ptr(self) -> geph_t:
        ...
class Arr1Dgis_pnt_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> gis_pnt_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dgis_pnt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gis_pnt_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: gis_pnt_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dgis_pnt_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dgis_pnt_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dgis_pnt_t) -> None:
        ...
    @property
    def ptr(self) -> gis_pnt_t:
        ...
class Arr1Dgis_poly_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> gis_poly_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dgis_poly_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gis_poly_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: gis_poly_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dgis_poly_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dgis_poly_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dgis_poly_t) -> None:
        ...
    @property
    def ptr(self) -> gis_poly_t:
        ...
class Arr1Dgis_polygon_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> gis_polygon_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dgis_polygon_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gis_polygon_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: gis_polygon_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dgis_polygon_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dgis_polygon_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dgis_polygon_t) -> None:
        ...
    @property
    def ptr(self) -> gis_polygon_t:
        ...
class Arr1Dgis_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> gis_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dgis_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gis_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: gis_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dgis_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dgis_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dgis_t) -> None:
        ...
    @property
    def ptr(self) -> gis_t:
        ...
class Arr1Dgisd_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> gisd_tag:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dgisd_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gisd_tag, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: gisd_tag) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dgisd_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dgisd_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dgisd_t) -> None:
        ...
    @property
    def ptr(self) -> gisd_tag:
        ...
class Arr1Dgtime_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> gtime_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dgtime_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gtime_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: gtime_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dgtime_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dgtime_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dgtime_t) -> None:
        ...
    @property
    def ptr(self) -> gtime_t:
        ...
class Arr1Dint:
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dint:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dint:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dint:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dint) -> None:
        ...
    @property
    def ptr(self) -> int:
        ...
class Arr1Dlong:
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dlong:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dlong:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dlong:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dlong) -> None:
        ...
    @property
    def ptr(self) -> int:
        ...
class Arr1Dnav_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> nav_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dnav_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: nav_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: nav_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dnav_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dnav_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dnav_t) -> None:
        ...
    @property
    def ptr(self) -> nav_t:
        ...
class Arr1Dobs_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> obs_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dobs_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: obs_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: obs_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dobs_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dobs_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dobs_t) -> None:
        ...
    @property
    def ptr(self) -> obs_t:
        ...
class Arr1Dobsd_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> obsd_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dobsd_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: obsd_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: obsd_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dobsd_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dobsd_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dobsd_t) -> None:
        ...
    @property
    def ptr(self) -> obsd_t:
        ...
class Arr1Dopt_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> opt_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dopt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: opt_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: opt_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dopt_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dopt_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dopt_t) -> None:
        ...
    @property
    def ptr(self) -> opt_t:
        ...
class Arr1Dpclk_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> pclk_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dpclk_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: pclk_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: pclk_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dpclk_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dpclk_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dpclk_t) -> None:
        ...
    @property
    def ptr(self) -> pclk_t:
        ...
class Arr1Dpcv_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> pcv_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dpcv_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: pcv_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: pcv_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dpcv_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dpcv_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dpcv_t) -> None:
        ...
    @property
    def ptr(self) -> pcv_t:
        ...
class Arr1Dpcvs_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> pcvs_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dpcvs_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: pcvs_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: pcvs_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dpcvs_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dpcvs_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dpcvs_t) -> None:
        ...
    @property
    def ptr(self) -> pcvs_t:
        ...
class Arr1Dpeph_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> peph_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dpeph_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: peph_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: peph_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dpeph_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dpeph_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dpeph_t) -> None:
        ...
    @property
    def ptr(self) -> peph_t:
        ...
class Arr1Dprcopt_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> prcopt_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dprcopt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: prcopt_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: prcopt_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dprcopt_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dprcopt_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dprcopt_t) -> None:
        ...
    @property
    def ptr(self) -> prcopt_t:
        ...
class Arr1Draw_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> raw_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Draw_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: raw_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: raw_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Draw_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Draw_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Draw_t) -> None:
        ...
    @property
    def ptr(self) -> raw_t:
        ...
class Arr1Drnxctr_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> rnxctr_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Drnxctr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rnxctr_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: rnxctr_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Drnxctr_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Drnxctr_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Drnxctr_t) -> None:
        ...
    @property
    def ptr(self) -> rnxctr_t:
        ...
class Arr1Drnxopt_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> rnxopt_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Drnxopt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rnxopt_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: rnxopt_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Drnxopt_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Drnxopt_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Drnxopt_t) -> None:
        ...
    @property
    def ptr(self) -> rnxopt_t:
        ...
class Arr1Drtcm_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> rtcm_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Drtcm_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rtcm_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: rtcm_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Drtcm_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Drtcm_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Drtcm_t) -> None:
        ...
    @property
    def ptr(self) -> rtcm_t:
        ...
class Arr1Drtk_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> rtk_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Drtk_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rtk_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: rtk_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Drtk_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Drtk_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Drtk_t) -> None:
        ...
    @property
    def ptr(self) -> rtk_t:
        ...
class Arr1Drtksvr_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> rtksvr_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Drtksvr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rtksvr_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: rtksvr_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Drtksvr_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Drtksvr_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Drtksvr_t) -> None:
        ...
    @property
    def ptr(self) -> rtksvr_t:
        ...
class Arr1Dsbs_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sbs_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsbs_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbs_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sbs_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsbs_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsbs_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsbs_t) -> None:
        ...
    @property
    def ptr(self) -> sbs_t:
        ...
class Arr1Dsbsfcorr_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sbsfcorr_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsbsfcorr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsfcorr_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sbsfcorr_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsbsfcorr_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsbsfcorr_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsbsfcorr_t) -> None:
        ...
    @property
    def ptr(self) -> sbsfcorr_t:
        ...
class Arr1Dsbsigp_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sbsigp_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsbsigp_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsigp_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sbsigp_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsbsigp_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsbsigp_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsbsigp_t) -> None:
        ...
    @property
    def ptr(self) -> sbsigp_t:
        ...
class Arr1Dsbsigpband_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sbsigpband_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsbsigpband_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsigpband_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sbsigpband_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsbsigpband_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsbsigpband_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsbsigpband_t) -> None:
        ...
    @property
    def ptr(self) -> sbsigpband_t:
        ...
class Arr1Dsbsion_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sbsion_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsbsion_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsion_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sbsion_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsbsion_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsbsion_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsbsion_t) -> None:
        ...
    @property
    def ptr(self) -> sbsion_t:
        ...
class Arr1Dsbslcorr_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sbslcorr_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsbslcorr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbslcorr_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sbslcorr_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsbslcorr_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsbslcorr_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsbslcorr_t) -> None:
        ...
    @property
    def ptr(self) -> sbslcorr_t:
        ...
class Arr1Dsbsmsg_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sbsmsg_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsbsmsg_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsmsg_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sbsmsg_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsbsmsg_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsbsmsg_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsbsmsg_t) -> None:
        ...
    @property
    def ptr(self) -> sbsmsg_t:
        ...
class Arr1Dsbssat_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sbssat_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsbssat_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbssat_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sbssat_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsbssat_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsbssat_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsbssat_t) -> None:
        ...
    @property
    def ptr(self) -> sbssat_t:
        ...
class Arr1Dsbssatp_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sbssatp_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsbssatp_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbssatp_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sbssatp_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsbssatp_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsbssatp_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsbssatp_t) -> None:
        ...
    @property
    def ptr(self) -> sbssatp_t:
        ...
class Arr1Dseph_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> seph_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dseph_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: seph_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: seph_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dseph_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dseph_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dseph_t) -> None:
        ...
    @property
    def ptr(self) -> seph_t:
        ...
class Arr1Dshort:
    @typing.overload
    def __getitem__(self, arg0: int) -> int:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dshort:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dshort:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dshort:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dshort) -> None:
        ...
    @property
    def ptr(self) -> int:
        ...
class Arr1Dsnrmask_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> snrmask_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsnrmask_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: snrmask_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: snrmask_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsnrmask_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsnrmask_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsnrmask_t) -> None:
        ...
    @property
    def ptr(self) -> snrmask_t:
        ...
class Arr1Dsol_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sol_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsol_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sol_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sol_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsol_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsol_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsol_t) -> None:
        ...
    @property
    def ptr(self) -> sol_t:
        ...
class Arr1Dsolbuf_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> solbuf_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsolbuf_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: solbuf_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: solbuf_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsolbuf_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsolbuf_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsolbuf_t) -> None:
        ...
    @property
    def ptr(self) -> solbuf_t:
        ...
class Arr1Dsolopt_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> solopt_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsolopt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: solopt_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: solopt_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsolopt_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsolopt_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsolopt_t) -> None:
        ...
    @property
    def ptr(self) -> solopt_t:
        ...
class Arr1Dsolstat_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> solstat_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsolstat_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: solstat_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: solstat_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsolstat_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsolstat_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsolstat_t) -> None:
        ...
    @property
    def ptr(self) -> solstat_t:
        ...
class Arr1Dsolstatbuf_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> solstatbuf_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsolstatbuf_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: solstatbuf_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: solstatbuf_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsolstatbuf_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsolstatbuf_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsolstatbuf_t) -> None:
        ...
    @property
    def ptr(self) -> solstatbuf_t:
        ...
class Arr1Dssat_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> ssat_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dssat_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ssat_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ssat_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dssat_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dssat_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dssat_t) -> None:
        ...
    @property
    def ptr(self) -> ssat_t:
        ...
class Arr1Dssr_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> ssr_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dssr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ssr_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: ssr_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dssr_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dssr_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dssr_t) -> None:
        ...
    @property
    def ptr(self) -> ssr_t:
        ...
class Arr1Dsta_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> sta_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dsta_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sta_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: sta_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dsta_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dsta_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dsta_t) -> None:
        ...
    @property
    def ptr(self) -> sta_t:
        ...
class Arr1Dstrconv_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> strconv_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dstrconv_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: strconv_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: strconv_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dstrconv_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dstrconv_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dstrconv_t) -> None:
        ...
    @property
    def ptr(self) -> strconv_t:
        ...
class Arr1Dstream_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> stream_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dstream_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: stream_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: stream_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dstream_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dstream_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dstream_t) -> None:
        ...
    @property
    def ptr(self) -> stream_t:
        ...
class Arr1Dstrsvr_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> strsvr_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dstrsvr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: strsvr_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: strsvr_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dstrsvr_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dstrsvr_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dstrsvr_t) -> None:
        ...
    @property
    def ptr(self) -> strsvr_t:
        ...
class Arr1Dtec_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> tec_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dtec_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: tec_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: tec_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dtec_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dtec_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dtec_t) -> None:
        ...
    @property
    def ptr(self) -> tec_t:
        ...
class Arr1Dtle_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> tle_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dtle_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: tle_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: tle_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dtle_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dtle_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dtle_t) -> None:
        ...
    @property
    def ptr(self) -> tle_t:
        ...
class Arr1Dtled_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> tled_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Dtled_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: tled_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: tled_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Dtled_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Dtled_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Dtled_t) -> None:
        ...
    @property
    def ptr(self) -> tled_t:
        ...
class Arr1Durl_t:
    @typing.overload
    def __getitem__(self, arg0: int) -> url_t:
        ...
    @typing.overload
    def __getitem__(self, arg0: slice) -> Arr1Durl_t:
        ...
    @typing.overload
    def __init__(self, arg0: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: url_t, arg1: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
    def __setitem__(self, arg0: int, arg1: url_t) -> None:
        ...
    @typing.overload
    def deepcopy(self) -> Arr1Durl_t:
        ...
    @typing.overload
    def deepcopy(self, arg0: int) -> Arr1Durl_t:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr1Durl_t) -> None:
        ...
    @property
    def ptr(self) -> url_t:
        ...
class Arr2Dalm_t:
    def __getitem__(self, arg0: tuple) -> alm_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: alm_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: alm_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dalm_t) -> None:
        ...
    @property
    def ptr(self) -> alm_t:
        ...
class Arr2Dambc_t:
    def __getitem__(self, arg0: tuple) -> ambc_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ambc_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: ambc_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dambc_t) -> None:
        ...
    @property
    def ptr(self) -> ambc_t:
        ...
class Arr2Dchar:
    def __getitem__(self, arg0: tuple) -> str:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: str) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dchar) -> None:
        ...
    @property
    def ptr(self) -> str:
        ...
class Arr2Ddgps_t:
    def __getitem__(self, arg0: tuple) -> dgps_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: dgps_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: dgps_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Ddgps_t) -> None:
        ...
    @property
    def ptr(self) -> dgps_t:
        ...
class Arr2Ddouble:
    def __getitem__(self, arg0: tuple) -> float:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: float) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Ddouble) -> None:
        ...
    @property
    def ptr(self) -> float:
        ...
class Arr2Deph_t:
    def __getitem__(self, arg0: tuple) -> eph_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: eph_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: eph_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Deph_t) -> None:
        ...
    @property
    def ptr(self) -> eph_t:
        ...
class Arr2Derp_t:
    def __getitem__(self, arg0: tuple) -> erp_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: erp_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: erp_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Derp_t) -> None:
        ...
    @property
    def ptr(self) -> erp_t:
        ...
class Arr2Derpd_t:
    def __getitem__(self, arg0: tuple) -> erpd_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: erpd_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: erpd_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Derpd_t) -> None:
        ...
    @property
    def ptr(self) -> erpd_t:
        ...
class Arr2Dfilopt_t:
    def __getitem__(self, arg0: tuple) -> filopt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: filopt_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: filopt_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dfilopt_t) -> None:
        ...
    @property
    def ptr(self) -> filopt_t:
        ...
class Arr2Dfloat:
    def __getitem__(self, arg0: tuple) -> float:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: float, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: float) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dfloat) -> None:
        ...
    @property
    def ptr(self) -> float:
        ...
class Arr2Dgeph_t:
    def __getitem__(self, arg0: tuple) -> geph_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: geph_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: geph_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dgeph_t) -> None:
        ...
    @property
    def ptr(self) -> geph_t:
        ...
class Arr2Dgis_pnt_t:
    def __getitem__(self, arg0: tuple) -> gis_pnt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gis_pnt_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: gis_pnt_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dgis_pnt_t) -> None:
        ...
    @property
    def ptr(self) -> gis_pnt_t:
        ...
class Arr2Dgis_poly_t:
    def __getitem__(self, arg0: tuple) -> gis_poly_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gis_poly_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: gis_poly_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dgis_poly_t) -> None:
        ...
    @property
    def ptr(self) -> gis_poly_t:
        ...
class Arr2Dgis_polygon_t:
    def __getitem__(self, arg0: tuple) -> gis_polygon_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gis_polygon_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: gis_polygon_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dgis_polygon_t) -> None:
        ...
    @property
    def ptr(self) -> gis_polygon_t:
        ...
class Arr2Dgis_t:
    def __getitem__(self, arg0: tuple) -> gis_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gis_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: gis_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dgis_t) -> None:
        ...
    @property
    def ptr(self) -> gis_t:
        ...
class Arr2Dgisd_t:
    def __getitem__(self, arg0: tuple) -> gisd_tag:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gisd_tag, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: gisd_tag) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dgisd_t) -> None:
        ...
    @property
    def ptr(self) -> gisd_tag:
        ...
class Arr2Dgtime_t:
    def __getitem__(self, arg0: tuple) -> gtime_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: gtime_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: gtime_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dgtime_t) -> None:
        ...
    @property
    def ptr(self) -> gtime_t:
        ...
class Arr2Dint:
    def __getitem__(self, arg0: tuple) -> int:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: int) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dint) -> None:
        ...
    @property
    def ptr(self) -> int:
        ...
class Arr2Dlong:
    def __getitem__(self, arg0: tuple) -> int:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: int) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dlong) -> None:
        ...
    @property
    def ptr(self) -> int:
        ...
class Arr2Dnav_t:
    def __getitem__(self, arg0: tuple) -> nav_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: nav_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: nav_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dnav_t) -> None:
        ...
    @property
    def ptr(self) -> nav_t:
        ...
class Arr2Dobs_t:
    def __getitem__(self, arg0: tuple) -> obs_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: obs_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: obs_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dobs_t) -> None:
        ...
    @property
    def ptr(self) -> obs_t:
        ...
class Arr2Dobsd_t:
    def __getitem__(self, arg0: tuple) -> obsd_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: obsd_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: obsd_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dobsd_t) -> None:
        ...
    @property
    def ptr(self) -> obsd_t:
        ...
class Arr2Dopt_t:
    def __getitem__(self, arg0: tuple) -> opt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: opt_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: opt_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dopt_t) -> None:
        ...
    @property
    def ptr(self) -> opt_t:
        ...
class Arr2Dpclk_t:
    def __getitem__(self, arg0: tuple) -> pclk_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: pclk_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: pclk_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dpclk_t) -> None:
        ...
    @property
    def ptr(self) -> pclk_t:
        ...
class Arr2Dpcv_t:
    def __getitem__(self, arg0: tuple) -> pcv_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: pcv_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: pcv_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dpcv_t) -> None:
        ...
    @property
    def ptr(self) -> pcv_t:
        ...
class Arr2Dpcvs_t:
    def __getitem__(self, arg0: tuple) -> pcvs_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: pcvs_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: pcvs_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dpcvs_t) -> None:
        ...
    @property
    def ptr(self) -> pcvs_t:
        ...
class Arr2Dpeph_t:
    def __getitem__(self, arg0: tuple) -> peph_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: peph_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: peph_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dpeph_t) -> None:
        ...
    @property
    def ptr(self) -> peph_t:
        ...
class Arr2Dprcopt_t:
    def __getitem__(self, arg0: tuple) -> prcopt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: prcopt_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: prcopt_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dprcopt_t) -> None:
        ...
    @property
    def ptr(self) -> prcopt_t:
        ...
class Arr2Draw_t:
    def __getitem__(self, arg0: tuple) -> raw_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: raw_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: raw_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Draw_t) -> None:
        ...
    @property
    def ptr(self) -> raw_t:
        ...
class Arr2Drnxctr_t:
    def __getitem__(self, arg0: tuple) -> rnxctr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rnxctr_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: rnxctr_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Drnxctr_t) -> None:
        ...
    @property
    def ptr(self) -> rnxctr_t:
        ...
class Arr2Drnxopt_t:
    def __getitem__(self, arg0: tuple) -> rnxopt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rnxopt_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: rnxopt_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Drnxopt_t) -> None:
        ...
    @property
    def ptr(self) -> rnxopt_t:
        ...
class Arr2Drtcm_t:
    def __getitem__(self, arg0: tuple) -> rtcm_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rtcm_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: rtcm_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Drtcm_t) -> None:
        ...
    @property
    def ptr(self) -> rtcm_t:
        ...
class Arr2Drtk_t:
    def __getitem__(self, arg0: tuple) -> rtk_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rtk_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: rtk_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Drtk_t) -> None:
        ...
    @property
    def ptr(self) -> rtk_t:
        ...
class Arr2Drtksvr_t:
    def __getitem__(self, arg0: tuple) -> rtksvr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: rtksvr_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: rtksvr_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Drtksvr_t) -> None:
        ...
    @property
    def ptr(self) -> rtksvr_t:
        ...
class Arr2Dsbs_t:
    def __getitem__(self, arg0: tuple) -> sbs_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbs_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sbs_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsbs_t) -> None:
        ...
    @property
    def ptr(self) -> sbs_t:
        ...
class Arr2Dsbsfcorr_t:
    def __getitem__(self, arg0: tuple) -> sbsfcorr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsfcorr_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sbsfcorr_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsbsfcorr_t) -> None:
        ...
    @property
    def ptr(self) -> sbsfcorr_t:
        ...
class Arr2Dsbsigp_t:
    def __getitem__(self, arg0: tuple) -> sbsigp_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsigp_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sbsigp_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsbsigp_t) -> None:
        ...
    @property
    def ptr(self) -> sbsigp_t:
        ...
class Arr2Dsbsigpband_t:
    def __getitem__(self, arg0: tuple) -> sbsigpband_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsigpband_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sbsigpband_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsbsigpband_t) -> None:
        ...
    @property
    def ptr(self) -> sbsigpband_t:
        ...
class Arr2Dsbsion_t:
    def __getitem__(self, arg0: tuple) -> sbsion_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsion_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sbsion_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsbsion_t) -> None:
        ...
    @property
    def ptr(self) -> sbsion_t:
        ...
class Arr2Dsbslcorr_t:
    def __getitem__(self, arg0: tuple) -> sbslcorr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbslcorr_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sbslcorr_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsbslcorr_t) -> None:
        ...
    @property
    def ptr(self) -> sbslcorr_t:
        ...
class Arr2Dsbsmsg_t:
    def __getitem__(self, arg0: tuple) -> sbsmsg_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbsmsg_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sbsmsg_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsbsmsg_t) -> None:
        ...
    @property
    def ptr(self) -> sbsmsg_t:
        ...
class Arr2Dsbssat_t:
    def __getitem__(self, arg0: tuple) -> sbssat_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbssat_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sbssat_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsbssat_t) -> None:
        ...
    @property
    def ptr(self) -> sbssat_t:
        ...
class Arr2Dsbssatp_t:
    def __getitem__(self, arg0: tuple) -> sbssatp_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sbssatp_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sbssatp_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsbssatp_t) -> None:
        ...
    @property
    def ptr(self) -> sbssatp_t:
        ...
class Arr2Dseph_t:
    def __getitem__(self, arg0: tuple) -> seph_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: seph_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: seph_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dseph_t) -> None:
        ...
    @property
    def ptr(self) -> seph_t:
        ...
class Arr2Dshort:
    def __getitem__(self, arg0: tuple) -> int:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: int) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dshort) -> None:
        ...
    @property
    def ptr(self) -> int:
        ...
class Arr2Dsnrmask_t:
    def __getitem__(self, arg0: tuple) -> snrmask_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: snrmask_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: snrmask_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsnrmask_t) -> None:
        ...
    @property
    def ptr(self) -> snrmask_t:
        ...
class Arr2Dsol_t:
    def __getitem__(self, arg0: tuple) -> sol_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sol_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sol_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsol_t) -> None:
        ...
    @property
    def ptr(self) -> sol_t:
        ...
class Arr2Dsolbuf_t:
    def __getitem__(self, arg0: tuple) -> solbuf_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: solbuf_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: solbuf_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsolbuf_t) -> None:
        ...
    @property
    def ptr(self) -> solbuf_t:
        ...
class Arr2Dsolopt_t:
    def __getitem__(self, arg0: tuple) -> solopt_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: solopt_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: solopt_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsolopt_t) -> None:
        ...
    @property
    def ptr(self) -> solopt_t:
        ...
class Arr2Dsolstat_t:
    def __getitem__(self, arg0: tuple) -> solstat_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: solstat_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: solstat_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsolstat_t) -> None:
        ...
    @property
    def ptr(self) -> solstat_t:
        ...
class Arr2Dsolstatbuf_t:
    def __getitem__(self, arg0: tuple) -> solstatbuf_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: solstatbuf_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: solstatbuf_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsolstatbuf_t) -> None:
        ...
    @property
    def ptr(self) -> solstatbuf_t:
        ...
class Arr2Dssat_t:
    def __getitem__(self, arg0: tuple) -> ssat_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ssat_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: ssat_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dssat_t) -> None:
        ...
    @property
    def ptr(self) -> ssat_t:
        ...
class Arr2Dssr_t:
    def __getitem__(self, arg0: tuple) -> ssr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ssr_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: ssr_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dssr_t) -> None:
        ...
    @property
    def ptr(self) -> ssr_t:
        ...
class Arr2Dsta_t:
    def __getitem__(self, arg0: tuple) -> sta_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: sta_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: sta_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dsta_t) -> None:
        ...
    @property
    def ptr(self) -> sta_t:
        ...
class Arr2Dstrconv_t:
    def __getitem__(self, arg0: tuple) -> strconv_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: strconv_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: strconv_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dstrconv_t) -> None:
        ...
    @property
    def ptr(self) -> strconv_t:
        ...
class Arr2Dstream_t:
    def __getitem__(self, arg0: tuple) -> stream_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: stream_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: stream_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dstream_t) -> None:
        ...
    @property
    def ptr(self) -> stream_t:
        ...
class Arr2Dstrsvr_t:
    def __getitem__(self, arg0: tuple) -> strsvr_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: strsvr_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: strsvr_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dstrsvr_t) -> None:
        ...
    @property
    def ptr(self) -> strsvr_t:
        ...
class Arr2Dtec_t:
    def __getitem__(self, arg0: tuple) -> tec_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: tec_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: tec_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dtec_t) -> None:
        ...
    @property
    def ptr(self) -> tec_t:
        ...
class Arr2Dtle_t:
    def __getitem__(self, arg0: tuple) -> tle_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: tle_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: tle_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dtle_t) -> None:
        ...
    @property
    def ptr(self) -> tle_t:
        ...
class Arr2Dtled_t:
    def __getitem__(self, arg0: tuple) -> tled_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: tled_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: tled_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Dtled_t) -> None:
        ...
    @property
    def ptr(self) -> tled_t:
        ...
class Arr2Durl_t:
    def __getitem__(self, arg0: tuple) -> url_t:
        ...
    @typing.overload
    def __init__(self, arg0: int, arg1: int) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: url_t, arg1: int, arg2: int) -> None:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> tuple:
        ...
    def __setitem__(self, arg0: tuple, arg1: url_t) -> None:
        ...
    def print(self) -> None:
        ...
    def set(self, arg0: Arr2Durl_t) -> None:
        ...
    @property
    def ptr(self) -> url_t:
        ...
class alm_t:
    A: float
    M0: float
    OMG0: float
    OMGd: float
    e: float
    f0: float
    f1: float
    i0: float
    omg: float
    sat: int
    svconf: int
    svh: int
    toa: gtime_t
    toas: float
    week: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> alm_t:
        ...
class ambc_t:
    fixcnt: int
    def __init__(self) -> None:
        ...
    @property
    def LC(self) -> Arr1Ddouble:
        ...
    @property
    def LCv(self) -> Arr1Ddouble:
        ...
    @property
    def epoch(self) -> Arr1Dgtime_t:
        ...
    @property
    def flags(self) -> Arr1Dchar:
        ...
    @property
    def n(self) -> Arr1Dint:
        ...
    @property
    def ptr(self) -> ambc_t:
        ...
class dgps_t:
    iod: int
    prc: float
    rrc: float
    t0: gtime_t
    udre: float
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> dgps_t:
        ...
class eph_t:
    A: float
    Adot: float
    M0: float
    OMG0: float
    OMGd: float
    cic: float
    cis: float
    code: int
    crc: float
    crs: float
    cuc: float
    cus: float
    deln: float
    e: float
    f0: float
    f1: float
    f2: float
    fit: float
    flag: int
    i0: float
    idot: float
    iodc: int
    iode: int
    ndot: float
    omg: float
    sat: int
    sva: int
    svh: int
    toc: gtime_t
    toe: gtime_t
    toes: float
    ttr: gtime_t
    week: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> eph_t:
        ...
    @property
    def tgd(self) -> Arr1Ddouble:
        ...
class erp_t:
    data: Arr1Derpd_t
    n: int
    nmax: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> erp_t:
        ...
class erpd_t:
    lod: float
    mjd: float
    ut1_utc: float
    xp: float
    xpr: float
    yp: float
    ypr: float
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> erpd_t:
        ...
class filopt_t:
    def __init__(self) -> None:
        ...
    @property
    def blq(self) -> Arr1Dchar:
        ...
    @property
    def dcb(self) -> Arr1Dchar:
        ...
    @property
    def eop(self) -> Arr1Dchar:
        ...
    @property
    def geexe(self) -> Arr1Dchar:
        ...
    @property
    def geoid(self) -> Arr1Dchar:
        ...
    @property
    def iono(self) -> Arr1Dchar:
        ...
    @property
    def ptr(self) -> filopt_t:
        ...
    @property
    def rcvantp(self) -> Arr1Dchar:
        ...
    @property
    def satantp(self) -> Arr1Dchar:
        ...
    @property
    def solstat(self) -> Arr1Dchar:
        ...
    @property
    def stapos(self) -> Arr1Dchar:
        ...
    @property
    def tempdir(self) -> Arr1Dchar:
        ...
    @property
    def trace(self) -> Arr1Dchar:
        ...
class geph_t:
    age: int
    dtaun: float
    frq: int
    gamn: float
    iode: int
    sat: int
    sva: int
    svh: int
    taun: float
    toe: gtime_t
    tof: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def acc(self) -> Arr1Ddouble:
        ...
    @property
    def pos(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> geph_t:
        ...
    @property
    def vel(self) -> Arr1Ddouble:
        ...
class gis_pnt_t:
    def __init__(self) -> None:
        ...
    @property
    def pos(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> gis_pnt_t:
        ...
class gis_poly_t:
    npnt: int
    pos: Arr1Ddouble
    def __init__(self) -> None:
        ...
    @property
    def bound(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> gis_poly_t:
        ...
class gis_polygon_t:
    npnt: int
    pos: Arr1Ddouble
    def __init__(self) -> None:
        ...
    @property
    def bound(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> gis_polygon_t:
        ...
class gis_t:
    def __init__(self) -> None:
        ...
    @property
    def bound(self) -> Arr1Ddouble:
        ...
    @property
    def data(self) -> Arr2Dgisd_t:
        ...
    @property
    def flag(self) -> Arr1Dint:
        ...
    @property
    def name(self) -> Arr2Dchar:
        ...
    @property
    def ptr(self) -> gis_t:
        ...
class gisd_t:
    data: ...
    next: Arr1Dgisd_t
    type: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> gisd_t:
        ...
class gtime_t:
    sec: float
    time: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> gtime_t:
        ...
class nav_t:
    alm: Arr1Dalm_t
    eph: Arr1Deph_t
    erp: erp_t
    geph: Arr1Dgeph_t
    n: int
    na: int
    namax: int
    nc: int
    ncmax: int
    ne: int
    nemax: int
    ng: int
    ngmax: int
    nmax: int
    ns: int
    nsmax: int
    nt: int
    ntmax: int
    pclk: Arr1Dpclk_t
    peph: Arr1Dpeph_t
    sbssat: sbssat_t
    seph: Arr1Dseph_t
    tec: Arr1Dtec_t
    def __init__(self) -> None:
        ...
    @property
    def cbias(self) -> Arr2Ddouble:
        ...
    @property
    def dgps(self) -> Arr1Ddgps_t:
        ...
    @property
    def glo_fcn(self) -> Arr1Dint:
        ...
    @property
    def ion_cmp(self) -> Arr1Ddouble:
        ...
    @property
    def ion_gal(self) -> Arr1Ddouble:
        ...
    @property
    def ion_gps(self) -> Arr1Ddouble:
        ...
    @property
    def ion_irn(self) -> Arr1Ddouble:
        ...
    @property
    def ion_qzs(self) -> Arr1Ddouble:
        ...
    @property
    def pcvs(self) -> Arr1Dpcv_t:
        ...
    @property
    def ptr(self) -> nav_t:
        ...
    @property
    def rbias(self) -> Arr2Ddouble:
        ...
    @property
    def sbsion(self) -> Arr1Dsbsion_t:
        ...
    @property
    def ssr(self) -> Arr1Dssr_t:
        ...
    @property
    def utc_cmp(self) -> Arr1Ddouble:
        ...
    @property
    def utc_gal(self) -> Arr1Ddouble:
        ...
    @property
    def utc_glo(self) -> Arr1Ddouble:
        ...
    @property
    def utc_gps(self) -> Arr1Ddouble:
        ...
    @property
    def utc_irn(self) -> Arr1Ddouble:
        ...
    @property
    def utc_qzs(self) -> Arr1Ddouble:
        ...
    @property
    def utc_sbs(self) -> Arr1Ddouble:
        ...
class obs_t:
    data: Arr1Dobsd_t
    n: int
    nmax: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> obs_t:
        ...
class obsd_t:
    rcv: int
    sat: int
    time: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def D(self) -> Arr1Dfloat:
        ...
    @property
    def L(self) -> Arr1Ddouble:
        ...
    @property
    def LLI(self) -> ...:
        ...
    @property
    def P(self) -> Arr1Ddouble:
        ...
    @property
    def SNR(self) -> ...:
        ...
    @property
    def code(self) -> ...:
        ...
    @property
    def ptr(self) -> obsd_t:
        ...
class opt_t:
    comment: Arr1Dchar
    format: int
    name: Arr1Dchar
    var: ...
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> opt_t:
        ...
class pclk_t:
    index: int
    time: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def clk(self) -> Arr2Ddouble:
        ...
    @property
    def ptr(self) -> pclk_t:
        ...
    @property
    def std(self) -> Arr2Dfloat:
        ...
class pcv_t:
    sat: int
    te: gtime_t
    ts: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def code(self) -> Arr1Dchar:
        ...
    @property
    def off(self) -> Arr2Ddouble:
        ...
    @property
    def ptr(self) -> pcv_t:
        ...
    @property
    def type(self) -> Arr1Dchar:
        ...
    @property
    def var(self) -> Arr2Ddouble:
        ...
class pcvs_t:
    n: int
    nmax: int
    pcv: Arr1Dpcv_t
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> pcvs_t:
        ...
class peph_t:
    index: int
    time: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def cov(self) -> Arr2Dfloat:
        ...
    @property
    def pos(self) -> Arr2Ddouble:
        ...
    @property
    def ptr(self) -> peph_t:
        ...
    @property
    def std(self) -> Arr2Dfloat:
        ...
    @property
    def vco(self) -> Arr2Dfloat:
        ...
    @property
    def vel(self) -> Arr2Ddouble:
        ...
    @property
    def vst(self) -> Arr2Dfloat:
        ...
class prcopt_t:
    armaxiter: int
    bdsmodear: int
    codesmooth: int
    dynamics: int
    elmaskar: float
    elmaskhold: float
    elmin: float
    freqopt: int
    glomodear: int
    initrst: int
    intpref: int
    ionoopt: int
    maxaveep: int
    maxgdop: float
    maxinno: float
    maxout: int
    maxtdiff: float
    minfix: int
    minlock: int
    mode: int
    modear: int
    navsys: int
    nf: int
    niter: int
    outsingle: int
    refpos: int
    rovpos: int
    sateph: int
    sbascorr: int
    sbassatsel: int
    sclkstab: float
    snrmask: snrmask_t
    soltype: int
    syncsol: int
    thresslip: float
    tidecorr: int
    tropopt: int
    def __init__(self) -> None:
        ...
    @property
    def antdel(self) -> Arr2Ddouble:
        ...
    @property
    def anttype(self) -> Arr2Dchar:
        ...
    @property
    def baseline(self) -> Arr1Ddouble:
        ...
    @property
    def eratio(self) -> Arr1Ddouble:
        ...
    @property
    def err(self) -> Arr1Ddouble:
        ...
    @property
    def exsats(self) -> ...:
        ...
    @property
    def odisp(self) -> Arr2Ddouble:
        ...
    @property
    def pcvr(self) -> Arr1Dpcv_t:
        ...
    @property
    def posopt(self) -> Arr1Dint:
        ...
    @property
    def pppopt(self) -> Arr1Dchar:
        ...
    @property
    def prn(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> prcopt_t:
        ...
    @property
    def rb(self) -> Arr1Ddouble:
        ...
    @property
    def rnxopt(self) -> Arr2Dchar:
        ...
    @property
    def ru(self) -> Arr1Ddouble:
        ...
    @property
    def std(self) -> Arr1Ddouble:
        ...
    @property
    def thresar(self) -> Arr1Ddouble:
        ...
class raw_t:
    ephsat: int
    ephset: int
    flag: int
    format: int
    icpc: float
    iod: int
    len: int
    nav: nav_t
    nbyte: int
    obs: obs_t
    obuf: obs_t
    outtype: int
    rcv_data: ...
    sbsmsg: sbsmsg_t
    sta: sta_t
    tbase: int
    time: gtime_t
    tod: int
    def __init__(self) -> None:
        ...
    @property
    def buff(self) -> ...:
        ...
    @property
    def dpCA(self) -> Arr1Ddouble:
        ...
    @property
    def freqn(self) -> Arr1Dchar:
        ...
    @property
    def halfc(self) -> ...:
        ...
    @property
    def icpp(self) -> Arr2Ddouble:
        ...
    @property
    def lockt(self) -> Arr2Ddouble:
        ...
    @property
    def msgtype(self) -> Arr1Dchar:
        ...
    @property
    def off(self) -> Arr1Ddouble:
        ...
    @property
    def opt(self) -> Arr1Dchar:
        ...
    @property
    def prCA(self) -> Arr2Ddouble:
        ...
    @property
    def ptr(self) -> raw_t:
        ...
    @property
    def subfrm(self) -> ...:
        ...
    @property
    def tobs(self) -> Arr2Dgtime_t:
        ...
class rnxctr_t:
    ephsat: int
    ephset: int
    nav: nav_t
    obs: obs_t
    sta: sta_t
    sys: int
    time: gtime_t
    tsys: int
    type: str
    ver: float
    def __init__(self) -> None:
        ...
    @property
    def opt(self) -> Arr1Dchar:
        ...
    @property
    def ptr(self) -> rnxctr_t:
        ...
    @property
    def tobs(self) -> Arr2Dchar:
        ...
class rnxopt_t:
    autopos: int
    freqtype: int
    halfcyc: int
    navsys: int
    obstype: int
    outiono: int
    outleaps: int
    outtime: int
    phshift: int
    rnxver: int
    sep_nav: int
    te: gtime_t
    tend: gtime_t
    tint: float
    trtcm: gtime_t
    ts: gtime_t
    tstart: gtime_t
    ttol: float
    tunit: float
    def __init__(self) -> None:
        ...
    @property
    def ant(self) -> Arr2Dchar:
        ...
    @property
    def antdel(self) -> Arr1Ddouble:
        ...
    @property
    def apppos(self) -> Arr1Ddouble:
        ...
    @property
    def comment(self) -> Arr2Dchar:
        ...
    @property
    def exsats(self) -> ...:
        ...
    @property
    def glo_cp_bias(self) -> Arr1Ddouble:
        ...
    @property
    def glofcn(self) -> Arr1Dint:
        ...
    @property
    def marker(self) -> Arr1Dchar:
        ...
    @property
    def markerno(self) -> Arr1Dchar:
        ...
    @property
    def markertype(self) -> Arr1Dchar:
        ...
    @property
    def mask(self) -> Arr2Dchar:
        ...
    @property
    def name(self) -> Arr2Dchar:
        ...
    @property
    def nobs(self) -> Arr1Dint:
        ...
    @property
    def prog(self) -> Arr1Dchar:
        ...
    @property
    def ptr(self) -> rnxopt_t:
        ...
    @property
    def rcvopt(self) -> Arr1Dchar:
        ...
    @property
    def rec(self) -> Arr2Dchar:
        ...
    @property
    def runby(self) -> Arr1Dchar:
        ...
    @property
    def shift(self) -> Arr2Ddouble:
        ...
    @property
    def staid(self) -> Arr1Dchar:
        ...
    @property
    def tobs(self) -> Arr2Dchar:
        ...
class rtcm_t:
    dgps: Arr1Ddgps_t
    ephsat: int
    ephset: int
    len: int
    nav: nav_t
    nbit: int
    nbyte: int
    obs: obs_t
    obsflag: int
    outtype: int
    seqno: int
    sta: sta_t
    stah: int
    staid: int
    time: gtime_t
    time_s: gtime_t
    word: int
    def __init__(self) -> None:
        ...
    @property
    def buff(self) -> ...:
        ...
    @property
    def cp(self) -> Arr2Ddouble:
        ...
    @property
    def lltime(self) -> Arr2Dgtime_t:
        ...
    @property
    def lock(self) -> ...:
        ...
    @property
    def loss(self) -> ...:
        ...
    @property
    def msg(self) -> Arr1Dchar:
        ...
    @property
    def msgtype(self) -> Arr1Dchar:
        ...
    @property
    def msmtype(self) -> Arr2Dchar:
        ...
    @property
    def nmsg2(self) -> ...:
        ...
    @property
    def nmsg3(self) -> ...:
        ...
    @property
    def opt(self) -> Arr1Dchar:
        ...
    @property
    def ptr(self) -> rtcm_t:
        ...
    @property
    def ssr(self) -> Arr1Dssr_t:
        ...
class rtk_t:
    P: Arr1Ddouble
    Pa: Arr1Ddouble
    na: int
    neb: int
    nfix: int
    nx: int
    opt: prcopt_t
    sol: sol_t
    tt: float
    x: Arr1Ddouble
    xa: Arr1Ddouble
    def __init__(self) -> None:
        ...
    @property
    def ambc(self) -> Arr1Dambc_t:
        ...
    @property
    def errbuf(self) -> Arr1Dchar:
        ...
    @property
    def ptr(self) -> rtk_t:
        ...
    @property
    def rb(self) -> Arr1Ddouble:
        ...
    @property
    def ssat(self) -> Arr1Dssat_t:
        ...
class rtksvr_t:
    bl_reset: float
    buffsize: int
    cputime: int
    cycle: int
    lock: pthread_mutex_t
    moni: Arr1Dstream_t
    nav: nav_t
    nave: int
    navsel: int
    nmeacycle: int
    nmeareq: int
    nsbs: int
    nsol: int
    prcout: int
    rtk: rtk_t
    state: int
    thread: int
    tick: int
    def __init__(self) -> None:
        ...
    @property
    def buff(self) -> ...:
        ...
    @property
    def cmd_reset(self) -> Arr1Dchar:
        ...
    @property
    def cmds_periodic(self) -> Arr2Dchar:
        ...
    @property
    def files(self) -> Arr2Dchar:
        ...
    @property
    def format(self) -> Arr1Dint:
        ...
    @property
    def ftime(self) -> Arr1Dgtime_t:
        ...
    @property
    def nb(self) -> Arr1Dint:
        ...
    @property
    def nmeapos(self) -> Arr1Ddouble:
        ...
    @property
    def nmsg(self) -> ...:
        ...
    @property
    def npb(self) -> Arr1Dint:
        ...
    @property
    def nsb(self) -> Arr1Dint:
        ...
    @property
    def obs(self) -> Arr2Dobs_t:
        ...
    @property
    def pbuf(self) -> ...:
        ...
    @property
    def ptr(self) -> rtksvr_t:
        ...
    @property
    def raw(self) -> Arr1Draw_t:
        ...
    @property
    def rb_ave(self) -> Arr1Ddouble:
        ...
    @property
    def rtcm(self) -> Arr1Drtcm_t:
        ...
    @property
    def sbsmsg(self) -> Arr1Dsbsmsg_t:
        ...
    @property
    def sbuf(self) -> ...:
        ...
    @property
    def solbuf(self) -> Arr1Dsol_t:
        ...
    @property
    def solopt(self) -> Arr1Dsolopt_t:
        ...
    @property
    def stream(self) -> Arr1Dstream_t:
        ...
class sbs_t:
    msgs: Arr1Dsbsmsg_t
    n: int
    nmax: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> sbs_t:
        ...
class sbsfcorr_t:
    ai: int
    dt: float
    iodf: int
    prc: float
    rrc: float
    t0: gtime_t
    udre: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> sbsfcorr_t:
        ...
class sbsigp_t:
    delay: float
    give: int
    lat: int
    lon: int
    t0: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> sbsigp_t:
        ...
class sbsigpband_t:
    bite: int
    bits: int
    x: int
    y: Arr1Dshort
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> sbsigpband_t:
        ...
class sbsion_t:
    iodi: int
    nigp: int
    def __init__(self) -> None:
        ...
    @property
    def igp(self) -> Arr1Dsbsigp_t:
        ...
    @property
    def ptr(self) -> sbsion_t:
        ...
class sbslcorr_t:
    daf0: float
    daf1: float
    iode: int
    t0: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def dpos(self) -> Arr1Ddouble:
        ...
    @property
    def dvel(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> sbslcorr_t:
        ...
class sbsmsg_t:
    prn: int
    rcv: int
    tow: int
    week: int
    def __init__(self) -> None:
        ...
    @property
    def msg(self) -> ...:
        ...
    @property
    def ptr(self) -> sbsmsg_t:
        ...
class sbssat_t:
    iodp: int
    nsat: int
    tlat: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> sbssat_t:
        ...
    @property
    def sat(self) -> Arr1Dsbssatp_t:
        ...
class sbssatp_t:
    fcorr: sbsfcorr_t
    lcorr: sbslcorr_t
    sat: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> sbssatp_t:
        ...
class seph_t:
    af0: float
    af1: float
    sat: int
    sva: int
    svh: int
    t0: gtime_t
    tof: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def acc(self) -> Arr1Ddouble:
        ...
    @property
    def pos(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> seph_t:
        ...
    @property
    def vel(self) -> Arr1Ddouble:
        ...
class snrmask_t:
    def __init__(self) -> None:
        ...
    @property
    def ena(self) -> Arr1Dint:
        ...
    @property
    def mask(self) -> Arr2Ddouble:
        ...
    @property
    def ptr(self) -> snrmask_t:
        ...
class sol_t:
    age: float
    ns: int
    ratio: float
    stat: int
    thres: float
    time: gtime_t
    type: int
    def __init__(self) -> None:
        ...
    @property
    def dtr(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> sol_t:
        ...
    @property
    def qr(self) -> Arr1Dfloat:
        ...
    @property
    def qv(self) -> Arr1Dfloat:
        ...
    @property
    def rr(self) -> Arr1Ddouble:
        ...
class solbuf_t:
    cyclic: int
    data: Arr1Dsol_t
    end: int
    n: int
    nb: int
    nmax: int
    start: int
    time: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def buff(self) -> ...:
        ...
    @property
    def ptr(self) -> solbuf_t:
        ...
    @property
    def rb(self) -> Arr1Ddouble:
        ...
class solopt_t:
    datum: int
    degf: int
    geoid: int
    height: int
    maxsolstd: float
    outhead: int
    outopt: int
    outvel: int
    posf: int
    solstatic: int
    sstat: int
    timef: int
    times: int
    timeu: int
    trace: int
    def __init__(self) -> None:
        ...
    @property
    def nmeaintv(self) -> Arr1Ddouble:
        ...
    @property
    def prog(self) -> Arr1Dchar:
        ...
    @property
    def ptr(self) -> solopt_t:
        ...
    @property
    def sep(self) -> Arr1Dchar:
        ...
class solstat_t:
    az: float
    el: float
    flag: int
    frq: int
    lock: int
    outc: int
    rejc: int
    resc: float
    resp: float
    sat: int
    slipc: int
    snr: int
    time: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> solstat_t:
        ...
class solstatbuf_t:
    data: Arr1Dsolstat_t
    n: int
    nmax: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> solstatbuf_t:
        ...
class ssat_t:
    phw: float
    sys: int
    vs: int
    def __init__(self) -> None:
        ...
    @property
    def azel(self) -> Arr1Ddouble:
        ...
    @property
    def fix(self) -> ...:
        ...
    @property
    def gf(self) -> Arr1Ddouble:
        ...
    @property
    def half(self) -> ...:
        ...
    @property
    def lock(self) -> Arr1Dint:
        ...
    @property
    def mw(self) -> Arr1Ddouble:
        ...
    @property
    def outc(self) -> ...:
        ...
    @property
    def ph(self) -> Arr2Ddouble:
        ...
    @property
    def pt(self) -> Arr2Dgtime_t:
        ...
    @property
    def ptr(self) -> ssat_t:
        ...
    @property
    def rejc(self) -> ...:
        ...
    @property
    def resc(self) -> Arr1Ddouble:
        ...
    @property
    def resp(self) -> Arr1Ddouble:
        ...
    @property
    def slip(self) -> ...:
        ...
    @property
    def slipc(self) -> ...:
        ...
    @property
    def snr(self) -> ...:
        ...
    @property
    def vsat(self) -> ...:
        ...
class ssr_t:
    hrclk: float
    iodcrc: int
    iode: int
    refd: int
    update: int
    ura: int
    yaw_ang: float
    yaw_rate: float
    def __init__(self) -> None:
        ...
    @property
    def cbias(self) -> Arr1Dfloat:
        ...
    @property
    def dclk(self) -> Arr1Ddouble:
        ...
    @property
    def ddeph(self) -> Arr1Ddouble:
        ...
    @property
    def deph(self) -> Arr1Ddouble:
        ...
    @property
    def iod(self) -> Arr1Dint:
        ...
    @property
    def pbias(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> ssr_t:
        ...
    @property
    def stdpb(self) -> Arr1Dfloat:
        ...
    @property
    def t0(self) -> Arr1Dgtime_t:
        ...
    @property
    def udi(self) -> Arr1Ddouble:
        ...
class sta_t:
    antsetup: int
    deltype: int
    glo_cp_align: int
    hgt: float
    itrf: int
    def __init__(self) -> None:
        ...
    @property
    def antdes(self) -> Arr1Dchar:
        ...
    @property
    def antsno(self) -> Arr1Dchar:
        ...
    @property
    def del(self) -> Arr1Ddouble:
        ...
    @property
    def glo_cp_bias(self) -> Arr1Ddouble:
        ...
    @property
    def marker(self) -> Arr1Dchar:
        ...
    @property
    def name(self) -> Arr1Dchar:
        ...
    @property
    def pos(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> sta_t:
        ...
    @property
    def recsno(self) -> Arr1Dchar:
        ...
    @property
    def rectype(self) -> Arr1Dchar:
        ...
    @property
    def recver(self) -> Arr1Dchar:
        ...
class strconv_t:
    itype: int
    nmsg: int
    otype: int
    out: rtcm_t
    raw: raw_t
    rtcm: rtcm_t
    stasel: int
    def __init__(self) -> None:
        ...
    @property
    def ephsat(self) -> Arr1Dint:
        ...
    @property
    def msgs(self) -> Arr1Dint:
        ...
    @property
    def ptr(self) -> strconv_t:
        ...
    @property
    def tick(self) -> ...:
        ...
    @property
    def tint(self) -> Arr1Ddouble:
        ...
class stream_t:
    inb: int
    inbt: int
    inr: int
    lock: pthread_mutex_t
    mode: int
    outb: int
    outbt: int
    outr: int
    port: ...
    state: int
    tact: int
    tick_i: int
    tick_o: int
    type: int
    def __init__(self) -> None:
        ...
    @property
    def msg(self) -> Arr1Dchar:
        ...
    @property
    def path(self) -> Arr1Dchar:
        ...
    @property
    def ptr(self) -> stream_t:
        ...
class strsvr_t:
    buff: ...
    buffsize: int
    cycle: int
    lock: pthread_mutex_t
    nmeacycle: int
    npb: int
    nstr: int
    pbuf: ...
    relayback: int
    state: int
    thread: int
    tick: int
    def __init__(self) -> None:
        ...
    @property
    def cmds_periodic(self) -> Arr2Dchar:
        ...
    @property
    def conv(self) -> Arr2Dstrconv_t:
        ...
    @property
    def nmeapos(self) -> Arr1Ddouble:
        ...
    @property
    def ptr(self) -> strsvr_t:
        ...
    @property
    def stream(self) -> Arr1Dstream_t:
        ...
    @property
    def strlog(self) -> Arr1Dstream_t:
        ...
class tec_t:
    data: Arr1Ddouble
    rb: float
    rms: Arr1Dfloat
    time: gtime_t
    def __init__(self) -> None:
        ...
    @property
    def hgts(self) -> Arr1Ddouble:
        ...
    @property
    def lats(self) -> Arr1Ddouble:
        ...
    @property
    def lons(self) -> Arr1Ddouble:
        ...
    @property
    def ndata(self) -> Arr1Dint:
        ...
    @property
    def ptr(self) -> tec_t:
        ...
class tle_t:
    data: Arr1Dtled_t
    n: int
    nmax: int
    def __init__(self) -> None:
        ...
    @property
    def ptr(self) -> tle_t:
        ...
class tled_t:
    M: float
    OMG: float
    bstar: float
    ecc: float
    eleno: int
    epoch: gtime_t
    etype: int
    inc: float
    n: float
    nddot: float
    ndot: float
    omg: float
    rev: int
    satclass: str
    def __init__(self) -> None:
        ...
    @property
    def alias(self) -> Arr1Dchar:
        ...
    @property
    def desig(self) -> Arr1Dchar:
        ...
    @property
    def name(self) -> Arr1Dchar:
        ...
    @property
    def ptr(self) -> tled_t:
        ...
    @property
    def satno(self) -> Arr1Dchar:
        ...
class url_t:
    tint: float
    def __init__(self) -> None:
        ...
    @property
    def dir(self) -> Arr1Dchar:
        ...
    @property
    def path(self) -> Arr1Dchar:
        ...
    @property
    def ptr(self) -> url_t:
        ...
    @property
    def type(self) -> Arr1Dchar:
        ...
def addsol(arg0: solbuf_t, arg1: sol_t) -> int:
    """
    rtklib addsol
    """
def adjgpsweek(arg0: int) -> int:
    """
    rtklib adjgpsweek
    """
def alm2pos(arg0: gtime_t, arg1: alm_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble) -> None:
    """
    rtklib alm2pos
    """
def antmodel(arg0: pcv_t, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: int, arg4: Arr1Ddouble) -> None:
    """
    rtklib antmodel
    """
def antmodel_s(arg0: pcv_t, arg1: float, arg2: Arr1Ddouble) -> None:
    """
    rtklib antmodel_s
    """
def bdt2gpst(arg0: gtime_t) -> gtime_t:
    """
    rtklib bdt2gpst
    """
def bdt2time(arg0: int, arg1: float) -> gtime_t:
    """
    rtklib bdt2time
    """
def closegeoid() -> None:
    """
    rtklib closegeoid
    """
def code2freq(arg0: int, arg1: int, arg2: int) -> float:
    """
    rtklib code2freq
    """
def code2idx(arg0: int, arg1: int) -> int:
    """
    rtklib code2idx
    """
def code2obs(arg0: int) -> str:
    """
    rtklib code2obs
    """
def convgpx(arg0: str, arg1: str, arg2: gtime_t, arg3: gtime_t, arg4: float, arg5: int, arg6: Arr1Ddouble, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
    """
    rtklib convgpx
    """
def convkml(arg0: str, arg1: str, arg2: gtime_t, arg3: gtime_t, arg4: float, arg5: int, arg6: Arr1Ddouble, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
    """
    rtklib convkml
    """
def convrnx(arg0: int, arg1: rnxopt_t, arg2: str, arg3: list[str]) -> int:
    """
    rtklib convrnx
    """
def covecef(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: Arr1Ddouble) -> None:
    """
    rtklib covecef
    """
def covenu(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: Arr1Ddouble) -> None:
    """
    rtklib covenu
    """
def createdir(arg0: str) -> None:
    """
    rtklib createdir
    """
def cross3(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: Arr1Ddouble) -> None:
    """
    rtklib cross3
    """
def decode_bds_d1(arg0: ..., arg1: eph_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble) -> int:
    """
    rtklib decode_bds_d1
    """
def decode_bds_d2(arg0: ..., arg1: eph_t, arg2: Arr1Ddouble) -> int:
    """
    rtklib decode_bds_d2
    """
def decode_frame(arg0: ..., arg1: eph_t, arg2: alm_t, arg3: Arr1Ddouble, arg4: Arr1Ddouble) -> int:
    """
    rtklib decode_frame
    """
def decode_gal_fnav(arg0: ..., arg1: eph_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble) -> int:
    """
    rtklib decode_gal_fnav
    """
def decode_gal_inav(arg0: ..., arg1: eph_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble) -> int:
    """
    rtklib decode_gal_inav
    """
def decode_glostr(arg0: ..., arg1: geph_t, arg2: Arr1Ddouble) -> int:
    """
    rtklib decode_glostr
    """
def decode_irn_nav(arg0: ..., arg1: eph_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble) -> int:
    """
    rtklib decode_irn_nav
    """
def decode_word(arg0: int, arg1: ...) -> int:
    """
    rtklib decode_word
    """
def deg2dms(arg0: float, arg1: Arr1Ddouble, arg2: int) -> None:
    """
    rtklib deg2dms
    """
def dl_exec(arg0: gtime_t, arg1: gtime_t, arg2: float, arg3: int, arg4: int, arg5: url_t, arg6: int, arg7: list[str], arg8: int, arg9: str, arg10: str, arg11: str, arg12: str, arg13: int, arg14: Arr1Dchar, arg15: str, arg16: str) -> int:
    """
    rtklib dl_exec
    """
def dl_readstas(arg0: str, arg1: list[str], arg2: int) -> int:
    """
    rtklib dl_readstas
    """
def dl_readurls(arg0: str, arg1: list[str], arg2: int, arg3: url_t, arg4: int) -> int:
    """
    rtklib dl_readurls
    """
def dl_test(arg0: gtime_t, arg1: gtime_t, arg2: float, arg3: url_t, arg4: int, arg5: list[str], arg6: int, arg7: str, arg8: int, arg9: int, arg10: str, arg11: str) -> None:
    """
    rtklib dl_test
    """
def dms2deg(arg0: Arr1Ddouble) -> float:
    """
    rtklib dms2deg
    """
def dops(arg0: int, arg1: Arr1Ddouble, arg2: float, arg3: Arr1Ddouble) -> None:
    """
    rtklib dops
    """
def dot(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: int) -> float:
    """
    rtklib dot
    """
def ecef2enu(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: Arr1Ddouble) -> None:
    """
    rtklib ecef2enu
    """
def ecef2pos(arg0: Arr1Ddouble, arg1: Arr1Ddouble) -> None:
    """
    rtklib ecef2pos
    """
def eci2ecef(arg0: gtime_t, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: Arr1Ddouble) -> None:
    """
    rtklib eci2ecef
    """
def enu2ecef(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: Arr1Ddouble) -> None:
    """
    rtklib enu2ecef
    """
def eph2clk(arg0: gtime_t, arg1: eph_t) -> float:
    """
    rtklib eph2clk
    """
def eph2pos(arg0: gtime_t, arg1: eph_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: Arr1Ddouble) -> None:
    """
    rtklib eph2pos
    """
def epoch2time(arg0: Arr1Ddouble) -> gtime_t:
    """
    rtklib epoch2time
    """
def execcmd(arg0: str) -> int:
    """
    rtklib execcmd
    """
def expath(arg0: str, arg1: list[str], arg2: int) -> int:
    """
    rtklib expath
    """
def eye(arg0: int) -> float:
    """
    rtklib eye
    """
def filter(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: Arr1Ddouble, arg5: int, arg6: int) -> int:
    """
    rtklib filter
    """
def free_raw(arg0: raw_t) -> None:
    """
    rtklib free_raw
    """
def free_rnxctr(arg0: rnxctr_t) -> None:
    """
    rtklib free_rnxctr
    """
def free_rt17(arg0: raw_t) -> None:
    """
    rtklib free_rt17
    """
def free_rtcm(arg0: rtcm_t) -> None:
    """
    rtklib free_rtcm
    """
def freenav(arg0: nav_t, arg1: int) -> None:
    """
    rtklib freenav
    """
def freeobs(arg0: obs_t) -> None:
    """
    rtklib freeobs
    """
def freesolbuf(arg0: solbuf_t) -> None:
    """
    rtklib freesolbuf
    """
def freesolstatbuf(arg0: solstatbuf_t) -> None:
    """
    rtklib freesolstatbuf
    """
def gen_nvs(arg0: str, arg1: ...) -> int:
    """
    rtklib gen_nvs
    """
def gen_rtcm2(arg0: rtcm_t, arg1: int, arg2: int) -> int:
    """
    rtklib gen_rtcm2
    """
def gen_rtcm3(arg0: rtcm_t, arg1: int, arg2: int, arg3: int) -> int:
    """
    rtklib gen_rtcm3
    """
def gen_stq(arg0: str, arg1: ...) -> int:
    """
    rtklib gen_stq
    """
def gen_ubx(arg0: str, arg1: ...) -> int:
    """
    rtklib gen_ubx
    """
def geodist(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: Arr1Ddouble) -> float:
    """
    rtklib geodist
    """
def geoidh(arg0: Arr1Ddouble) -> float:
    """
    rtklib geoidh
    """
def geph2clk(arg0: gtime_t, arg1: geph_t) -> float:
    """
    rtklib geph2clk
    """
def geph2pos(arg0: gtime_t, arg1: geph_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: Arr1Ddouble) -> None:
    """
    rtklib geph2pos
    """
def getbits(arg0: ..., arg1: int, arg2: int) -> int:
    """
    rtklib getbits
    """
def getbitu(arg0: ..., arg1: int, arg2: int) -> int:
    """
    rtklib getbitu
    """
def getcodepri(arg0: int, arg1: int, arg2: str) -> int:
    """
    rtklib getcodepri
    """
def geterp(arg0: erp_t, arg1: gtime_t, arg2: Arr1Ddouble) -> int:
    """
    rtklib geterp
    """
def getseleph(arg0: int) -> int:
    """
    rtklib getseleph
    """
def getsol(arg0: solbuf_t, arg1: int) -> sol_t:
    """
    rtklib getsol
    """
def getsysopts(arg0: prcopt_t, arg1: solopt_t, arg2: filopt_t) -> None:
    """
    rtklib getsysopts
    """
def gis_free(arg0: gis_t) -> None:
    """
    rtklib gis_free
    """
def gis_read(arg0: str, arg1: gis_t, arg2: int) -> int:
    """
    rtklib gis_read
    """
def gpst2bdt(arg0: gtime_t) -> gtime_t:
    """
    rtklib gpst2bdt
    """
def gpst2time(arg0: int, arg1: float) -> gtime_t:
    """
    rtklib gpst2time
    """
def gpst2utc(arg0: gtime_t) -> gtime_t:
    """
    rtklib gpst2utc
    """
def gst2time(arg0: int, arg1: float) -> gtime_t:
    """
    rtklib gst2time
    """
def imat(arg0: int, arg1: int) -> int:
    """
    rtklib imat
    """
def init_raw(arg0: raw_t, arg1: int) -> int:
    """
    rtklib init_raw
    """
def init_rnxctr(arg0: rnxctr_t) -> int:
    """
    rtklib init_rnxctr
    """
def init_rt17(arg0: raw_t) -> int:
    """
    rtklib init_rt17
    """
def init_rtcm(arg0: rtcm_t) -> int:
    """
    rtklib init_rtcm
    """
def initsolbuf(arg0: solbuf_t, arg1: int, arg2: int) -> None:
    """
    rtklib initsolbuf
    """
def input_bnx(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_bnx
    """
def input_bnxf(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_bnxf
    """
def input_cres(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_cres
    """
def input_cresf(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_cresf
    """
def input_javad(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_javad
    """
def input_javadf(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_javadf
    """
def input_nvs(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_nvs
    """
def input_nvsf(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_nvsf
    """
def input_oem3(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_oem3
    """
def input_oem3f(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_oem3f
    """
def input_oem4(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_oem4
    """
def input_oem4f(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_oem4f
    """
def input_raw(arg0: raw_t, arg1: int, arg2: int) -> int:
    """
    rtklib input_raw
    """
def input_rawf(arg0: raw_t, arg1: int, arg2: str, arg3: str) -> int:
    """
    rtklib input_rawf
    """
def input_rnxctr(arg0: rnxctr_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_rnxctr
    """
def input_rt17(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_rt17
    """
def input_rt17f(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_rt17f
    """
def input_rtcm2(arg0: rtcm_t, arg1: int) -> int:
    """
    rtklib input_rtcm2
    """
def input_rtcm2f(arg0: rtcm_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_rtcm2f
    """
def input_rtcm3(arg0: rtcm_t, arg1: int) -> int:
    """
    rtklib input_rtcm3
    """
def input_rtcm3f(arg0: rtcm_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_rtcm3f
    """
def input_sbf(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_sbf
    """
def input_sbff(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_sbff
    """
def input_ss2(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_ss2
    """
def input_ss2f(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_ss2f
    """
def input_stq(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_stq
    """
def input_stqf(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_stqf
    """
def input_ubx(arg0: raw_t, arg1: int) -> int:
    """
    rtklib input_ubx
    """
def input_ubxf(arg0: raw_t, arg1: str, arg2: str) -> int:
    """
    rtklib input_ubxf
    """
def inputsol(arg0: int, arg1: gtime_t, arg2: gtime_t, arg3: float, arg4: int, arg5: solopt_t, arg6: solbuf_t) -> int:
    """
    rtklib inputsol
    """
def ionmapf(arg0: Arr1Ddouble, arg1: Arr1Ddouble) -> float:
    """
    rtklib ionmapf
    """
def ionmodel(arg0: gtime_t, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: Arr1Ddouble) -> float:
    """
    rtklib ionmodel
    """
def ionocorr(arg0: gtime_t, arg1: nav_t, arg2: int, arg3: Arr1Ddouble, arg4: Arr1Ddouble, arg5: int, arg6: Arr1Ddouble, arg7: Arr1Ddouble) -> int:
    """
    rtklib ionocorr
    """
def ionppp(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: float, arg3: float, arg4: Arr1Ddouble) -> float:
    """
    rtklib ionppp
    """
def iontec(arg0: gtime_t, arg1: nav_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: int, arg5: Arr1Ddouble, arg6: Arr1Ddouble) -> int:
    """
    rtklib iontec
    """
def jgd2tokyo(arg0: Arr1Ddouble) -> int:
    """
    rtklib jgd2tokyo
    """
def lambda(arg0: int, arg1: int, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: Arr1Ddouble, arg5: Arr1Ddouble) -> int:
    """
    rtklib lambda
    """
def lambda_reduction(arg0: int, arg1: Arr1Ddouble, arg2: Arr1Ddouble) -> int:
    """
    rtklib lambda_reduction
    """
def lambda_search(arg0: int, arg1: int, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: Arr1Ddouble, arg5: Arr1Ddouble) -> int:
    """
    rtklib lambda_search
    """
def loaddatump(arg0: str) -> int:
    """
    rtklib loaddatump
    """
def loadopts(arg0: str, arg1: opt_t) -> int:
    """
    rtklib loadopts
    """
def lsq(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: int, arg3: int, arg4: Arr1Ddouble, arg5: Arr1Ddouble) -> int:
    """
    rtklib lsq
    """
def mat(arg0: int, arg1: int) -> float:
    """
    rtklib mat
    """
def matcpy(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: int, arg3: int) -> None:
    """
    rtklib matcpy
    """
def matfprint(arg0: Arr1Ddouble, arg1: int, arg2: int, arg3: int, arg4: int, arg5: str, arg6: str) -> None:
    """
    rtklib matfprint
    """
def matinv(arg0: Arr1Ddouble, arg1: int) -> int:
    """
    rtklib matinv
    """
def matmul(arg0: str, arg1: int, arg2: int, arg3: int, arg4: float, arg5: Arr1Ddouble, arg6: Arr1Ddouble, arg7: float, arg8: Arr1Ddouble) -> None:
    """
    rtklib matmul
    """
def matprint(arg0: Arr1Ddouble, arg1: int, arg2: int, arg3: int, arg4: int) -> None:
    """
    rtklib matprint
    """
def norm(arg0: Arr1Ddouble, arg1: int) -> float:
    """
    rtklib norm
    """
def normv3(arg0: Arr1Ddouble, arg1: Arr1Ddouble) -> int:
    """
    rtklib normv3
    """
def obs2code(arg0: str) -> int:
    """
    rtklib obs2code
    """
def open_rnxctr(arg0: rnxctr_t, arg1: str, arg2: str) -> int:
    """
    rtklib open_rnxctr
    """
def opengeoid(arg0: int, arg1: str) -> int:
    """
    rtklib opengeoid
    """
def opt2buf(arg0: opt_t, arg1: Arr1Dchar) -> int:
    """
    rtklib opt2buf
    """
def opt2str(arg0: opt_t, arg1: Arr1Dchar) -> int:
    """
    rtklib opt2str
    """
def outnmea_gga(arg0: ..., arg1: sol_t) -> int:
    """
    rtklib outnmea_gga
    """
def outnmea_gsa(arg0: ..., arg1: sol_t, arg2: ssat_t) -> int:
    """
    rtklib outnmea_gsa
    """
def outnmea_gsv(arg0: ..., arg1: sol_t, arg2: ssat_t) -> int:
    """
    rtklib outnmea_gsv
    """
def outnmea_rmc(arg0: ..., arg1: sol_t) -> int:
    """
    rtklib outnmea_rmc
    """
def outprcopt(arg0: str, arg1: str, arg2: prcopt_t) -> None:
    """
    rtklib outprcopt
    """
def outprcopts(arg0: ..., arg1: prcopt_t) -> int:
    """
    rtklib outprcopts
    """
def outrnxcnavh(arg0: str, arg1: str, arg2: rnxopt_t, arg3: nav_t) -> int:
    """
    rtklib outrnxcnavh
    """
def outrnxgnavb(arg0: str, arg1: str, arg2: rnxopt_t, arg3: geph_t) -> int:
    """
    rtklib outrnxgnavb
    """
def outrnxgnavh(arg0: str, arg1: str, arg2: rnxopt_t, arg3: nav_t) -> int:
    """
    rtklib outrnxgnavh
    """
def outrnxhnavb(arg0: str, arg1: str, arg2: rnxopt_t, arg3: seph_t) -> int:
    """
    rtklib outrnxhnavb
    """
def outrnxhnavh(arg0: str, arg1: str, arg2: rnxopt_t, arg3: nav_t) -> int:
    """
    rtklib outrnxhnavh
    """
def outrnxinavh(arg0: str, arg1: str, arg2: rnxopt_t, arg3: nav_t) -> int:
    """
    rtklib outrnxinavh
    """
def outrnxlnavh(arg0: str, arg1: str, arg2: rnxopt_t, arg3: nav_t) -> int:
    """
    rtklib outrnxlnavh
    """
def outrnxnavb(arg0: str, arg1: str, arg2: rnxopt_t, arg3: eph_t) -> int:
    """
    rtklib outrnxnavb
    """
def outrnxnavh(arg0: str, arg1: str, arg2: rnxopt_t, arg3: nav_t) -> int:
    """
    rtklib outrnxnavh
    """
def outrnxobsb(arg0: str, arg1: str, arg2: rnxopt_t, arg3: obsd_t, arg4: int, arg5: int) -> int:
    """
    rtklib outrnxobsb
    """
def outrnxobsh(arg0: str, arg1: str, arg2: rnxopt_t, arg3: nav_t) -> int:
    """
    rtklib outrnxobsh
    """
def outrnxqnavh(arg0: str, arg1: str, arg2: rnxopt_t, arg3: nav_t) -> int:
    """
    rtklib outrnxqnavh
    """
def outsol(arg0: str, arg1: str, arg2: sol_t, arg3: Arr1Ddouble, arg4: solopt_t) -> None:
    """
    rtklib outsol
    """
def outsolex(arg0: str, arg1: str, arg2: sol_t, arg3: ssat_t, arg4: solopt_t) -> None:
    """
    rtklib outsolex
    """
def outsolexs(arg0: ..., arg1: sol_t, arg2: ssat_t, arg3: solopt_t) -> int:
    """
    rtklib outsolexs
    """
def outsolhead(arg0: str, arg1: str, arg2: solopt_t) -> None:
    """
    rtklib outsolhead
    """
def outsolheads(arg0: ..., arg1: solopt_t) -> int:
    """
    rtklib outsolheads
    """
def outsols(arg0: ..., arg1: sol_t, arg2: Arr1Ddouble, arg3: solopt_t) -> int:
    """
    rtklib outsols
    """
def peph2pos(arg0: gtime_t, arg1: int, arg2: nav_t, arg3: int, arg4: Arr1Ddouble, arg5: Arr1Ddouble, arg6: Arr1Ddouble) -> int:
    """
    rtklib peph2pos
    """
def pntpos(arg0: obsd_t, arg1: int, arg2: nav_t, arg3: prcopt_t, arg4: sol_t, arg5: Arr1Ddouble, arg6: ssat_t, arg7: Arr1Dchar) -> int:
    """
    rtklib pntpos
    """
def pos2ecef(arg0: Arr1Ddouble, arg1: Arr1Ddouble) -> None:
    """
    rtklib pos2ecef
    """
def postpos(arg0: gtime_t, arg1: gtime_t, arg2: float, arg3: float, arg4: prcopt_t, arg5: solopt_t, arg6: filopt_t, arg7: list[str], arg8: int, arg9: Arr1Dchar, arg10: str, arg11: str) -> int:
    """
    rtklib postpos
    """
def ppp_ar(arg0: rtk_t, arg1: obsd_t, arg2: int, arg3: Arr1Dint, arg4: nav_t, arg5: Arr1Ddouble, arg6: Arr1Ddouble, arg7: Arr1Ddouble) -> int:
    """
    rtklib ppp_ar
    """
def pppnx(arg0: prcopt_t) -> int:
    """
    rtklib pppnx
    """
def pppos(arg0: rtk_t, arg1: obsd_t, arg2: int, arg3: nav_t) -> None:
    """
    rtklib pppos
    """
def pppoutstat(arg0: rtk_t, arg1: Arr1Dchar) -> int:
    """
    rtklib pppoutstat
    """
def read_leaps(arg0: str) -> int:
    """
    rtklib read_leaps
    """
def readblq(arg0: str, arg1: str, arg2: Arr1Ddouble) -> int:
    """
    rtklib readblq
    """
def readdcb(arg0: str, arg1: nav_t, arg2: sta_t) -> int:
    """
    rtklib readdcb
    """
def readerp(arg0: str, arg1: erp_t) -> int:
    """
    rtklib readerp
    """
def readnav(arg0: str, arg1: nav_t) -> int:
    """
    rtklib readnav
    """
def readpcv(arg0: str, arg1: pcvs_t) -> int:
    """
    rtklib readpcv
    """
def readpos(arg0: str, arg1: str, arg2: Arr1Ddouble) -> None:
    """
    rtklib readpos
    """
def readrnx(arg0: str, arg1: int, arg2: str, arg3: obs_t, arg4: nav_t, arg5: sta_t) -> int:
    """
    rtklib readrnx
    """
def readrnxc(arg0: str, arg1: nav_t) -> int:
    """
    rtklib readrnxc
    """
def readrnxt(arg0: str, arg1: int, arg2: gtime_t, arg3: gtime_t, arg4: float, arg5: str, arg6: obs_t, arg7: nav_t, arg8: sta_t) -> int:
    """
    rtklib readrnxt
    """
def readsap(arg0: str, arg1: gtime_t, arg2: nav_t) -> int:
    """
    rtklib readsap
    """
def readsol(arg0: list[str], arg1: int, arg2: solbuf_t) -> int:
    """
    rtklib readsol
    """
def readsolstat(arg0: list[str], arg1: int, arg2: solstatbuf_t) -> int:
    """
    rtklib readsolstat
    """
def readsolstatt(arg0: list[str], arg1: int, arg2: gtime_t, arg3: gtime_t, arg4: float, arg5: solstatbuf_t) -> int:
    """
    rtklib readsolstatt
    """
def readsolt(arg0: list[str], arg1: int, arg2: gtime_t, arg3: gtime_t, arg4: float, arg5: int, arg6: solbuf_t) -> int:
    """
    rtklib readsolt
    """
def readsp3(arg0: str, arg1: nav_t, arg2: int) -> None:
    """
    rtklib readsp3
    """
def readtec(arg0: str, arg1: nav_t, arg2: int) -> None:
    """
    rtklib readtec
    """
def reppath(arg0: str, arg1: Arr1Dchar, arg2: gtime_t, arg3: str, arg4: str) -> int:
    """
    rtklib reppath
    """
def reppaths(arg0: str, arg1: list[str], arg2: int, arg3: gtime_t, arg4: gtime_t, arg5: str, arg6: str) -> int:
    """
    rtklib reppaths
    """
def resetsysopts() -> None:
    """
    rtklib resetsysopts
    """
def rtk_crc16(arg0: ..., arg1: int) -> int:
    """
    rtklib rtk_crc16
    """
def rtk_crc24q(arg0: ..., arg1: int) -> int:
    """
    rtklib rtk_crc24q
    """
def rtk_crc32(arg0: ..., arg1: int) -> int:
    """
    rtklib rtk_crc32
    """
def rtk_uncompress(arg0: str, arg1: Arr1Dchar) -> int:
    """
    rtklib rtk_uncompress
    """
def rtkclosestat() -> None:
    """
    rtklib rtkclosestat
    """
def rtkfree(arg0: rtk_t) -> None:
    """
    rtklib rtkfree
    """
def rtkinit(arg0: rtk_t, arg1: prcopt_t) -> None:
    """
    rtklib rtkinit
    """
def rtkopenstat(arg0: str, arg1: int) -> int:
    """
    rtklib rtkopenstat
    """
def rtkoutstat(arg0: rtk_t, arg1: Arr1Dchar) -> int:
    """
    rtklib rtkoutstat
    """
def rtkpos(arg0: rtk_t, arg1: obsd_t, arg2: int, arg3: nav_t) -> int:
    """
    rtklib rtkpos
    """
def rtksvrclosestr(arg0: rtksvr_t, arg1: int) -> None:
    """
    rtklib rtksvrclosestr
    """
def rtksvrfree(arg0: rtksvr_t) -> None:
    """
    rtklib rtksvrfree
    """
def rtksvrinit(arg0: rtksvr_t) -> int:
    """
    rtklib rtksvrinit
    """
def rtksvrlock(arg0: rtksvr_t) -> None:
    """
    rtklib rtksvrlock
    """
def rtksvrmark(arg0: rtksvr_t, arg1: str, arg2: str) -> int:
    """
    rtklib rtksvrmark
    """
def rtksvropenstr(arg0: rtksvr_t, arg1: int, arg2: int, arg3: str, arg4: solopt_t) -> int:
    """
    rtklib rtksvropenstr
    """
def rtksvrostat(arg0: rtksvr_t, arg1: int, arg2: gtime_t, arg3: Arr1Dint, arg4: Arr1Ddouble, arg5: Arr1Ddouble, arg6: list[list[int]], arg7: Arr1Dint) -> int:
    """
    rtklib rtksvrostat
    """
def rtksvrsstat(arg0: rtksvr_t, arg1: Arr1Dint, arg2: Arr1Dchar) -> None:
    """
    rtklib rtksvrsstat
    """
def rtksvrstart(arg0: rtksvr_t, arg1: int, arg2: int, arg3: Arr1Dint, arg4: list[str], arg5: Arr1Dint, arg6: int, arg7: list[str], arg8: list[str], arg9: list[str], arg10: int, arg11: int, arg12: Arr1Ddouble, arg13: prcopt_t, arg14: solopt_t, arg15: stream_t, arg16: Arr1Dchar) -> int:
    """
    rtklib rtksvrstart
    """
def rtksvrstop(arg0: rtksvr_t, arg1: list[str]) -> None:
    """
    rtklib rtksvrstop
    """
def rtksvrunlock(arg0: rtksvr_t) -> None:
    """
    rtklib rtksvrunlock
    """
def sat2freq(arg0: int, arg1: int, arg2: nav_t) -> float:
    """
    rtklib sat2freq
    """
def satantoff(arg0: gtime_t, arg1: Arr1Ddouble, arg2: int, arg3: nav_t, arg4: Arr1Ddouble) -> None:
    """
    rtklib satantoff
    """
def satazel(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: Arr1Ddouble) -> float:
    """
    rtklib satazel
    """
def satexclude(arg0: int, arg1: float, arg2: int, arg3: prcopt_t) -> int:
    """
    rtklib satexclude
    """
def satid2no(arg0: str) -> int:
    """
    rtklib satid2no
    """
def satno(arg0: int, arg1: int) -> int:
    """
    rtklib satno
    """
def satno2id(arg0: int, arg1: Arr1Dchar) -> None:
    """
    rtklib satno2id
    """
def satpos(arg0: gtime_t, arg1: gtime_t, arg2: int, arg3: int, arg4: nav_t, arg5: Arr1Ddouble, arg6: Arr1Ddouble, arg7: Arr1Ddouble, arg8: Arr1Dint) -> int:
    """
    rtklib satpos
    """
def satposs(arg0: gtime_t, arg1: obsd_t, arg2: int, arg3: nav_t, arg4: int, arg5: Arr1Ddouble, arg6: Arr1Ddouble, arg7: Arr1Ddouble, arg8: Arr1Dint) -> None:
    """
    rtklib satposs
    """
def satsys(arg0: int, arg1: Arr1Dint) -> int:
    """
    rtklib satsys
    """
def savenav(arg0: str, arg1: nav_t) -> int:
    """
    rtklib savenav
    """
def saveopts(arg0: str, arg1: str, arg2: str, arg3: opt_t) -> int:
    """
    rtklib saveopts
    """
def sbsdecodemsg(arg0: gtime_t, arg1: int, arg2: ..., arg3: sbsmsg_t) -> int:
    """
    rtklib sbsdecodemsg
    """
def sbsioncorr(arg0: gtime_t, arg1: nav_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: Arr1Ddouble, arg5: Arr1Ddouble) -> int:
    """
    rtklib sbsioncorr
    """
def sbsoutmsg(arg0: str, arg1: str, arg2: sbsmsg_t) -> None:
    """
    rtklib sbsoutmsg
    """
def sbsreadmsg(arg0: str, arg1: int, arg2: sbs_t) -> int:
    """
    rtklib sbsreadmsg
    """
def sbsreadmsgt(arg0: str, arg1: int, arg2: gtime_t, arg3: gtime_t, arg4: sbs_t) -> int:
    """
    rtklib sbsreadmsgt
    """
def sbssatcorr(arg0: gtime_t, arg1: int, arg2: nav_t, arg3: Arr1Ddouble, arg4: Arr1Ddouble, arg5: Arr1Ddouble) -> int:
    """
    rtklib sbssatcorr
    """
def sbstropcorr(arg0: gtime_t, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: Arr1Ddouble) -> float:
    """
    rtklib sbstropcorr
    """
def sbsupdatecorr(arg0: sbsmsg_t, arg1: nav_t) -> int:
    """
    rtklib sbsupdatecorr
    """
def screent(arg0: gtime_t, arg1: gtime_t, arg2: gtime_t, arg3: float) -> int:
    """
    rtklib screent
    """
def searchopt(arg0: str, arg1: opt_t) -> opt_t:
    """
    rtklib searchopt
    """
def searchpcv(arg0: int, arg1: str, arg2: gtime_t, arg3: pcvs_t) -> pcv_t:
    """
    rtklib searchpcv
    """
def seph2clk(arg0: gtime_t, arg1: seph_t) -> float:
    """
    rtklib seph2clk
    """
def seph2pos(arg0: gtime_t, arg1: seph_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: Arr1Ddouble) -> None:
    """
    rtklib seph2pos
    """
def setbits(arg0: ..., arg1: int, arg2: int, arg3: int) -> None:
    """
    rtklib setbits
    """
def setbitu(arg0: ..., arg1: int, arg2: int, arg3: int) -> None:
    """
    rtklib setbitu
    """
def setcodepri(arg0: int, arg1: int, arg2: str) -> None:
    """
    rtklib setcodepri
    """
def setseleph(arg0: int, arg1: int) -> None:
    """
    rtklib setseleph
    """
def setsysopts(arg0: prcopt_t, arg1: solopt_t, arg2: filopt_t) -> None:
    """
    rtklib setsysopts
    """
def settime(arg0: gtime_t) -> None:
    """
    rtklib settime
    """
def settspan(arg0: gtime_t, arg1: gtime_t) -> None:
    """
    rtklib settspan
    """
def sleepms(arg0: int) -> None:
    """
    rtklib sleepms
    """
def smoother(arg0: Arr1Ddouble, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: int, arg5: Arr1Ddouble, arg6: Arr1Ddouble) -> int:
    """
    rtklib smoother
    """
def solve(arg0: str, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: int, arg4: int, arg5: Arr1Ddouble) -> int:
    """
    rtklib solve
    """
def sortobs(arg0: obs_t) -> int:
    """
    rtklib sortobs
    """
def str2num(arg0: str, arg1: int, arg2: int) -> float:
    """
    rtklib str2num
    """
def str2opt(arg0: opt_t, arg1: str) -> int:
    """
    rtklib str2opt
    """
def str2time(arg0: str, arg1: int, arg2: int, arg3: gtime_t) -> int:
    """
    rtklib str2time
    """
def strclose(arg0: stream_t) -> None:
    """
    rtklib strclose
    """
def strconvfree(arg0: strconv_t) -> None:
    """
    rtklib strconvfree
    """
def strconvnew(arg0: int, arg1: int, arg2: str, arg3: int, arg4: int, arg5: str) -> strconv_t:
    """
    rtklib strconvnew
    """
def strgettime(arg0: stream_t) -> gtime_t:
    """
    rtklib strgettime
    """
def strinit(arg0: stream_t) -> None:
    """
    rtklib strinit
    """
def strinitcom() -> None:
    """
    rtklib strinitcom
    """
def strlock(arg0: stream_t) -> None:
    """
    rtklib strlock
    """
def stropen(arg0: stream_t, arg1: int, arg2: int, arg3: str) -> int:
    """
    rtklib stropen
    """
def strread(arg0: stream_t, arg1: ..., arg2: int) -> int:
    """
    rtklib strread
    """
def strsendcmd(arg0: stream_t, arg1: str) -> None:
    """
    rtklib strsendcmd
    """
def strsendnmea(arg0: stream_t, arg1: sol_t) -> None:
    """
    rtklib strsendnmea
    """
def strsetdir(arg0: str) -> None:
    """
    rtklib strsetdir
    """
def strsetopt(arg0: Arr1Dint) -> None:
    """
    rtklib strsetopt
    """
def strsetproxy(arg0: str) -> None:
    """
    rtklib strsetproxy
    """
def strsettimeout(arg0: stream_t, arg1: int, arg2: int) -> None:
    """
    rtklib strsettimeout
    """
def strstat(arg0: stream_t, arg1: Arr1Dchar) -> int:
    """
    rtklib strstat
    """
def strstatx(arg0: stream_t, arg1: Arr1Dchar) -> int:
    """
    rtklib strstatx
    """
def strsum(arg0: stream_t, arg1: Arr1Dint, arg2: Arr1Dint, arg3: Arr1Dint, arg4: Arr1Dint) -> None:
    """
    rtklib strsum
    """
def strsvrinit(arg0: strsvr_t, arg1: int) -> None:
    """
    rtklib strsvrinit
    """
def strsvrstart(arg0: strsvr_t, arg1: Arr1Dint, arg2: Arr1Dint, arg3: list[str], arg4: list[str], arg5: list[list[strconv_t]], arg6: list[str], arg7: list[str], arg8: Arr1Ddouble) -> int:
    """
    rtklib strsvrstart
    """
def strsvrstat(arg0: strsvr_t, arg1: Arr1Dint, arg2: Arr1Dint, arg3: Arr1Dint, arg4: Arr1Dint, arg5: Arr1Dchar) -> None:
    """
    rtklib strsvrstat
    """
def strsvrstop(arg0: strsvr_t, arg1: list[str]) -> None:
    """
    rtklib strsvrstop
    """
def strsync(arg0: stream_t, arg1: stream_t) -> None:
    """
    rtklib strsync
    """
def strunlock(arg0: stream_t) -> None:
    """
    rtklib strunlock
    """
def strwrite(arg0: stream_t, arg1: ..., arg2: int) -> int:
    """
    rtklib strwrite
    """
def sunmoonpos(arg0: gtime_t, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: Arr1Ddouble) -> None:
    """
    rtklib sunmoonpos
    """
def test_glostr(arg0: ...) -> int:
    """
    rtklib test_glostr
    """
def testsnr(arg0: int, arg1: int, arg2: float, arg3: float, arg4: snrmask_t) -> int:
    """
    rtklib testsnr
    """
def tickget() -> int:
    """
    rtklib tickget
    """
def tidedisp(arg0: gtime_t, arg1: Arr1Ddouble, arg2: int, arg3: erp_t, arg4: Arr1Ddouble, arg5: Arr1Ddouble) -> None:
    """
    rtklib tidedisp
    """
def time2bdt(arg0: gtime_t, arg1: Arr1Dint) -> float:
    """
    rtklib time2bdt
    """
def time2doy(arg0: gtime_t) -> float:
    """
    rtklib time2doy
    """
def time2epoch(arg0: gtime_t, arg1: Arr1Ddouble) -> None:
    """
    rtklib time2epoch
    """
def time2gpst(arg0: gtime_t, arg1: Arr1Dint) -> float:
    """
    rtklib time2gpst
    """
def time2gst(arg0: gtime_t, arg1: Arr1Dint) -> float:
    """
    rtklib time2gst
    """
def time2str(arg0: gtime_t, arg1: Arr1Dchar, arg2: int) -> None:
    """
    rtklib time2str
    """
def time_str(arg0: gtime_t, arg1: int) -> str:
    """
    rtklib time_str
    """
def timeadd(arg0: gtime_t, arg1: float) -> gtime_t:
    """
    rtklib timeadd
    """
def timediff(arg0: gtime_t, arg1: gtime_t) -> float:
    """
    rtklib timediff
    """
def timeget() -> gtime_t:
    """
    rtklib timeget
    """
def timereset() -> None:
    """
    rtklib timereset
    """
def timeset(arg0: gtime_t) -> None:
    """
    rtklib timeset
    """
def tle_name_read(arg0: str, arg1: tle_t) -> int:
    """
    rtklib tle_name_read
    """
def tle_pos(arg0: gtime_t, arg1: str, arg2: str, arg3: str, arg4: tle_t, arg5: erp_t, arg6: Arr1Ddouble) -> int:
    """
    rtklib tle_pos
    """
def tle_read(arg0: str, arg1: tle_t) -> int:
    """
    rtklib tle_read
    """
def tokyo2jgd(arg0: Arr1Ddouble) -> int:
    """
    rtklib tokyo2jgd
    """
def traceb(arg0: int, arg1: ..., arg2: int) -> None:
    """
    rtklib traceb
    """
def traceclose() -> None:
    """
    rtklib traceclose
    """
def tracegnav(arg0: int, arg1: nav_t) -> None:
    """
    rtklib tracegnav
    """
def tracehnav(arg0: int, arg1: nav_t) -> None:
    """
    rtklib tracehnav
    """
def tracelevel(arg0: int) -> None:
    """
    rtklib tracelevel
    """
def tracemat(arg0: int, arg1: Arr1Ddouble, arg2: int, arg3: int, arg4: int, arg5: int) -> None:
    """
    rtklib tracemat
    """
def tracenav(arg0: int, arg1: nav_t) -> None:
    """
    rtklib tracenav
    """
def traceobs(arg0: int, arg1: obsd_t, arg2: int) -> None:
    """
    rtklib traceobs
    """
def traceopen(arg0: str) -> None:
    """
    rtklib traceopen
    """
def tracepclk(arg0: int, arg1: nav_t) -> None:
    """
    rtklib tracepclk
    """
def tracepeph(arg0: int, arg1: nav_t) -> None:
    """
    rtklib tracepeph
    """
def tropcorr(arg0: gtime_t, arg1: nav_t, arg2: Arr1Ddouble, arg3: Arr1Ddouble, arg4: int, arg5: Arr1Ddouble, arg6: Arr1Ddouble) -> int:
    """
    rtklib tropcorr
    """
def tropmapf(arg0: gtime_t, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: Arr1Ddouble) -> float:
    """
    rtklib tropmapf
    """
def tropmodel(arg0: gtime_t, arg1: Arr1Ddouble, arg2: Arr1Ddouble, arg3: float) -> float:
    """
    rtklib tropmodel
    """
def uniqnav(arg0: nav_t) -> None:
    """
    rtklib uniqnav
    """
def utc2gmst(arg0: gtime_t, arg1: float) -> float:
    """
    rtklib utc2gmst
    """
def utc2gpst(arg0: gtime_t) -> gtime_t:
    """
    rtklib utc2gpst
    """
def xyz2enu(arg0: Arr1Ddouble, arg1: Arr1Ddouble) -> None:
    """
    rtklib xyz2enu
    """
def zeros(arg0: int, arg1: int) -> float:
    """
    rtklib zeros
    """
ARMODE_CONT: int = 1
ARMODE_FIXHOLD: int = 3
ARMODE_INST: int = 2
ARMODE_OFF: int = 0
ARMODE_TCAR: int = 5
ARMODE_WLNL: int = 4
AS2R: float = 4.84813681109536e-06
AU: float = 149597870691.0
CLIGHT: float = 299792458.0
CODE_L1A: int = 10
CODE_L1B: int = 11
CODE_L1C: int = 1
CODE_L1D: int = 56
CODE_L1E: int = 9
CODE_L1I: int = 47
CODE_L1L: int = 8
CODE_L1M: int = 5
CODE_L1N: int = 6
CODE_L1P: int = 2
CODE_L1Q: int = 48
CODE_L1S: int = 7
CODE_L1W: int = 3
CODE_L1X: int = 12
CODE_L1Y: int = 4
CODE_L1Z: int = 13
CODE_L2C: int = 14
CODE_L2D: int = 15
CODE_L2I: int = 40
CODE_L2L: int = 17
CODE_L2M: int = 22
CODE_L2N: int = 23
CODE_L2P: int = 19
CODE_L2Q: int = 41
CODE_L2S: int = 16
CODE_L2W: int = 20
CODE_L2X: int = 18
CODE_L2Y: int = 21
CODE_L3I: int = 44
CODE_L3Q: int = 45
CODE_L3X: int = 46
CODE_L4A: int = 66
CODE_L4B: int = 67
CODE_L4X: int = 68
CODE_L5A: int = 49
CODE_L5B: int = 50
CODE_L5C: int = 51
CODE_L5D: int = 57
CODE_L5I: int = 24
CODE_L5P: int = 58
CODE_L5Q: int = 25
CODE_L5X: int = 26
CODE_L5Z: int = 59
CODE_L6A: int = 30
CODE_L6B: int = 31
CODE_L6C: int = 32
CODE_L6E: int = 60
CODE_L6I: int = 42
CODE_L6L: int = 36
CODE_L6Q: int = 43
CODE_L6S: int = 35
CODE_L6X: int = 33
CODE_L6Z: int = 34
CODE_L7D: int = 61
CODE_L7I: int = 27
CODE_L7P: int = 62
CODE_L7Q: int = 28
CODE_L7X: int = 29
CODE_L7Z: int = 63
CODE_L8D: int = 64
CODE_L8I: int = 37
CODE_L8P: int = 65
CODE_L8Q: int = 38
CODE_L8X: int = 39
CODE_L9A: int = 52
CODE_L9B: int = 53
CODE_L9C: int = 54
CODE_L9X: int = 55
CODE_NONE: int = 0
D2R: float = 0.017453292519943295
DFRQ1_GLO: float = 562500.0
DFRQ2_GLO: float = 437500.0
DLOPT_FORCE: int = 1
DLOPT_HOLDERR: int = 4
DLOPT_HOLDLST: int = 8
DLOPT_KEEPCMP: int = 2
DTTOL: float = 0.025
EFACT_CMP: float = 1.0
EFACT_GAL: float = 1.0
EFACT_GLO: float = 1.5
EFACT_GPS: float = 1.0
EFACT_IRN: float = 1.5
EFACT_QZS: float = 1.0
EFACT_SBS: float = 3.0
EPHOPT_BRDC: int = 0
EPHOPT_PREC: int = 1
EPHOPT_SBAS: int = 2
EPHOPT_SSRAPC: int = 3
EPHOPT_SSRCOM: int = 4
FE_WGS84: float = 0.0033528106647474805
FREQ1: float = 1575420000.0
FREQ1_CMP: float = 1561098000.0
FREQ1_GLO: float = 1602000000.0
FREQ1a_GLO: float = 1600995000.0
FREQ2: float = 1227600000.0
FREQ2_CMP: float = 1207140000.0
FREQ2_GLO: float = 1246000000.0
FREQ2a_GLO: float = 1248060000.0
FREQ3_CMP: float = 1268520000.0
FREQ3_GLO: float = 1202025000.0
FREQ5: float = 1176450000.0
FREQ6: float = 1278750000.0
FREQ7: float = 1207140000.0
FREQ8: float = 1191795000.0
FREQ9: float = 2492028000.0
FREQTYPE_ALL: int = 255
FREQTYPE_L1: int = 1
FREQTYPE_L2: int = 2
FREQTYPE_L3: int = 4
FREQTYPE_L4: int = 8
FREQTYPE_L5: int = 16
GEOID_EGM2008_M10: int = 3
GEOID_EGM2008_M25: int = 2
GEOID_EGM96_M150: int = 1
GEOID_EMBEDDED: int = 0
GEOID_GSI2000_M15: int = 4
GEOID_RAF09: int = 5
HION: float = 350000.0
INT_SWAP_STAT: float = 86400.0
INT_SWAP_TRAC: float = 86400.0
IONOOPT_BRDC: int = 1
IONOOPT_EST: int = 4
IONOOPT_IFLC: int = 3
IONOOPT_OFF: int = 0
IONOOPT_QZS: int = 6
IONOOPT_SBAS: int = 2
IONOOPT_STEC: int = 8
IONOOPT_TEC: int = 5
LLI_BOCTRK: int = 4
LLI_HALFA: int = 64
LLI_HALFC: int = 2
LLI_HALFS: int = 128
LLI_SLIP: int = 1
MAXANT: int = 64
MAXBAND: int = 10
MAXCODE: int = 68
MAXCOMMENT: int = 100
MAXDTOE: float = 7200.0
MAXDTOE_CMP: float = 21600.0
MAXDTOE_GAL: float = 14400.0
MAXDTOE_GLO: float = 1800.0
MAXDTOE_IRN: float = 7200.0
MAXDTOE_QZS: float = 7200.0
MAXDTOE_S: float = 86400.0
MAXDTOE_SBS: float = 360.0
MAXERRMSG: int = 4096
MAXEXFILE: int = 1024
MAXFREQ: int = 7
MAXGDOP: float = 300.0
MAXGISLAYER: int = 32
MAXLEAPS: int = 64
MAXNGEO: int = 4
MAXNIGP: int = 201
MAXNRPOS: int = 16
MAXOBS: int = 96
MAXOBSBUF: int = 128
MAXOBSTYPE: int = 64
MAXPRNCMP: int = 63
MAXPRNGAL: int = 36
MAXPRNGLO: int = 27
MAXPRNGPS: int = 32
MAXPRNIRN: int = 0
MAXPRNLEO: int = 0
MAXPRNQZS: int = 0
MAXPRNQZS_S: int = 0
MAXPRNSBS: int = 158
MAXRAWLEN: int = 16384
MAXRCV: int = 64
MAXRCVCMD: int = 4096
MAXRCVFMT: int = 12
MAXSAT: int = 197
MAXSBSAGEF: float = 30.0
MAXSBSAGEL: float = 1800.0
MAXSBSMSG: int = 32
MAXSBSURA: int = 8
MAXSOLBUF: int = 256
MAXSOLMSG: int = 8191
MAXSOLQ: int = 7
MAXSTA: int = 255
MAXSTRMSG: int = 1024
MAXSTRPATH: int = 1024
MAXSTRRTK: int = 8
MINPRNCMP: int = 1
MINPRNGAL: int = 1
MINPRNGLO: int = 1
MINPRNGPS: int = 1
MINPRNIRN: int = 0
MINPRNLEO: int = 0
MINPRNQZS: int = 0
MINPRNQZS_S: int = 0
MINPRNSBS: int = 120
NEXOBS: int = 0
NFREQ: int = 3
NFREQGLO: int = 2
NSATCMP: int = 63
NSATGAL: int = 36
NSATGLO: int = 27
NSATGPS: int = 32
NSATIRN: int = 0
NSATLEO: int = 0
NSATQZS: int = 0
NSATSBS: int = 39
NSYS: int = 4
NSYSCMP: int = 1
NSYSGAL: int = 1
NSYSGLO: int = 1
NSYSGPS: int = 1
NSYSIRN: int = 0
NSYSLEO: int = 0
NSYSQZS: int = 0
NULL: int = 0
OBSTYPE_ALL: int = 255
OBSTYPE_CP: int = 2
OBSTYPE_DOP: int = 4
OBSTYPE_PR: int = 1
OBSTYPE_SNR: int = 8
OMGE: float = 7.2921151467e-05
P2_11: float = 0.00048828125
P2_15: float = 3.0517578125e-05
P2_17: float = 7.62939453125e-06
P2_19: float = 1.9073486328125e-06
P2_20: float = 9.5367431640625e-07
P2_21: float = 4.76837158203125e-07
P2_23: float = 1.19209289550781e-07
P2_24: float = 5.960464477539063e-08
P2_27: float = 7.450580596923828e-09
P2_29: float = 1.862645149230957e-09
P2_30: float = 9.313225746154785e-10
P2_31: float = 4.656612873077393e-10
P2_32: float = 2.328306436538696e-10
P2_33: float = 1.164153218269348e-10
P2_35: float = 2.91038304567337e-11
P2_38: float = 3.63797880709171e-12
P2_39: float = 1.818989403545856e-12
P2_40: float = 9.09494701772928e-13
P2_43: float = 1.13686837721616e-13
P2_48: float = 3.552713678800501e-15
P2_5: float = 0.03125
P2_50: float = 8.881784197001252e-16
P2_55: float = 2.775557561562891e-17
P2_6: float = 0.015625
PATCH_LEVEL: str = 'b34'
PI: float = 3.141592653589793
PMODE_DGPS: int = 1
PMODE_FIXED: int = 5
PMODE_KINEMA: int = 2
PMODE_MOVEB: int = 4
PMODE_PPP_FIXED: int = 8
PMODE_PPP_KINEMA: int = 6
PMODE_PPP_STATIC: int = 7
PMODE_SINGLE: int = 0
PMODE_STATIC: int = 3
POSOPT_FILE: int = 2
POSOPT_POS: int = 0
POSOPT_RINEX: int = 3
POSOPT_RTCM: int = 4
POSOPT_SINGLE: int = 1
R2D: float = 57.29577951308232
RE_WGS84: float = 6378137.0
RNX2VER: float = 2.1
RNX3VER: float = 3.0
SBSOPT_FCORR: int = 2
SBSOPT_ICORR: int = 4
SBSOPT_LCORR: int = 1
SBSOPT_RANGE: int = 8
SC2RAD: float = 3.1415926535898
SNR_UNIT: float = 0.001
SOLF_ENU: int = 2
SOLF_GSIF: int = 5
SOLF_LLH: int = 0
SOLF_NMEA: int = 3
SOLF_STAT: int = 4
SOLF_XYZ: int = 1
SOLQ_DGPS: int = 4
SOLQ_DR: int = 7
SOLQ_FIX: int = 1
SOLQ_FLOAT: int = 2
SOLQ_NONE: int = 0
SOLQ_PPP: int = 6
SOLQ_SBAS: int = 3
SOLQ_SINGLE: int = 5
STRFMT_BINEX: int = 10
STRFMT_CRES: int = 6
STRFMT_JAVAD: int = 8
STRFMT_NMEA: int = 17
STRFMT_NVS: int = 9
STRFMT_OEM3: int = 3
STRFMT_OEM4: int = 2
STRFMT_RINEX: int = 13
STRFMT_RNXCLK: int = 15
STRFMT_RT17: int = 11
STRFMT_RTCM2: int = 0
STRFMT_RTCM3: int = 1
STRFMT_SBAS: int = 16
STRFMT_SEPT: int = 12
STRFMT_SP3: int = 14
STRFMT_SS2: int = 5
STRFMT_STQ: int = 7
STRFMT_UBX: int = 4
STR_FILE: int = 2
STR_FTP: int = 7
STR_HTTP: int = 8
STR_MEMBUF: int = 12
STR_MODE_R: int = 1
STR_MODE_RW: int = 3
STR_MODE_W: int = 2
STR_NONE: int = 0
STR_NTRIPCAS: int = 9
STR_NTRIPCLI: int = 6
STR_NTRIPSVR: int = 5
STR_SERIAL: int = 1
STR_TCPCLI: int = 4
STR_TCPSVR: int = 3
STR_UDPCLI: int = 11
STR_UDPSVR: int = 10
SYS_ALL: int = 255
SYS_CMP: int = 32
SYS_GAL: int = 8
SYS_GLO: int = 4
SYS_GPS: int = 1
SYS_IRN: int = 64
SYS_LEO: int = 128
SYS_NONE: int = 0
SYS_QZS: int = 16
SYS_SBS: int = 2
TIMES_GPST: int = 0
TIMES_JST: int = 2
TIMES_UTC: int = 1
TROPOPT_EST: int = 3
TROPOPT_ESTG: int = 4
TROPOPT_OFF: int = 0
TROPOPT_SAAS: int = 1
TROPOPT_SBAS: int = 2
TROPOPT_ZTD: int = 5
TSYS_CMP: int = 5
TSYS_GAL: int = 3
TSYS_GLO: int = 2
TSYS_GPS: int = 0
TSYS_IRN: int = 6
TSYS_QZS: int = 4
TSYS_UTC: int = 1
VER_RTKLIB: str = '2.4.3'
chisqr: Arr1Ddouble  # value = <pyrtklib.Arr1Ddouble object>
formatstrs: Arr2Dchar  # value = <pyrtklib.Arr2Dchar object>
igpband1: Arr2Dsbsigpband_t  # value = <pyrtklib.Arr2Dsbsigpband_t object>
igpband2: Arr2Dsbsigpband_t  # value = <pyrtklib.Arr2Dsbsigpband_t object>
prcopt_default: prcopt_t  # value = <pyrtklib.prcopt_t object>
solopt_default: solopt_t  # value = <pyrtklib.solopt_t object>
sysopts: Arr1Dopt_t  # value = <pyrtklib.Arr1Dopt_t object>
