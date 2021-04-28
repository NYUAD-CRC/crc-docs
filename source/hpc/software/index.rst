Software
========

On HPC:

1. The Operating System is CentOS 7. Windows / Mac software is not supported.
2. No GUI. No display. (Although we do have a few Visualization nodes, Please refer to the section :doc:`here </hpc/system/visual_nodes>`)

Software Modules
----------------

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
    Alternatively, you can use Dalma miniconda for hassle-free, independent Python environment. Follow this page: :doc:`Miniconda in Dalma </hpc/software/python/dalma_miniconda>`

More information about the software modules in dalma can 
be found in the document here :download:`Dalma SW modules </hpc/docs/Dalma-SWModules.pdf>`

For running Jobs: Please refer to the :doc:`Jobs Management </hpc/jobs/index>` section.

.. important::
    If you have a job with independent computations, then 
    :doc:`Job arrays </hpc/jobs/job_array>` and :doc:`Parallel Job Array </hpc/jobs/parallel_job_array>`  
    are one of the most easiest ways to parallelize 
    your computations. Follow the corresponding highlighted links for a much more detailed example.

.. _dalma_miniconda:

Dalma Miniconda
---------------

We have a centralized installation of :doc:`Miniconda </hpc/software/python/dalma_miniconda>`, 
:doc:`TensorFlow </hpc/software/python/dalma_tensorflow>` and :doc:`PyTorch </hpc/software/python/dalma_pytorch>` in Dalma. Please refer to the highlighted sections for more details.

.. toctree::
   :maxdepth: 1
   :hidden:

   /hpc/software/python/index

.. tip::
    Know more about the GPU nodes available :doc:`here</hpc/system/gpu_nodes>`

R with Dalma Miniconda
----------------------

Users can have their own local installation of R. You can find more details about the same here: :doc:`R in Dalma Miniconda <r_dalma_miniconda>`.

.. toctree::
   :maxdepth: 1
   :hidden:

   /hpc/software/r_dalma_miniconda
   