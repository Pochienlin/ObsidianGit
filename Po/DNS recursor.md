# DNS recursor
UID: 202204171557
Tags: #🌲 
Links: [[DNS]]

#### Recursive DNS resolver

The recursive resolver is the computer that responds to a recursive request from a client and takes the time to track down the [DNS record](https://www.cloudflare.com/learning/dns/dns-records/). It does this by making a series of requests until it reaches the authoritative DNS nameserver for the requested record (or times out or returns an error if no record is found). Luckily, recursive DNS resolvers do not always need to make multiple requests in order to track down the records needed to respond to a client; [caching](https://www.cloudflare.com/learning/cdn/what-is-caching/) is a data persistence process that helps short-circuit the necessary requests by serving the requested resource record earlier in the DNS lookup.

![How DNS works - the 10 steps in a DNS query](https://www.cloudflare.com/img/learning/dns/what-is-dns/dns-record-request-sequence-1.png)