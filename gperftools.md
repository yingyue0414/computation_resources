### gperftools

06/03 by @think92 

- make sure you have gperftools and graphviz installed

> 
> For the Mac users, it can be done by one command using the homebrew. If you never used homebrew to install software before, you need to install the homebrew first on your Mac by typing the following command in the terminal:
> `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
> then,
> `brew install gperftools`
> will install gperftools easily.
> For the Ubuntu users, you can follow these commands to install the gperftools:
> ```
> sudo apt install libunwind8-dev libtool dh-autoreconf
> git clone https://github.com/gperftools/gperftools.git
> cd gperftools
> ./autogen.sh
> ./configure
> make
> sudo make install
> sudo ldconfig
> ```
> Here is the model that we will profile, where the larger time-step iterations are faster than the smaller time-step. We will figure out the reason that slowing down one iteration using smaller time-step and look for some optimization room.
> 
> Kcachegrind (Ubuntu)
> ```
> sudo apt install kcachegrind
> sudo apt-get install graphviz gv
> ```
> qcacehgrind (Mac)
> ```
> brew install graphviz
> brew install qcachegrind
> ```

- In makefile, add -lprofiler  
 ```
LIBS = $(shell gsl-config --libs) -lprofiler
```
Should be the same as  
`g++ -lprofiler my_code.cpp`

- make file
```
make clean
make serial
```

- create profiler directory
```
mkdir profiler
cd profiler
```

- The following steps are based upon [gprofiler tutorial ](https://developer.ridgerun.com/wiki/index.php/Profiling_with_GPerfTools)

- specify `LD_PRELOAD` with path to the `libprofiler.so` where you installed your gprofiler library if on linux and `CPUPROFILE` with an output file name. 
Example:
```
env LD_PRELOAD=/usr/local/lib/libprofiler.so CPUPROFILE=test.prof ../bin/nerdss
```

- Copy` hex.mol `and `parms_phex.inp` into `/nerdss_development/profiler/` and decrease iteration number (in `parms_phex.inp`) if a quick test run is needed.
- Run the simluation with the following command which profile the whole runtime
```
LD_PRELOAD=/usr/local/lib/libprofiler.so CPUPROFILE=dt05.prof ../bin/nerdss -f parms_phex.inp > out.log
```

- Use `pprof` to view analysis of CPU profiling results with the following command (output `.pdf` map)
```
pprof --pdf ../bin/nerdss dt05.prof > dt05.pdf
```
- `(pprof) help` prints out all available commands in `pprof`
- `(pprof) top` outputs functions with highest percentage samples. Referenced from [cpuprofile documentation](https://gperftools.github.io/gperftools/cpuprofile.html):

> Text mode has lines of output that look like this:
> 
>        14   2.1%  17.2%       58   8.7% std::_Rb_tree::find
> Here is how to interpret the columns:
> 
> 1.Number of profiling samples in this function
> 2.Percentage of profiling samples in this function
> 3.Percentage of profiling samples in the functions printed so far
> 4.Number of profiling samples in this function and its callees
> 5.Percentage of profiling samples in this function and its callees
> 6.Function name

- Repeat the process with a lower time step of 0.01 (changing parameters in `parms_phex.inp`). 
- Sample `.pdf` map output:

![image](https://user-images.githubusercontent.com/44514233/171945065-f0bf5ad4-37df-4b37-abf4-48a68705ad19.png)

> Class Name
> Method Name
> local (percentage)
> of cumulative (percentage)


- The section between the following command are mapped.
```
ProfilerStart("outGaussV.prof")
/****
CODE
****/
ProfilerStop()
```
- remove restarts and pdb folder when rerunning simulation
```
rm -r PDB/ RESTARTS/
```
- If environment is defined, no need for redefinition 
```
../bin/nerdss -f parms_phex.inp > out.og
```
