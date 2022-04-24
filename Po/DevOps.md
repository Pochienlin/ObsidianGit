# DevOps
UID: 202204241910
Tags: #🌱 
Links: [[Enterprise Solution Management]]

----
![[Pasted image 20220424191105.png]]
# DevOps and Maturity
```ad-info
**DevOps is a mature process because:**

-   Maturity is measured by the reproducibility of processes. 
-   As automation increases, reproducibility also increase and hence maturity also increases. 
-   Processes get embedded in code rather than documents.

  
Therefore, DevOps is a mature methodology.
```
# What is devops?
The word 'DevOps' is a combination of two words 'development' and 'operations‘.
- DevOps is a *culture* which promotes collaboration between Development and Operations teams to deploy systems to production in less turnaround time in an automated way.
```ad-abstract
title: In simple words...
DevOps is as an alignment of development and IT operations with better communication and collaboration.
```
| Six essential principles for DevOps adoption                                                                                                        |
| --------------------------------- |
| Customer-Centric Action: DevOps teams focus on customer-centric actions constantly investing in products and services. |
| End-To-End Responsibility: DevOps teams provide support for the whole life of the product enhancing the overall quality of the products engineered. |
| Continuous Improvement: DevOps culture focuses on continuous improvement to minimize waste and speed up improvements to the product or services.    |
| Automate everything: Automation is a core principle of DevOps processes for software development and for infrastructure. |
| Work as one team: In a DevOps culture the designers, developers, and testers work as one team in complete collaboration. |
| Monitor and test everything: It is very important for DevOps teams to have robust monitoring and testing procedures. |

## Before DevOps...
![[Pasted image 20220424191435.png]]
- Before DevOps, the development and operation teams worked in isolation.
- Testing and Deployment were isolated activities done after design-build consuming extra time than during build cycles 
![[Pasted image 20220424191601.png]]
- Manual code deployment leads to human errors in production.
- Developers & operation teams can have separate timelines and are not in synch.
- Large companies like Amazon and Netflix use DevOps for high-speed change with new deployments every 10 minutes or less.
| Key Reasons         | DevOps                                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Predictability      | DevOps offers significantly lower failure rate of new deployments.                                                 |
| Reproducibility     | Versioning everything so that earlier version can be restored anytime.                                             |
| Maintainability     | Effortless recovery in the event of a deployment disabling the current system.                                     |
| Time to market      | DevOps reduces the time to market up to 50%.                                                                       |
| Greater Quality     | DevOps helps the team to improve quality of application development and IT operations.                             |
| Reduced Risk        | DevOps incorporates security in software, reduces defects across the lifecycle and uses containers such as Docker. |
| Resiliency          | The system is more stable, secure, and changes are auditable.                                                      |
| Cost Efficiency     | DevOps offers cost efficiency in software development.                                                             |
| Smaller code pieces | DevOps is based on the agile programming methods breaking larger code bases into smaller and manageable chunks.    |
## Classic Waterfall
![[Pasted image 20220424191802.png]]
Integration = Code-and-Fix, might be iterative but only within the steps, possibly extending to deployment

| Waterfall                                                                                                                                                                                              | DevOps                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -Requirement Definition (Analysis and Specification)<br/>- Software Design<br/>- Implementation (Coding)<br/>- Testing<br/>- Deployment (Installation)<br/>- Maintenance<br/>- Retirement (Withdrawal) | - Cross-functional team and skills <br/>- Continuous delivery<br/>- Optimum utilization of toolsets<br/>- Automated deployment pipeline<br/>- Continuous assessment                                                                                                   |
| - Testing occurs at the end of the project<br/>- Any issues can cause the process to re-start from the requirements down.                                                                              | - Automated testing, continuous integration and delivery<br/>- Direct value stream mapping<br/>- Motivate people<br/>- Continuous improvement of products, services and processes<br/>- A culture that encourages development and operations teams to work together." |

### Error cost
![[Pasted image 20220424192316.png]]

# DevOps Lifecycle
|Lifecycle|DevOps|
|---|----|
|Plan|Change requests are managed and assigned by a development manager.|
|Code|Coding takes place constantly in small development cycles.|
|Build|As the developers check in code it is automatically scanned for quality and security and built into libraries and executable files.|
|Testing|Automated unit testing is performed on new code and QA teams use automated testing tools like Selenium.|
|Integration|New functionality is constantly integrated with the prevailing code and re-tested.|
|Deployment|Deployment takes place continuously. Containers such as Docker are used so that code changes do not affect the functioning of the application.|
|Operate|All versions in all system environments are kept identical.|
|Monitoring|Monitoring automatically includes new changes.|

## Tools
![[Pasted image 20220424192416.png]]
# DevSecOps
Traditionally, security is often only considered at the end of development. 
### DevSecOps:
- Automates core security by embedding security controls and processes early in the software development life cycle
- Minimizes vulnerabilities 
- Everyone in the software development life cycle is responsible for security (like quality)
- Brings operations and development together with security functions. 
- For example, when migrating to microservices, compliance automation or testing cloud infrastructure.

##### The benefits are: 
- More automation reduces misadministration and mistakes.
- Reduces the need to manually configure security consoles.

# SRE: Site reliability engineering
**Site Reliability Engineering by Google (SRE)**
-   Treats operations as if it’s a software problem. 
-   Used to protect, provide for, and progress software and systems.
-   Is behind all of Google’s public services.
-   Keeps an ever-watchful eye on availability, latency, performance, and capacity. 

To know more see [video](https://youtu.be/bwt6TZjefGM)
## Self-healing: AI Ops
Uses AI to detect and repair systems.

Before doing self-healing:
-   Get to know your systems. 
-   Set up automated alerts to see which error scenarios are most common.
-   Take a holistic look at problems to identify and fix the root causes where possible ![[Pasted image 20220424192721.png]]
**Benefits:**
-   Happier dev and ops teams. 
-   Benefits to users and operations. 
-   Reduced support burden
-   Less rote and menial work

[[IT Support Role]]