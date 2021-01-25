.. _mount_work:

Mount $WORK with SSHFS
=======================

This page explains how to mount ``$WORK`` on Dalma with SSHFS on your local workstation. Only recent Linux distributions and MacOS are supported. Only ``$WORK`` is supported, not ``$HOME`` , ``$SCRATCH`` or any other file system on Dalma.

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


.. admonition:: Info

    Reference: https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh