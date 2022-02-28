NYU VPN 
=======

For all details regarding the Virtual Private Network (VPN) and how to connect to NYU VPN for Windows/Mac
(`NYU VPN Page <https://intranet.nyuad.nyu.edu/administrative-services/technology-services/wireless-network-connectivity/remote-connectivity-vpn/>`__).


NYU VPN for Linux
=================

This article describes how to connect to NYU VPN using Linux.


NYU IT does not support VPN for Linux officially (**Use it at your Own Risk**). 

 

Step-by-step guide
------------------

1. Install OpenConnect using any of the following:
    * (For Debian / Ubuntu user): OpenConnect is available on the repository. 
       * Run this in your local machine terminal:

       .. code-block:: bash

        sudo apt-get install openconnect
        
    * Or Compile from source code: 
       * Download source code and compile yourself. http://www.infradead.org/openconnect/download.html

2. Connect NYU VPN using OpenConnect:
    * Run this in your local machine terminal:

    .. code-block:: bash

        sudo openconnect vpn.abudhabi.nyu.edu

    * Type your netid and passwords
       * First password is your netid password.
       * Second password is the multi factor authentication passcode.
    * After successful login, all network traffic will be under VPN.
    * When VPN is no longer needed, type Ctrl+c to exit OpenConnect.
 
