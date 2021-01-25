NYU VPN for Linux
=================

This article describes how to connect NYU VPN using Linux.

Use at Your Own Risk

NYU IT does not support VPN for Linux officially. The following instructions are tested with Mint Linux based on Ubuntu 14.04 LTS. They come with absolutely no warranty.

 

Step-by-step guide
------------------

1. Install OpenConnect.
    * (For Debian / Ubuntu user): OpenConnect is available on the repository. Run this in your local machine terminal:

    .. code-block:: bash

        sudo apt-get install openconnect

    * (Compile from source): Download source code and compile yourself. http://www.infradead.org/openconnect/download.html

2. Connect NYU VPN using OpenConnect:
    * Run this in your local machine terminal:

    .. code-block:: bash

        sudo openconnect vpn.abudhabi.nyu.edu

    * Type your netid and password.
    * After successful login, all network traffic will be under VPN.
    * When VPN is no longer needed, type Ctrl+c to exit OpenConnect.
 