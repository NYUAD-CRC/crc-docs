Storage
=======

We have 4 storage systems for you: ``$HOME`` (``/home/<NetID>``), ``$SCRATCH`` (``/scratch/<NetID>``), ``$WORK`` (``/work/<NetID>``) and ``$ARCHIVE`` (``/archive/<NetID>``).

In short, you should 

- Put all your data to  ``$SCRATCH`` and run your jobs from there. 
- Only a small persistent fraction to ``$HOME`` (e.g., source code, executables). 
- For long-term storage, archive them to ``$ARCHIVE``. 
- ``$WORK`` is not visible on compute nodes but mountable on your local workstation, best suited to quick post-processing, analysis and visualization, without moving your data.

Backing up is a user's own responsibility. E.g., if a user deleted something accidentally, we can not recover, unfortunately.



**Summary**


.. list-table:: 
    :widths: 1 1 1 1 1 
    :header-rows: 1

    * - 
      - $HOME
      - $SCRATCH
      - $WORK
      - $ARCHIVE
    * - Use for storing 
      - source code / executables 
      - data 
      - anything 
      - anything
    * - Accessible From
      - login / compute	
      - login / compute	
      - login	
      - login
    * - Use to Run Jobs	
      - No	
      - Yes	
      - No	
      - No
    * - Retention Time (Days)	
      - No Limit	
      - 90	
      - 120	
      - No Limit
    * - Mountable	
      - No	
      - No	
      - Yes	
      - No
    * - Default Quota (star)	
      - 5GB, 100K Files	
      - 5TB, 500K Files	
      - 5TB, 500K Files	
      - 5TB, 125K Files

**Know Your Quota**


- Run ``myquota`` command in the terminal on Dalma to check your current usage and quota. Example output:

::

                        DISK SPACE                # FILES (1000's)
    filesystem       size      quota            number      quota
                --------------------------   --------------------------
    /home         131KB     6442MB ( 0%)           0        100 ( 0%)
    /scratch      220GB     5242GB ( 4%)           4        500 ( 1%)
    /work         4KB       5242GB ( 0%)           0        512 ( 0%)
    /archive      418GB     5242GB ( 8%)           3        125 ( 3%)




For data transfers please refer to the **Data Trasnfers** section :ref:`here <data_transfers>`


.. toctree::
    :glob:
   :maxdepth: 2
   

   /hpc/storage/home_scratch
   /hpc/storage/work
   /hpc/storage/archive
   
   