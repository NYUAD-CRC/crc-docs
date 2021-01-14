Dalma Patch Management
======================

Introduction
Patches are updates that incorporate changes in source code. They can be applied to the Linux kernel or to applications and other systems code running on a Linux server. Patches update security, incorporate new features, and fix coding errors to address such issues as Linux system and application performance and vulnerabilities. Patch management is basically the process of acquiring, testing and installing multiple code changes (patches) to hardware firmwares, systems software and applications. It includes maintaining current knowledge of available patches, determining which patches are appropriate, ensuring that patches are installed properly, testing patches in the target code after installation, and documenting all patches and the configuration(s) in which each patch was deployed. Below is an outline to deploy patches on the HPC cluster

Types of Patches
Patches are consist of the following types:

Firmware. Firmware patches are software for the Read only memory, BIOS/EFI, hardware components of a computing device. These patches affect system options, vulnerabilities, and stability of your computing or network devices. Example of such a firmware would be a driver update to the RAID controller of your hardware.
Operating System. Operating system patches are software to address bugs, known issues, and vulnerabilities on the operating system and the packages installed on the operating system. These include drivers, kernel updates, and packages fixes.
Applications. Application patches are software changes to address bugs, known issues and vulnerabilities on end user applications that sit on top of the operating system.
Severity of Patches
Vendors typical rate the impact of security issues found in their software using typical four-point scale (Low, Moderate, Important, and Critical), as well as Common Vulnerability Scoring System (CVSS) base scores. These provide a prioritized risk assessment to help you understand and schedule upgrades to your systems, enabling informed decisions on the risk each issue places on your unique environment. The severity scale tells you how serious vendors considers an issue to be, helping you judge the severity and determine what the most important updates are. The scale takes into account the potential risk based on a technical analysis of the exact flaw and its type.

 

 	Critical impact	This rating is given to flaws that could be easily exploited by a remote unauthenticated attacker and lead to system compromise (arbitrary code execution) without requiring user interaction. These are the types of vulnerabilities that can be exploited by worms. Flaws that require an authenticated remote user, a local user, or an unlikely configuration are not classed as Critical impact.
 	Important impact	This rating is given to flaws that can easily compromise the confidentiality, integrity, or availability of resources. These are the types of vulnerabilities that allow local users to gain privileges, allow unauthenticated remote users to view resources that should otherwise be protected by authentication, allow authenticated remote users to execute arbitrary code, or allow remote users to cause a denial of service.
 	Moderate impact	This rating is given to flaws that may be more difficult to exploit but could still lead to some compromise of the confidentiality, integrity, or availability of resources, under certain circumstances. These are the types of vulnerabilities that could have had a Critical impact or Important impact but are less easily exploited based on a technical evaluation of the flaw, or affect unlikely configurations.
 	Low impact	This rating is given to all other issues that have a security impact. These are the types of vulnerabilities that are believed to require unlikely circumstances to be able to be exploited, or where a successful exploit would give minimal consequences.
The CVSS scores can aide us in determining the severity of the vulnerability. A CVSS Base Score greater than 7.5 indicates a compromise down to the Operating System of the targeted system where the product executes. The following rules of thumb can be used to keep CVSS Base Score in proper perspective:

 	10	A value of 10.0 indicates an easy, over the network, unauthenticated, and full takeover down to the Operating System where the product executes
 	9.0	A value of 9.0 typically indicates a relatively easy, over the network, and full takeover of the system down to the Operating System, where the product executes, but a low privilege authentication is required
 	7.5	A value of 7.5 with no "Complete" value reported in the impact columns of the risk matrix indicates an easy, over the network unauthenticated takeover of the product.
 	< 7.5	Medium impact
What to Patch
The security patch management model that will be applied to the cluster will be the "hard shell" /"soft center". The HPC team will apply security patches to the management servers, login nodes, and any physical or virtual machines that are facing the NYUAD LAN. The compute nodes will be left unpatched as patching will create havoc on the stability of the cluster. NYUAD will be applying the following patches:

