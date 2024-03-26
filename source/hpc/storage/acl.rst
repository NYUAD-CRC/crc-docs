Data Sharing with ACL
=======================

Introduction
------------

When sharing files on a cluster with other users, it's recommended to use Access Control Lists (ACL). ACL mechanisms allow for fine-grained control over access to files, enabling users 
to share access to their data with others. Unlike setting permissions with ``chmod 777``, which can 
lead to data loss, FACL provides a safer and more flexible way to manage access. This document 
outlines how to use FACLs with the ``getfacl`` and ``setfacl`` commands to view and set access 
permissions.

.. caution:: Sharing your ``$SCRATCH`` (``scratch/<NetID>``) directories with collaborators using ``chmod 777`` is highly 
    discouraged due to the significant security risks it poses. This practice exposes your data and 
    files to everyone, potentially leading to data theft or deletion.


Access Control Lists (ACL) Levels 
---------------------------------

ACL mechanisms, similar to standard Linux POSIX permissions, provide three levels of access control:

- Read (``r``)
- Write (``w``)
- Execute (``x``)

These levels of access can be granted to:

- User (owner of the file)
- Group (owner group)
- Other (everyone else)

ACL allows for granting the same type of access without modifying file ownership or POSIX permissions.

Viewing Permissions
-------------------

To retrieve access permissions for a file, use the ``getfacl`` command:

.. code-block:: bash

    $ getfacl myfile.txt
    # file: myfile.txt
    # owner: ab123
    # group: users
    user::rw-
    group::---
    other::---

Setting Permissions
--------------------

To modify access permissions, use the ``setfacl`` command with the following options:

- ``-m``: Modify ACL
- ``-x``: Remove ACL
- ``-R``: Apply the action recursively (to all files and directories within a directory)

For example, To grant read and write permissions to the user ``abc12`` on the directory ``/scratch/xyz12/abc/def/xyz``, 
follow these steps:

1. Grant execute permissions to each directory in the hierarchy::

    

        setfacl -m u:abc12:x /scratch/xyz12/
        setfacl -m u:abc12:x /scratch/xyz12/abc/
        setfacl -m u:abc12:x /scratch/xyz12/abc/def/

2. Grant read and write permissions to the final directory::

       setfacl -R -m u:abc12:rwx /scratch/xyz12/abc/def/xyz

.. note:: The ``-R`` option in the above step,  will recursively apply the permissions (``rwx``) to 
    all files within the directory and its subdirectories. 

User ``xyz12`` will have read-write permissions to the directory mentioned above.
By setting only execute (``x``) permissions on intermediate directories, access to the contents of those directories is denied to other users.


.. Important::
    When setting ACL for a file like ``/a/b/c/example.out``, ensure appropriate ACLs are also set for all parent directories in the path. 
    For example, to grant read/write/execute permissions for ``/a/b/c/example.out``, also grant at least ``x`` 
    permissions to the directories ``/a``, ``/a/b``, and ``/a/b/c``.

Removing Permissions
--------------------

To remove access permissions set by ACL, you can use the ``setfacl`` command with the ``-x`` 
option followed by the specific entry you want to remove. Below is an example of removing ACL 
permissions for a user ``xyz12`` from the path ``/scrtach/abc12/example/group1``:

.. code-block:: bash

    $ setfacl -x "u:xyz12" /scrtach/abc12/example/group1

This command will remove the access permissions previously granted to the user ``xyz12`` 
to the path ``/scrtach/abc12/example/group1``.

.. note:: ACL permissions can be set or modified only for files and directories 
    that are owned by you.

Flags
-----

Refer to the ``setfacl`` manual page for possible flags. For example:

- ``-m``: Modify
- ``-x``: Remove
- ``-R``: Recursive
- ``-d``: Default

Additional Information
-----------------------

For more details about the ``setfacl`` command, refer to its manual page or visit the following link: `ACL Documentation <https://linux.die.net/man/1/setfacl>`_.
