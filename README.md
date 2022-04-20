## MFA-DVR: *Direct Volume Rendering of MFA Models*
Created by <a href="https://github.com/sunjianxin" target="_blank">Jianxin Sun</a>, <a href="http://vis.unl.edu/~yu/" target="_blank">Hongfeng Yu</a> from University of Nebraska-Lincoln, and <a href="https://mathweb.ucsd.edu/~dlenz/" target="_blank">David Lenz</a>, <a href="https://www.mcs.anl.gov/~tpeterka/" target="_blank">Tom Peterka</a> from Argonne National Laboratory

![results](https://github.com/sunjianxin/VTK_MFA-DVR/blob/main/doc/teaser.png)
Demo video can be found <a href="https://youtu.be/FHzvs5nITpw" target="_blank">here</a>.

### Introduction
This work is the implementation of MFA-DVR, direct volume rendering pipeline using MFA model, on top of <a href="https://github.com/Kitware/VTK" target="_blank">VTK</a> for accessibility to scieintific visualization community. The VTK version used is 9.0.3. 
   
### Installation
1. Get VTK_MFA-DVR source code
```bash
git clone https://github.com/sunjianxin/VTK_MFA-DVR.git
```
2. Configure VTK_FMA-DVR using ccmake
    * Initialize the cache by typing ‘c’ for configure.
    * Turn on BUILD_EXAMPLES and BUILD_SHARED_LIBS.
    * Replace Debug by Release under CMAKE_BUILD_TYPE.
    * Once this is done type ‘c’ again.
    * Type ‘c’ one last time to rerun the configuration with those parameters.
    * Type ‘g’. CMake should exit after having generated a Makefile
```bash
cd VTK_MFA-DVR
mkdir build
cd build
ccmake ..
```
3. Configure VTK_MFA-DVR using config file
Shade can be turn on and off in *external/config.h file*
4. Build and install
```bash
make install
```
### Example
To visualize volumetric data usimg MFA-DVR, please find the examples with detailed instruction in <a href="https://github.com/sunjianxin/example_MFA-DVR" target="_blank">example_MFA-DVR</a>.
