# Layers of Service-Oriented Architecture
UID: 202203241550
Tags: #🌱 
Links: [[Enterprise Solution Development]]

## Defining a service in IT
A service may be defined as:

A unit that provides one or many functionalities needed to support business requirements and can be used by other applications or services over the network via a standard interface that is independent of programming languages and platforms
![[Pasted image 20220324155218.png]]
The Service Provider Interface and the Service Consumer Interface refer to some code that is at the provider and consumer end respectively and enables data exchange between the provider and the consumer.

## Service-Oriented Architecture
- Consider turning all IT systems into services
- Each service can be small, simple, or large, complex
- Develop and maintain enterprise solutions as assemblies of loosely-coupled services
- Manage assemblies at various layers of different functionality and/or complexity. Sample layers:
 ![[Pasted image 20220324155341.png]]
e.g. OCBC and CASA: current accounts saving accounts
- Simple services do not call other services
- Complex services call other services. It's job is to **orchestrate**
- UI
	- [[Model-view controller]]
		- Separating data with service from app view.
#### Why separate into layers?
- Programmers can work in parallel
- Allow for specialisation

## Microservices recap
microservice may be defined as:
- A service that can be independently developed and deployed and provides one or a few functionalities needed to support business requirements
- Develop and maintain enterprise solutions as assemblies of loosely-coupled microservices
- Provide all functionalities needed as microservices
- Each microservice is relative small, simple

##### Sample SOA layers with microservices:
![[Pasted image 20220324160002.png]]
## Types of microservices
#### Atomic/Simple (Micro)Service
- A (micro)service that provides functionality related to one kind of entity of a business concern (e.g., Book, Customer, etc.)
	- The operations provided by the (micro)service can be CRUD
- The implementation details of the (micro)service within its interface is independent of others within an enterprise context
	- It may be developed with any tool in any language on any OS of choice
	- An atomic microservice is self-contained, without depending on a monolith or other (micro)services
	- An atomic service may depend on others, as a “**wrapper**” to expose some functionality in a monolith or external APIs
		- Hides implementation details: we can simply change the wrapper to wrap a new version and remove the complications in configurations
#### Composite/Complex (Micro)Service
- A (micro)service that provides functionality related to more than one entity (e.g., Place an order, Process a shipping record, Restock inventory, etc.)
- The functionality provided by it consists of a set/sequence of activities (including direct communication with others) for a business process, which may depend on others
	- It may be developed with any tool in any language on any OS of choice
	- A composite microservice may depend on other (micro)services, but should not directly depend on a monolith
	- A composite service may depend on a monolith and other (micro)services, but not recommended
##### Atomic/Simple (Micro)Service
- A (micro)service that provides functionality related to one kind of entity of a business concern (e.g., Book, Customer, etc.)
	- The operations provided by the (micro)service can be CRUD
- The implementation details of the (micro)service within its interface is independent of others within an enterprise context
	- It may be developed with any tool in any language on any OS of choice
	- An atomic microservice is self-contained, without depending on a monolith or other (micro)services
	- An atomic service may depend on others, as a “wrapper” to expose some functionality in a monolith or external APIs

##### Composite/Complex (Micro)Service
- A (micro)service that provides functionality related to more than one entity (e.g., Place an order, Process a shipping record, Restock inventory, etc.)
- The functionality provided by it consists of a set/sequence of activities (including direct communication with others) for a business process, which may depend on others
	- It may be developed with any tool in any language on any OS of choice
	- A composite microservice may depend on other (micro)services, but should not directly depend on a monolith
	- A composite service may depend on a monolith and other (micro)services, but not recommended

## Sample SOA Layers for an Enterprise
![[Pasted image 20220331161107.png]]
- Note: Microservices layer is different from Atomic Microservices Layer. See [[ESD Revision]]
- Composite Services Layer -> Think [[Business Process Modelling]]
- Right column: supporting technologies
##### Components
###### User Interface Layer
- Provides the interfaces for interactive activities with users
- Can trigger a business process, which may trigger composite and/or atomic (micro)services
- Do NOT invoke monoliths directly; only use monoliths indirectly via other (micro)services
###### Business Process Layer
- A business process can be long-running involving user interactions (e.g., Loan Approval that requires a human approval) or straight-through (e.g., one-click ordering)
- A business process can be implemented as a (micro)service, usually composite
###### Composite (Micro)Services Layer(s)
- Can directly communicate to other (micro)services in the same or lower layers, but not to (micro)services in the higher layers 
###### Atomic (Micro)Services Layer(s)
- An atomic microservice can be independently developed, deployable, and scalable
- An atomic service may depend on a monolithic IT system or some external services
- Do NOT directly communicate to other atomic (micro)services
###### IT Systems Layer
- Applications (COTS, Custom or Legacy) that provide one or many functionalities
- Do NOT directly communicate to other applications
###### External Services Layer
- External services from third-parties, usually beyond the control of the enterprise; may or may not be microservices
- May be directly used by components other layers
###### API Gateways
- Manage accesses to (micro)services, usually for external service consumers 
###### Business Process Management Software Suites (BPMS)
- Manage business processes (including design, modelling, analysis, implementation, execution, monitoring, optimization, etc.)
###### Enterprise Service Buses
- Manage accesses to (micro)services, usually for internal uses in an enterprise
###### Communication Technologies
- Message brokers
- HTTP servers
###### Storage Servers
- DBMS, SharePoint, Drive, …

## Benefits of Microservice and SOA Layers
###### Enforce a high degree of modularity and help to manage complexity in large enterprise solutions
- Atomic “Wrapper” services are less modular than atomic microservices due to their dependency on the underlying (monolithic) applications
###### Microservices are loosely coupled from each other
- Independently developed, deployable, scalable
###### (Micro)services interact with each other through standards-based interfaces
- Independent of programming languages or platforms
- Common errors (e.g., timeout, network interruption, wrong data format, etc.) may be handled in a standard way.
###### Easier to reuse a (micro)service than a monolith
- Implementing a business process is like to assemble a composite microservice that reuses other (micro)services.
###### Easier to change individual (micro)services than to change monoliths
- Easier to support continuous integration and deployment (CI/CD) for changing business requirements
