Software Modules
================

You can compile / install your own software, and/or use our Module system. For the latter, first check what applications are available.

.. code-block:: bash

    # Run the following commands after logging in Dalma
    module avail

Then you could select the desired software to load. The following example shows how to load a self-sufficient-single-application environment for gromacs.

.. code-block:: bash

    # Run the following commands after logging in Dalma
    module load gromacs
    # or use the full module name with version
    module load gromacs/5.0.4

The following example shows how to load an environment for compiling source code from scratch.

.. code-block:: bash

    # Run the following commands after logging in Dalma
    module load gcc
    # multiple modules could be loaded in one line
    module load openmpi fftw3

At this point, compilers like ``gcc``, ``gfortran`` and ``g++`` are available, in a sense that the paths to those executables are prepended to ``$PATH``. Also, paths to libraries files from ``FFTW3`` will be prepended to ``$LD_LIBRARY_PATH``.

**If you cannot find a certain version of the software (for example, you are looking for Python 3, but only to find Python 2 is available), try running the following command to make all modules visible first.**

.. code-block:: bash

    # Run the following commands after logging in Dalma
    module load all
    module avail python
    --------------------------------------- /share/apps/NYUAD/modules/ALL -------------------------------
    python/2.7.11 python/3.5.1

As you can see, ``Python 3`` is available then. You could load ``Python 3`` by loading the specific module.

.. code-block:: bash

    module load python/3.5.1

At this point, you should be able to invoke the executable, e.g., ``python``. 

.. note::
    Alternatively, you can use Dalma miniconda for hassle-free, independent Python environment. Follow this page: :doc:`Miniconda in Dalma </hpc/software/dalma_miniconda>`

More information about the software modules in dalma can 
be found in the document here :download:`Dalma SW modules </hpc/docs/Dalma-SWModules.pdf>`