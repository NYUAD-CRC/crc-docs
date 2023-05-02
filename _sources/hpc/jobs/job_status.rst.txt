Checking Job Status
===================

Before and During Job Execution
-------------------------------

This command shows all your current jobs.

``squeue``

Example output:

.. code-block:: console

    [wz22@login-0-1 ~]$ squeue -j 31408
                JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                31408   ser_std  job1.sh     wz22  R       0:02      1 compute-21-4

It means the job with Job ID ``31408``, has been running (``ST: R``) for 2 minutes on ``compute-21-4``.

For more verbose information, use ``scontrol show job``.

.. code-block:: console

    [wz22@login1]$ scontrol show job <jobid>

After Job Execution
-------------------

Once the job is finished, the job can't be inspected by squeue or scontrol show job. At this point, you could inspect the job by sacct.

.. code-block:: console

    [wz22@login1]$ sacct -j <jobid>

The following commands give you extremely verbose information on a job.

.. code-block:: console

    [wz22@login1]$ sacct -j <jobid> -l

