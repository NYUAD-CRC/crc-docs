Software
========

On HPC:

1. The Operating System is CentOS 8.2. Windows / Mac software is not supported.

For running Jobs: Please refer to the :doc:`Jobs Management </hpc/jobs/index>` section.

.. important::
    If you have a job with independent computations, then 
    :doc:`Job arrays </hpc/jobs/job_array>` and :doc:`Parallel Job Array </hpc/jobs/parallel_job_array>`  
    are one of the most easiest ways to parallelize 
    your computations. Follow the corresponding highlighted links for a much more detailed example.


Software Modules and environment
--------------------------------

.. toctree::
   :maxdepth: 1
   

   /hpc/software/software_modules

.. _hpc_miniconda:

HPC Miniconda
---------------

We have a centralized installation of :doc:`Miniconda </hpc/software/hpc_miniconda>`, 
:doc:`TensorFlow </hpc/software/hpc_tensorflow>` and :doc:`PyTorch </hpc/software/hpc_pytorch>` in the HPC. Please refer to the highlighted sections for more details.

.. toctree::
   :maxdepth: 2
   

   /hpc/software/hpc_miniconda
   /hpc/software/hpc_pytorch
   /hpc/software/hpc_tensorflow

.. tip::
    Know more about the GPU nodes available :doc:`here</hpc/system/gpu_nodes>`
    

Matlab
------

.. toctree::
   :maxdepth: 2

   /hpc/software/matlab_parallel


Singularity
-----------

.. toctree::
   :maxdepth: 2
   

   /hpc/software/singularity
   /hpc/software/singularity_commands
   /hpc/software/singularity_overlays

Miscellaneous
----------------------

.. toctree::
   :maxdepth: 2
   

   /hpc/software/r_hpc_miniconda
   /hpc/software/vscode
   /hpc/software/gdrive
   
