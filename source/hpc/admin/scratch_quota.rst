
Enable Quota on scratch storage
===============================


Quotas limit the amount of disk space a user, group or project can use. Lustre filesystem quotas are set by root and can be specified for individual users, groups, and/or projects.


To enable quotas on ClusterStor systems OEM installed at NEO 2.0 and above, the following commands can be used.

1. To check if quotas are enabled

n00 # pdsh -g lustre 'lctl get_param 'osd-*.*.quota_slave.info' ' |grep "quota enabled"

2. To enable quotas
MGS # lctl conf_param $FSNAME.quota.<ost|mdt>=<u|g|p|ug|up|gp|ugp|none>
Examples:

MGS # lctl conf_param $FSNAME.quota.ost=ug
## Enables OST block quotas for users and groups

MGS # lctl conf_param $FSNAME.quota.mdt=ug
## Enables MDT inode quotas for users and groups

MGS # lctl conf_param $FSNAME.quota.ost=ugp
## Enables OST block quotas for users, groups and projects

3. Verify quotas are enabled

n00 # pdsh -g lustre 'lctl get_param 'osd-*.*.quota_slave.info' ' |grep "quota enabled"

 

 


NOTE: Project quotas are supported in software release CSL 3.1 and above. Project quotas are not enabled by default. Additional steps are required


To enable project quotas (CSL 3.1 and above only)

1. Check if project quotas are enabled. For each OST and MDT RAID device, run the following, replacing mdX with the relevant device name.

MDS/OSS # dumpe2fs -h /dev/mdX |grep project
Examples:

n00 # pdsh 2>/dev/null -g oss=primary 'dumpe2fs -h /dev/md0 | grep project'
n00 # pdsh 2>/dev/null -g oss=secondary 'dumpe2fs -h /dev/md1 | grep project'
n00 # pdsh 2>/dev/null -g mds=primary 'dumpe2fs -h /dev/md0 | grep project'
n00 # pdsh 2>/dev/null -g mds=secondary 'dumpe2fs -h /dev/md1 | grep project'

2. Take the filesystem offline, leaving raid devices assembled
pdsh -g mds=primary,oss=primary "crm_mon -1 | awk '/fsys/ {print \$1}' | xargs -I {} stop_xyraid {}"

3. Verify the filesystem is stopped (all nodes should return "0")

n00 # pdsh -g lustre "mount -t lustre | wc -l"

4. Run the following tune2fs command for all OST and MDT RAID devices. NOTE: NO MD wildcards for multiple devices. Replace mdX with the relevant device name.
MDS/OSS # tune2fs -O project /dev/mdX
Examples:
n00 # pdsh -g oss=primary 'tune2fs -O project /dev/md0'
n00 # pdsh -g oss=secondary 'tune2fs -O project /dev/md1'
n00 # pdsh -g mds=primary 'tune2fs -O project /dev/md0'
n00 # pdsh -g mds=secondary 'tune2fs -O project /dev/md1'

5. Verify project quotas were enabled successfully, replace mdX with the relevant md device.
MDS/OSS # dumpe2fs -h /dev/mdX |grep project
Examples:
n00 # pdsh 2>/dev/null -g oss=primary 'dumpe2fs -h /dev/md0 | grep project'
n00 # pdsh 2>/dev/null -g oss=secondary 'dumpe2fs -h /dev/md1 | grep project'
n00 # pdsh 2>/dev/null -g mds=primary 'dumpe2fs -h /dev/md0 | grep project'
n00 # pdsh 2>/dev/null -g mds=secondary 'dumpe2fs -h /dev/md1 | grep project'
NOTE: If ESUs and/or additional MDTs are in use, the examples above will need to be adjusted for the specific GridRAID numbering that exists on the system, (e.g. md2, md3, md4 etc)

6. Mount the filesystem

n00 # pdsh -g mds=primary,oss=primary "crm_mon -1 | awk '/fsys/ {print \$1}' | xargs -I {} start_xyraid {}"

To enable quotas on ClusterStor systems CUP installed to NEO 2.0, follow this procedure

1. Take the filesystem offline, leaving raid devices assembled

n00 # pdsh -g mds=primaryåoss=primary "crm_mon -1 | awk '/fsys/ {print \$1}' | xargs -I {} stop_xyraid {}"

2. Verify the filesystem is stopped (all nodes should return "0")
n00 # pdsh -g lustre "mount -t lustre | wc -l"

3. Run the following for all OST and MDT targets. Replace mdX with the relevant device name.

MDS/OSS # tunefs.lustre --quota /dev/mdX
Examples:
n00 # pdsh -g mds=primary tunefs.lustre --quota /dev/md66
n00 # pdsh -g oss=primary tunefs.lustre --quota /dev/md0
n00 # pdsh -g oss=secondary tunefs.lustre --quota /dev/md1
NOTE: If ESUs and/or additional MDTs are in use, the examples above will need to be adjusted for the specific GridRAID numbering that exists on the system, (e.g. md2, md3, md4 etc)

4. Mount the filesystem

pdsh -g mds=primary,oss=primary "crm_mon -1 | awk '/fsys/ {print \$1}' | xargs -I {} start_xyraid {}"

 

More information about lustre quotas can be found in the "Configuring and Managing Quotas" section of the lustre manual

https://build.whamcloud.com/job/lustre-manual/lastSuccessfulBuild/artifact/lustre_manual.xhtml#configuringquotas