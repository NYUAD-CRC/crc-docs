Software
========

Software modules
----------------

HPC systems differ from desktop/laptop computers in how
software is installed. In a desktop/laptop you install software
in a pre-defined centralized location where all users can
access it. For instance the command ``apt install python`` or ``yum install python``
will install python version 2.7.5 (on CentOS 8) under /usr/bin.
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

    [wz22@login1 ~]$ matlab
    -bash: matlab: command not found
    [wz22@login1 ~]$ which matlab
    /usr/bin/which: no matlab in (/share/apps/NYUAD/miniconda/3-4.8.2/condabin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/ibutils/bin:/opt/slurm/default/bin:/opt/slurm/default/sbin:/share/apps/dalma/tools:/share/apps/NYUAD/screen/4.3.1/bin:/home/wz22/.local/bin:/home/wz22/bin)
    [wz22@login1 ~]$ module avail matlab

    ---------------------------------------- /share/apps/NYUAD/modules/SOFTWARE ----------------------------------------
    matlab/R2015b matlab/R2019a
    [wz22@login1 ~]$ module load matlab/R2019a
    Loading module 'matlab/R2019a'
    [wz22@login1 ~]$ which matlab
    /share/apps/NYUAD/matlab/R2019a/bin/matlab


``module avail matlab`` shows you all available versions of matlab on Dalma. ``module load matlab/R2019a`` loads the R2019a
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
    matlab –nodisplay –nodesktop –r "mycode.m"

If you use ``csh`` then you need to initialize the software module environment before using ``module`` commands:

.. code-block:: bash

    #!/bin/csh
    source /usr/share/Modules/init/csh
    module purge
    module load matlab
    matlab –nodisplay –nodesktop –r "mycode.m"


Miniconda (Important for Python Users)
--------------------------------------

.. toctree::
   :maxdepth: 2

   /hpc/training/miniconda