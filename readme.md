# PyRTKLIB
# PyRTKLIB is a bridge between AI and GNSS.
Deep learning has reached the state-of-the-art in many fields, including 
## Introduction
This is a Python binding for [RTKLIB](https://github.com/tomojitakasu/RTKLIB), the most popular GNSS-RTK positioning C library. However, many researchers are currently using Python for research, especially in deep learning field. Thus, we implement this Python interface of RTKLIB to build a bridge between Python and positioning. By means of RTKLIB, you can easily read data from rinex file and process the positioning using the methods provided by RTKLIB, such as SPP, RTK, PPP.
<table>
<tr>
<td>

```python
# Python code for Hello World
print("Hello, World!")
</td>
<td>
// JavaScript code for Hello World
console.log("Hello, World!");
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