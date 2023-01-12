# DHCP
UID: 202204171548
Tags: #🌱 
Links: [[Web applications]] [[Web app development]] [[Basic Networking HTTP]]

The Dynamic Host Configuration Protocol (DHCP) is a network management protocol used on Internet Protocol (IP) networks for automatically assigning IP addresses and other communication parameters to devices connected to the network using a client–server architecture.

The technology eliminates the need for individually configuring network devices manually, and consists of two network components, a centrally installed network DHCP server and client instances of the protocol stack on each computer or device. When connected to the network, and periodically thereafter, a client requests a set of parameters from the DHCP server using the DHCP protocol.

DHCP can be implemented on networks ranging in size from residential networks to large campus networks and regional ISP networks.[2] Many routers and residential gateways have DHCP server capability. Most residential network routers receive a unique IP address within the ISP network. Within a local network, a DHCP server assigns a local IP address to each device.

DHCP services exist for networks running Internet Protocol version 4 (IPv4), as well as version 6 (IPv6). The IPv6 version of the DHCP protocol is commonly called DHCPv6.
![[Pasted image 20220417175019.png]]
```jsx
ipconfig/ all
```

To check DHCP server, DNS server, Gateway etc.

> [!warning]
> Dynamic address is set by the router, not the host 

## Allocation
Dynamic addresses changes regularly to free up unused addresses, whereas static need not be changed
 Internet Protocol (IP) defines how devices communicate within and across local networks on the Internet. A DHCP server can manage IP settings for devices on its local network, e.g., by assigning IP addresses to those devices automatically and dynamically.

DHCP operates based on the client–server model. When a computer or other device connects to a network, the DHCP client software sends a DHCP broadcast query requesting the necessary information. Any DHCP server on the network may service the request. The DHCP server manages a pool of IP addresses and information about client configuration parameters such as default gateway, domain name, the name servers, and time servers. On receiving a DHCP request, the DHCP server may respond with specific information for each client, as previously configured by an administrator, or with a specific address and any other information valid for the entire network and for the time period for which the allocation (lease) is valid. A DHCP client typically queries for this information immediately after booting, and periodically thereafter before the expiration of the information. When a DHCP client refreshes an assignment, it initially requests the same parameter values, but the DHCP server may assign a new address based on the assignment policies set by administrators.

On large networks that consist of multiple links, a single DHCP server may service the entire network when aided by DHCP relay agents located on the interconnecting routers. Such agents relay messages between DHCP clients and DHCP servers located on different subnets.

Depending on implementation, the DHCP server may have three methods of allocating IP addresses:

#### Dynamic allocation
A network administrator reserves a range of IP addresses for DHCP, and each DHCP client on the LAN is configured to request an IP address from the DHCP server during network initialization. The request-and-grant process uses a lease concept with a controllable time period, allowing the DHCP server to reclaim and then reallocate IP addresses that are not renewed.

#### Automatic allocation
The DHCP server permanently assigns an IP address to a requesting client from a range defined by an administrator. This is like dynamic allocation, but the DHCP server keeps a table of past IP address assignments, so that it can preferentially assign to a client the same IP address that the client previously had.

#### Manual allocation

This method is also variously called static DHCP allocation, fixed address allocation, reservation, and MAC/IP address binding. An administrator maps a unique identifier (a client id or MAC address) for each client to an IP address, which is offered to the requesting client. DHCP servers may be configured to fall back to other methods if this fails.
DHCP services are used for Internet Protocol version 4 (IPv4) and IPv6. The details of the protocol for IPv4 and IPv6 differ sufficiently that they may be considered separate protocols. For the IPv6 operation, devices may alternatively use stateless address autoconfiguration. IPv6 hosts may also use link-local addressing to achieve operations restricted to the local network link.