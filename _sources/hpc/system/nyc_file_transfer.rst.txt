Fast Transfer Between NYU NYC and Dalma
=======================================

The default MLPS link between NY and AD has a low bandwidth. Using port 922 on Dalma will use a 
high bandwidth ANKABUT link instead.

Specifying the port directly
----------------------------

For infrequent data transfer, directly specify the port 922 in your scp command. From your host in NY, run this in the terminal.

**Pulling data from Dalma**

.. code-block:: bash

    scp -P 922 <NetID>@dalma.abudhabi.nyu.edu:~/filename ./

**Pushing data to Dalma**
 
.. code-block:: bash

    scp -P 922 filename <NetID>@dalma.abudhabi.nyu.edu:~/

Setup an alias
--------------

If you need to transfer data frequently, it is easier to setup an alias in your ssh config. In your ``~/.ssh/config``, append the following entries.

.. code-block:: bash

    Host dalma-fast
        Hostname     dalma.abudhabi.nyu.edu
        Port         922
        User         <your-NetID>

Now you should be able to scp to / from Dalma using the ANKABUT fast link by the following commands.

.. code-block:: bash

    scp filename dalma-fast:~/


 

 

 

Windows user can do the same thing by specifying the port 922 in the file transfer software. E.g., FileZilla.