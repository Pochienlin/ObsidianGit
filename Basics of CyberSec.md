# Basics of CyberSec
UID: 202301121330
Tags: #🌱 
Links: [[Foundations of Cybersecurity]]

----
## Overview
```toc 
style: number 
min_depth: 1 
max_depth: 6 
```

## Objectives 
- Describe various security threats and objectives
- Understand confidentiality, integrity, availability properties

---
## Case Study
[[2017 Ukraine ransomware attacks]]
<iframe width="560" height="315" src="https://www.youtube.com/embed/KaUL-YQk7jM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe height = 800 width = 100% padding = 0.0 margin = 0.0 src="http://www.bbc.com/future/story/20170704-the-day-a-mysterious-cyber-attack-crippled-ukraine" style="background-color: #FEF5CA;"> /iframe>

- A series of powerful cyberattacks swamped websites of Ukrainian organizations on 27 June
- Similar infections in France, Germany, Italy, Poland, Russia, United Kingdom, the United States and Australia
- The attack originated from an update of a Ukrainian tax accounting package called MeDoc 
- Based on a modified version of the Petya ransomware: Encrypt some key Windows system boot files and send US$300 in bitcoin to one of three wallets to receive instructions to decrypt their computer
- Though the target is more likely aimed at crippling the Ukrainian state rather than for monetary reasons
- Major impacts
- The radiation monitoring system at Ukraine's Chernobyl Nuclear Power Plant went offline
- Several Ukrainian ministries, banks, metro systems and state-owned enterprises

------

## Importance of Cyber Security
- Cyberattacks affect all people 
- They can quickly cripple a country/organization
- Threats to personal information
- Hackers attack a computer in the US every 39 seconds
- Advanced in technology will cause a boom in cyberattacks
- More powerful computing
- Faster speed of broadband services
- Better AI, IoT, virtual reality techniques, etc.
- E.g., increasingly automated cyberattacks

## What is cyber?
“Involving, using, or relating to computers, especially the internet”
Not just PCs, but also smartphones, wearables,…, any devices related/linked to Internet 

## What does security mean?
To protect the items you value, called the assets of a computer system, from being compromised by different types of threats
Hardware, software, and data

## What are assets?
Any computer items we value
Value of each item varies significantly in different contexts

| Hardware                         | Software                                  | Data                               |
| -------------------------------- | ----------------------------------------- | ---------------------------------- |
| Computers, devices, network gear | OS, Utilities, COTS apps, individual apps | Docs, photos, music, video, emails |

-----

# Security Threats
## What are threats
- Threat to a computing system is a set of circumstances or a likely event that has the potential to cause loss or harm to the system 
- A potential violation of security
- Data breach
- Denial of service
- Fabrication of data
- …

Cybersecurity 101 

<iframe width="560" height="315" src="https://www.youtube.com/embed/sdpxddDzXfE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Fundamental Reasons
1. Resource Sharing
    - e.g., programs running under the same OS, computers in the same network, virtual machines in the same cloud, …
2. Dependence
    - e.g., OS execution depending on application inputs (occasionally), a communication depending on intermediary devices, a program execution depending on inputs from the network …
3. There always exist some vulnerabilities in the system 
    - Vulnerability is a weakness in the security system (i.e., in procedures, design, or implementation), that might be exploited to cause loss or harm.

## Threat
- Something bad that could happen
- Vulnerability
- Weakness in an information system that could be exploited

## Incident
- When a vulnerability is exploited to compromise the security of systems, the result is a security incident

## Attack
- Some actions taken by a malicious intruder
- A human (criminal) who exploits a vulnerability perpetrates an attack on the system

## Passive attacks
- A passive attack can monitor, observe or build use of the system’s data for sure functions. It doesn’t have any impact on the system resources, and also, the data can stay unchanged, e.g., eavesdropping attack
- Active attacks – Modify or alter the content and impact the system resource, e.g., Denial-of-Service attacks (DoS)

## Types of threats
Analogy of visiting someone's home

