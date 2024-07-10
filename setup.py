import os
import pathlib
from setuptools import setup
from setuptools import Extension
from setuptools.command.build_ext import build_ext
import distutils.sysconfig
import subprocess
import shutil

pyinc = distutils.sysconfig.get_python_inc()

class CMakeExtension(Extension):
    def __init__(self, name):
        super().__init__(name, sources=[])

class BuildExt(build_ext):
    def run(self):
        for ext in self.extensions:
            if isinstance(ext, CMakeExtension):
                self.build_cmake(ext)
        super().run()
        # 在构建结束后复制 DLL 文件
        if os.name == 'nt':
            self.copy_dll()

    def build_cmake(self, ext):
        cwd = pathlib.Path().absolute()
        build_temp = f"{pathlib.Path(self.build_temp)}/{ext.name}"
        os.makedirs(build_temp, exist_ok=True)
        extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
        extdir.mkdir(parents=True, exist_ok=True)

        config = "Debug" if self.debug else "Release"
        cmake_args = [
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + str(extdir.parent.absolute())+"/pyrtklib",
            "-DCMAKE_BUILD_TYPE=" + config,
            "-DPYTHON_INCLUDE_DIR=" + pyinc
        ]
        if self.debug:
            cmake_args.append("-DDEBUG=ON")

        if os.name == "nt":
            cmake_args += [
                "-DCMAKE_GENERATOR=Visual Studio 16 2019",
                "-A", "x64",
                "-DCMAKE_C_FLAGS_RELEASE=/MT",
                "-DCMAKE_CXX_FLAGS_RELEASE=/MT",
                "-DWIN32=ON",
                "-DCMAKE_CXX_FLAGS=/bigobj /DWIN32",
                "-DCMAKE_C_FLAGS=/bigobj /DWIN32",
                "-DCMAKE_EXE_LINKER_FLAGS=/bigobj",
                "-DCMAKE_SHARED_LINKER_FLAGS=/bigobj",
                "-DADDITIONAL_LIBRARIES=winmm;ws2_32",
                "-DCMAKE_RUNTIME_OUTPUT_DIRECTORY=${CMAKE_BINARY_DIR}",
                "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=${CMAKE_BINARY_DIR}"
            ]
            print("Windows config successfully")

        build_args = ["--config", config]
        if os.name != "nt":
            build_args += ["--", "-j8"]

        os.chdir(build_temp)
        self.spawn(["cmake", f"{str(cwd)}/{ext.name}"] + cmake_args)
        if not self.dry_run:
            self.spawn(["cmake", "--build", "."] + build_args)
        os.chdir(str(cwd))

    def copy_dll(self):
        dll_name = "pyrtklib.dll"  # 根据实际的 DLL 名称更改
        source_dll_path = os.path.join(self.build_lib, dll_name)
        target_dll_path = os.path.join(self.build_lib, "pyrtklib", dll_name)
        if os.path.exists(source_dll_path):
            shutil.copy(source_dll_path, target_dll_path)
        else:
            print("DLL file not found!")

pyrtklib = CMakeExtension("pyrtklib")

setup(name="pyrtklib",
      version="0.2.6",
      description="This is a python binding for rtklib",
      author="Runzhi Hu",
      author_email="run-zhi.hu@connect.polyu.hk",
      url="https://github.com/IPNL-POLYU/pyrtklib",
      packages=["pyrtklib"],
      package_data={
        'pyrtklib':['pyrtklib.pyi','__init__.py']
      },
      ext_modules=[pyrtklib],  
      cmdclass={"build_ext": BuildExt}
)