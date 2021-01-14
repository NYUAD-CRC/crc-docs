Dalma User Limits
=================

MGMT1,MGMT2
    Login only for group wheel
    No ssh root login
    Can login as root to any machine on the cluster
    No X, agent forwarding
MGMT3
    Login only for groups wheel, apps (no apps user)
    No ssh root login
    Can login as root to login, compute, devel nodes
    No X, agent, TCP forwarding
    No ssh tunneling to other cluster nodes for non-wheel group
    Max 512 processes per normal user
    Max 1024 open files per normal user
MX1,MX2,MONITOR1,MONITOR2,MONITOR-DB,MOD,SALT1,SALT2,WAREWULF,REPO
    Login only for group wheel
    No ssh root login
    Web interface (if supported) only on https port
SYSLOG,SLURM1,SLURM2,IDM,LICENSE
    Login only for groups wheel, apps
    No ssh root login
LOGIN NODES
    No agent, TCP forwarding
    No ssh tunneling to other cluster nodes
    No direct sshfs to /scratch, /fastscratch, /archive; for data transfer to these directories, use sftp to /home and cd to there (not implemented yet)
    Per normal user limits of:
        256 processes
        1024 open files
        2 CPUs (if available)
        6GB RAM
        Throttled I/O to local disk to 50MB/s, 50 IOPS
        Throttled network I/O to admin network (eth0) to 10mbps
        1 hour run time of processes with >90% CPU usage
DEVELOPMENT NODES
    Full outgoing network access
    Per normal user limits of:
        4096 processes
        4096 open files
COMPUTE NODES
    User can login if his/her own job(s) are running on the node
    Groups wheel, apps (no apps user) can login anytime for troubleshooting
    Any processes with open files for "write/update" to /home will be automatically killed (not implemented yet)
MISC
    All internal nodes can not connect to outside world unless specifically allowed. This is because all ethernet traffic passes through MGMT1/MGMT2 on 1Gbps admin network. Allowed services:
        Matlab license ports on NYUAD library servers
    Full /etc/passwd (with NetID users) are only available on IDM, MGMT3, LOGIN, COMPUTE, DEVEL NODES