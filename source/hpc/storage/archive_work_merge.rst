Merge of $WORK and $ARCHIVE
===========================

In order to simplify the storage mount points and the user experience in storing their data on the 
Jubail HPC, We have merged the functionalities of two storages, ``$WORK`` (``/work/<NetID>``) and 
``$ARCHIVE`` (``/archive/NetID>``) into a single storage ``$ARCHIVE`` (``/archive/<NetID>``).

This section highlights the major changes which 
affect's the user experience after the merge.

1. Storage Mountpoints
2. Functionality
3. Archiving


Summary
-------
.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - 
      - **Before**
      - **Now**
    * - **Storage Mountpoints**
      - 
      - 
    * - 
      - The filesystems available for each user were as follows:

        - ``$HOME (/home/<NetID>)``

        - ``$SCRATCH (/scratch/<NetID>)``

        - ``$WORK (/work/<NetID>)``

        - ``$ARCHIVE (/archive/<NetID>)``
      - The filesystems available for each user is now:

        - ``$HOME (/home/<NetID>)``

        - ``$SCRATCH (/scratch/<NetID>)``

        - ``$ARCHIVE (/archive/<NetID>)``
    * - 
      -
      -  
        - The ``/work/<NetID>`` has been discontinued from 2nd Feb 2023. The previous data in ``/work/<NetID>`` is 
          moved to ``/archive/work/<NetID>`` as a temporary staging area to allow users to move out their 
          existing data from ``$WORK`` to archive (``/archive/<NetID>/…``). 
        
        - The ``/archive/work/<NetID>`` will be available for the users from the 3rd of Feb 2023 and 
          would be deprecated after a period of 180 days.
    * - **Functionality**
      - 
      - 
    * - 
      - The basic funcionality of ``$WORK`` and ``$ARCHIVE`` were as follows:

        - ``$WORK``: Additional form of storage for researchers which is also externally mountable on a local workstation/PC.

        - ``$ARCHIVE``: A long term storage solution in the form of tape drives for data which isn't frequently used. 
      - 
        
        - The merging of two mountpoints (``$ARCHIVE`` and ``$WORK`` ) into a single mountpoint (``$ARCHIVE``)
          incorporates the functionalities of both and hence reducing the complexity at the user end.
        
        - The new ``$ARCHIVE`` acts as a from of storage that can be externally mounted to local workstation/PC 
          and acts as a solution for long term storage as well. 
    * - **Accessing $ARCHIVE**
      -
      -
    * - 
      - ``$ARCHIVE`` was inaccessible using the general unix commands (``cd , cp , mv`` etc) and was
        accessible only using the dmf commands (``dmfls , dmfput , dmfget`` etc).
      - Users can move their files directly to archive using the traditional unix commands (``cp , mv`` etc) 
        instead of the earlier dmf commands (``dmfput,dmfget`` etc) which are still available.
    * - 
      - 
      - Users would also be able to navigate through their ``/archive/<NetID>`` directory unlike earlier.
    * - 
      -
      - More details on the commands for ``$ARCHIVE`` can be found :doc:`here </hpc/storage/archive>`
    


