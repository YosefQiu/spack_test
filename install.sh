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
install_path=$(spack location -i sycl-ocean)/third_bin
echo "Adding $install_path to PATH..."
export PATH=$install_path:$PATH