| On the road                                          | At home                                 | Guest house              |
| ---------------------------------------------------- | --------------------------------------- | ------------------------ |
| eavesdropping, tampering, phishing, rogue routing, … | spyware, ransomware, trojan horse, worm | •leakage from the server | 

## Sources of threats
| Source of threat | Threat description |
|---|---|
|Bot-network operators| Use a network, or bot-net, of compromised, remotely controlled systems to coordinate attacks and to distribute phishing schemes, spam, and malware attacks. The services of these networks are sometimes made available on underground markets.|
|Criminal groups|Seek to attack systems for monetary gain (e.g., identity theft and online fraud) or conduct industrial espionage. They hire or develop hacker talent.|
|Hackers| Break into networks for the thrill of the challenge, bragging rights in the hacker community, revenge, stalking others, and monetary gain, among other reasons|
|Insiders| Includes disgruntled employees, contractors hired by the organization, as well as employees who accidentally introduce malware into systems. |
|Nations|Nations use cyber tools as part of their information-gathering and espionage activities. In addition, several nations are aggressively working to develop information warfare doctrine, programs, and capabilities.|
|Phishers|Individuals, or small groups, execute phishing schemes in an attempt to steal identities or information for monetary gain |
|Spammers|Individuals or organizations distribute unsolicited e-mail with hidden or false information in order to sell products, conduct phishing schemes, distribute spyware/malware, or attack organizations (i.e., denial of service). |
|Spyware/malware authors| Individuals or organizations with malicious intent carry out attacks against users by producing and distributing spyware and malware. |
|Terrorists|Seek to destroy, incapacitate, or exploit critical infrastructures in order to threaten national security, cause mass casualties, weaken a nation’s economy, and damage public morale and confidence.|

## Key aspects of threat modeling
- Assets: What are we trying to protect? How valuable are those assets?
- Adversaries: Who might try to attack, and why?
- Vulnerabilities: How might the system be weak?
- Threats: What actions might an adversary take to exploit vulnerabilities?
- Risk: How important are assets? How likely are these assets exploited?
- Possible Defenses

