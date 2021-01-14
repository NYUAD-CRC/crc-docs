Seagate storage disk replacement
================================

Disk replacement procedure on Segatestorage-CS9000

Before replacing the disk please make sure that no pd-repair operation is happening at that time , if so wait until it completes or replace the disk after 3-4 hours of failure.

For Example: 

[root@scratchn07 ~]# cat /proc/mdstat

 [=========>...........]  pd-repair = 49.8% (3775454016/7579094016) finish=244.1min speed=64914K/sec.



If any disk failure detected , please go through below steps to replace with spare disk

Run below commands to see any drive is removed/failed
       cat /proc/mdstat

       [41/40/1] [UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUrUUUU] 

       mdadm -D /dev/md0 or /dev/md1– to get the details of  raid group

2. Make sure the slot number of the failed disk before pulling the disk from the enclosure.

       [root@scratchn00 log]# zgrep -i "failed device" messages.gz

       Nov 16 12:01:19 scratchn06 diskmonitor: Failed Device:                 

       5000c50083ad1e27, encl: 50050cc10c402caf, slot: 27, array: md0

3. Identify the enclosure where the disk failure is occurred – simply note the amber on the enclosure LED.

4. Pull the drive bay slowly and you can see the failed drive on amber ( May the drive bay will be locked, so use L-key to unlock )

5. Below steps is optional if the failed drive does not show the amber,

 Light the drive LED  (node 010 slot 11)

       ssh to node

       cd /sys/class/enclosure/9:0:0:0/11

       check status cat locate

       echo 0 > locate = off

       echo 1 > locate =on

       example

       [root@snx11001n010 ~]# cd /sys/class/enclosure/9:0:0:0/11

       [root@snx11001n010 11]# cat locate 0

6. Once you identify the failed drive unlock and pull it slowly.

      Wait for minimum 2 minutes before inserting new drive.

 7. Insert new drive and lock it properly and wait for 5 minutes to detect new drive disk monitor process. ( Make sure you lock it in first attempt otherwise even if you inserted the disk may not recognize )

8. Run dm_report | grep –i rot  command to check the new drive status

       cat /proc/mdstat

       [41/40/1] [UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUrUUUU]

       [===============>.....]  recovery = 76.3%

      The r flag still will be there until the recovery completion

        mdadm -D /dev/md0 – to get the details of the raid group