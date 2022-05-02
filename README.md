# icmp-pinger

## Description
The goal of the ICMP Pinger project was to create the client side functionality of a Ping application using Internet Control Message Protocol in Python. The Pinger application should be able to send ping requests to a specified host separated by approximately one second each. The application should wait up to one second to receive a reply, and in the case that a reply is not received within this time, we should assume that the ping or pong packet was lost. Each packet should contain a payload of data that includes a timestamp. Using the Python 2 skeleton code that was provided, the objective of this project was to fill in the incomplete functionality and add extensions. The functionality to be implemented involved fetching the ICMP Header, extracting the information from the header fields, and building and returning the “reply from” in the doOnePing() function, as well as creating a raw socket in the sendOnePing() function. The extensions to be implemented involved displaying a summary of packets lost and received as well as time/delay statistics for the ping request. To test functionality, the application should be able to successfully send three pings to each of the following servers: localhost, google.com, utexas.edu, www.u-tokyo.ac.jp, and telecom-paris.fr. In addition, the source code was converted to run identically using Python 3.

## Prerequisites
- The Python2 version was developed using Python 2.7.18
- The Python3 version was developed using Python 3.7.6
### Dependancies
All packages references are included in both Python2 and Python3
- socket
- os
- sys
- struct
- time
- select
- binascii

## Installation
Both versions of the pinger application are standalone scripts that will run in its appropriate Python interpreter
### To install with git bash
`git clone repo github.com/vmullassery/icmp-pinger`

## References
[SOCK_RAW](https://sock-raw.org/papers/sock_raw)
