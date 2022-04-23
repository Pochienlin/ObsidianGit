# Readiness for change
UID: 202203091253
tag: #🌲 
links: [[Enterprise Solution Management]] [[Business Change]]  [[RACI]]

### Main Questions to consider
1.  What will be deployed
2.  Who is involved
3.  When to make the changes
4.  Success criteria

# What will be deployed
## Requirements
The support team must know what will be changed and the business impacts.

|Technical|Business|Ticketing|
|----|----|----|
|The components and configuration that will change|The requirements expected|Log a change ticket|
## Stages of change
### **Versioning x.y.z**
-   X = major version - main feature
-   Y = minor version - functional change
-   Z = revision - bug-fix, security patch

**Example:**
-   Before a change: Version x.y.z
-   After a minor change: Version x.(y+1).0

E.g. Version 8.1.3 has 2FA added to login -> 8.2.0

**Note:** reset the sub version number when changing the upper number

# Who needs to be involved?
###### We know what is the change about, so next is:
-   Who needs to be involved - before, during and after
-   Communication - to whom and from whom
###### Who needs to be involved in is affected by the implementation, consider:
-   Technical
	-   Developers
	-   Database administrator
	-   Infrastructure
	-   Security
-   Business
	-   Requestor
	-   Process owners
	-   Department owners including legal and compliance
	-   Customer relationship managers for important clients

Recall: [[RACI matrix]]

### Stakeholder management
For the groups of people that need to be informed (e.g. users, customers, etc) create a communication plan considering the following:
-   Who is in each group 
-   What to tell them e.g. RAG, details, spin
-   When to communicate e.g. ad hoc, at certain points during the change, hourly, etc
-   How - to communicate e.g. face to face, meeting, email, website
      
# When to make the change
The changes need be executed to a well-defined schedule:
-   When things will happen - rollout, checks
-   How the steps of the implementation will proceed
-   Approvals - depends on size of change
-   Communication - when to communicate
-   Risks managed
On the day everyone needs to know exactly what they will do and when they will be expected to do it. 
This can be communicated and tracked by an hour-by-hour plan
[Hour-By-Hour Plan Example](https://docs.google.com/spreadsheets/d/1-TTWQOleomiUFdRzUT_JBAHZM0Ht6AT_zIDfK_nkEDQ/edit#gid=839546569)

## Rollback
Before the implementation occurs it is crucial to define:
-   Clear conditions for a rollback to be initiated - e.g. major function or performance issue
-   A clear timeline for initiating a rollback e.g. if issues can’t be fixed by 10am Sunday morning.
-   How a rollback will be performed - maybe partial or full
-   What tests to perform after a rollback
-   Who signs-off for post-rollback testing
## Readiness Checklist
- [ ]   **Testing** completed - Unit testing, UAT, SIT, Rollback (Recall IDP)
- [ ]   **Approvals** - UAT, test manager, department head, process owner, CAB
- [ ]   **Training** completed - users, support
- [ ]  **Implementation team** ready
- [ ]  **Implementation plan** ready, including rollback plan and communication plan
- [ ]  **Implementation packages** ready
- [ ]  **Communications** done.