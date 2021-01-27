Job Array
=========

This example shows how to submit a job array, 
consist of 100 jobs, with environmental variable ``SLURM_ARRAY_TASK_ID`` varies from 1 to 100.

.. code-block:: bash

    #!/bin/bash
    # Set number of tasks to run
    #SBATCH --ntasks=1
    # Walltime format hh:mm:ss
    #SBATCH --time=00:30:00
    # Output and error files
    #SBATCH -o job.%J.out
    #SBATCH -e job.%J.err
    #SBATCH -a 1-100
    
    # **** Put all #SBATCH directives above this line! ****
    # **** Otherwise they will not be effective! ****
    
    echo "I am running job $SLURM_ARRAY_TASK_ID"

Or you can varies ``SLURM_ARRAY_TASK_ID`` from 51 to 100.

.. code-block:: bash

    #SBATCH -a 50-100

Or set the maximum number of simultaneously running tasks from the job array to 10.

.. code-block:: bash

    #SBATCH -a 1-100%10

We only allow a maximum of 200 jobs in queue for any given user.

.. important::
    If you have a job with independent computations, then 
    :doc:`Job arrays </hpc/jobs/job_array>` and :doc:`Parallel Job Array </hpc/jobs/parallel_job_array>`  
    are one of the most easiest ways to parallelize 
    your computations. Follow the corresponding highlighted links for a much more detailed example.