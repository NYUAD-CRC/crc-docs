User's group Modification
=========================

The application team takes the responsibility to modify NetId user primary and/or secondary groups.

Group property info:

Run all below commands on idm server as root
A cron is run every 15 minutes for admin servers and 1 hour for login, compute nodes to resync password and group files.
GID >= 1000 (RHEL7 now uses GID < 1000 for system groups)
Don't use system groupnames (if you feel a groupname might cause problems, ask first)
Add a new group (automatically selected GID): $ groupadd <groupname>

Add a user to a (secondary) group: $ gpasswd -a <username> <groupname>

Delete a user from a (secondary) group: $ gpasswd -d <username> <groupname>

Change a user's primary group: $ usermod -g <groupname> <username>

To enable group's other members to access a user main directory (by default umask is 0022, all subdirectories should be readable; otherwise use -R option to chgrp or modify subdirectory permission): 

$ chmod g+rx /home/<username>; chgrp <groupname> /home/<username>

$ chmod g+rx /archive/<username>; chgrp <groupname> /archive/<username>

$ chmod g+rx,o+r /scratch/<username>; chgrp <groupname> /scratch/<username>