Fast Transfer Between NYU NYC and NYUAD
=======================================

The default MLPS(Multiprotocol Label Switching) link between NY and AD has a low bandwidth but using port 922 on NYUAD HPC will use a 
high bandwidth ANKABUT link instead.

Specifying the port directly
----------------------------

For infrequent data transfer, directly specify the port 922 in your scp command.

* Original scp command (low bandwidth):

.. code-block:: bash

    scp source_file_name username@destination_host:destination_folder
    
* Addition of port 922 to the original scp command uses a high bandwidth ANKABUT link instead.
.. code-block:: bash

    scp -P 922 source_file_name username@destination_host:destination_folder

For Example from your host in NY, run this in the terminal.

**For Pulling data from Jubail**

.. code-block:: bash

    scp -P 922 <NetID>@jubail.abudhabi.nyu.edu:~/filename ./

**For Pushing data to Jubail**
 
.. code-block:: bash

    scp -P 922 filename <NetID>@jubail.abudhabi.nyu.edu:~/

Setup an alias
--------------

If you need to transfer data frequently, it is easier to setup an alias in your ssh config. In your ``~/.ssh/config``, append the following entries.

.. code-block:: bash

    Host jubail-fast
        Hostname     jubail.abudhabi.nyu.edu
        Port         922
        User         <your-NetID>

Now you should be able to scp to / from NYUAD HPC from your host in NY using the ANKABUT fast link by the following commands.

.. code-block:: bash

    scp filename jubail-fast:~/


 

 

 

Windows user can do the same thing by specifying the port 922 in the file transfer software. E.g., :doc:`FileZilla </hpc/system/filezilla_transfer>`.
