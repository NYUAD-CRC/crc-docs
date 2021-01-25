SLURM Setup
===========

Build
-----

Slurm build documentation is inside Salt's build/slurm.sls file.

Install
-------

In slurm management VMs and login nodes, Slurm is installed from built tar files through Salt's dalma/slurm.sls and dalma/node-login.sls. This way we can keep old versions of Slurm concurrently on the server in case of a need to switch back to a previous version.

On other nodes (compute, gpu, etc.) they are installed from built RPM packages through Salt's dalma/node-*.sls.

On each node, Slurm is installed in /opt/slurm/<version>. /opt/slurm/default symlink refers to currently running version. On slurm management VMs and login nodes, you need to manually change the symlink to refer to another version of Slurm in case of a version change; on slurm management VMs, make sure to stop slurmctld and slurmdbd before the symlink change, and restart after this change.

Config files
------------

Slurm's config files are placed in /opt/slurm/default/etc/slurm. Any permanent changes to config files should be stored in the git repository and Salt's highstate run on Slurm's masters and vnfs. At this point, all warewulf-created nodes are still using the old config files; you need to sync the files manually. If it's only one file, e.g. slurm.conf, then use clush from mgmt3 to sync. Only after the config files are the same on all nodes, restart systemctld (or slurmdbd if slurmdbd.conf changes) on the masters, and run on one of the masters 'scontrol reconfig'.

Scripts
-------

All slurm scripts are placed in /opt/slurm/scripts in each node. Refer to individual scripts for documentation.

High availability
-----------------

Mariadb is run in an active-active mode. Mariadb does an automatic asynchronous replication so there is no need to do manual syncing. Slurm's internal state are shared by both VMs in /opt/slurm/state; do not touch this directory. 