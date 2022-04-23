# Introduction to  Change
UID: 202203091301
Tags: #🌲 
Links: [[Business Change]] [[ITIL]] [[Enterprise Solution Management]]

### Defining change
The addition, modification, or removal of anything that could have a direct or indirect effect on services

## Case study
[[Example - EastCity]] is a 20 year old regional financial investment company based in Singapore. It has 15 offices around Asia-Pacific serving 1,000’s of companies. It has fund investment products and performs trading for its customers.

There is a staff of 300 people and a team of 44 people in IT. The IT team comprises of 15 developers, 4 in cybersecurity, 5 infrastructure support, 1 database administrator, 5 in application support, 2 project managers and 5 business analysts, 1 CTO and 2 administrators.

There are 30 applications used in total with some used regionally and others only in local offices.

### The problem
**Eastcity** needed to upgrade its trading system for a new Chinese currency, **CNH**. 

There were 5 applications to change. All the changes had been tested and signed off by users. The changes involved:
-   5 compiled executables
-   15 scripts
-   20 new scheduled jobs
-   1 firewall change
-   30 database changes

|**When**|**Who**|**What**|
|---|---|---|
|Friday, 19:00|DBA|Copy of the Database|
|Saturday, 09:00|Server Team|Backup of the code|
|Saturday, 10:00|Change Team|Perform changes|
|Saturday, 14:00|Support Team|Test changes|
|Saturday, 16:00|Users|Test changes|

#### Potential issues
- There is an issue and no one knows what's the version that caused it
- Important stakeholders weren't informed
- Test data remains in implemented code
- Unclear who initiated and authorised the changees