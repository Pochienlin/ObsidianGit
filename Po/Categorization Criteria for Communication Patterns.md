# Categorization Criteria for Communication Patterns
UID: 202204171720
Tags: #🌱 
Links: [[Communication technologies]]

| No. of receivers expected | Reply expected? | Online at the same time? | Type of communication               | Remarks           |
| ------------------------- | --------------- | ------------------------ | ----------------------------------- | ----------------- |
| 1                         | Yes             | Yes                      | one-to-one, request-reply, sync     |                   |
| 1                         | Yes             | No                       | one-to-one, request-reply, async    |                   |
| >1                        | Yes             | Yes                      | one-to-many, request-reply, sync    |                   |
| >1                        | Yes             | No                       | one-to-many, request-reply, async   |                   |
| 1                         | No              | Yes                      | one-to-one, fire-and-forget, sync   | highly improbable |
| 1                         | No              | No                       | one-to-one, fire-and-forget, async  |                   |
| >1                        | No              | Yes                      | one-to-many, fire-and-forget, sync  | highly improbable |
| >1                        | No              | No                       | one-to-many, fire-and-forget, async |                   |
We rarely have a use case for one-to-many + request reply. However this is theoretically possible: e.g. parallel flow in a process flow diagram, where token has to be collected from multiple receivers before a service can be continued.

We also rarely have cases where fire-and-forget and synchronous: if it is one way, there is hardly a reason for the receiver to be synchronised with the sender, since from the sender's perspective there would be no difference, sync or async. It would make sense then to deploy async instead in most if not all such cases.
```ad-question
 How many receivers does the sender expect for the same data sent?
```
### One receiver: one-to-one
![Untitled](Enterprise%209aa48/Untitled%203.png)
        
### Many receivers: one-to-many
![Untitled](Enterprise%209aa48/Untitled%204.png)
- E.g.,
            Email to all SMU addresses
            Public Warning System sounds an emergency message
            
#### All receivers: one-to-all
![Untitled](Enterprise%209aa48/Untitled%205.png)
- E.g.,
            WhatsApp to a group
            Email to selected SMU addresses
- Selected receivers: one-to-selected (can be zero, one, multiple, or all)
	- E.g.,
            Mail a letter to a person
            Email to one address
```ad-question
Does the sender expect a reply for the data sent?
```
##### No: fire-and-forget (fire & forget, one-way)
![Untitled](Enterprise%209aa48/Untitled%206.png)
	- E.g.,
            - Send an anonymous suggestion letter
            - Radio broadcasting
            - Lecturing (old-school)
##### Yes: request-reply (request-response)
![Untitled](Enterprise%209aa48/Untitled%207.png)
- E.g.,
	- - Phone call
	- Flipped classroom learning & teaching
	- Place an order for a book
```ad-question
Do the sender and the receiver need to be online at the same time to realize the communication?
```
##### Yes: synchronous (synchronized, sync.)
![Untitled](Enterprise%209aa48/Untitled%208.png)
- Usually have reply data too
        - E.g.,
            - Phone call
            - Place an order for a book
##### No: asynchronous (asynchronized, async.)
![Untitled](Enterprise%209aa48/Untitled%209.png)
- May or may not have reply data
- Usually have some intermediary(-ies)
- E.g.,
            - Mail a letter to a person
            - Email to all SMU addresses