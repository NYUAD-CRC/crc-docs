Software Modules
================

HPC systems differ from desktop/laptop computers in how
software is installed. In a desktop/laptop you install software
in a pre-defined centralized location where all users can
access it. For instance the command ``apt install python`` or ``yum install python``
will install python version 2.7.5 (on CentOS 7) under /usr/bin.
But in a large system hosting a multitude of users it is not
practical to have a single version of "python" installed. Some
users may need access to the latest version, while others
have hard dependencies on an earlier version. And of
course, this applies to all applications. So in an HPC system
software is installed as independent modules which users
must explicitly load into their shell environment.

Here's an example with matlab.

When you login your shell environment is empty of all software modules

.. code-block:: bash

    [wz22@login-0-1 ~]$ matlab
    -bash: matlab: command not found
    [wz22@login-0-1 ~]$ which matlab
    /usr/bin/which: no matlab in (/share/apps/NYUAD/miniconda/3-4.8.2/condabin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/ibutils/bin:/opt/slurm/default/bin:/opt/slurm/default/sbin:/share/apps/the HPC/tools:/share/apps/NYUAD/screen/4.3.1/bin:/home/wz22/.local/bin:/home/wz22/bin)
    [wz22@login-0-1 ~]$ module avail matlab

    ---------------------------------------- /share/apps/NYUAD/modules/SOFTWARE ----------------------------------------
    matlab/R2021a  matlab/R2023a  matlab/R2023b  matlab/R2024a  matlab/R2024b  matlab/R2025a
    [wz22@login-0-1 ~]$ module load matlab
    Loading module 'matlab/R2024b'
    [wz22@login-0-1 ~]$ which matlab
    /share/apps/NYUAD/matlab/R2024b/install/bin/matlab


``module avail matlab`` shows you all available versions of matlab on the HPC. ``module load matlab/R2024b`` loads the R2024b
version into your shell environment. So when you invoke ``matlab`` you actually use the correct version.

Software module environment are set on a per shell instance. So if you open a new terminal on a login node the
environment you may have set in another terminal will not be propagated.
You can control and monitor the contents of your software modules environment with the following commands:

.. list-table::
    :widths: auto
    :header-rows: 1

    *   - Command
        - Description
    *   - ``module list``
        - Display contents of your software modules environment
    *   - ``module purge``
        - Reset your software modules environment
    *   - ``module avail``
        - Display the list of all software modules available
    *   - ``module load XXX``
        - Load software module XXX into your environment
    *   - ``module unload XXX``
        - Unload software module XXX from your environment


As a guideline you should:

- Never add ``module load`` into your .bashrc file
- Use ``module purge`` before loading a new module environment to run an application
- Use a shell script to run an application and include the necessary modules in the script:

.. code-block:: bash

    #!/bin/bash
    module purge
    module load matlab
    matlab –batch mycode

If you use ``csh`` then you need to initialize the software module environment before using ``module`` commands:

.. code-block:: bash

    #!/bin/csh
    source /usr/share/Modules/init/csh
    module purge
    module load matlab
    matlab –batch mycode
    
            
You can compile / install your own software, and/or use our Module system. For the latter, first check what applications are available.

.. code-block:: bash

    # Run the following commands after logging in the HPC
    module avail

Then you could select the desired software to load. The following example shows how to load a self-sufficient-single-application environment for gromacs.

.. code-block:: bash

    # Run the following commands after logging in the HPC
    module load gromacs
    # or use the full module name with version
    module load gromacs/5.0.4

The following example shows how to load an environment for compiling source code from scratch.

.. code-block:: bash

    # Run the following commands after logging in the HPC
    module load gcc
    # multiple modules could be loaded in one line
    module load openmpi fftw3

At this point, compilers like ``gcc``, ``gfortran`` and ``g++`` are available, in a sense that the paths to those executables are prepended to ``$PATH``. Also, paths to libraries files from ``FFTW3`` will be prepended to ``$LD_LIBRARY_PATH``.

**If you cannot find a certain version of the software (for example, you are looking for Python 3, but only to find Python 2 is available), try running the following command to make all modules visible first.**

.. code-block:: bash

    # Run the following commands after logging in the HPC
    module load all
    module avail python
    --------------------------------------- /share/apps/NYUAD/modules/ALL -------------------------------
    python/2.7.11 python/3.5.1

As you can see, ``Python 3`` is available then. You could load ``Python 3`` by loading the specific module.

.. code-block:: bash

    module load python/3.5.1

At this point, you should be able to invoke the executable, e.g., ``python``. 

.. note::
    Alternatively, you can use the HPC miniconda for hassle-free, independent Python environment. Follow this page: :doc:`Miniconda in HPC </hpc/software/hpc_miniconda>`

More information about the software modules in the HPC can 
be found in the document here :download:`HPC SW modules </hpc/docs/Dalma-SWModules.pdf>`