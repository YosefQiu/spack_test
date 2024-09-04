from spack import *

class SyclOcean(CMakePackage):
    """SYCL_OCEAN is a CMake-based project for ocean modeling using SYCL."""

    homepage = "https://github.com/YosefQiu/sycl_ocean"
    git      = "https://github.com/YosefQiu/sycl_ocean.git"

    maintainers = ['YosefQiu']

    version('main', branch='master')  # 定义明确的版本

    # Add required dependencies
    depends_on('intel-oneapi-compilers+nvidia')
    depends_on('netcdf-c@4.9+mpi')
    depends_on('vtk+mpi')
    depends_on('yaml-cpp')
    
    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            make()
            make("install")