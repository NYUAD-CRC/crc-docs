Storage
=======

We have 4 storage systems for you: ``$HOME`` (``/home/<NetID>``), ``$SCRATCH`` (``/scratch/<NetID>``), ``$WORK`` (``/work/<NetID>``) and ``$ARCHIVE`` (``/archive/<NetID>``).

In short, you should 

- Put all your data to  ``$SCRATCH`` and run your jobs from there. 
- Only a small persistent fraction to ``$HOME`` (e.g., source code, executables). 
- For long-term storage, archive them to ``$ARCHIVE``. 
- ``$WORK`` is not visible on compute nodes but mountable on your local workstation, best suited to quick post-processing, analysis and visualization, without moving your data.

Backing up is a user's own responsibility. E.g., if a user deleted something accidentally, we can not recover, unfortunately.

.. caution::
    Running jobs from ``/home`` is a **serious violation** of HPC policy. Any users who intentionally violate this policy will get their account suspended. 
    ``$HOME`` SSDs are not designed for this purpose, it will kill the SSDs quickly. 



Summary
-------


.. list-table:: 
    :widths: auto 
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
      - 20GB, 150K Files	
      - 5TB, 500K Files	
      - 5TB, 500K Files	
      - 5TB, 125K Files


.. toctree::

  /hpc/storage/home_scratch
  /hpc/storage/work
  /hpc/storage/archive
  /hpc/storage/data_sharing
  
* :doc:`$HOME and $SCRATCH <home_scratch>`
* :doc:`$WORK <work>`
* :doc:`$ARCHIVE <archive>`
* :doc:`Data Sharing with Collaborators <data_sharing>`

Know Your Quota
---------------


- Run ``myquota`` command in the terminal on the HPC to check your current usage and quota. Example output:

::

                        DISK SPACE                # FILES (1000's)
    filesystem       size      quota            number      quota
                --------------------------   --------------------------
    /home         131KB     20GB   ( 0%)           0        150 ( 0%)
    /scratch      220GB     5242GB ( 4%)           4        500 ( 1%)
    /work         4KB       5242GB ( 0%)           0        512 ( 0%)
    /archive      418GB     5242GB ( 8%)           3        125 ( 3%)




For data transfers please refer to the **Data Trasnfers** section :ref:`here <data_transfers>`



   
