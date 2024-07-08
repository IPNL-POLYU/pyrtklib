#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <memory>
#include <iostream>

namespace py = pybind11;
#define BINDARR1D(Type) pybind11::class_<Arr1D<Type>>(m,"Arr1D"#Type)\
    .def(py::init([](int len){return std::unique_ptr<Arr1D<Type>>(new Arr1D<Type>(len));}))\
    .def(py::init([](Type* src,int len){return std::unique_ptr<Arr1D<Type>>(new Arr1D<Type>((void*)src,len));}))\
    .def("__len__",[](Arr1D<Type> &arr){return &arr.len;})\
    .def("__getitem__",[](Arr1D<Type> &arr,int i){return arr.src+i;},py::return_value_policy::reference)\
    .def("__getitem__",[](Arr1D<Type> &arr,py::slice slice){long start,stop,step;PySlice_Unpack(slice.ptr(),&start,&stop,&step);return new Arr1D<Type>(arr.src+start,stop-start);},py::return_value_policy::reference)\
    .def("__setitem__",[](Arr1D<Type> &arr,int i, Type v){arr.src[i]=v;})\
    .def("__iter__",[](Arr1D<Type> &arr){return pybind11::make_iterator(arr.src,arr.src+arr.len);})\
    .def("deepcopy",static_cast<Arr1D<Type>*(Arr1D<Type>::*)()>(&Arr1D<Type>::deepcopy))\
    .def("deepcopy",static_cast<Arr1D<Type>*(Arr1D<Type>::*)(int)>(&Arr1D<Type>::deepcopy))\
    .def_readonly("ptr",&Arr1D<Type>::src,py::return_value_policy::reference)\
    .def("set",[](Arr1D<Type> &arr,Arr1D<Type> *nsrc){arr.src = (Type*)nsrc->src;})\
    .def("print",[](Arr1D<Type> &arr){std::cout<<(arr.src)<<std::endl;});

#define BINDARR2D(Type) pybind11::class_<Arr2D<Type>>(m,"Arr2D"#Type)\
    .def(py::init([](int row,int col){return std::unique_ptr<Arr2D<Type>>(new Arr2D<Type>(row,col));}))\
    .def(py::init([](Type* src,int row,int col){return std::unique_ptr<Arr2D<Type>>(new Arr2D<Type>((void*)src,row,col));}))\
    .def("__len__",[](Arr2D<Type> &arr){return pybind11::make_tuple(arr.row,arr.col);})\
    .def("__getitem__",[](Arr2D<Type> &arr,pybind11::tuple index){return arr.src+(index[0].cast<int>())*arr.col+(index[1].cast<int>());},py::return_value_policy::reference)\
    .def("__setitem__",[](Arr2D<Type> &arr,pybind11::tuple index, Type v){*(arr.src+(index[0].cast<int>())*arr.col+(index[1].cast<int>()))=v;})\
    .def("__iter__",[](Arr2D<Type> &arr){return pybind11::make_iterator(arr.src,arr.src+arr.row*arr.col);})\
    .def_readonly("ptr",&Arr2D<Type>::src,py::return_value_policy::reference)\
    .def("set",[](Arr2D<Type> &arr,Arr2D<Type> *nsrc){arr.src = (Type*)nsrc->src;})\
    .def("print",[](Arr2D<Type> &arr){std::cout<<(arr.src)<<std::endl;});


template <class T>
class Arr1D{
    public:
        typedef T value_type;
        T* src;
        int len;
        //I'm thinking about add a reflection here so the setter can be implemented here rather than in the class.
        //void* obj;
        /*
        Arr1D(void *arr,int len,void *obj){
            this->len = len;
            this->obj = obj;
            this->src = obj->src;
        }
        */
        Arr1D(int len){
            this->len = len;
            this->src = (T*)calloc(len,sizeof(T));
            //std::cout<<(void*)(this->src)<<std::endl;
        };
        Arr1D(void *arr,int len){
            this->src = (T*)arr;
            this->len = len;
        };
        Arr1D<T>* deepcopy(){
            if(len<0){
                throw std::length_error("array without known length can't be copied");
            }
            Arr1D<T>* newArr = new Arr1D<T>(len);
            for(int i=0;i<len;i++){
                newArr->src[i] = src[i];
            }
            return newArr;
        };
        Arr1D<T>* deepcopy(int length){
            Arr1D<T>* newArr = new Arr1D<T>(length);
            for(int i=0;i<length;i++){
                newArr->src[i] = src[i];
            }
            return newArr;
        };
};

