Interactive Sessions
====================

You could get an interactive session directly from your terminal, on compute nodes. Only short interactive jobs should be used (e.g., experimenting with new modifications to your Matlab code).

To start an interactive session, use srun command:

.. code-block:: bash

    srun --pty -n 1 /bin/bash

Then you can run your applications on the terminal directly. E.g., 

.. code-block:: bash

    [wz22@login-0-1 ~]$ srun --pty -n 1 /bin/bash
    srun: job 775175 queued and waiting for resources
    srun: job 775175 has been allocated resources
    [wz22@compute-21-1 ~]$

.. warning::
    In a real scenario, the system might be 
    exhausted with no available resources to you. You need to wait in this circumstance.

In this example, user ``wz22`` requested 1 CPU core (``-n 1``) on login node (``login-0-1``). The system responded, assigned a job id (``775175``), queued the job and assigned 1 CPU core from one of the compute nodes (``compute-21-1``) to the user.

To exit the interactive session, type ``Ctrl+d``, or 

.. code-block:: bash

    exit    
