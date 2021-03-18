.. _mount_work:

Mount $WORK with SSHFS
=======================

This page explains how to mount ``$WORK`` on Dalma with SSHFS on your local workstation. 
Only ``$WORK`` is supported, not ``$HOME`` , ``$SCRATCH`` or any other file system on Dalma.
For mounting ``$WORK`` on Windows, Kindly follow the section :ref:`here <mount_work_windows>`

Step-by-step guide
------------------
.. Note:: You might need ``sudo`` for the operations below.

1. **Install SSHFS on your workstation.**
    * Ubuntu:

    .. code-block:: bash

        apt-get install sshfs


    * CentOS:

    .. code-block:: bash

        yum install fuse-sshfs 


    * MacOS: 

    ::
        
        Install FUSE and SSHFS from their official website https://osxfuse.github.io/

2. **On your terminal, mount the drive**
    .. code-block:: bash

        sshfs <NetID>@hpc-cng.abudhabi.nyu.edu:/work/<NetID> <Your-Local-Mount-Point>

    For example, this command mount the ``$WORK`` of NetID ``wz22`` to the local path ``$HOME/work-wz22``

    .. code-block:: bash

        sshfs gh50@hpc-cng.abudhabi.nyu.edu:/work/gh50 $HOME/work-gh50

    These options might increase the speed.

    .. code-block:: bash

        sshfs -o auto_cache -o cache=yes -o kernel_cache -o compression=no -o large_read -o big_writes -o Ciphers=arcfour <NetID>@hpc-cng.abudhabi.nyu.edu:/work/<NetID> <Your-Local-Mount-Point>


3. **Once done, unmount the drive.**
    .. code-block:: bash

        umount <Your-Local-Mount-Point>

.. _mount_work_windows:

Mount $WORK on Windows
----------------------

1. Download the following applications and install them.
    * SSHFS-Win: https://github.com/billziss-gh/sshfs-win/releases/download/v3.5.20024/sshfs-win-3.5.20024-x64.msi
    * WinFsp: https://github.com/billziss-gh/winfsp/releases/download/v1.7/winfsp-1.7.20172.msi
2. Navigate to your Windows File explorer
    .. image:: ../img/mount_work1.png
3. Right click on ‘This PC’ and select ‘Map network drive’:
    .. image:: ../img/mount_work2.png
4. Enter the details and click ‘Finish’:
    .. image:: ../img/mount_work3.png

    * The ‘Drive’ corresponds to the local mountpoint
    * The Folder corresponds to the remote location.It should be noted that by default it connects to the /home and a relative path to the mounting point (/work) should be specified. So in this case the syntax should be as follows:

    .. code-block:: bash

        \\sshfs\<net-id>@cng-hpc.abudhabi.nyu.edu\..\..\work\<netid>

    * For example:

    .. code-block:: bash

        \\sshfs\wz22@cng-hpc.abudhabi.nyu.edu\..\..\work\wz22

5. You will be prompted for a password, after which you would have successfully mounted “$WORK” on to your local workstation.


.. admonition:: Info

    Reference: https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh