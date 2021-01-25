Dalma HA Setup
==============

HA servers
----------

High-availability setup for Dalma mgmt1 and mgmt2 is done through several methods:

. KVM-based shared storage method where one needs to manually start VM on the either mgmt1 or mgmt2
    . idm
    . monitor-db
    . repo
    . syslog
    . warewulf
. Automatic active-active setup (fault-tolerant):
    . mgmt1/mgmt2
    . slurm1/slurm2
    . mx1/mx2
. Manual active-active setup (fault-tolerant):
    . monitor1/monitor2
    . salt1/salt2

Services
--------

Because of the need to perform syncing of any static config changes while the server was possibly down, one needs to manually start the services below (start the primary server first).

. salt1/salt2:
    . salt-master
. slurm1/slurm2:
    . slurmdbd
    . slurmctld
. monitor1/monitor2:
    . nagios
    . nsca
These services need to be started the first time the cluster is booted up (when no secondary servers are running) and during Recovery Step 3 below.

. home2/ssc1:
    . lsyncd
. slurm1:
    . ifup eth0:0
. apps2:
    . ifup ib0:0
    . ifup eth0:0
. mgmt1:
    . ifup br0:0
    . lsyncd
. salt1:
    . ifup eth0:0
    . lsyncd
. monitor1:
    . ifup eth0:0
    . lsyncd
    . nagios-notifications start
    . nagios-event_handlers start
. archive3:
    . ifup eth0:0

Recovery
--------

**Step 1. Fault-tolerant servers**
For any of the fault-tolerant servers above, after booting up, make sure to run Salt's highstate for the server to sync any static config changes which might occur when the server was down. Then reboot and manually start services as described above.

**Step 2. Manual dynamic files/folders sync**
First servers (mgmt1, salt1, etc.) are always the primary servers, except for home1 (home2 is the primary server). Automatic syncing of dynamic files/folders is done by lsync from primary servers to secondary servers; if the secondary servers go down, one does not need to do any manual syncing during recovery. If primary servers go down, the following files/folders need to synced (rsync --dry-run -a --delete; rsync -a --delete) from secondary servers to primary servers before flipping the floating IPs.

mgmt1/mgmt2:

. /etc/idm
. /var/log/idm
. /etc/hosts--warewulf
. /etc/libvirt/qemu/shared-*

salt1/salt2:

. /srv/salt
. /etc/salt/pki/master
. Git repositories (sync through git push from a client, not through rsync)

monitor1/monitor2:

. /etc/nagiosql

**Step 3. Floating IPs switch**

Several floating IPs are required for the functioning of active-active setup of services:

. mgmt-gw
. salt-gw
. monitor-gw
. slurm-gw
. apps-gw, apps-gw.fast
. archive-gw
There are automatic flipping of IPs through /etc/cron.d/gateway-ip-public on monitor1/monitor2, and /etc/cron.d/gateway-ip on secondary servers (mgmt2, monitor2, slurm2, salt2, apps1,archive4). To switch from secondary servers to primary servers, one needs to perform prior syncing above.