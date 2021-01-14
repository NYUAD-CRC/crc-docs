DalmaNG System Tasks
====================

Kubernetes
----------

8 mgmt servers (replacement for mgmt[1-3], home[1-2], apps[1-2]):
    2 x 24 port 10G low latency switch
    3 1U master - Ubuntu 20.04 servers:
        min 2 x 2.0GHz 8-core Intel Xeon Cascade/Cooper Lake CPU
        128GB RAM
        1Gb En for 2-port NYUAD external*
        2x2 10Gb En for 2-port storage + 2-port (K8S+admin)
        Battery-backed storage controller
        min 800GB RAID1 mixed use SATA SSD
    3 1U worker - Ubuntu 20.04 servers:
        min 2 x 2.4GHz 16-core Intel Xeon Cascade/Cooper Lake CPU
        256GB RAM
        1Gb En for 2-port NYUAD external*
        2x2 10Gb En for 2-port storage + 2-port (K8S+admin)
        1 EDR IB for NFS
        Battery-backed storage controller
        min 800GB RAID1 mixed use SATA SSD
        min 6TB (system 1TB, home 3TB, apps ??) mixed use NVME (min DWPD 3)
    2 worker - Ubuntu 18.04.5 servers:
        1Gb En for NYUAD external
        2x 1Gb En for K8S
        2x 10Gb En for admin
        1 EDR IB for lustre
        RAID1 mixed use SATA SSD
Docker private registry HA (done)
    Registry backup
    need proper CA (done)
    imagePullPolicy: Always
    HPC Centos 8.2 base image (done)
    HPC Ubuntu 18.04 base image (done)
    HPC Ubuntu 20.04 base image (done)
Rancher

    v2.5
    on Ubuntu 20.04 (done)
    Feature overview (done)

    Cluster template (done)

    RCS HCI frontend (done)
    RCS HCI HPC Lab (mini production) + project (development) space (pending Nasser/Fayizal)
    Upgrade/downgrade procedure (done; check single-node upgrade/downgrade for v2.4.x)
    Vendor support for Multus CNI (done; deprecated; pending switch 802.1q multi VLAN test)
    IB SRIOV with static IP (done; deprecated; pending switch 802.1q multi VLAN test)
    etcd recovery (done; delete node, re-register)
    certificate rotation (done)
    Pod security policy (done; assigned at the Project defn)
    Project network isolation (done)
    Cluster monitoring (done)
    Local block PV for ZFS (done)
Longhorn

    v1.1.0 (expected early Nov; node failure handling cleanup; rebuild from existing replica; data locality)
    I/O performance (done)
    Storage tags (done)
    Disaster Recovery procedure (done)
    PV snapshots and backups (done; nfs blocksize 2MB)
    NFS user quota (done)
    Pod's terminationGracePeriodSeconds: 30
Canal CNI
    Pods security policy
    Project network isolation (for IDM especially) (done)
Monitoring (prometheus/grafana)
    Cluster monitoring
        Node selector (done; label node first)
    Project monitoring
Pod resource policy and quota
    Ephemeral storage for each pod
    Project quotas
    Memory request/limit
    Default request/limit for namespace/project
Lustre
    v. lustre-2.12.0.5_cray_327_g809416f
    CentOS 8.2 client (done)
    Ubuntu 18.04.5 (done)
Beegfs
    v7.2
    Require metadata-storage downtime to upgrade datastructure
    CentOS 8.2 client (done)
    Ubuntu 18.04.5 (done)
UFM
    v6.1.0
    SRIOV (done)
Containers
    Lustre hostPath mount in pod and volumeMount in container
    Use limitrange, quota, PSP, securityContext
    Pods:
    Master (ubuntu20 base)
        MX
        monitor (Ganglia/nagios) + monitor-db
        Syslog
        Salt
        Docker registry backup
    Worker1 (ubuntu20 base)
        syslog-elk
        Repo + repo-centos
        Slurm (centos8)
        Warewulf + warewulf-ubuntu
        IDM (centos8; ssh)
        Docker registry (backup in master)
    Worker2 (ubuntu20 base)
        home (longhorn nfs)
    Worker3 (ubuntu20 base)
        apps (longhorn nfs)
    Worker4/5 (ubuntu18 base)
        mgmt3 (centos8; autofs /home; ssh; syslog-apps)
        mgmt-backend
        home-backup
Warewulf
    v3.9-devel
    PXE through IB (working on Mellanox ConnectX5, not working for current HP ConnectX4)
        FlexBoot firmware update for ConnectX4 (at least FlexBoot 3.5.403_4115)
    UEFI PXE booting (done)
    Current CentOS 7.2 images support (done; need to copy current initrd.gz files)
    CentOS 8.2 support
