Storage
=======

We have 3 storage systems for you: ``$HOME`` (``/home/<NetID>``), ``$SCRATCH`` (``/scratch/<NetID>``), and ``$ARCHIVE`` (``/archive/<NetID>``).

In short, you should 

- Put all your data to  ``$SCRATCH`` and run your jobs from there. 
- Only a small persistent fraction to ``$HOME`` (e.g., source code, executables). 
- For long-term storage, archive them to ``$ARCHIVE``. 
- ``$ARCHIVE`` is not visible on compute nodes but mountable on your local workstation using this :doc:`link <../storage/mount_archive>`, it is
  best suited to quick post-processing, analysis and visualization, without moving your data.

.. Important::
    Backing up is a user's own responsibility. E.g., if a user deletes something accidentally, we can not recover, unfortunately.
    
.. caution::
    Running jobs from ``/home`` is a **serious violation** of HPC policy. Any users who intentionally violate this policy will get their account suspended. 
    ``$HOME`` SSDs are not designed for running jobs, it will kill the SSDs quickly. 


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


- Run ``myquota`` command in the terminal on the HPC to check your current usage and quota where it is only accessible from the login nodes. Example output:

::

                          DISK SPACE                # FILES (1000's)
          filesystem       size      quota            number      quota
                      --------------------------   --------------------------
               /home       92KB       50GB (  0%)         0       500 (  0%)
            /scratch        4KB     5000GB (  0%)         0       500 (  0%)
            /archive        4KB     5120GB (  0%)         0       125 (  0%)

Best Practices
--------------

.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - Dos
      - Remarks
    * - Periodically clean your ``/scratch`` 
      - Files which have not been accessed for 90 days in ``/scratch`` are deleted.  
    * - Once a project is completed move the data over to ``/archive`` using this :doc:`link <../storage/archive>` 
      - Moving data to ``/archive`` frees up space from ``/scratch`` and avoids deletion of files if older than 90 days.
    * - Use tar files to archive directories with large file count	
      - Lesser the number of files, faster is the archiving and dearchiving process

   
