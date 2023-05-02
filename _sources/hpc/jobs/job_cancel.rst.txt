Cancelling a Job
================

If you decide to end a job prematurely, use ``scancel``

.. code-block:: console

    [wz22@login1]$ scancel <jobid>

.. admonition:: Use with Cautions
    
    To cancel all jobs from your account. Run this on the HPC terminal.

    .. code-block:: console

        [wz22@login1]$ scancel -u <NetID>
