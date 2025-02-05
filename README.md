## Instructions for build
Installation is done through Spack. If you don't have Spack installed or if Spack is new to you. 

I use spack **0.24.0.dev0 (e1b579a8b491b01579a24e18e520c27e7089f24f)**

Please make sure that the spack version is greater than **0.23.0**.  
You can confirm this with the following command
```bash
spack --version
```


```bash
git clone https://github.com/YosefQiu/spack_test.git
spack env create ocn_env
spack env activate ocn_env
spack repo add MOPS
spack add MOPS
spack install
```