Repo
    CentOS 8.2 repository (done)
    Ubuntu 20.04 repository (done)
    Ubuntu 18.04 repository (done)
    CentOS 8.2 kickstart (done; replace quiet boot line in linuxefi with: inst.ks="http://repo.hpc.abudhabi.nyu.edu/get-kickstart.php?profile=centos8-static&hostname=<FQDN_HOSTNAME>&ip=<IP>" ip=<IP>::<GATEWAY>:<NETMASK>::<KSDEVICE|ens1f0>:none:<DNS0>:0.0.0.0 console=tty0 console=ttyS1,115200 selinux=0)

    Ubuntu 20.04 Live Installer image (done)
    Ubuntu 20.04 autoinstall (done; add after quiet boot line in linux with: autoinstall fsck.mode=skip hostname=<HOSTNAME> "ds=nocloud-net;s=http://repo.hpc.abudhabi.nyu.edu/public/kickstarts/ubuntu2004/" ip=<IP>::<GATEWAY>:<NETMASK>::<KSDEVICE|ens1f0>:none:<DNS0>:0.0.0.0)
    Ubuntu 18.04 Alternate Installer image (done)
    Ubuntu 18.04 preseed (done; replace file=... quiet with auto=true priority=critical selinux=0 url="http://10.0.0.26/get-kickstart.php?profile=ubuntu1804-static&hostname=<HOSTNAME>&ip=<IP>"; optionally to auto-config network: interface=<KSDEVICE> netcfg/disable_autoconfig=true netcfg/get_ipaddress=<IP> netcfg/get_netmask=<NETMASK> netcfg/get_gateway=<GATEWAY> netcfg/get_nameservers=<DNS> netcfg/confirm_static=true)
    Metadata versioning fix for hpc repo (done)
Salt
    v3001.1
    CentOS 8.2 client
    Ubuntu 20.04 client
    Password management (done)
    Merge secret repos (done)
    Salt-SSH (done)
    SaltGUI (done)
    Node type inherit from warewulf (done; patched warewulf to add wwgroups to kernel args)
    GPG (done)
Git
    gitattributes for encryption (deprecated; use GPG)
    pre-commit hook to check attribute content
    post-receive hook (git diff-tree --no-commit-id --name-only -r <SHA>)
Slurm
    v20.02.3
    CentOS 8.2 client (done)
    PMIx support (done)
    slurmtop (done)
    Remove legacy PBS support
    Remove legacy BLCR support
    Remove mpiexec support
    Remove showq support (PBS command)
    Remove OSU shmem pmi2 patch(question) (not available for slurm v20; Jorge requested this for current Slurm version)
License
    Check if still needed otherwise apps team to create containers
        Intel (to be removed)
        DDT (to be removed)
        IDL/Harris (to be removed)
        Lumerical (to be removed)
Elasticsearch-Logstash-Grafana
    ELK v7.6.2 (done)
    Grafana v4.6.5 (done)
Ballast
    v2.2
    Daemon on Ubuntu 20.04 (done)
    Client on CentOS 8.2 (done)

K8S nodes
---------

GC cleanup (as per Rancher)
    /var/lib/kubelet (emptyDir)
    /var/log → /var/lib/docker/containers (https://success.docker.com/article/how-to-setup-log-rotation-post-installation)
    /var/lib/docker
        image

        **kubelet args**
        services:
        kubelet:
            extra_args:
            image-gc-high-threshold: 60

        volumes (manual cleanup)
        overlay2 (sparse file: du -shc /var/lib/docker/overlay2/*/diff)
Add master/worker-mgmt node labels
Enforce Allocatable on pods only (not kube-reserved nor system-reserved)
HA NFS-server routes  (deprecated; pending switch 802.1q multi VLAN test)
    Ubuntu: netplan should have critical keyword on ib0 (systemd <=242 DHCP: CriticalConnection, >=243 Network: KeepConfiguration)
    RHEL: Disable NetworkManager

Compute node
------------

UEFI storage (done)
UEFI booting (done)
BIOS: Enable C-states, disable C2 through OS (cpupower idle-set -d 2)
Disable TurboBoost
    intel_pstate: echo 1 > /sys/devices/system/cpu/intel_pstate/no_turbo
    acpi-cpufreq: echo 0 > /sys/devices/system/cpu/cpufreq/boost
Disable HT (cat /sys/devices/system/cpu/cpu*/topology/thread_siblings_list | awk -F, '{print $2}' | sort -n | uniq | ( while read X ; do echo $X ; echo 0 > /sys/devices/system/cpu/cpu$X/online ; done ))
Governor: intel_pstate=passive (Intel), acpi-cpufreq (AMD): schedutil/ondemand
traffic-control for /home write (throttled to 15kbps) (done)
HA default route
    keepalived v2.1.0
    login nodes (done)
    nsca check_procs (done)
Rebuild Ganglia (done)

Viz node
--------

NVidia
    v440.82 (done)
VirtualGL (done)
TurboVNC (done)
LDAP (done)