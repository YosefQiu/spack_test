spack env create test_env24
spack env activate test_env24
spack add intel-oneapi-compilers+nvidia
spack add netcdf-c@4.9+mpi
spack add vtk+mpi
spack add yaml-cpp
spack install
spack load intel-oneapi-compilers
spack load netcdf-c
spack load vtk
spack load yaml-cpp
spack repo add spack_test
spack add sycl-ocean
spack install
spack load sycl-ocean
install_path=$(spack find -p sycl-ocean | grep "sycl-ocean" | awk '{print $2}')
if [ -d "$install_path" ]; then
    cd "$install_path"
    echo "Current directory: $(pwd)"
else
    echo "Directory not found: $install_path"
fi