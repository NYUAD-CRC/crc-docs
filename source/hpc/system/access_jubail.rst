Access Jubail
=============

Want to access Jubail? Follow the guide below for Linux / Mac and Windows.

Linux / Mac
------------

**Inside NYU Network**

For Linux/Mac, execute the following command, change ``<NetID>`` to your actual username.

.. code-block:: bash

    ssh <NetID>@jubail.abudhabi.nyu.edu

If you need ``X11`` for GUI interface, add the ``-X`` option.

.. code-block:: bash

    ssh <NetID>@jubail.abudhabi.nyu.edu -X

Outside NYU Network
-------------------

**VPN**

You could either first connect to NYU VPN :doc:`NYU VPN</hpc/help/linux_vpn>` and then connect to Jubail directly. Choose ``vpn.abudhabi.nyu.edu`` as your VPN server.

**Bastion Host**

Or, use bastion host as instructed below.

1. Connect to bastion host.

.. code-block:: bash
    
    ssh <NetID>@hpc.abudhabi.nyu.edu -p 4410


2. On bastion host, connect to Jubail.

.. code-block:: bash
    
    ssh <NetID>@jubail.abudhabi.nyu.edu


**Tunnel configuration**

Or, use tunnel configuration to make things easier as instructed below.

1. Add the following to your ``$HOME/.ssh/config`` on your local workstation. Replace ``<NetID>`` with your actual ``NetID``. Make sure your local port 8023 is available.

.. code-block:: bash

 Host tunnel-ad-hpc
    HostName hpc.abudhabi.nyu.edu
    Port 4410
    ForwardX11 yes
    LocalForward 8023 jubail.abudhabi.nyu.edu:22
    User <NetID>


 Host tunnel-jubail
    HostName localhost
    Port 8023
    ForwardX11 yes
    User <NetID>


2. Open a terminal. Run the following and keep this terminal alive.

.. code-block:: bash

    ssh tunnel-ad-hpc


3. Open a new terminal. Run the following to connect to Jubail.

.. code-block:: bash

    ssh tunnel-jubail

4. If you want to transfer data instead, use the following example.

.. code-block:: bash

    rsync -rav ./local-folder-to-upload tunnel-jubail:/scratch/<NetID>/remote-folder-on-jubail


Windows
-------

**Inside NYU Network**

We recommend Mobaxterm/Putty as your ssh client. Putty is available for download here: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html. 

1. (First-time login only) Setup Butinah session in your putty.
    a. Open Putty. Go to Category -> Session. 
    b. Type jubail.abudhabi.nyu.edu in Host Name (or IP address).
    c. Type Jubail under Saved Sessions.
    d. Click Save button. A new session called Jubail will appear in Saved Sessions. 

.. image:: /hpc/img/putty.png


2. Select Jubail session. Click Load button. 
3. Click Open button.

The configuration will look like this screenshot.



**Outside NYU Network**

You could either first connect to NYU VPN :doc:`NYU VPN</hpc/help/linux_vpn>` and then connect to Jubail directly. Choose vpn.abudhabi.nyu.edu as your VPN server.

Or, use bastion host as instructed below.

1. Follow the instructions above as inside NYU Network, but connect to the host **hpc.abudhabi.nyu.edu** with port **4410** instead of jubail.abudhabi.nyu.edu.
2. Once you are connected, run this in the terminal on hpc.abudhabi.nyu.edu

.. code-block:: bash

    ssh <NetID>@jubail.abudhabi.nyu.edu

Now you are on Jubail.
