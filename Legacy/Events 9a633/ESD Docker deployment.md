# Enterprise Solution Developmt | Docker service deployment

Archive?: No
End: January 27, 2022 6:45 PM
Start: January 27, 2022 3:30 PM

# Objectives

On completing this module, you will be able to:

- Understand the concepts of containers and containerization in the context of microservices
- Deploy microservices using docker technology

# Topics

- Service deployment
- Docker
- Image vs. container
- Dockerfile
- Basic networking for containers

# Deploying a Microservice – Running a Microservice on Another Machine

![Untitled](Enterprise%20dd655/Untitled.png)

- The book microservice runs on my machine for development, but after the source code is transferred to the server machine, it does not run. What could be the reasons?
    - Microservice code: [book.py](http://book.py/)
        - Python not installed or installed with a different version
        - Relevant modules not installed or installed with a wrong version. E.g., Flask, Flask-SQLAlchemy, mysql-connector-python, etc.
    - Database problems:
        - Access to the WampServer/MySQL DB fails because of various network issues. E.g., wrong URI, wrong account, firewall filters
        - The WampServer/MySQL DB server is not installed or is not running or does not contain the needed DB table(s)

Imagine you are organizing a sports event in the open ground and you have to distribute lunch for 100 people. Each person needs to get some French fries, chicken nuggets and some salad.

- How would you go about doing this?

## Example: Shipping industry

![Untitled](Enterprise%20dd655/Untitled%201.png)

Similar problem exists in the shipping industry too. Downside of loading & unloading of arbitrary items without standardize "boxes" that can hold most kinds of items:

- Ships spend more time at ports than in the sea, due to slow loading & unloading; which lead to lower ship utilization rate, higher shipping cost.
- Need to hire many workers to load different things at port; high wage cost; high location restrictions for the workers; small items can go missing easily.
    - Watch Wendover Production: [https://www.youtube.com/watch?v=F-ZskaqBshs](https://www.youtube.com/watch?v=F-ZskaqBshs) till 4:07.
    - Containerization: The Most Influential Invention That You've Never Heard Of Or WSJ youtube video: [https://www.youtube.com/watch?v=0MUkgDIQdcM](https://www.youtube.com/watch?v=0MUkgDIQdcM) till 2:11.
    - How a Steel Box Changed the World: A Brief History of Shipping

## Containerisation

Manufacturers can load items into containers at their places, with more flexible worker sources, not restricted by the port, and safer for small goods.

Faster to load and unload containers at ports.

What's amazing: the whole world cannot agree on which side of road to drive, power plug type, currency, video format, software operating systems we use…, but the container sizes are standardized.

Containerization provides an easy method to load, transport and unload the goods, it provides:

- Flexibility- carry a wide variety of goods
- Velocity- rapid and reduced port turnaround time
- Lower Cost- for loading and unloading

### Containerisation of Microservice

![Untitled](Enterprise%20dd655/Untitled%202.png)

Containerization of a microservice

- Package necessary items needed to run a microservice into an image that can be transferred to and run as a container on another machine

---

# Docker

> It is an open platform for developers and system administrators to package, transfer, and run microservices (or any* application) on any* machine either on premise or on the cloud
> 

---

- Docker itself can run on some (not all) versions of Windows, macOS, Linux.
    - The containers running on Docker can be Linux-based or Windows-based or macOS-based (not officially supported though).
    - There are alternatives to Docker (beyond the course scope), e.g.,
    - LXD (pronounced “lexdi”) from Canonical Ltd., the company behind Ubuntu, [https://linuxcontainers.org/](https://linuxcontainers.org/)
    - rkt (pronounced ‘rocket’) from the Linux distributor, CoreOS and RedHat, [https://cloud.redhat.com/learn/topics/rkt](https://cloud.redhat.com/learn/topics/rkt)
    - Linux VServer, [http://linux-vserver.org/Welcome_to_Linux-VServer.org](http://linux-vserver.org/Welcome_to_Linux-VServer.org)
    - Windows Containers by Microsoft, [https://docs.microsoft.com/en-us/virtualization/windowscontainers/about/](https://docs.microsoft.com/en-us/virtualization/windowscontainers/about/)

![Untitled](Enterprise%20dd655/Untitled%203.png)

- Dockerfile contains the instructions for Docker to build an image (FROM, COPY, RUN, etc.)
- Note: (beyond scope):
    - Docker images can be pushed to or pulled from the docker hub [https://hub.docker.com/](https://hub.docker.com/)
    - Additional notes (beyond the course scope):
    - Cf. [https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html](https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html)
    - Docker images on Windows can be stored as Hyper-V virtual hard disk files. They can be saved to a tar/zip file to be transferred as a usual file; and then be loaded into the docker running on another machine. cf. [https://stackoverflow.com/questions/23935141/how-to-copy-docker-images-from-one-host-to-another-without-using-a-repository](https://stackoverflow.com/questions/23935141/how-to-copy-docker-images-from-one-host-to-another-without-using-a-repository)
    - Relevant docker commands:
    - docker save -o <path and file name for the generated tar file> <image name>docker load -i <path to the tar file>Dockerfile reference: [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)

## Docker architecture

We install Docker on our machine, which provides the docker daemon (or called engine / server). The machine with the docker engine installed is called a docker host.

The docker client can run from another machine; in our lab, we use a cmd window on the same machine with the docker daemon installed (i.e., the docker host).

- Downsides of containerization:
    - Every machine that needs to run the microservice needs to have Docker installed, which introduces some performance overhead.
    - Upfront investment is thus higher; images/containers take space, even if empty; many unused containers lying around may need proper management too.
    - Images/containers can get damaged/lost.
    - It makes it easier to package inappropriate/illegal/malicious contents into images/containers without being detected.
- There are alternative container runtime engines (beyond the course scope); they can load and run images built by Docker. e.g.,
    - containerd: [https://containerd.io/](https://containerd.io/)
    - CRI-O: [https://cri-o.io/](https://cri-o.io/)

## Communication on a Docker Host

![Untitled](Enterprise%20dd655/Untitled%204.png)

![Untitled](Enterprise%20dd655/Untitled%205.png)

---

# IP Address

![Untitled](Enterprise%20dd655/Untitled%206.png)

Each machine may belong to multiple (sub)networks at the same time. It can have multiple IP addresses at the same time too.

Different machines in different (sub)networks can have the same IP address at the same time.

Broadly speaking, two machines can communicate with each other as long as they have a way to identify each other in a network. 

But in reality, there are many other factors in play that may affect the communication, 

- e.g., firewalls installed on the machines and in the network may block the communication; the machines may belong to different (sub)networks and they don't recognize each other's IP; etc.

![Untitled](Enterprise%20dd655/Untitled%207.png)

![Untitled](Enterprise%20dd655/Untitled%208.png)

---

# Container networking

![Untitled](Enterprise%20dd655/Untitled%209.png)

Each container running on a docker host is in an internal subnetwork set up by the docker engine. Docker engine acts as a gateway for the containers, providing networking capabilities.

A docker engine sets up an internal network on the docker host, and assigns dynamic IP address(es) to each container in the internal network, often in the range of 172.x.x.x. The IP addresses are only valid for the internal network.

There are different ways to enable communications among containers.

- Our course covers the basic default ways to enable communication among containers:
    1. Containers and the host in the same internal network by default can communicate with each other by using their IP addresses in the same internal network.
    2. Each container can be assigned a name too; a container can communicate with other containers in the same subnetwork via the container names (act like hostnames for physical machines).
    3. The latest version of Docker defines a special hostname host.docker.internal on Windows or macOS for the docker host in the internal network; so, a program running within a container can use the special hostname to communicate with its host.
    4. Each container communicating with external network(s) needs network address translation (NAT) through the docker engine and docker host, e.g., port mapping (a particular kind of NAT).
    - Additional notes (beyond the course scope):
        
        docker inspect <container id> will show a lot of information about the container, including its IPAddress.
        
        Whether containers and hosts across different internal networks can communicate with each other depends on many networking settings between the different hosts.
        
        Further in-depth technical details (beyond the course scope): [https://docs.docker.com/network/](https://docs.docker.com/network/)
        

### Can container 1 be parked in subnetwork Y?

Not directly. By Docker alone they are isolated within their own machine internally, but there are external apps that can help surface it to the subnetwork and let Machine D receive it

# Accessing a Microservice inside a container

![Untitled](Enterprise%20dd655/Untitled%2010.png)

An external client may directly access the host IPs in the external network but not the container IPs (because internal IPs are invalid externally)

A common solution is to have an intermediary to translate between external and internal IPs

*The docker engine can be such an intermediary for network address translation.

## Network Address Translation (NAT) review

Map one network address (e.g., an IP and a port number) to another by modifying the address information in network communication data

So that, data can be (re)routed by the network to a different receiver or can appear to come from a different sender.

E.g., the router at our home

### NAT enabled router

![Untitled](Enterprise%20dd655/Untitled%2011.png)

![Untitled](Enterprise%20dd655/Untitled%2012.png)

## Accessing a Microservice inside a container via Port Mapping/ Forwarding

Port mapping is a kind of NAT, redirecting communication data from an IP:port number to another IP:port number

- Each container gets its internal IP address(es) when it is started by the docker engine.
- Each container, like a virtual machine, also has its (internal) port numbers, the same as a normal machine.
- The docker engine maps an (external) port of the docker host (a.k.a. host port) to an (internal) port of the container (a.k.a. container port);
    - after that, all incoming request data going to the host port is forwarded to the container port of a particular container;
    - the data replied from the container is forwarded by the docker engine and host back to the original client.
- References (beyond the course scope):
    - [https://en.wikipedia.org/wiki/Network_address_translation](https://en.wikipedia.org/wiki/Network_address_translation)
    - [https://en.wikipedia.org/wiki/Port_forwarding](https://en.wikipedia.org/wiki/Port_forwarding)

![Untitled](Enterprise%20dd655/Untitled%207.png)

![Untitled](Enterprise%20dd655/Untitled%2013.png)