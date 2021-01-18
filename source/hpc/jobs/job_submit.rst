Submitting a Job
================

Once you have your job script prepared, you could use the command 
**sbatch** to submit your job.

.. code-block:: bash

    sbatch <jobscript>

Let say if you saved your job script into a file called ``job.sh``. Then you should run the following.

.. code-block:: bash

    sbatch job.sh

After the submission, it will return the corresponding job id. E.g.,

.. code-block:: bash

    [wz22@login-0-1 overview]$ sbatch threads-job.sh
    Submitted batch job 775602

In this case, the job id is ``775602``. You can safely log off Dalma at this point. Once the system can accommodate your request, the script will be executed. The screen output will be saved to the files you specified in the job script.
