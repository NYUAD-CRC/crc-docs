Jobs Management
===============



On HPC, you don't run it directly on the login nodes. Instead, you submit jobs on login nodes. These jobs will be queued to the system and executed eventually. Conceptually, each job is a 2-step process:

1. You request certain resources from the system. The most common resources are CPU cores. 
2. With the assigned resources, you run your computational tasks.


 
.


.. toctree::
   :maxdepth: 2
      
   /hpc/jobs/quick_start
   /hpc/jobs/job_jubail


.. important::
    If you have a job with independent computations, then 
    :doc:`Job arrays </hpc/jobs/job_array>` and :doc:`Parallel Job Array </hpc/jobs/parallel_job_array>`  
    are one of the most easiest ways to parallelize 
    your computations. Follow the corresponding highlighted links for a much more detailed example.

.. seealso::
    A detailed SLURM guide with more info on the accounts,usage limits can be found :doc:`here <hpc_slurm>`
    and can be downloaded from here :download:`Dalma SLURM </hpc/docs/Dalma-SLURM.pdf>`

.. toctree::
   :maxdepth: 2
      
   /hpc/jobs/batch_job
   /hpc/jobs/interactive
   /hpc/jobs/job_array
   /hpc/jobs/parallel_job_array
   /hpc/jobs/job_submit
   /hpc/jobs/job_status
   /hpc/jobs/job_cancel
   /hpc/jobs/gpu_jobs
   /hpc/jobs/performance
   /hpc/jobs/hpc_slurm
