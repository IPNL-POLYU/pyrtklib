# PyRTKLIB
# PyRTKLIB is a bridge between AI and GNSS.
Deep learning has reached the state-of-the-art in many fields, including 
## Introduction
This is a Python binding for [RTKLIB](https://github.com/tomojitakasu/RTKLIB), the most popular GNSS-RTK positioning C library. However, many researchers are currently using Python for research, especially in deep learning field. Thus, we implement this Python interface of RTKLIB to build a bridge between Python and positioning. By means of RTKLIB, you can easily read data from rinex file and process the positioning using the methods provided by RTKLIB, such as SPP, RTK, PPP.
<table>
<tr>
<td>

```python
from pyrtklib import *
if __name__ == "__main__":
    gnss_file_list = []
    gnss_file_list.append("data/20210714.2.whampoa.ublox.f9p.obs")
    gnss_file_list.append("data/hksc1950.21f")
    gnss_file_list.append("data/hksc1950.21n")
    gnss_file_list.append("data/hksc1950.21o")
    output_path = "pyexample_output.txt"

# get debug tracec level and solution statistics level
    trace_lv = 3
    stat_lv = 3

# setting rtklib options
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
```
</td>
<td>

```C
#define MAXFILE 10
#include "rtksrc/rtklib.h"
#include "vector"
#include "string"

int main(int argc, char *argv[]) {
    std::vector<std::string> gnss_file_list;
    gnss_file_list.push_back("../data/20210714.2.whampoa.ublox.f9p.obs");
    gnss_file_list.push_back("../data/hksc1950.21f");
    gnss_file_list.push_back("../data/hksc1950.21n");
    gnss_file_list.push_back("../data/hksc1950.21o");
    std::string output_path = "example_output.txt";
    
    // get debug tracec level and solution statistics level
    int trace_lv=3;
    int stat_lv=3;

    /* setting rtklib options */
    prcopt_t prcopt = prcopt_default;
    solopt_t solopt = solopt_default;
    filopt_t filopt = {""};
    gtime_t ts = {0};
    gtime_t te = {0};
    double tint = 0.0;
    double es[] = {2000, 1, 1, 0, 0, 0};
    double ee[] = {2000, 12, 31, 23, 59, 59};
    double pos[3];
    int i, j, n = 0, ret;
    char *infile[MAXFILE], infile_[10][1024] = {""};
    char *outfile, outfile_[1024] = {""};
    char *p;
    char *rov = "", *base = "";
    ts.time = 0;
    te.time = 0;

    for (int i = 0; i < MAXFILE; i++) { infile[i] = infile_[i]; }
    outfile = outfile_;

    /* setup input & output files */
    for (int i = 0; i < gnss_file_list.size(); i++) {
        printf("%s\n", gnss_file_list[i].c_str());
        strcpy(infile[n++], strdup(gnss_file_list[i].c_str()));
    }
    strcpy(outfile, strdup(output_path.c_str()));
    printf("%s\n", outfile);

    snrmask_t snrmask;
    snrmask.ena[0] = 1;
    snrmask.ena[1] = 1;
    for (int i = 0; i < NFREQ; i++) {
        for (int j = 0; j < 9; j++) {
            snrmask.mask[i][j] = 10.0;
        }
    }

    prcopt.mode = PMODE_KINEMA; //PMODE_SINGLE;
    prcopt.soltype = 2;
    prcopt.nf = 3;
    prcopt.navsys = SYS_ALL;
    prcopt.sateph = EPHOPT_BRDC;
    prcopt.modear = 3;
    prcopt.glomodear = 1;
    prcopt.bdsmodear = 1;
    prcopt.ionoopt = IONOOPT_BRDC;
    prcopt.tropopt = TROPOPT_SAAS;
    prcopt.posopt[4] = 0;
    prcopt.rb[0] = -2414266.9197;
    prcopt.rb[1] = 5386768.9868;
    prcopt.rb[2] = 2407460.0314;
    solopt.posf = SOLF_LLH;
    solopt.times = TIMES_GPST;
    solopt.timef = 0;
    solopt.timeu = 3;
    solopt.degf = 0;
    solopt.outhead = 1;
    solopt.outopt = 1;
    solopt.datum = 0;
    solopt.height = 0;
    solopt.geoid = 0;
    solopt.sstat = stat_lv;
    solopt.trace = trace_lv;
    printf("starting rtklib ... \n");
    ret = postpos(ts,te,tint,0.0,&prcopt,&solopt,&filopt,infile,n,outfile,rov,base);
    printf("\nrtklib status: %d; rov: %s; base: %s\n", ret, rov, base);
    return 0;
}
```
</td>
</tr>
</table>

## Installation
Installation of pyrtklib is very easy, just clone the code and install it.

0. Dependencies
   
    We don't provide pre-compiled package so far, thus, this library will be compiled in time. (Looking forward one day it can be directly installed by pip!) It requires several dependencies, including gcc and cmake. If you are using on a MacOS, please first install gcc by brew and set the compiler path, because RTKLIB used GNU C features, which is hard to solve in clang. MSVC is not tested.
1. Clone from github
```shell
git clone git@github.com:IPNL-POLYU/pyrtklib.git
```
2. Install
```shell
cd pyrtklib
python3 setup.py install
```
Then you can use this lib by importing it.
```python
from pyrtklib import *
```
## Key Feature
The aim for this binding is to make a interface of RTKLIB, without changing any code in RTKLIB. However the biggest obstucle is that RTKLIB enoumously uses function side effect. For example, the reading function ***readrnx***, you should pass the *obs*, *nav*, *sta* as input parameters, and the process result will be directly written to *obs*, *nav*, and *sta*. Thus, these functions only receive the pointer and it requires the Python interface contains the original pointer. Unfortunately, the STL container can't satisfy this requirement because STL container will copy the data. If Python receives a STL container, it's not the original version of the data.

Thus, we implement ***Arr1D*** and ***Arr2D*** to handle the array and can also be used as the pointer. **Arr1D** has a structure like this:
```C
template<class T>
struct Arr1D<T>{
    T* src;
    int len;
}
```
If you want to create it in Python, just use "Arr1D"+"ctype", for example, if you want a *char* type array, then, it should be:
```python
myarr = Arr1Dchar(3)
```
The constructor parameter is the length. In the above example, the length is 5. You can directly to modify the data:
```
myarr[0]='a'
myarr[1]='b'
myarr[2]='c'
```
And you can also use the slides:
```python
yourarr=myarr[0:2]
```
So far, the Arr1D and Arr2D don't have the ability to print itself, if you use
```python
print(myarr)
```
you'll get:
```
<pyrtklib.Arr1Dchar object at 0x7fe3799a6ef0>
```
So, if you want to see the content, you can change it to a list by:
```python
list(myarr)
```
Then the result will be:
```python
['a','b','c']
```
<span style="color:red;font-size:20px">**Warning:** Be really carefull to use Arr1D and Arr2D, because it doesn't have a bounary check. In some cases, it's a pure pointer and doesn't know how long itself is. So be careful to set the index, or the segmentation fault will occur.</span>

## Usage
This binding provides all the functions and data structures in rtklib. The structures in rtklib is used as a class in Python. For example, if you want a obs_t, then you can use it by:
```python
obs = obs_t()
```
And the data in obs can be accessed by:
```python
obs.data[0]
```
Notice that obs.data is a Arr1Dobsd_t class. In other words, this is an array of obsd_t.
For more detail, you can see in the example.py.

## Citation
If you find this tool useful, you can cite our paper as:


```latex
@inproceedings{hu2023fisheye,
  title={Fisheye camera aided NLOS exclusion and learning-based pseudorange correction},
  author={Hu, Runzhi and Wen, Weisong and Hsu, Li-ta},
  booktitle={2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC)},
  pages={1--8},
  year={2023},
  organization={IEEE}
}
```