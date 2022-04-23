# ESD Revision
UID: 202203311606
Tags: #🌱 
Links: [[Enterprise Solution Development]]

#### Monolithic vs Microservices: Benefits versus one another
Reusability

#### API Patterns
- Intermediary
	- Communcations between client and services can be helpful in:
		1.  Monitoring
		2. Access control, authentication
		3. Caching
		4. Versioning
			1.  Allow changing of variables without having to go to specific microservices/ containers
		5. Load balancing
		6.  Service-data aggregation
			1.  In practice, not clear that Kong gateway supports it
			2. Complex thing for API gateway to do: merging data, editing before forwarding
			3. Possible, unlikely to come out in exam

#### Docker Compose Review
- Images need not be built before running Docker Compose
- YAML is used to configure containers
- YAML file is not a Dockerfile
	- YAML is a superset of JSON
	- Service defined in YAML can have dependencies
> read up more on versioning and YAML
- Kong can function as a gateway without Konga, Konga is meant to interface and manage Kong, but other means of configuring Kong is possible
 
|Attribute|Atomic/Simple|Composite/Complex|
|----|---|---|
|Independently Deployable|Yes|Yes|
|Independently Scalable|Yes|Yes|
|Any Programming Language|Yes|Yes|
|Encapsulates…|… a single “atomic” entity (e.g., Customer, Product)|… a single process. It often orchestrates or aggregates other atomic/composite (micro)services.|
|Naming Convention|Noun E.g. book, order, shipping_record|Verb E.g. Place order, Process shipping|
|Can invoke other services|Never|Yes, that is its main purpose|
|Data ownership|Typically has exclusive ownership of the database tables for its data entities |Typically does not own data, but requests the data via the APIs of other services|

#### Atomic vs. Services
| Micro | Normal Service|
|---|---|
|Independently scalable| Dependent on IT Systems|
| Independently deployable | Needs to be deployed with IT Systems|
| Exclusive control over own databases | Interacts with IT system for database|
| Size - fewer functionality* | more robust functionalities|

*obeys the [[two pizza rule]]* *
