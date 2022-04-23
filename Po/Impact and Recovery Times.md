# **Impact and Recovery Times**
UID: 202203091434
Tags: #🌲 
Links: [[ITIL]] [[ITIL Problem Management]] [[Enterprise Solution Management]]

> A business must define the recovery time objectives (RTO) and recovery point objective (RPO).

## RTO: How far back?
> RTO - maximum agreed acceptable period of time following a service disruption that can elapse before business functions are severely impacted.
> 

## RPO: How long to recover?
> RPO - the point to which information used by a business activity must be restored to enable the activity to operate on resumption of the service.

![Untitled](Enterprise%205bd06/Untitled%203.png)
- Example
    - A company specifies - RTO = 2 hours and RPO = 24 hours
    - Data is backed up every day at midnight
    - The database is corrupted at 4pm
    - The database is back online at 5:35pm
    - The database is restored from the last backup
    - Is the RTO met and the RPO met?
        - Yes, both are
---
## Problems and risk
- It is good practice to assess high risk areas for any underlying problems.
- From the previous example: “*Customer can’t log a claim*” has low likelihood but extreme business impact.
- All possible failure modes can be examined for any underlying problems e.g. the network router is old and has no redundancy.
