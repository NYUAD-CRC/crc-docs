BeeGFS Recovery
===============

Reference URL is www.beegfs.io/wiki/FSCheck. Example is for /fastscratch.

. Kill all jobs running on /fastscratch. Unmount /fastcratch from all nodes.
. Replace server or parts.
. Optional: Recreate / fileysystem.
. Remount mgmtd and/or metadata and/or storage targets on new server and start BeeGFS daemons.

**On client node (no need to mount BeeGFS filesystem)**

. Login as root to a client node (e.g. compute-22-10). Use /tmpdata as working directory:
    . ``mkdir /tmpdata/fsck``
. Clean pending-deleted files (www.beegfs.io/wiki/FAQ#disposals):
    . ``beegfs-ctl  --disposeunused --printstats --dispose --cfgFile=/etc/beegfs/fastscratch.d/beegfs-client.conf``
. Read-only BeeGFS fsck:
    . ``beegfs-fsck --checkfs --readOnly --databasePath=/tmpdata/fsck --cfgFile=/etc/beegfs/fastscratch.d/beegfs-client.conf``
. BeeGFS fsck:
    . ``beegfs-fsck --checkfs --noFetch --databasePath=/tmpdata/fsck --cfgFile=/etc/beegfs/fastscratch.d/beegfs-client.conf``

**OPTIONAL: On server nodes**

. If beegfs-fsck can not repair the filesystem, then the disk partition needs to be repaired:
    . xfs_repair /dev/mapper/VD*-storage or fsck.ext4 /dev/mapper/VD*-meta
