Software
========

On HPC:

1. The Operating System is CentOS 7. Windows / Mac software is not supported.
2. No GUI. No display. (Although we do have a few Visualization nodes, Please refer to the section :doc:`here </hpc/system/visual_nodes>`)

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

.. _dalma_miniconda:

Dalma Miniconda
---------------

We have a centralized installation of :doc:`Miniconda </hpc/software/dalma_miniconda>`, 
:doc:`TensorFlow </hpc/software/dalma_tensorflow>` and :doc:`PyTorch </hpc/software/dalma_pytorch>` in Dalma. Please refer to the highlighted sections for more details.

.. toctree::
   :maxdepth: 2
   

   /hpc/software/dalma_miniconda
   /hpc/software/dalma_pytorch
   /hpc/software/dalma_tensorflow

.. tip::
    Know more about the GPU nodes available :doc:`here</hpc/system/gpu_nodes>`
    
    
Singularity
-----------

.. toctree::
   :maxdepth: 2
   

   /hpc/software/singularity
   /hpc/software/singularity_commands
   /hpc/software/singularity_conda

Miscellaneous
----------------------

.. toctree::
   :maxdepth: 2
   

   /hpc/software/r_dalma_miniconda
   
   /hpc/software/dalma_jupyter
   