Security patches that are classified as Critical or has a CVSS score of greater than 7.5. 
Firmware patches on storage system that rectify security vulnerabilities, stability issues, and improve performance. Storage devices will be patched according to the following conditions:
Security patches should not require us to install a new kernel on the storage servers and install a new client on the compute nodes to comply with the security update.
Does not impact performance and stability of the storage system
Risk Assessment
HPC staff should identify the associated risks and actions that need to be taken once a security vulnerability has been confirmed, and assess any impact associated with installing a security patch once that patch becomes available. Before applying a patch, system administrators need to ensure that the new patch is not going to affect the overall functionality of the system and its applications. What to patch should answer the following questions:

Will applying or not applying the patch impact critical HPC applications
Will applying or not applying the patch impact the stability or performance of the hardware components in the cluster such as the storage systems, switches, and compute nodes
Are there mitigations currently in place in the cluster that reduce the threat
Will the cluster or users be affected if an attack exploits a vulnerability that hasn't been addressed by a patch
The following table should be filled

 	 	 	 	 	 
Processes to Follow
A) Testing Environment

When a vendor releases a critical security alert or a patch it will be discussed on the weekly meeting to discuss risks outlined above, and whether to go ahead to deploy on the testing environment

Create a case with the vendor to know about vendor tests of security patch and implications and to coordinate with HPC team on how to deploy patch
When applying the patch on the operating system the table below should be filled
 	 	 	 	 	 
When applying firmware updates on hardware components the table below should be filled 
 	 	 	 	 	 
When applying the patch on the use application the table below should be filled
 	 	 	 	 	 
After the patch is deployed, HPC team will run scripts created by the HPC team to measure certain benchmarks and criteria to validate the patch on the cluster. These scripts will determine impact on CPU, infiniband health, I/O workloads on the parallel file systems, Slurm job queues functionalities and workloads, application stability and performace, and overall stability of the cluster. The table below should be filled before and after deploying the patch to see if there are any differences.
 	 	 	 	 	 	 	 	 
Testing results are either pass or fail
The testing will be monitored for two weeks to determine whether to push to production or not
B) Production Environment. Once it is has been determined that patch is suitable for production deployment the following should be followed:

Once patch is validated in testing environment, patching will be implemented on Saturdays where the cluster is taken offline. 
Only one patch is applied. This will allows to know that the patch is causing issues in case of problems.
Testing will be monitored for a 1 month
Notify users about patch deployment and what steps they should fellow to report problems.
Create a Roll back plan in case patch creates havoc with the Cluster
Patching are changes to the system therefore must logged in service link to have a history of records.
The HPC team will execute the scripts again on the production environment to validate the patch or firmware. The table below should be filled before and after deploying the patch to see if there are any differences.

 	 	 	 	 	 	 	 	 
In Google Drive keep the following tables of dates patch applied, type of patch(os,firmware,app), patch name, Version number before patch, version number after patch, and on what nodes.
 	 	 	 	 	 
Saltstack is the tool to be used for Operating System and Application patches. For firmware vendor tools are used
Once patch for operating system has been successful it will be included in the operating system image deployed by Warewulf. Older images will be kept in case we need to roll back to a functioning state
Once firmware update has been successful, older versions of the firmware should be kept in case we need to roll back to a functioning state
C) Production VS. Testing Environments. Production and testing environments should be as close as possible with deviation documents. This will assist us in troubleshooting when patches misbehave. Also the team should determine how far is the deviation should be between the two environments
D) Deviations in patch levels in Production Environment .Because of the"hard shell" /"soft center" security model, compute nodes will have different patch levels than the rest of the nodes. What is an acceptable deviations will be determined by team from the perspective of the stability of cluster to the end users. Deviations should be documented.

Kernel Patching
 Help required.

Description of Benchmark scripts
These scripts are executed pre and post patching. They measure application, network, I/O performance of the cluster. They output parameters, which act as a baseline to the cluster. The scripts will let us know after post patch execution whether these parameters have deviated from the baseline to determine whether that patch has caused this deviation. These scripts are: