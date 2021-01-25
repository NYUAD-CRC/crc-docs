Salt Setup
==========


salt:// Source Location
Salt source locations and priorities are listed in Salt's masters /etc/salt/master.d/local.conf. In general, locations are structured as follow (in no priority ordering):

Git-based locations for text files (the master branch is the production branch):
    salt-state
    salt-state-secret (these are the stuff which shouldn't go to github, like ssh keys, etc.)
    salt-pillar
    salt-pillar-secret (mostly user passwords and uid/gid)
Filesystem-based locations for binaries, etc.:
    /srv/salt/production/state (production files)
    /srv/salt/development (development files which need access to production files)

Notes:

    /srv/salt/development is used to test features which require the use of production's state SLS files. Note that even if this is called development folder, anything used here might affect production nodes if a node Salt's id matches. Therefore, any independent testing should be done in your own separate Salt master/client installation.
    git cli on Salt's master is aliased. git command (for user purposes) should not be run on Salt's masters because it can mess up the permission of files (and therefore the sync from clients) on the git repositories. Use git from your own laptop/desktop.

Pillar file/folder structure
----------------------------

Actual pillar inheritance structure is given in the top.sls file. In general, pillar state SLS are named based on domain/node-group/node names; individual node files are placed inside nodes folder. So we have something like this:

nyuad
    dalma
        dalma-mgmt
            nodes/mgmt1
            nodes/mgmt2
        dalma-mx
        nodes/mx1
        nodes/mx2
    nodes/mgmt3
    nodes/syslog
    ...
    hadoop
        nodes/aduae183-lap
        ...
salt-pillar-secret are mostly user/password files, so they only have flat directory structure. Any child pillar with the same name can replace the parent pillar with the same name. Pillar is also additive.

State file/folder structure
State folder SLS files are structured as follow:

Service SLS files
Config SLS files
Config folders which contain configs for more complex setup:
    slurm
    beegfs
build folder
    package SLS files
files folder (non-SLS files)
    folders corresponding to service SLS files
    folders corresponding to config SLS files
    folders corresponding to cluster folders
scripts folder
Cluster folders, such as:
hadoop
dalma
    node SLS files
    units folder (common service/config SLS files which can be called by node files)

High availability
-----------------
Salt masters are running in active-active mode with salt1 the primary. Salt files in the filesystem /srv/salt are synced using lsync. Salt files in the git repositories are not synced, you need to manually have push to both servers salt1 and salt2 during git push.