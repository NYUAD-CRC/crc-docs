File Transfer using FileZilla
=============================

You want to transfer data from / to Dalma under Windows, Mac or Linux. But you don't want to use command line. Instead, you want to use an open-source SFTP client with easy-to-use GUI. Then, FileZilla is the choice for you. Follow the instructions below.

Step-by-step guide
------------------

First, install and configure FileZilla in your workstation. These steps need to be done only once.

1. Open your browser in your workstation.
2. Open this page: https://filezilla-project.org/
3. Click Download FileZilla Client.
4. After finishing the downloading, finish the installation. If in question, contact us or check this guide: https://wiki.filezilla-project.org/Client_Installation

Once the installation is done,

1. If you are outside campus network, connect to NYU VPN first.
    :doc:`NYU VPN</hpc/help/linux_vpn>`
2. Open FileZilla. It will prompt a GUI.

    .. image:: /hpc/img/open.png

3. Enter the **Host**, **Username**, **Password** and **Port**. Click **Quickconnect**, as shown in the screenshot below:
    * Host: dalma.abudhabi.nyu.edu
    * Username: Your NetID
    * Password: Your NetID password
    * Port: 22

    .. image:: /hpc/img/quickconnect.png

4. Remote host is connected. The window on the left is local site (your workstation), while the window on the right is remote site (Dalma). By default, the remote path is ``$HOME``, e.g., ``/home/NetID``.

    .. image:: /hpc/img/loggedin.png

5. If you want to change the current directory, double click the target folder.

    .. image:: /hpc/img/change.png

6. To upload a folder or file, right click the target folder or file from local site, select **Upload**.

    .. image:: /hpc/img/upload.png

7. To download a folder or file, right click the target folder or file from remote site, select **Download**.

    .. image:: /hpc/img/download.png


 
.. Note:: 
    
    Check this link for general help on FileZilla (how to change directory, upload / download and comparison...): https://wiki.filezilla-project.org/Using
