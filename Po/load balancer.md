# load balancer
UID: 202204171552
Tags: #🌱 
Links: [[Enterprise Solution Development]] [[Enterprise Applications and Business Processes]] [[Web applications]] [[Web app development]] [[Networking Basics]] [[Basic Networking HTTP]]

## What does a load balancer do?
Route network traffics to different receivers and dispatch processing workloads among them

![Untitled](Enterprise%209b3bb/Untitled%2017.png)

**Load balancing** refers to efficiently distributing incoming network traffic across a group of backend servers, also known as a _server farm_ or _server pool_.

Modern high‑traffic websites must serve hundreds of thousands, if not millions, of concurrent requests from users or clients and return the correct text, images, video, or application data, all in a fast and reliable manner. To cost‑effectively scale to meet these high volumes, modern computing best practice generally requires adding more servers.

A **load balancer** acts as the “traffic cop” sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests in a manner that maximizes speed and capacity utilization and ensures that no one server is overworked, which could degrade performance. If a single server goes down, the load balancer redirects traffic to the remaining online servers. When a new server is added to the server group, the load balancer automatically starts to send requests to it.

In this manner, a load balancer performs the following functions:

-   Distributes client requests or network load efficiently across multiple servers
-   Ensures high availability and reliability by sending requests only to servers that are online
-   Provides the flexibility to add or subtract servers as demand dictates

![load balancing diagram](https://www.nginx.com/wp-content/uploads/2014/07/what-is-load-balancing-diagram-NGINX-1024x518.png)

## Types of load balancing
1. **Round Robin** - or "RR"
	1. The load balancer sends the first request to server 1, second request to server 2, ..., nth request to server n and (n+1)th request to server 1
	2. By far the most popular load balancing method
	3. Pros: Simple, cheap to configure, does not require powerful processing hardware/ software to support
	4. Cons: for session times with large variances, the load can become imbalanced over time
2. **Smart load Balancing** - aka load based balancing
	1. The load balancer and servers constantly communicates to find out the traffic of each server
	2. The balancer then diverts traffic to the least burdened server
	3. Pros: more efficient as servers are fully utilised
	4. Cons: harder to set up, configure, maintain. Higher starting cost.
3. **Random distribution**
	1. The load balancer uses a ```rand()``` function to assign an arbitrary server to the request
	2. WIth sufficient traffic, this aggregates out to a predictable balance
	3. Pros: like RR, simple and cheap to set up
	4. Cons: naive in the same way as RR is, though less susceptible as statistically it is less likely to be skewed
```