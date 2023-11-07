import os
import pathlib
from setuptools import setup
from setuptools import Extension
from setuptools.command.build_ext import build_ext
import distutils.sysconfig
import subprocess

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

    def build_cmake(self, ext):

        cwd = pathlib.Path().absolute()

        build_temp = f"{pathlib.Path(self.build_temp)}/{ext.name}"
        os.makedirs(build_temp, exist_ok=True)
        extdir = pathlib.Path(self.get_ext_fullpath(ext.name))
        extdir.mkdir(parents=True, exist_ok=True)

        config = "Debug" if self.debug else "Release"
        cmake_args = [
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=" + str(extdir.parent.absolute()),
            "-DCMAKE_BUILD_TYPE=" + config,
            "-DPYTHON_INCLUDE_DIR="+pyinc
        ]
        if self.debug:
            cmake_args.append("-DDEBUG=ON")

        if os.sys.platform == "darwin":
                gcc_version_output = subprocess.check_output(["brew", "list", "--versions", "gcc"])
                gcc_version = gcc_version_output.decode("utf-8").split()[1].split('.')[0]
                gcc_path = '/'.join(subprocess.check_output(['which','gcc-13']).decode('utf8').split('/')[:-1])
                cmake_args.append("-DCMAKE_C_COMPILER="+gcc_path+'/gcc-'+gcc_version)
                cmake_args.append("-DCMAKE_CXX_COMPILER="+gcc_path+'/g++-'+gcc_version)
                cmake_args.append("-DDARWIN=ON")
                print("set gcc compiler successfully")

        build_args = [
            "--config", config,
            "--", "-j8"
        ]

        os.chdir(build_temp)
        self.spawn(["cmake", f"{str(cwd)}/{ext.name}"] + cmake_args)
        if not self.dry_run:
            self.spawn(["cmake", "--build", "."] + build_args)
        os.chdir(str(cwd))


pyrtklib = CMakeExtension("pyrtklib")

setup(name="pyrtklib",
      version="0.2.4",
      description="This is a python binding for rtklib",
      author="Runzhi Hu",
      author_email = "run-zhi.hu@connect.polyu.hk",
      url = "https://github.com/IPNL-POLYU/pyrtklib",
      packages=["pyrtklib"],
      package_data={
        'pyrtklib':['pyrtklib.pyi']
      },
      ext_modules=[pyrtklib],  
      cmdclass={"build_ext": BuildExt}
)
