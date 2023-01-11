# UiPath Overview
UID: 202205191449
Tags: #🌱 
Links: [[UiPath]] [[RPA Basics and Introduction to UiPath]]

## Overview
- describe UiPath, 
- its products and core components, 
- explain robots, analyze types of robots

UiPath is a global software company that makes robotic process automation (RPA) software. It was founded in Bucharest, Romania, by Daniel Dines and Marius Tîrcă. Its headquarters are in New York City. The company's software monitors user activity to automate repetitive front and back office tasks, including those performed using other business software such as customer relationship management or enterprise resource planning (ERP) software.

In December 2020, the company filed confidentially for an initial public offering, and became public on April 21, 2021.

## History
UiPath was founded in 2005 in Bucharest, Romania as DeskOver, by Romanian entrepreneurs Daniel Dines and Marius Tîrcă.

In 2013, the company released the first UiPath Desktop Automation product line, which gave companies RPA tools to automate manual and repetitive back office tasks.

In 2015, the company changed its name to UiPath. Also in 2015, after receiving seed funding from Accel Partners and earlier investors, the company also opened offices in London, New York City, Bangalore, Paris, Singapore, Washington, D.C., and Tokyo.

By April 2016, the company had released its Front Office and Back Office Server suites, and also released its Studio Community Edition. Within six months, the company had 10,000 active members, and more than 250 enterprise customers.

In 2017, UiPath reported 590 employees and moved its headquarters to New York to be closer to its international customer base.

In June 2019, research firm Gartner announced that from 2017 to 2018 UiPath moved from #5 to #1 in RPA market share. In September, UiPath was ranked #3 on the Forbes Cloud 100. The company was the featured cover story of the September 30, 2019 Forbes print edition with UiPath CEO Daniel Dines called "Boss of the Bots."

In October 2019, UiPath announced the acquisition of Ukrainian process documentation company StepShot and Dutch process mining company ProcessGold. Also in October, the company announced UiPath Explorer, a new product using technology from the acquired companies; a robot communication tool called UiPath Apps; a low code robot programming tool called UiPath StudioX; an embedded analytics tool called UiPath Insights; and UiPath Connect, a tool that allowed every employee to find new processes to automate.

In November of the same year, the company reported it had 5,000 customers worldwide, and a developer community of more than 500,000 people. In November, the company was ranked first in the Deloitte Technology Fast 500.

In April 2020, UiPath was named the top tech company and #2 overall in the Financial Times FT1000 ranking of Americas' fastest growing companies 2020. In June, UiPath was named to the CNBC 2020 Disruptor 50 ranking. In September, UiPath was ranked #3 on the Forbes Cloud 100 list for the second consecutive year. On December 17, Bloomberg reported that UiPath filed confidentially for an initial public offering (IPO).

In April 2021, UiPath raised $1.3 billion in an initial public offering on the New York Stock Exchange in one of the largest US software IPOs in history.


## UiPath Platform
### Discover. 
To identify the automation opportunities in an organization with the help of AI,
- Automation Hub. 
	Web application where you collaborate within the organization to identify Automation ideas. 
- Task capture. 
	Creates activity maps by recording the actions taken to complete a process. These activity maps are then used to build robots. 
- Process Mining. 
	Transforms data from the IT systems of an organization into a visual map. 
- Task mining. 
	AI based tool used to map and recommend which tasks can be automated. 

### Build. 
Automations are built for the identified automation opportunities. 
- StudioX 
	no code platform to build RPA projects
	primarily used by business users.
- Studio
	Used by RPA Devs to build projects
- Document understanding. 
	extract and interpret data from documents. 
- Marketplace. 
	In marketplace, you can find prebuilt automation components and templates. 

### Manage. 
manage, deploy, and optimize automation at enterprise scale. 
- Orchestrator 
	deploying and monitoring robots. 
- AI Center 
	deploying, managing, and improving machine learning models and using them with RPA workflows. 
- Test Suite 
	contains various product components to test RPA projects. 
- Data Service 
	no code data modeling and storage tool. 
- UiPath Insights 
	track, measure, and forecast the performance of an automation program. 

### Run. 
You can run automations with software robots. 
Robots can either be attended or unattended. 
1. Attended robots work along with the humans on their desktops and act as personal assistants. 
2. Unattended robots work independently in the background. 

- UiPath Apps
	Cloud-based, low-code application development platform to build and share custom applications that interact with automations. 
- Action Center. 
	switch tasks from robot to human and vice versa 
		- approvals
		- escalation
		- exception handling
- UiPath Asistant
	desktop application used to interact with the robots through an easy to use Launchpad. 
- Chatbots 
	trigger robots through messaging.


## UiPath Core Components
> [!abstract]
> Studio (Design) ---Deploy---> Orchestrator (Monitor) ---Execute---> Robots (Execute)
1. Studio
	1. Design automation workflows visually
	2. Minimal use of code
2. Orchastrator
	1. Control, Manage and monitor the robots
3. Robot
	1. Execute workflows and Instructions



-----
# Robots and their types

## Introduction to Robots
A robot is an automation execution agent. 

A robot can perform multiple steps in multiple applications.  

Software robots can
- perform complex calculations 
- decision making based on data and predefined rules
- mimic human actions such as type, click, and read data.  RPA robots interact with applications.  
- They can log into applications, move files or folders, and  copy and paste data. 
- This interaction is **non-invasive**.  

A robot is a piece of software program to execute steps on a computer according to work flow.  

Once developed, robots can perform complex data processing tasks and  decide with precision. 

## Types of Robots
> [!note]
> These are not comparative, just a list of their attributes. Not sure why the course structured them by these points specifically
| Attended                                        | Unattended                                               |
| ----------------------------------------------- | -------------------------------------------------------- |
| Work with humans on business activities         | Scheduled to start and stop as per business requirements |
| Collaborators in service and help desk          | Runs in both physcial and virtual environments           |
| Require human intervention                      | Operates without human intervention                      |
| Ensure high rpoductivity and low handling times | Maintained and guided remotely through Orchestrator      |

