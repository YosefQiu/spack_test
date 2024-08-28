from spack import *

class SyclOcean(CMakePackage):
    """SYCL_OCEAN is a CMake-based project for ocean modeling using SYCL."""

    homepage = "https://github.com/YosefQiu/sycl_ocean"
    git      = "https://github.com/YosefQiu/sycl_ocean.git"

    maintainers = ['your-github-username']

    version('main', branch='master')

    # 添加依赖项
    depends_on('intel-oneapi-compilers+nvidia')
    depends_on('yaml-cpp')
    depends_on('vtk')
    depends_on('netcdf-c')
    depends_on('netcdf-cxx')

    def cmake_args(self):
        args = []

        # 设置编译器
        args.append('-DCMAKE_C_COMPILER=icx')
        args.append('-DCMAKE_CXX_COMPILER=icpx')

        # 添加 SYCL 编译标志
        args.append('-DCMAKE_C_FLAGS=-fsycl -fno-fast-math')
        args.append('-DCMAKE_CXX_FLAGS=-fsycl -fno-fast-math -fsycl-targets=nvptx64-nvidia-cuda')
        args.append('-DCMAKE_EXE_LINKER_FLAGS=-fsycl')

        # 添加 NetCDF 库
        netcdf_libs = self.spec['netcdf-c'].libs.joined(';')
        netcdf_cxx_libs = self.spec['netcdf-cxx'].libs.joined(';')
        args.append('-DNetCDF_LIBRARIES={0};{1}'.format(netcdf_libs, netcdf_cxx_libs))

        return args

    def setup_build_environment(self, env):
        # 设置构建环境，确保找到 NetCDF 和其他依赖项的头文件
        env.prepend_path('CPATH', self.spec['netcdf-c'].headers.directories[0])
        env.prepend_path('CPATH', self.spec['netcdf-cxx'].headers.directories[0])
        env.prepend_path('LD_LIBRARY_PATH', self.spec['netcdf-c'].libs.directories[0])
        env.prepend_path('LD_LIBRARY_PATH', self.spec['netcdf-cxx'].libs.directories[0])

    def setup_run_environment(self, env):
        # 设置运行环境
        env.prepend_path('CPATH', self.spec['netcdf-c'].headers.directories[0])
        env.prepend_path('CPATH', self.spec['netcdf-cxx'].headers.directories[0])
        env.prepend_path('LD_LIBRARY_PATH', self.spec['netcdf-c'].libs.directories[0])
        env.prepend_path('LD_LIBRARY_PATH', self.spec['netcdf-cxx'].libs.directories[0])
