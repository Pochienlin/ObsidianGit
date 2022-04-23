# Analyse (ITIL monitoring)
UID: 202204232058
Tags: #🌲 
Links: [[Monitoring with ITIL v 4.0 — 5.2.7]]

## # Analyse
```ad-abstract
title: what to analyse?
Analyse the data available, including peaks and trends
```

## Peaks
- Examples
    - Spike in network traffic
    - CPU utilisation to 100%
    - Increase in the number of users logging in
    - Memory at 100%
- What might a peak be a symptom of?
    - A virus
    - Application process in an infinite loop
    - DoS attack
    - Big database query

| Peak | Cause | Response |
| --- | --- | --- |
| Spike in network traffic | Virus | Alert security team |
| CPU utilisation to 100% | Process hung | Alert users, restart the process, alert tier 3 |
| Memory at 100% | Large database query | Clear db cache, alert dev team |
| Increase in number of users | Product sale | No action |
- What is the response to a peak?
    - Don’t panic
    - Investigate the cause
    - Check the frequency of the spikes - increasing or random
    - Decide if any further action is required

## Trends
```ad-tip
title: Trends are...
Trends are usually defined as a number of consecutive  data points away from the average in the same direction, often 3 data points are used as the definition of a trend.
```

- Trends are key to ensuring robust, long-lived systems. Trend analysis can be used for:
    - Alerts for warnings
    - Predicting component failures
    - Capacity planning
    - Estimating IT needs for future business plans
- Example:
    
    ![Untitled](Enterprise%20f610f/Untitled%2011.png)
    
Some points on this control chart:
    - The first half of the graph is normal noise.
    - The red circled dots may be showing a downward trend.
    - The yellow line may show a trend of a new average.
    - The blue circled dot is unusual (special case) as it is more than 3 standard deviations (𝝈) away from the average.
    Conditions 2 to 4 are warnings of a possible problem and should be checked to see if they persist.
- #### Response approach:
    - Don’t panic.
    - If beyond control lines then:
        - For peaks - check frequency, increasing or random
        - For trends - investigate the cause
        - Decide if any further action is required
###### For example:
- Number of complaints increase by more than 10% above average
    - Alert the product manager