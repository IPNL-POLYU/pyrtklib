import pycparser
from pycparser import parse_file
import re
import copy

def remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/') or s.startswith('#'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'#.*?$|//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

def getDefine(txt,DEFINE):
	pat = re.compile(r"\\\n",re.DOTALL)
	src = re.sub(pat,"",txt)
	pat = re.compile(r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"')
	src = re.sub(pat,"",src)
	pat = re.compile(" +",re.DOTALL)
	src = re.sub(pat," ",src)
	srcs = src.split('\n')
	defs = []
	i = 0
	while i < len(srcs):
		if srcs[i].find("#define") != -1 and srcs[i].find("thread") == -1:
			j = srcs[i].strip().split(' ')
			if len(j) > 2:
				defs.append([j[1],j[2]])
			i += 1
		elif srcs[i].find("#ifdef") != -1:
			j = srcs[i].strip().split(' ')
			k = 0
			while srcs[i+k].find("#endif") == -1:
				k += 1
			l = 0
			while srcs[i+l].find("#else") == -1 and l < k:
				l += 1
			if l != k:
				if j[1] in DEFINE:
					start = 0
					end = l
				else:
					start = l + 1
					end = k
			else:
				start = 0
				end = k
			for m in range(end-start):
				if srcs[i+start+m].find("#define") != -1 and srcs[i+start+m].find("thread") == -1:
					n = srcs[i+start+m].strip().split(' ')
					if len(n) > 2:
						defs.append([n[1],n[2]])
			i += k
		else:
			i += 1
	return defs
	

#gen the bind file
header = '''#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "rtksrc/rtklib.h"
#include "iostream"
#include "cbind.h"
namespace py = pybind11;
std::map<void*,void*> gmap;
'''
footer = '''
}
'''
#bindTemp = '    BINDARR1D(%s);\n    BINDARR2D(%s);\n'
bindTemp = '    bindArr1D<%s>(m,"%s");\n    bindArr2D<%s>(m,"%s");\n'
structTemp = '    py::class_<%s>(m,"%s").def(py::init())\n'
structMemTemp = '        .def_readwrite("%s",&%s::%s)\n'
structProperTemp = '''        .def_property_readonly("%s",[](%s& o) {%s* tmp = new %s(%s);return tmp;},py::return_value_policy::reference)\n'''
# structProperTemp = '''        .def_property_readonly("%s",[](py::object& obj) {
#             %s& o = obj.cast<%s&>();
# 			%s* retv;
# 			std::map<void*,void*>::iterator iter;
# 			iter = gmap.find((void*)&o);
# 			if(iter==gmap.end()){
#                 %s* tmp = new %s(%s);
#                 auto ret = gmap.insert(std::pair<void*,void*>((void*)&o,(void*)tmp));
#                 retv = (%s*)ret.first->second;
#             }else{
#                 retv = (%s*)iter->second;
#             }
#             return retv;
#             },py::return_value_policy::reference)\n'''
attrArrTemp = '    m.attr("%s") = new %s<%s>(%s);\n'
attrTemp = '    m.attr("%s") = new %s_t(%s);\n'
funcTemp = '    m.def("%s",&%s,"rtklib %s");\n'
def gen_struct(struct):
	name = struct['name']
	temp = structTemp%(name,name)
	for i in struct['member']:
		temp += structMemTemp%(i,name,i)
	for i in struct['proper']:
		dim = []
		if len(i['dims']) == 1:
			if i['dims'][0] == '':
				dim.append('-1')
			else:
				dim.append(i['dims'][0])
			ttype = 'Arr1D'+'<'+i['type']+'>'
			temp += structProperTemp%(i['name'],name,ttype,ttype,"o."+i['name']+','+dim[0])
		else:
			if i['dims'][0] == '':
				dim.append('-1')
			else:
				dim.append(i['dims'][0])
			if i['dims'][1] == '':
				dim.append('-1')
			else:
				dim.append(i['dims'][1])
			ttype = 'Arr2D'+'<'+i['type']+'>'
			temp += structProperTemp%(i['name'],name,ttype,ttype,"o."+i['name']+','+dim[0]+','+dim[1])
	temp+='        .def_property_readonly("ptr",[](%s& o){return &o;},py::return_value_policy::reference);\n\n'%(name)
	return temp

def gen_attrarr(i):
	dim = []
	temp = ''
	if len(i['dims']) == 1:
		if i['dims'][0] == '':
			dim.append('-1')
		else:
			dim.append(i['dims'][0])
		temp += attrArrTemp%(i['name'],'Arr1D',i['type'],"(void*)"+i['name']+','+dim[0])
	else:
		if i['dims'][0] == '':
			dim.append('-1')
		else:
			dim.append(i['dims'][0])
		if i['dims'][1] == '':
			dim.append('-1')
		else:
			dim.append(i['dims'][1])
		temp += attrArrTemp%(i['name'],'Arr2D',i['type'],"(void*)"+i['name']+','+dim[0]+','+dim[1])
	return temp

def gen_attr(attr):
	return attrTemp%(attr,attr.replace("_default",""),attr)

def gen_func(func):
	return funcTemp%(func,func,func)

def gen_multidef(funcs):
	tmp = ""
	i = funcs
	tmp += i['multidef'].rstrip('; ')+"{\n"
	for j in i['dconvert']:
		if j[0] == "char":
			tmp += "    %s **%s = convertChar(D%s);\n"%(j[0],j[1],j[1])
		else:
			tmp += "    %s **%s = convertType(D%s);\n"%(j[0],j[1],j[1])
	for j in i['sconvert']:
		tmp += "    %s *%s = S%s.src;\n"%(j[0],j[1],j[1])
	if i['fconvert']:
		tmp += '	FILE *fp = fopen(Ffp,mode);\n'
	params = re.findall("\(.*\)",i['src'])[0].lstrip('(').rstrip(')')
	params = params.split(',')
	p = []
	for k in params:
		p.append(k.split(' ')[-1].strip('*'))
	params = ', '.join(p)
	if i['type'] != 'void':
		tmp += "    auto tmp = %s(%s);\n"%(i['name'],params)
		for j in i['dconvert']:
			tmp += '    free(%s);\n'%j[1]
		if i['fconvert']:
			tmp += '	fclose(fp);\n'
		tmp += "    return tmp;\n}\n"
	else:
		tmp += "    %s(%s);\n"%(i['name'],params)
		for j in i['dconvert']:
			tmp += '    free(%s);\n'%j[1]
		if i['fconvert']:
			tmp += '	fclose(fp);\n'
		tmp += "\n}\n"
	return tmp

def gen_functionPointer(funcs):
	tmp = ""
	i = funcs
	params = re.findall("\(.*\)",i['multidef'])[0].lstrip('(').rstrip(')')
	tmp += '    m.def("%s",static_cast<%s(*)(%s)>(&%s),"rtklib %s");\n'%(i['name'],i['type'],params,i['name'],i['name'])
	return tmp

def gen_defs(defs):
	tmp = ""
	for i in defs:
		tmp+='    m.attr("%s")=%s;\n'%(i[0],i[1])
	return tmp

DEFINE = ['ENACMP','ENAGAL','ENAGLO']
#parse the header
with open('pyrtklib/rtksrc/rtklib.h','r') as f:
	src = f.read()
defines = getDefine(src,DEFINE)
src = remover(src)
rec = re.compile('extern "C" {(.*)}',re.DOTALL)
src = rec.findall(src)[0]
src = src.replace('"Copyright (C) 2007-2018 by T.Takasu\\n',"")
src = src.replace('All rights reserved."',"")
src = "typedef long time_t;\ntypedef long lock_t;\ntypedef long thread_t;\ntypedef long FILE;\n"+src
src = re.sub('\\n+','\\n',re.sub(' \\n','\\n',src).strip())
parser = pycparser.CParser()
ast = parser.parse(src)
#ast = parse_file('rtklib.h',use_cpp=True,cpp_path='gcc',cpp_args=['-E',r'-I./pycparser/utils/fake_libc_include'])
elements = ast.children()
rtk_flag = False
struct = []
attr = []
function = []
functionDouble = []
bind_types = []
srcs = src.split('\n')
attrArr = []

for e in elements:
	if e[1].name == "gtime_t":
		rtk_flag = True
	if rtk_flag:
		if type(e[1]) == pycparser.c_ast.Typedef:#export struct
			node = {}
			node['name'] = e[1].name
			node['member'] = []
			node['proper'] = []
			struct_mem = e[1].children()[0][1].children()[0][1].children()
			for i in struct_mem:
				if type(i[1].type) != pycparser.c_ast.ArrayDecl:
					proper = {}
					line = srcs[i[1].coord.line-1]		
					proper['name'] = i[1].name
					proper['type'] = line.replace("const","",).replace('unsigned ','').strip().split(' ')[0]
					proper['dims'] = []
					if line.find('*') != -1:
						proper['dims'].append('')
						node['proper'].append(proper)
					else:
						node['member'].append(i[1].name)
				else:
					proper = {}
					line = srcs[i[1].coord.line-1]					
					proper['name'] = i[1].name
					proper['type'] = line[:i[1].coord.column-1].strip()
					proper['dims'] = []
					if proper['type'].find(',')!= -1:
						tmpType = proper['type']
						tmpType = ' '.join(tmpType.split(' ')[:-1])
						proper['type'] = tmpType
					if proper['type'].find('*')!= -1:
						proper['type'] = proper['type'].replace('*','').strip()
						proper['dims'].append('')
					bind_types.append(proper['type'].replace('const ','').replace('unsigned ',''))
					dims = re.findall('\[.*?\]',line[i[1].coord.column-1:])
					for j in dims:
						k = j.rstrip(']').lstrip('[')
						proper['dims'].append(k)
					node['proper'].append(proper)
			struct.append(node)
		if type(e[1]) == pycparser.c_ast.Decl:#function or attr
			if type(e[1].children()[0][1]) == pycparser.c_ast.FuncDecl:
				k = e[1]
				if srcs[k.coord.line-1].find(';') != -1:
					lll = srcs[k.coord.line-1]
				else:
					lll = srcs[k.coord.line-1]
					iii = k.coord.line
					while(srcs[iii].find(';') == -1):
						iii+=1
					ext = ''.join([re.sub(" +",' ',kkk) for kkk in srcs[k.coord.line:iii+1]])
					ext = ext.replace('\n','')
					lll = lll + ext
				if lll.find("...") != -1 or lll.find("stec_") != -1:
					continue
				if len(re.findall("\*[a-zA-Z]*?\[\]",lll)) != 0:
					tttmp = re.findall("\*[a-zA-Z]*?\[\]",lll)[0]
					lll = lll.replace(tttmp,"*"+tttmp[:-2])
				if lll.find("*") == -1:
					function.append(e[1].name)
				else:
					S =0
					D = 0
					F = 0
					proper = {}
					proper['name'] = e[1].name
					proper['multidef'] = ''
					proper['dconvert'] = []
					proper['sconvert'] = []
					proper['fconvert'] = False
					proper['type'] = lll[:k.coord.column-1].replace('extern',"").replace('const',"").strip()
					params = re.findall("\(.*\)",lll)[0].lstrip('(').rstrip(')')
					proper['src'] = copy.deepcopy(lll)
					ddp = params.split(',')
					for k in ddp:
						if k.find("FILE") != -1:
							lll = lll.replace("FILE *fp","const char *Ffp, const char *mode")
							proper['fconvert'] = True
							F += 1
							continue
						if k.find('**') != -1:
							ttt = k.strip().split(' ')[0]
							nnn = k.strip().split(' ')[1].strip('*')
							proper['dconvert'].append((ttt,nnn))
							if ttt == 'char':
								lll = lll.replace(k,'std::vector<std::string> '+"D"+nnn)
							else:
								lll = lll.replace(k,'std::vector<std::vector<%s>> '%ttt+"D"+nnn)
							D += 1
							continue
						if k.find('*') != -1:
							if k.find('const char') != -1:
								continue
							nnn = k.strip().split('*')[-1].strip()
							ttt = k.strip().split('*')[0].strip()
							# ttt = k.strip().split(' ')[0]
							# nnn = k.strip().split(' ')[1].strip('*')
							if ttt.find('double') != -1 or ttt.find('float') != -1 or ttt.find('char') != -1 or ttt.find('int') != -1:
								proper['sconvert'].append((ttt,nnn))
								lll = lll.replace(k,'Arr1D<%s> '%ttt.replace("const","").strip()+"S"+nnn)
								S += 1
							continue
					if S == 0 and D == 0 and F == 0:
						function.append(e[1].name)
					else:
						proper['multidef'] = lll
						functionDouble.append(proper)
			elif type(e[1].children()[0][1]) == pycparser.c_ast.ArrayDecl:
				i = e[1].children()[0][1]
				proper = {}
				line = srcs[i.coord.line-1]					
				proper['name'] = e[1].name
				proper['dims'] = []
				proper['type'] = line[:i.coord.column-1].strip().replace('extern ','')
				if proper['type'].find(',')!=-1:
					tmpType = proper['type']
					tmpType = ' '.join(tmpType.split(' ')[:-1])
					proper['type'] = tmpType
				if proper['type'].find('*')!= -1:
					proper['type'] = proper['type'].replace('*','').strip()
					proper['dims'].append('')
				proper['type'] = proper['type'].replace('const ','').replace('unsigned ','')
				bind_types.append(proper['type'])
				dims = re.findall('\[.*?\]',line[i.coord.column-1:])
				for j in dims:
					k = j.rstrip(']').lstrip('[')
					proper['dims'].append(k)
				attrArr.append(proper)
			else:
				attr.append(e[1].name)
#generate the file
content = ""
#process multi first
for i in functionDouble:
	content += gen_multidef(i)
content += '''PYBIND11_MODULE(pyrtklib, m) {
    m.doc() = "rtklib python interface by pybind11";
	m.attr("NULL") = __null;
'''
content += gen_defs(defines)
# for i in set(bind_types):
# 	k = i.replace('const ','')
# 	content += bindTemp%(k,k)
for i in struct:
	content += bindTemp%(i['name'],i['name'],i['name'],i['name'])
for i in ['long double','double','float','char','unsigned char','int','unsigned int','short','unsigned short','long','unsigned long','short','unsigned short']:
	content += bindTemp%(i,i,i,i)
	if i == "char":
		content += '''	py::class_<Arr1D<char>>(m, "char")
    	.def(py::init([](const std::string& s) {
            auto* arr = new Arr1D<char>(s.size()+1);
            std::memcpy(arr->src, s.data(), arr->len);
            arr->src[arr->len] = '\\0';  // Null-terminate the string
            return arr;
        }), "Constructor from Python str");\n'''
for i in struct:
	content += gen_struct(i)
for i in attrArr:
	content += gen_attrarr(i)
for i in attr:
	content += gen_attr(i)
for i in functionDouble:
	content += gen_functionPointer(i)
for i in function:
	content += gen_func(i)
content = content.replace('.def_readwrite("data",&obs_t::data)','.def_property_readonly("data",[](obs_t& o) {Arr1D<obsd_t>* tmp = new Arr1D<obsd_t>(o.data,-1);return tmp;},py::return_value_policy::reference)\n        .def("set_data",[](obs_t& o,Arr1D<obsd_t> *nsrc){o.data = nsrc->src;})')
content = content.replace('.def_property_readonly("y",[](sbsigpband_t& o) {Arr1D<short>* tmp = new Arr1D<short>(o.y,-1);return tmp;},py::return_value_policy::reference)','.def_property_readonly("y",[](sbsigpband_t& o) {Arr1D<short>* tmp = new Arr1D<short>(const_cast<short*>(o.y),-1);return tmp;},py::return_value_policy::reference)')
with open('pyrtklib/pyrtklib.cpp','w') as f:
	f.write(header+content+footer)
