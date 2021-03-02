VNC access to Linux Servers
===========================


This document will help to configure VNC software to connect to Linux Servers. VNC is a graphical desktop sharing system which used to share GUI of servers ( mostly Linux in our case ) 


Connect VPN and Login
---------------------

Connect VPN if accessing the system from outside campus

( See How to access NYUAD VPN for more details ) 



Start Server
------------


After login to remote server: 

.. code-block :: bash  

    $ vncserver

If it runs successfully, it will provide you a session number. This will be used in VNC client.

Next, set VNC password:

.. code-block :: bash

    $ vncpasswd

.. note ::

    This needs to be done only once and the same password can be reused for future connections


Start Client
------------

From your preferred VNC client, use FQDN or IP address of the remote machine
with the session number (from `<Start Server>`_) to connect to remote server.




