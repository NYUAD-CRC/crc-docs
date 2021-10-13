$ARCHIVE
========

When storage is shared among many users rules must be set to prevent users to consume disk space
excessively at the expense of others. For this purpose HPC systems enforce disk quotas to users and
groups of users. The regular cleanup of the ``/scratch`` storage is essential to maintain its efficiency 
and easily manage the capacity. 
The current policy is to remove any files(data) that have not been accessed (viewed, created or modified) 
for more than 90 days.

On Dalma disk quotas are enforced on ``/home`` and ``/scratch`` (not ``/archive`` ). There are two
quota constraints: the total amount of disk space and the total number of files. Once you reach a quota
limit your jobs may be killed. So it is a good practice to check your quota before submitting a job that
will generate a lot of data.

Run ``myquota`` command in the terminal on Dalma to check your current usage and quota. Example output:

::

                        DISK SPACE                # FILES (1000's)
    filesystem       size      quota            number      quota
                --------------------------   --------------------------
    /home         131KB     6442MB ( 0%)           0        100 ( 0%)
    /scratch      220GB     5242GB ( 4%)           4        500 ( 1%)
    /work         4KB       5242GB ( 0%)           0        512 ( 0%)
    /archive      418GB     5242GB ( 8%)           3        125 ( 3%)


Quick Glance into the archive commands
--------------------------------------

.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - Action
      - Command
      - Example
    * - List the Files 
      - ``dmfls <path-to-archive>`` 
      - ``dmfls /achive/wz22``
    * - Copy to Archive
      - ``dmfput <full-path-to-scracth> <full-path-to-archive>``	
      - ``dmfput /scratch/wz22/abc/def /archive/wz22/.``
    * - Retrieve from Archive	
      - ``dmfget <full-path-to-archive> <full-path-to-scratch>``
      - ``dmfget /archive/wz22/def /scratch/wz22/abc/.``	
    * - Delete from archive	
      - ``dmfrm -r <full-path-to-archive-dir>``
      - ``dmfrm -r /archive/wz22/def``


.. important::
    The guide to long term storage (archive) can be downloaded from here: :download:`Dalma Storage <../docs/Dalma-Storage.pdf>`

.. note::
    You can use the following command to list the contents of the folder not accessed for "N" number of days.
    
    .. code-block:: bash

        #lfs find <path-to-folder> --atime +<number-of-days> --type f

        #example:
        lfs find /scratch/wz22/abc --atime +250 --type f

.. tip::
    The archiving (``dmfput`` & ``dmfget``) might take some time for larger files. Hence It is 
    advisable to use ``screen`` sessions to run the same in the background.

    