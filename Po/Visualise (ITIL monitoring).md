# Visualise (ITIL monitoring)
UID: 202204232057
Tags: #🌲 
Links: [[Monitoring with ITIL v 4.0 — 5.2.7]]

Measurements and analysis has to be actionable as quickly as possibly and with as much depth as possible.
This is performed in a variety of ways:

## RAG (report)
Red, Amber, Green reports
- Example: AWS
    
    ![Untitled](Enterprise%20f610f/Untitled%208.png)
    
- Example: JIRA
    ![Untitled](Enterprise%20f610f/Untitled%209.png)
    

## Run charts
- Run charts are common in monitoring tools.
- Example: Network utilisation charts
    
    ![Untitled](Enterprise%20f610f/Untitled%2010.png)
    

## Alarms/ alerts
Monitoring tools must provide a wide range of alerts that inform the right people at the right time when an event occurs. This include:
- **Failure** (Red)
    - A process has failed and could not be recovered.
    - Immediate action is required
- **Warnings** (Amber)
    - There may not be a problem or something failed but has recovered.
    - Not an immediate problem but needs to be investigated.
- **Success** (Green)
    - A process has completed successfully.
    - No action required.
    - Useful data for regular review.