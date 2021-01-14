Warewulf Setup
==============

Build
Warewulf build documentation is inside warewulf build SLS file.

Create Warewulf master
Define warewulf VM in dalma-vm.sls pillar file, then on salt1 master, run each of the following steps, making sure each step finishes successfully:

.. code-block:: bash

    salt hpc-mgmt1 cmd.script salt://scripts/vm-create.sh template=jinja pillar='{"guesthost": "warewulf"}'
    salt-key -a warewulf
    salt warewulf state.highstate

After rebooting warewulf VM:

::

    salt warewulf cmd.script salt://scripts/warewulf/master-config.sh template=jinja

Set default settings
On warewulf master:

.. code-block:: bash

    wwsh -y object modify DEFAULT -s KARGS="crashkernel=256M\ intel_pstate=disable\ transparent_hugepage=never"
    wwsh pxe update
    wwsh dhcp update
    wwsh dhcp restart

Notes:

. Don't use "wwsh object" (dangerous!) to set properties unless "wwsh provision, node, file, etc." don't work properly
. Don't set "--cluster" name (it complicates host naming)
. "wwsh pxe, dhcp update/restart" is only needed when setting KARGS


Create VNFS images
------------------

Define a vnfs (e.g. compute-centos7-v1) in dalma-vnfs.sls pillar file then create and configure:

::

    salt warewulf cmd.script salt://scripts/warewulf/vnfs-create.sh template=jinja pillar='{"vnfshost": "compute-centos7-v1"}'
    salt compute-centos7-v1 state.highstate
    wwvnfs compute-centos7-v1

Notes:

. Make sure to run "wwvnfs compute-centos7-v1" everytime its contents are changed (in this case through salt compute-centos7-v1 state.highstate)
. Because of a bug in systemd, you need to reboot warewulf VM everytime after a vnfs is created through vnfs-create.sh

Set compute/gpu node settings
-----------------------------

Define DEFAULT node type to be compute node:

::

    wwbootstrap --chroot=/var/chroots/compute-centos7-v1 3.10.0-327.10.1.el7.x86_64
    wwsh -y provision set DEFAULT --vnfs=compute-centos7-v1 --bootstrap=3.10.0-327.10.1.el7.x86_64

Pre-define IP addresses and properties for compute nodes:

::

    wwsh -y node new compute-*-* --domain=local --groups=compute --netdev=eth0 --ipaddr=<eth0_IP> --netmask=255.255.0.0 --gateway=10.0.0.4
    wwsh -y node set compute-*-* --netdev=ib0 --ipaddr=<ib0_IP> --netmask=255.255.0.0
    wwsh -y provision set compute-*-* --files=dynamic_hosts,ifcfg-ib0

Pre-define IP addresses and properties for gpu nodes:

::

    wwsh -y node new compute-21-* --domain=local --groups=gpu --netdev=eth0 --ipaddr=<eth0_IP> --netmask=255.255.0.0 --gateway=10.0.0.4
    wwsh -y node set compute-21-* --netdev=ib0 --ipaddr=<ib0_IP> --netmask=255.255.0.0
    wwsh -y provision set compute-21-* --vnfs=gpu-centos7-v2 --bootstrap=3.10.0-327.10.1.el7.x86_64
    wwsh -y provision set compute-21-* --files=dynamic_hosts,ifcfg-ib0,local-postboot-post.sh--gpu

Notes:

. Replace <eth0_IP> and <ib0_IP> with corresponding IPs
. You can use Bash for loops to define per set (e.g. compute-1-[1-18], ...)
. gpu and devel nodes follow compute node example

Set login node settings
-----------------------

::

    wwsh -y node new login-0-* --domain=local --groups=login --netdev=eth0 --ipaddr=<eth0_IP> --netmask=255.255.0.0
    wwsh -y node set login-0-* --netdev=bond1 --ipaddr=<bond1_IP> --netmask=255.255.255.0 --gateway=10.230.42.1
    wwsh -y node set login-0-* --netdev=ib0 --ipaddr=<ib0_IP> --netmask=255.255.0.0
    wwsh -y provision set login-0-* --vnfs=login-centos7-v2 --bootstrap=3.10.0-327.36.3.el7.x86_64
    wwsh -y provision set login-0-* --files=dynamic_hosts,ifcfg-bond1,ifcfg-ib0

Notes:

. Replace <eth0_IP>, <bond1_IP> and <ib0_IP> with corresponding IPs

Set devel node settings
-----------------------

