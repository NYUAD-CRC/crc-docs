Data Sharing with Collaborators
===============================

Apart from the existing data sharing options (Groups and ACLs) avaiable on the HPC,
Users can now also share the data/files with their collaborators via a common location (``/scratch/tmp``),
hence minimizing the complexity for quick/temporary sharing of data/files.

.. caution:: Sharing your ``$SCRATCH`` (``scratch/<NetID>``) directories with collaborators using ``chmod 777`` is highly 
    discouraged due to the significant security risks it poses. This practice exposes your data and 
    files to everyone, potentially leading to data theft or deletion.

The instructions for the same are given below:

1. Copy the data to ``/scratch/tmp``
    The owner can copy/transfer the data from his/her account to a folder in ``/scratch/tmp``

    .. code-block:: bash

        cp -r /scratch/<Netid>/data /scratch/tmp/.

2. Copy the data from ``/scratch/tmp``        
    The collaborator can then transfer the data from ``/scratch/tmp`` to his/her account

    .. code-block:: bash

        cp -r /scratch/tmp/data /scratch/<NetId>/data/.


3. **(Optional)** Change permissions of the folder if you would like the data to be private

    

    .. code-block:: bash

        #Change the permission of the copied directory to be accessed only by the owner.
        chmod 700 /scratch/tmp/data
            
        #Allow access to your collaborator to the shared directory.
        setfacl -m u:<NetId>:rx /scratch/tmp/data


.. caution:: **Terms and Conditions**

    * The quota will apply to the owner of data/file residing in ``/scratch/tmp``
    * Users are requested to cleanup the shared data  files on their own.
    * The files will be autocleaned after 7 days





