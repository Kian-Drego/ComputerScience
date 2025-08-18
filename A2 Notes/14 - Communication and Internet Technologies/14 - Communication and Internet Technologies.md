# 14 - Communication and Internet Technologies
## Intro & Structure
##### - What are protocol?
##### - TCP/IP Protocols
##### - Common Protocols

---
## What are protocol?
 - set of rule that enables communication between devices (from different manufacturers)

## Protocols as a "Stack"
- Structured in layers, with each layer responsible for a part of the communication process
- Data packets transferred one by one from top layer to bottom layer before being set sent off
- Each layer, which corresponds to specific rules and software to validate these rules operates independently

## TCP/IP Protocol
- Enables computers to communicate over the internet and other networks


| **Application Layer**<br>	`- User Interface - Where the user submits data to be transmitted via web browser, etc`<br>	`- Security - Data is encrypted/secured for transmission`<br>	`- Translation - Data is translated/formatted for transmission over network`      |                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Transport Layer**<br>	`- Segmentation - divides data into data packets`<br>	`- Sequencing  - decides order in which packets will be transmitted, add this information to packet header`<br>	`- Received data from Application layer, sends packet to Network later` | ![](../Assets/Pasted%20image%2020250818192426.png) |
| **Network Layer**<br>	`- Decides optimum route through which packets will travel`<br>	`- Address packets with their source and destination IP address`<br>	`- Transmit packets down to Network Access (Physical/Data Link) layer`                                     |                                                    |
| **Network Access Physical/Data Link) layer**<br>	`- Turns data into raw signal to be transmitted over network`<br>	`- Controls rate at which data is transmitted`<br>	`- Responsible for physical connection(Wi-Fi, ethernet, etc.))`                                 |                                                    |