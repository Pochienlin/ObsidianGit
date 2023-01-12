# Network hosting
UID: 202204171547
Tags: #🌱 
Links: [[Enterprise Solution Development]] [[Enterprise Applications and Business Processes]] [[Networking Basics]] [[Web applications]] [[Web app development]]

## [[DHCP | Dynamic Host Configuration Protocol]]

## [[Ping]]

## Loopback address

`127.0.0.1` is the standard IP address referring to the current host

- If a program tries to connect to `127.0.0.1`, it is immediately looped back to the machine that currently runs the program
- Usually used for testing purposes, where you do not have another machine for conducting the test
- We may use this address in some labs in this course
- This is also called localhost

## Ports

![Untitled](Enterprise%209b3bb/Untitled%2013.png)

Ports are used to identify a particular process/application running on a machine so that the data sent to the machine can be relayed to the right application

- It is often present in some header of a network data packet; but can be omitted if using the standard ones
- E.g., [http://google.com:80](http://google.com/)