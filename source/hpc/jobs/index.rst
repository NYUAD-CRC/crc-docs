Jobs Management
===============



On HPC, you don't run it directly on the login nodes. Instead, you submit jobs on login nodes. These jobs will be queued to the system and executed eventually. Conceptually, each job is a 2-step process:

1. You request certain resources from the system. The most common resources are CPU cores. 
2. With the assigned resources, you run your computational tasks.



.. toctree::
    :glob:
   :maxdepth: 2
   

   
   /hpc/jobs/batch_job
   /hpc/jobs/interactive
   /hpc/jobs/job_array
   /hpc/jobs/parallel_job_array
   /hpc/jobs/job_submit
   /hpc/jobs/job_status
   /hpc/jobs/job_cancel
   /hpc/jobs/performance