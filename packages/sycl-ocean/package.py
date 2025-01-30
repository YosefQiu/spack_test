from spack.package import *

class SyclOcean(CMakePackage):
    """SYCL_OCEAN is a CMake-based project for ocean modeling using SYCL."""

    homepage = "https://github.com/YosefQiu/sycl_ocean"
    git      = "https://github.com/YosefQiu/sycl_ocean.git"

    maintainers = ['YosefQiu']

    version('main', branch='master')  # 定义明确的版本

    # Add required dependencies
    depends_on("intel-oneapi-compilers +nvidia", type=("build", "run"))
    depends_on("ndarray +mpi +netcdf", type=("build", "link", "run"))
    depends_on("vtk +mpi", type=("build", "link", "run"))
    depends_on("yaml-cpp", type=("build", "link", "run"))
    
    def cmake_args(self):
        args = []
        args.append("-DCMAKE_C_COMPILER=icx")
        args.append("-DCMAKE_CXX_COMPILER=icpx")
        args.append("-DMPASO_USE_NDARRAY=ON")
        args.append("-DNDARRAY_DIR=" + self.spec["ndarray"].prefix)
        return args