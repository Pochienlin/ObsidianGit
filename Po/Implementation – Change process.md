# Implementation Change process
UID: 202203091326
Tags: #🌲 
Links [[Business Change]] [[Enterprise Solution Management]] [[ITIL]]

----
-   Implementation execution – how to do
-   Post-check – smoke test, user sign off
-   Rollback – what is it, how to do it, testing before and after
-   Clean up – ensure all test data is removed, remove install scripts
## Pre-Change
- [ ] Who to loop in:
	- Technical
		- Developers
		- Database administrator
		- Infrastructure
		- Security
	- Business
		- Requestor
		- Process owners
		- Department owners including legal and compliance
		- Customer relationship managers for important clients
- [ ] When to make the change
	- [ ] Hour-by-hour plan
	- [ ] Rollback plan
- [ ] Testing completed - Unit testing, UAT, SIT, Rollback (Recall IDP)
	Vendor Manager – contact vendor to ensure testing complete
	Approvals - UAT, test manager, department head, process owner, CAB
- [ ] Implementation packages ready
- [ ] Hour-by-hour plan ready
- [ ] Roll-back plan ready
## **During the actual implementation check:**
- [ ]  **Backups completed successfully** - code, configuration and data
- [ ] **Changes implemented** the components - working through the implementation steps in the hour-byhour plan.
- [ ] **Test** the implementation. If not okay then rollback and test the rollback.
- [ ] Get **sign off** that implementation succeeded from:
	- [ ]  The requester of the change - all is as expected
	- [ ]  The support manager - ready to support from now
## Post-Change
- [ ] Check if any unnecessary files leftover
- [ ] Check if any testing data leftover
