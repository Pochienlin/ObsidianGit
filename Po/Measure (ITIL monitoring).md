# Measure (ITIL monitoring)
UID: 202204232054
Tags: #🌲 
Links: [[Monitoring with ITIL v 4.0 — 5.2.7]]

```ad-abstract
title: Why measure?
The enterprise landscape contains many systems and subsystems all working together to deliver business value. 
Monitoring needs to be applied to both the business processes and the IT infrastructure.
```
### IT infrastructure

![Untitled](Enterprise%20f610f/Untitled%206.png)

- **Server** - disk, CPU, processes, memory
- **Network** - utilisation, latency
- **Processes** - number, time, fails
- **Storage** - Input/Output (IO) rates, capacity, availability
- **Connections** - DB, web
- **Database** - space, connections, locks
###### Example of IT infrastructure metrics    
| Element                 | Description                         | Response                             | 
| ----------------------- | ----------------------------------- | ------------------------------------ | 
| CPU Usage               | CPU usage and idle times            | WARNING if high for extended period  |
| Memory Usage            | Memory usage and free memory, in MB | WARNING if high for extended period  |
| Active HTTP Connections | Number of active HTTP connections   | WARNING if above a defined threshold |
| Connection Duration     | Length of time for connections      | WARNING if above a defined threshold |

### Business Metrics
![Untitled](Enterprise%20f610f/Untitled%207.png)

The business is expecting certain service levels, monitoring needs to ensure these are within limits. 

- For example:
    - Communication interface responsiveness - e.g. User and API
    - Process volumes
    - Throughput
    - Application processes
    - Business processes end to end
###### Example of Business Metrics    
| Element | Description | Response |
| --- | --- | --- |
| Application Processes | Busy and idle process metrics | WARNING if too many are busy for too long |
| Request Throughput | Request throughput (requests per second) | WARNING if above a defined threshold |
| Request Processing Time | Request processing time, in seconds | WARNING  if too long |
| Response Data Throughput | Response data throughput, in KB per second | WARNING if above a defined threshold |
| Response Data Processed | Response data processed, in KB per second | WARNING if above a defined threshold |
| Data of change | Size, staleness, incoming rate (too slow or too fast) | WARNING if above defined thresholds |

