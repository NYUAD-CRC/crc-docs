Performance Considerations
==========================


Job Throughput
--------------

1. It is crucial to specify a more or less accurate runtime for your job.
    Requesting too little will result in job abortion, while requesting too much will have a 
    negative impact on job start time and job throughput: Firstly, jobs with a shorter runtime have a greater chance to benefit from being backfilled between long running jobs and may therefore start earlier if resources are scarce. Secondly, a short running job may still start when a scheduled downtime is getting closer while long running jobs won’t start because they are not guaranteed to finish before the start of the downtime.
2. It is crucial to request the correct amount of cores for your job.
    Requesting cores that your job cannot utilize is a waste of resources that 
    could otherwise be allocated to other jobs. Hence, jobs that theoretically 
    could run have to wait for the resources to become available. For potential consequences of requesting too less cores on job performance, see below.
3. It is crucial to request the correct amount of memory for your job.
    Requesting too little memory will result in job abortion. 
    Requesting too much memory is a waste of resources that could otherwise be allocated to other jobs.

Job Performance/Runtime
-----------------------

- It is crucial to request the correct amount of cores for your job.
    For parallel jobs (shared memory, MPI, hybrid) requesting less cores than processes/threads are spawned by the job will lead to potentially overbooked compute nodes. This is because your job will nevertheless spawn the required number of processes/threads (use a certain number of cores) while to the scheduler it appears that some of the utilized resources are still available, and thus the scheduler will allocate those resources to other jobs. Although under certain circumstances it might make sense to share cores among multiple processes/threads, the above reasoning should be considered as a general guideline, especially for unexperienced user.