::

    wwsh -y node new compute-60-* --domain=local --groups=devel --netdev=eth0 --ipaddr=<eth0_IP> --netmask=255.255.0.0
    wwsh -y node set compute-60-* --netdev=ib0 --ipaddr=<ib0_IP> --netmask=255.255.0.0 --gateway=$(host public-gw.fast | head -1 | awk '{print $4}')
    wwsh -y provision set compute-60-* --vnfs=devel-centos7-v1 --bootstrap=3.10.0-327.10.1.el7.x86_64
    ... (also for compute-15-1)
    
    wwsh -y provision set compute-60-1 --files=dynamic_hosts,ifcfg-ib0-gw,local-postboot-post.sh--compute-60-1
    wwsh -y provision set compute-60-2 --files=dynamic_hosts,ifcfg-ib0-gw,local-postboot-post.sh--compute-60-2
    wwsh -y provision set compute-60-[3-4] --files=dynamic_hosts,ifcfg-ib0-gw,local-postboot-post.sh--devel
    wwsh -y provision set compute-15-1 --files=dynamic_hosts,ifcfg-ib0-gw,local-postboot-post.sh--compute-15-1

Set visual node settings
------------------------

::

    wwsh -y node new visual* --domain=local --groups=visual --netdev=eth0 --ipaddr=<eth0_IP> --netmask=255.255.0.0
    wwsh -y node set visual* --netdev=eth1 --ipaddr=<eth1_IP> --netmask=255.255.255.0 --gateway=10.230.42.1
    wwsh -y node set visual* --netdev=ib0 --ipaddr=<ib0_IP> --netmask=255.255.0.0
    wwsh -y provision set visual* --vnfs=visual-centos7-v2 --bootstrap=3.10.0-327.36.3.el7.x86_64
    
    wwsh -y provision set visual[1-4] --files=dynamic_hosts,ifcfg-eth1,ifcfg-ib0,local-postboot-post.sh--gpu

Notes:

. Replace <eth0_IP>, <eth1_IP> and <ib0_IP> with corresponding IPs

Special settings for non-compute node
--------------------------------------

::
    wwsh -y object modify login-centos7-v2 --set NOCACHE=1
    wwsh -y object modify gpu-centos7-v1 --set NOCACHE=1
    wwsh -y object modify gpu-centos7-v2 --set NOCACHE=1
    wwsh -y object modify devel-centos7-v1 --set NOCACHE=1
    wwsh -y object modify devel-centos7-v2 --set NOCACHE=1
    wwsh -y object modify visual-centos7-v2 --set NOCACHE=1
    ...

Notes:

. NOCACHE is used to safe filesystem space

Special settings for gpu and visual nodes
------------------------------------------

::

    wwsh -y object modify compute-21-* -s KARGS="crashkernel=256M\ intel_pstate=disable\ rd.driver.blacklist=nouveau"
    wwsh pxe update
    wwsh dhcp update
    wwsh dhcp restart
    wwsh -y provision set compute-21-* --console=ttyS0,115200

Special settings for new supermicro nodes
-----------------------------------------

::

    wwsh -y object modify compute-27-[7-14] -s KARGS="crashkernel=256M\ intel_pstate=disable\ transparent_hugepage=never\ nomodeset\ xdriver=vesa\ brokenmodules=ast"
    wwsh pxe update
    wwsh dhcp update
    wwsh dhcp restart

Special settings for superfat
-----------------------------

::

    wwsh -y object modify compute-22-[9-12] -s KARGS="crashkernel=256M\ intel_pstate=disable"
    wwsh -y provision set compute-22-10 --files=dynamic_hosts,ifcfg-ib0,local-postboot-post.sh--superfat

Special settings for system devel node
--------------------------------------

::

    wwsh -y provision set sysdev* --files=dynamic_hosts,ifcfg-ib0-gw,local-postboot-pre.sh--sysdev,local-postboot-post.sh--sysdev

Chroot/Vnfs content changes
---------------------------

Everytime changes are made to the content of a chroot/vnfs through Salt's state change, one needs to run wwnfs, e.g.:

::

    wwvnfs compute-centos7-v1

Provision nodes
---------------

Run wwnodescan and boot corresponding nodes in order:

::

    wwnodescan --replace --netdev=eth0 login-0-[1-4]
    wwnodescan --replace --netdev=eth0 compute-1-[1-9]
    wwnodescan --replace --netdev=eth0 compute-1-[10-18]
    wwnodescan --replace --netdev=eth0 compute-2-[1-9]
    ...

Backup
------

Warewulf runtime data is backed up through /etc/cron.weekly/backup to mgmt-gw host's /backup/warewulf/ folder. The filesystem portion is backed up through rsync, the mariadb portion through innobackupex.

Recovery from corrupted VM
---------------------------

Optionally, first re-create warewulf master as above. Then, on warewulf master, stop relevant services:

::

    systemctl stop dhcpd
    systemctl stop tftp
    systemctl stop mariadb
    rm -fr /var/lib/mysql/*

From mgmt-gw host which contains the last <version> copy, run:

::

    cd /var/backup/warewulf
    rsync -a etc var warewulf:/
    rsync -a mariadb/backup-my.cnf warewulf:/root/
    rsync -a mariadb/<version>/ warewulf:/var/lib/mysql/

Finally, on warewulf master:

::

    innobackupex --defaults-file=/root/backup-my.cnf --apply-log --redo-only --use-memory=1G /var/lib/mysql
    innobackupex --defaults-file=/root/backup-my.cnf --apply-log --use-memory=1G /var/lib/mysql
    shutdown -r now