template <class T>
class Arr2D{
    public:
        typedef T value_type;
        T* src;
        int row,col;
        Arr2D(int row, int col){
            this->row = row;
            this->col = col;
            this->src = (T*)calloc(row*col,sizeof(T));
        }
        Arr2D(void* arr,int row,int col){
            this->src = (T*)arr;
            this->row = row;
            this->col = col;
        };
};

template<typename Type>
void bindArr1D(py::module_& m, const std::string& typeName) {
    auto cls = py::class_<Arr1D<Type>>(m, ("Arr1D" + typeName).c_str())
    .def(py::init([](int len){return std::unique_ptr<Arr1D<Type>>(new Arr1D<Type>(len));}))
    .def(py::init([](Type* src,int len){return std::unique_ptr<Arr1D<Type>>(new Arr1D<Type>((void*)src,len));}))
    .def("__len__",[](Arr1D<Type> &arr){return &arr.len;})
    .def("__getitem__",[](Arr1D<Type> &arr,int i){return arr.src+i;},py::return_value_policy::reference)
    .def("__getitem__",[](Arr1D<Type> &arr,py::slice slice){long start,stop,step;PySlice_Unpack(slice.ptr(),&start,&stop,&step);return new Arr1D<Type>(arr.src+start,stop-start);},py::return_value_policy::reference)
    .def("__setitem__",[](Arr1D<Type> &arr,int i, Type v){arr.src[i]=v;})
    .def("__iter__",[](Arr1D<Type> &arr){return pybind11::make_iterator(arr.src,arr.src+arr.len);})
    .def("deepcopy",static_cast<Arr1D<Type>*(Arr1D<Type>::*)()>(&Arr1D<Type>::deepcopy))
    .def("deepcopy",static_cast<Arr1D<Type>*(Arr1D<Type>::*)(int)>(&Arr1D<Type>::deepcopy))
    .def_readonly("ptr",&Arr1D<Type>::src,py::return_value_policy::reference)
    .def("set",[](Arr1D<Type> &arr,Arr1D<Type> *nsrc){arr.src = (Type*)nsrc->src;})
    .def("print",[](Arr1D<Type> &arr){std::cout<<(arr.src)<<std::endl;});

    if constexpr (std::is_same<Type, char>::value) {
        cls.def(py::init([](const std::string& s) {
                auto* arr = new Arr1D<char>(s.size()+1);
                std::memcpy(arr->src, s.data(), s.size());
                arr->src[s.size()] = '\0';  // Null-terminate the string
                return arr;
            }), py::arg("s"), "Constructor from Python str");
    }

}


template<typename Type>
void bindArr2D(py::module_& m, const std::string& typeName) {
    py::class_<Arr2D<Type>>(m, ("Arr2D" + typeName).c_str())
    .def(py::init([](int row,int col){return std::unique_ptr<Arr2D<Type>>(new Arr2D<Type>(row,col));}))
    .def(py::init([](Type* src,int row,int col){return std::unique_ptr<Arr2D<Type>>(new Arr2D<Type>((void*)src,row,col));}))
    .def("__len__",[](Arr2D<Type> &arr){return pybind11::make_tuple(arr.row,arr.col);})
    .def("__getitem__",[](Arr2D<Type> &arr,pybind11::tuple index){return arr.src+(index[0].cast<int>())*arr.col+(index[1].cast<int>());},py::return_value_policy::reference)
    .def("__setitem__",[](Arr2D<Type> &arr,pybind11::tuple index, Type v){*(arr.src+(index[0].cast<int>())*arr.col+(index[1].cast<int>()))=v;})
    .def("__iter__",[](Arr2D<Type> &arr){return pybind11::make_iterator(arr.src,arr.src+arr.row*arr.col);})
    .def_readonly("ptr",&Arr2D<Type>::src,py::return_value_policy::reference)
    .def("set",[](Arr2D<Type> &arr,Arr2D<Type> *nsrc){arr.src = (Type*)nsrc->src;})
    .def("print",[](Arr2D<Type> &arr){std::cout<<(arr.src)<<std::endl;});
}



char **convertChar(std::vector<std::string> str){
    char **tmp = (char**)calloc(str.size(),sizeof(char*));
    for(int i=0;i<str.size();i++){
        tmp[i] = (char*)calloc(strlen(str[i].c_str())+1,sizeof(char));
        strcpy(tmp[i],str[i].c_str());
    }
    return tmp;
}

template<class T>
T **convertType(const std::vector<std::vector<T>>& obj) {
    T **tmp = (T**)calloc(obj.size(), sizeof(T*));
    for (size_t i = 0; i < obj.size(); i++) {
        tmp[i] = (T*)calloc(obj[i].size(), sizeof(T)); 
        memcpy(tmp[i], obj[i].data(), obj[i].size() * sizeof(T));
    }
    return tmp;
}