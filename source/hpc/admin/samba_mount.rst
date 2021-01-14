Samba Mount
===========

To enable a user to mount /work through Samba, do:

Create a local public user as in Dalma User Account 

On one of login nodes as root, add <unix_username> to Samba password file and set a temporary password:

    /usr/bin/smbpasswd -a <unix_username>
Ask  <unix_username> to login to Dalma and change Samba password using: smbpasswd

On client server, mount \\hpc-cng.abudhabi.nyu.edu\work with user: dalma\<unix_username>