.. _mount_archive:

Mount $ARCHIVE with SSHFS
==========================

This page explains how to mount ``$ARCHIVE`` on the HPC with SSHFS on your local workstation. 
Only ``$ARCHIVE`` is supported, not ``$HOME`` , ``$SCRATCH`` or any other file system on the HPC.
For mounting ``$ARCHIVE`` on Windows, Kindly follow the section :ref:`here <mount_ARCHIVE_windows>`

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

        sshfs <NetID>@hpc-cng.abudhabi.nyu.edu:/archive/<NetID> <Your-Local-Mount-Point>

    For example, this command mount the ``$ARCHIVE`` of NetID ``wz22`` to the local path ``$HOME/work-wz22``

    .. code-block:: bash

        sshfs wz22@hpc-cng.abudhabi.nyu.edu:/archive/wz22 $HOME/work-wz22

    These options might increase the speed.

    .. code-block:: bash

        sshfs -o auto_cache -o cache=yes -o kernel_cache -o compression=no -o large_read -o big_writes -o Ciphers=arcfour <NetID>@hpc-cng.abudhabi.nyu.edu:/archive/<NetID> <Your-Local-Mount-Point>


3. **Once done, unmount the drive.**
    .. code-block:: bash

        umount <Your-Local-Mount-Point>

.. _mount_archive_windows:

Mount $ARCHIVE on Windows
--------------------------

1. Download the following applications and install them on your local Windows PC.
    * :download:`SSHFS-Win<https://github.com/billziss-gh/sshfs-win/releases/download/v3.5.20024/sshfs-win-3.5.20024-x64.msi>`
    * :download:`WinFsp<https://github.com/billziss-gh/winfsp/releases/download/v1.7/winfsp-1.7.20172.msi>`
2. **Navigate to your Windows File explorer**
3. Right click on ``This PC`` and select ``Map network drive``:
    .. image:: ../img/mount_work1.png
4. Enter the details and click ``Finish``:
    .. image:: ../img/mount_work2.png

    * The ``Drive`` corresponds to the local mountpoint
    * The ``Folder`` corresponds to the remote location.It should be noted that by default it connects to the ``/home`` and a relative path to the mounting point (``/work``) should be specified. So in this case the syntax should be as follows:

    .. code-block:: bash

        \\sshfs\<net-id>@hpc-cng.abudhabi.nyu.edu\..\..\archive\<netid>

    * For example:

    .. code-block:: bash

        \\sshfs\wz22@hpc-cng.abudhabi.nyu.edu\..\..\archive\wz22

5. You will be prompted for a password, after which you would have successfully mounted ``$ARCHIVE`` on to your local workstation.
    .. image:: ../img/mount_work3.png

.. admonition:: Info

    Reference: https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh
