IIQ User Operation
==================

IIQ is the user account management used by NYU Account Management office. The account sync is done through user account 'idm' on idm server. This user is allowed to run selective sudo with the command list given in IIQ_CMDS variable in /etc/sudoers.

At the moment, some IIQ commands initiated from NY don't quite make sense, therefore there are some commands such as /bin/echo which need to be listed in the sudo file.

IIQ also initiated some prechecks by running some commands such as /usr/sbin/useradd which we don't want because useradd creates user account but don't properly create /scratch, /archive, etc. as well as password and group files sync. Hence useradd, usermod, userdel commands are moved to <command>.real and in their place a wrapper is created to disable idm user execution of these commands.

Dalma IIQ scripts
There are 5 IIQ scripts which we use to manage user accounts on Dalma: iiq_archiveUser.sh, iiq_createUser.sh, iiq_deleteUser.sh, iiq_expireUser.sh, iiq_renewUser.sh; all in /usr/sbin. A configuration settings is placed in /etc/idm/iiq_config.sh and log files in /var/log/idm. Using a single script to perform many subtasks is preferable because of our abilities to do error logging as well as parallel tasks execution. The scripts also optionally perform prechecks of the account operation logic.

Because user filesystems (/home, /scratch, etc.) are not mounted on idm server, the user account operation is split into two steps. The first step is done on idm server; the 5 scripts only modify password, group, shadow, gshadow files. These password, etc. files are immediately synced to /etc/idm folder on mgmt-gw server; then synced within 15 minutes to admin servers and within 1 hour from login, compute, etc. nodes.

In the second step, inside these 5 scripts (on idm server), an ssh connection is made into mgmt-gw to perform folders creation and bastion host account operation. The corresponding 5 scripts on mgmt-gw server do not modify password, etc. files on mgmt1 or mgmt2 server.

The IIQ scripts have the following functions:

iiq_createUser.sh: On idm server, create a user account; on mgmt-gw server, create user folder in /home, /archive, and /scratch, and apply quotas. If old folders in expired folder exist, they will be used instead of creating new folders. Also create account in the bastion host.

iiq_expireUser.sh: On idm server, change user shells into expiredshell; on mgmt-gw server, perform the same to bastion host.

iiq_renewUser.sh: On idm server, change user shells back into default user shells; on mgmt-gw server, perform the same to bastion host.

iiq_archiveUser.sh: On idm server, delete user accounts; on mgmt-gw server, archive user folders to expired folders and delete user accounts on bastion host. This is performed 90 days after account has expired (as per current policy).

iiq_deleteUser.sh: On mgmt-gw server, delete archived user folders. This is performed 180 days after account has expired.


The log files for the scripts are written to /var/log/idm/iiq_*. iiq_error.log list the the overall status of scripts execution. Even if this log shows 0 failure, it could be that some subtasks have failed. These subtasks log is given in iiq_output.log. A script run failure on idm server would trigger a second try from NY. If only some subtasks failed, we could correct these ourselves. The previous day failure for script and subtasks are checked in Dalma daily status report.