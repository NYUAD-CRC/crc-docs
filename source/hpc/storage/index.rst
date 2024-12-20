Storage
=======

We have 3 storage systems for you: ``$HOME`` (``/home/<NetID>``), ``$SCRATCH`` (``/scratch/<NetID>``) and ``$ARCHIVE`` (``/archive/<NetID>``).

.. note::
  Kindly note that ``$WORK`` is now discontinued. ``$WORK`` and ``$ARCHIVE`` are mereged together to ``$ARCHIVE``
  to incoporate both their functionalities into one. Kindly refer the doc :doc:`here <archive_work_merge>`
  for the major changes

In short, you should 

- Put all your data to  ``$SCRATCH`` and run your jobs from there. 
- Only a small persistent fraction to ``$HOME`` (e.g., source code, executables). 
- For long-term storage, archive them to ``$ARCHIVE``. 
- ``$ARCHIVE`` is not visible on compute nodes but mountable on your local workstation, 
  best suited to quick post-processing, analysis and visualization, without moving your data.

Backing up is a user's own responsibility. E.g., if a user deleted something accidentally, 
we can not recover, unfortunately.

.. caution::
    Running jobs from ``/home`` is a **serious violation** of HPC policy. Any users who intentionally violate this policy will get their account suspended. 
    ``$HOME`` SSDs are not designed for this purpose, it will kill the SSDs quickly. 


.. toctree::

  /hpc/storage/home_scratch
  /hpc/storage/archive
  /hpc/storage/data_sharing
  /hpc/storage/acl
  /hpc/storage/archive_work_merge
  /hpc/storage/mount_archive

Summary
-------


.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - 
      - $HOME
      - $SCRATCH
      - $ARCHIVE
    * - Use for storing 
      - source code / executables 
      - data  
      - anything
    * - Accessible From
      - login / compute	
      - login / compute		
      - login
    * - Use to Run Jobs	
      - No	
      - Yes	
      - No
    * - Retention Time (Days)	
      - No Limit	
      - 90	
      - No Limit
    * - Mountable	
      - No	
      - No		
      - Yes
    * - Default Quota	
      - 50GB, 500K Files	
      - 5TB, 500K Files		
      - No Limit


  


Know Your Quota
---------------


- Run ``myquota`` command in the terminal on the HPC to check your current usage and quota. Example output:

::

                             DISK SPACE                # FILES (1000's)
          filesystem       size      quota            number      quota
                      --------------------------   --------------------------
               /home       39GB       50GB ( 80%)       328       500 ( 66%)
            /scratch       67GB     5000GB (  1%)       191       500 ( 38%)
            /archive          0          0 (  0%)         0         0 (  0%)


For data transfers please refer to the **Data Trasnfers** section :ref:`here <data_transfers>`

Best Practices
--------------

.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - Dos
      - Remarks
    * - Periodically clean your ``/scratch`` 
      - Files which have not been accessed for 90 days in ``/scratch`` are deleted.  
    * - Once a project is completed move the data over to ``/archive`` using this :doc:`link <./archive>`
      - Moving data to ``/archive`` frees up space from ``/scratch`` and avoids deletion of files if older than 90 days.
    * - Use tar files to archive directories with large file count	
      - Lesser the number of files, faster is the archiving and dearchiving process
    

   
