Fast Transfer Between NYU NYC and NYUAD
=======================================

The default MLPS(Multiprotocol Label Switching) link between NY and AD has a low bandwidth. Using port 922 on NYUAD HPC will use a 
high bandwidth ANKABUT link instead.

Specifying the port directly
----------------------------

For infrequent data transfer, directly specify the port 922 in your scp command. From your host in NY, run this in the terminal.

**Pulling data from Jubail**

.. code-block:: bash

    scp -P 922 <NetID>@jubail.abudhabi.nyu.edu:~/filename ./

**Pushing data to Jubail**
 
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

Now you should be able to scp to / from NYUAD HPC using the ANKABUT fast link by the following commands.

.. code-block:: bash

    scp filename jubail-fast:~/


 

 

 

Windows user can do the same thing by specifying the port 922 in the file transfer software. E.g., FileZilla.
