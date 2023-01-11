# Events and incidents
UID: 202204241705
Tags: #🌲 
Links: [[Enterprise Solution Management]]

----

# Why manage incidents?
##### Maintaining Service Levels
-   Keep your service up and running using applications and infrastructure monitoring
-   Define how you will attempt to predict incidents.
-   Use performance management solutions to ensure availability.
##### **Improving User Satisfaction**
-   Ensuring incidents are avoided and speed up restoration if not avoided. 
-   Capacity planning software. 
##### **Increasing Staff Efficiency and Productivity**
-   Using monitoring tools.

# ITL Service Support
[[ITIL]] Service Management Practices ensure that services deliver agreed levels of availability to meet the needs of customers and users.
1. **_Event -_** any change of state that has significance for the management of a service. Typically, they are notifications from monitoring tools.
2. **_Incident_** - an unplanned interruption to a service or reduction in the quality of service.
3. **_Problem_** - a cause, or potential cause, of one or more incidents

# Steps
#### 1. Identify
Firstly, incidents need to be identified. They come from two main sources:
-   **Users** - walk-ups, self-service, phone calls, emails, support chats,
-   **Alerts** - application monitoring software or system scanning utilities.
> [!tip]
> **Decide if the issue is really an** **incident** **or if it’s a** **request**. Requests are not incidents and should go through the change management process.**
![[Pasted image 20220424172610.png]]
#### 2.  Log
Once an event is identified as an incident it is logged in a ticketing system as per enterprise standard procedures
- Categorise
- Prioritise

**The incident log should at least include the information:**
-   User’s name and contact information
-   Incident description - e.g. steps taken before the incident, has it previously appeared
-   Date and time of the incident
-   Date and time of the incident report

#### 3. Categorise
Categorization involves:
-   Assigning a category e.g. application 
-   Assigning at least one subcategory e.g. slow

This serves several purposes:
-   Allows sorting and model incidents
-   Allows some issues to be automatically prioritized. 
-   Provide accurate incident tracking and see patterns emerge. 

For example, an incident might be:
-   Category = “Application” 
-   Sub-category of “Slow”.
> [!note] **Categories examples:**
> 
> **Network**
> -   Outage
> -   Slow
> 
> **Application**
> -   Fault
> -   Slow
> -   Access control
> 
> **Data**
> -   Missing
> -   Incorrect

#### 4. Prioritise
**An incident priority is determined by:**
-   **Impact** on users and the business - the measure of the extent of potential damage the incident may cause.
-   **Urgency** is how quickly a resolution is required to reduce the business impact
see also: [[Risk management]]
> [!warning]
> -   Prioritization is especially important for triaging incidents during major outages.
> -   Prioritization may change during the lifetime of the incident.
| Low Priority                                                      | Medium Priority                                        | High Priority                                                                      |
| ----------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Does not interrupt users or the business and can be worked around | Affects a few staff and interrupts work to some degree | Affects many users or customers, interrupts business, and affects service delivery |
| Services to user and customers can be maintained                  | Customers may be slightly affected or inconvenienced   | These incidents almost always have a financial impact                                                                                   |
![[Pasted image 20220424173520.png]]


## Incident Resolution activities
**Resolution of an incident involves the following activities:**
1.  **Initial diagnosis:** User describes the problem and answers troubleshooting questions.
2.  **Incident escalation:** Send to specialist support staff and inform relevant stakeholders. 
3.  **Monitor** the situation and **communicate** regularly
4.  **Investigation and diagnosis:** The incident hypothesis is confirmed. 
5.  **Resolution**: Staff apply a solution, such as changing software settings or applying a software patch.
6.  **Recovery**: Confirmation that the service has been restored.
7.  **Incident closure:** User confirms the service is restored and the incident is considered closed. Problem ticket raised if necessary.
## Incident status tracking
Incident statuses mirror the incident process and include:
1.  **New** - incident received but not yet assigned
2.  **Assigned** - incident has been assigned
3.  **In progress** - assigned but not yet resolved
4.  **On hold** - incident requires some extra information or response from the user or from a third party
5.  **Resolved** - incident is resolved and the user’s service has been restored 
6.  **Closed** - user confirms service is restored and no further actions to be taken.
![[Pasted image 20220424173729.png]]

![[Pasted image 20220424173747.png]]

# Post-incident review
**Review the following:**
-   Check the users’ perception
-   Check the business process and infrastructure metrics e.g. servers and transaction rates
-   Decide if an underlying problem exists and raise a ticket if necessary.

# Summary diagram
![[Pasted image 20220424173853.png]]

# Incident Communication
**Communication is very important when incidents occur.** 
This includes:
-   Finding out what actually happened 
-   Escalating to specialists and management
-   Updating on progress
-   Reporting the incident impact and resolution
-   Confirming the resolution with the users
## Satisfaction surveys
> [!abstract]
> Satisfaction surveys are a good method of monitoring user perception and expectations. To ensure success you should address several key points:
> -   Decide on the **scope** of the survey and the target audience
> -   Clearly **define** the questions and make the survey easy to complete
> -   **Conduct** the survey regularly
> -   Make sure that your users **understand** the benefits
> -   **Publish** the results
> -   **Translate** survey results into actions
> -   **Follow through** on survey results

[[Example of a user satisfaction survey]]

## Incident report
Include the following:
##### **Basic summary:**
-   Incident ticket number
-   Description incident including any event notification
-   Impact to business agreed service levels
-   Resolution time
##### **Causes found** 
-   The technical analysis of the incident
##### **Actions taken including:**
-   Short-term workarounds
-   Improvements to avoid similar occurrences
##### **Post-incident follow up:**
-   Measurements taken after the fix
-   Elimination of the root cause or problem tickets raised
-   User surveys performed
#### Other details to include
Regular incident report summaries can be produced to ensure incident management is effective. Details include:
-   The number of incidents logged week on week
-   The average length of time taken to resolve incidents 
-   The types of incident reported
-   The percentage of incidents handled within the agreed response time
-   The percentage of incidents closed by the service desk without escalation (i.e. by tier 1)
-   Summarise in non-technical language and show where improvements could be made.

# Security concerns
When an incident occurs security may be affected in the following ways:
-   The incident may occur due to a security event such as:
	-   Unauthorised access
	-   Virus
	-   Cyber attack
-   Elevated system access may need to be granted to resolve an incident.
-   Data may be lost or leaked.

**The security team must be informed of all security related incidents**

[[IT Support Role]]

----
- [[ITIL Incident Management]]
- [[ESM Event Management]]
- [[ITIL Problem Management]]