[Class wooclap](https://app.wooclap.com/23CS440W1G2?from=instruction-slide)

-----
# Security Objectives

## C-I-A
![[Pasted image 20230112141728.png]]

### Confidentiality
Confidentiality is the concealment of information
- Eavesdropping: Secretly listening to the private conversation or communications of others without their consents
- Packet sniffing is a technique whereby packet data flowing across the network is detected and observed

### Integrity 
Integrity is the prevention of unauthorized changes
1. Interception
2. tamper
3. release again

### Availability
Availability is the ability to use information or resources
- Overwhelm to crash servers (DDoS)
- Disrupt infrastructure

| C-I-A lost | Threats|
|---|---|
|Confidentiality |In an interception means that some unauthorized party has gained access to an asset.|
|Availability|In an interruption, an asset of the system becomes lost, unavailable, or unusable.|
|Integrity|If an unauthorized party not only accesses but tampers (forges) with an asset, the threat is a modification.|
|Integrity| Finally, an unauthorized party might create a fabrication of counterfeit objects on a computing system.|

![[Pasted image 20230112142428.png]]

### Classic Security Objectives

When we talk about computer/cyber security, we mean that we are addressing three important aspects of any computer-related system: confidentiality, integrity, and availability (CIA)

1. Confidentiality ensures that computer-related assets are accessed only by authorized parties.
    - i.e. reading, viewing, printing, or even knowing their existence
    - Secrecy or privacy

2. Integrity means that assets can be modified only by authorized parties or only in authorized ways.
    - i.e. writing, changing, deleting, creating

3. Availability means that assets are accessible to authorized parties at appropriate times. 
    - i.e. often, availability is known by its opposite, denial of service.

In fact, these three characteristics can be independent, can overlap, and can even be mutually exclusive.

![[Pasted image 20230112142619.png]]

```ad-example
we can have a private conversation with our friends via some messaging apps at any proper time, while at the same time guaranteeing the privacy of the conversation and the authenticity of the sent messages

```
# Security Challenges

## Goals 
Prevention
- Prevent attackers from violating security policy (Stop an attack)

Detection
- Detect attackers’ violation of security policy (Detect ongoing/past attacks)

Response and Resilience
- Respond to / recover from attacks
- Continue to function correctly even if attack succeeds

## Asymmetry: Defense is hard

```ad-note
title: Principle of Easiest Penetration
An intruder can exploit any vulnerability to launch a penetration or attack
```


- An intruder only needs to find one vulnerability
    - This is because “security is only as strong as the weakest link”
- Defender needs to control all possible vulnerabilities
    - Securing a system involves a whole-system view
        -Cryptography, Implementation, People, Physical security, and Everything in between


## Control: How to achieve security
Control: We use a control as a protective measure. 
- That is, a control is an action, device, procedure, or technique that removes or reduces a vulnerability

![[Pasted image 20230112142930.png]]


## How to achieve control
Policy
- What we are trying to protect
    - Unambiguously partition system states
    - Correctly capture security requirements
Mechanism
- How to enforce the security policy
    - Encryption, software/network system controls, web applications controls
    - Agreed-on procedures or policies among users
    - Physical controls (e.g., lock on doors, backup copy of data)
    - Etc.
Assurance
- How well the security mechanism enforces the policy
    - Correctly and cost-effectively

![[Pasted image 20230112143249.png]]


## Security Tradeoffs
Security is not (never) free

>
>“Security professionals balance the cost and effectiveness of controls with the likelihood and severity of harm”
>

![[Pasted image 20230112143409.png]]

## Security by Obscurity
- A system would be secure if we hide its insides?

**It won’t work well**
- Vendor-independent standards
- Open source
- Widespread knowledge and expertise

```ad-note
title: Kerckhoff’s Principle (1883):
Only the key should be kept secret, while the algorithm itself should be publicly known.
```
----

# Basics of computer and [[Basic Networking HTTP | Networking]]

## Computer components
Instruction execution
Memory
CPU privilege


## Execution of flow of instructions 
![[Pasted image 20230112144151.png]]
```
CPU: Central Processing Unit
MMU: Memory Management Unit
```

1. CPU continuously fetches instructions from the main memory.
2. The address of the instruction to fetch is stored in a register which is updated automatically.
3. All addresses used by CPU are virtual addresses.
4. MMU maps virtual addresses to physical address.
5. Using different address spaces:
    - more efficient physical memory utilization
    - more flexible control of the software


## Memory Access
- A translation lookaside buffer (TLB) is a memory cache that is used to reduce the time taken to access a user memory location
- A bus (short for Latin omnibus) is a communication system that transfers data between components inside a computer

![[Pasted image 20230112144911.png]]

## Importance of memory

The main memory, called RAM, is the storage for code and data.
- It is “physically shared” by ALLLLL programs in the computer, though “virtually separated”  
- Many malware compromises require memory corruption or illicit memory accesses.
    - memory corruption: modified code or data
    - illicit memory access: information leakage. 

## Importance of CPU Privilege

The hardware (CPU + memory) is software semantic agnostic. 

CPU privilege level set controls the access of the program currently running on the processor to resources such as memory regions, I/O ports, and special instructions

![[Pasted image 20230112145429.png]]

## CPU Privilege ring
CPU always runs in a particular Ring which decides:
- whether the current code accesses the memory and I/O ports; 
    - Some memory regions (e.g., I/O registers, kernel code) can only be accessed when CPU in Ring 0. 
- whether an instruction can be executed. 
    -(Some instructions can only be run when CPU in Ring 0, e.g., loading control registers)

```ad-note
CPU Privilege is NOT related to user/root privilege
```
![[Pasted image 20230112145613.png]]

-----
# Takeaways
![[Pasted image 20230112145825.png]]

- [ ] Properties and security objectives
- [ ] Relevant threats w.r.t. C-I-A
