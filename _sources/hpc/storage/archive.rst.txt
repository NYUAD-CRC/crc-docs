$ARCHIVE
========

When storage is shared among many users rules must be set to prevent users to consume disk space
excessively at the expense of others. For this purpose HPC systems enforce disk quotas to users and
groups of users. The regular cleanup of the ``/scratch`` storage is essential to maintain its efficiency 
and easily manage the capacity. 
The current policy is to remove any files(data) that have not been accessed (viewed, created or modified) 
for more than 90 days.

On the HPC disk quotas are enforced on ``/home`` and ``/scratch`` (not ``/archive`` ). There are two
quota constraints: the total amount of disk space and the total number of files. Once you reach a quota
limit your jobs may be killed. So it is a good practice to check your quota before submitting a job that
will generate a lot of data.

Run ``myquota`` command in the terminal on the HPC to check your current usage and quota. Example output:

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
      - ``dmfls /archive/wz22``
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
    The guide to long term storage (archive) can be downloaded from here: :download:`Archive Storage <../docs/Dalma-Storage.pdf>`


archive.sh
----------

We also have a script ``archive.sh`` which facilitates this process. The ``archive.sh`` takes one argumnet in the form 
of the path of the directory to be archived. 

The ``archive.sh`` does the follwoing:

1. Create a tar with the same name and the date appended.
2. Archive the tar using dmfput.

.. code-block:: bash

    #USAGE:
    #archive.sh <Path-to-dir-to-be-archived>

    #example
    archive.sh /scratch/wz22/abc/def

* This will create a tar in the directory ``/scratch/wz22/abc`` with the name ``def-ddmmyyyy.tar.gz`` where
    ``ddmmyyyy`` corresponds to date the script ``archive.sh`` was invoked.
* Once the tar creation is done, the tar is archived using ``dmpfput``

.. tip::
    If you have a larger directory to be archived, you could use **screen.sh** script to run the 
    command in background as follows:
    
    .. code-block:: bash

        #screen.sh <command to be executed>

        #example:
        screen.sh "archive.sh /scratch/wz22/abc/def"   
         
        This script will do three things:
        * Execute the command in the background (inside the screen).
        * Echo/ Print the command to the terminal.
        * keep track of the command and its progress in a file in the same working directory called output_background.log

 
.. note::
    You can use the following command to list the contents of the folder not accessed for "N" number of days.
    
    .. code-block:: bash

        #lfs find <path-to-folder> --atime +<number-of-days> --type f

        #example:
        lfs find /scratch/wz22/abc --atime +250 --type f

.. tip::
    The archiving (``dmfput`` & ``dmfget``) might take some time for larger files. Hence It is 
    advisable to use ``screen`` sessions to run the same in the background.

