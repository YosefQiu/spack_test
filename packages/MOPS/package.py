from spack.package import *

class Mops(CMakePackage):
    """MOPS is a CMake-based project for mpas-ocean partaicles trajectory using SYCL."""

    homepage = "https://github.com/YosefQiu/MOPS"
    git      = "https://github.com/YosefQiu/MOPS.git"

    maintainers = ['YosefQiu']

    version('main', branch='spack')  

    variant('vtk', default=True, description='Enable VTK support')

    # Add required dependencies
    depends_on("intel-oneapi-compilers +nvidia", type=("build", "run"))
    depends_on("ndarray+hdf5+netcdf+mpi+cuda+vtk", type=("build", "link", "run"))
    depends_on("vtk@9.2.2", when='+vtk', type=("build", "link", "run"))
    depends_on("yaml-cpp", type=("build", "link", "run"))
    depends_on("netcdf-c", type=("build", "link", "run"))
    
    def cmake_args(self):
        args = []
        args.append("-DCMAKE_C_COMPILER=icx")
        args.append("-DCMAKE_CXX_COMPILER=icpx")
        args.append("-DMPASO_USE_NDARRAY=ON")
        args.append("-DNDARRAY_DIR=" + self.spec["ndarray"].prefix)
        
        if '+vtk' in self.spec:
            args.append("-USE_VTK=ON")
            args.append("-DVTK_DIR=" + self.spec["vtk"].prefix)
        
        return args
