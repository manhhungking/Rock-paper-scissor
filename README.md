# Industry track

# Student List:

| Group Member  | Student ID | Email                         | Chosen destiny |
| ------------- | ---------- | ----------------------------- | -------------- |
| Hung Trinh    | 2307229    | Hung.TRINH@student.oulu.fi    | Corporate      |
| Mazen Hassaan | 2307227    | Mazen.Hassaan@student.oulu.fi | Corporate      |
| Umer Yaseen   | 2307645    | Umer.Yaseen@student.oulu.fi   | Corporate      |
| Ida Haataja   | Y69019019  | ida.haataja@student.oulu.fi   | Corporate      |

## Project Title

Multiplayer Rock, Paper, Scissors Game

## About the project

### Course Project Overview

The project aims to design and implement a distributed system used for a multiplayer Rock, Paper, Scissors game. The software and system architecture aim to address key distributed system functionalities, including synchronization algorithms, resource naming and sharing mechanisms, and secure communication. The application involves smart IoT devices acting as game nodes, a central server managing game state and communication, and features request queuing and prioritization based on game conditions.

### Project Objectives

- Design and implement a distributed system for a multiplayer Rock, Paper, Scissors game.
- Implement synchronization algorithms to ensure real-time gameplay between players.
- Develop resource naming and sharing mechanisms to manage game state and communication.
- Implement secure communication protocols to protect sensitive player data.
- Utilize smart IoT devices as game nodes to enhance gameplay experience and interactivity.

### Expected Outcomes

- A functional multiplayer Rock, Paper, Scissors game accessible to players from different locations.
- Real-time gameplay experience with immediate feedback on match results.
- Efficient resource utilization and scalability through load balancing mechanisms.
- Secure communication channels to protect player data and ensure privacy.
- Demonstrated application of distributed system principles in building responsive and scalable gaming applications.

## Implemented components:

Detailed description of the system architecture (Application-specific system components):

- System must have at least three nodes (e.g, containers)
- Each node must have a role: client, server, peer, broker, etc.

Participating nodes must:

- Exchange information (messages): RPC, client-server, publish/subscribe, broadcast, streaming, etc.
- Log their behavior understandably: messages, events, actions, etc.

Nodes (or their roles) do not have to be identical
For example, one acts as server, broker, monitor / admin, etc.
Each node must be an independent entity and (partially) autonomous

Detailed descriptions of relevant principles covered in the course (architecture, processes, communication, naming, synchronization, consistency and replication, fault tolerance); irrelevant principles can be left out.

## Built with:

Detailed description of the system functionality and how to run the implementation

- If you are familiar with a particular container technology, feel free to use it (Docker is not mandatory)
- Any programming language can be used, such as: Python, Java, JavaScript, ..
- Any communication protocol / Internet protocol suite can be used: HTTP(S), MQTT, AMQP, CoAP, ..

## Getting Started:

Instructions on setting up your project locally:
**How to Run the Server**

```
$ git clone https://github.com/manhhungking/Rock-paper-scissor.git
$ cd Rock-Paper-Scissors
$ python server.py
```

Open `settings.py` and change the IP to the network IP of the device running the server and change the PORT number to any open port as desired such as `ip = <Your Local Network IP address>` and `port = <CHOSEN PORT NUMBER>`.

**How to Run the Client**

Run infinte instances of the terminal - 2 clients have to open and connected to start a game

```
$ python client.py
```

## Results of the tests:

Detailed description of the system evaluation
Evaluate your implementation using selected criteria, for example:

- Number of messages / lost messages, latencies, ...
- Request processing with different payloads, ..
- System throughput, ..

Design two evaluation scenarios that you compare with each other, for example:

- Small number / large number of messages
- Small payload / big payload

Collect numerical data of test cases:

- Collecting logs of container operations
- Conduct simple analysis for documentation purposes (e.g. plots or graphs)

## Acknowledgments:

We would like to express our gratitude to the following individuals and organizations for their contributions to this project:

- **David Barclay**: For providing the initial implementation and inspiration for the multiplayer Rock-Paper-Scissors game. [GitHub](https://github.com/barclayd/Multiplayer-Rock-Paper-Scissors)
- **GitHub Community**: For their valuable feedback, suggestions, and contributions to the project repository.
- **Stack Overflow**: For providing a wealth of knowledge and resources that helped address technical challenges encountered during the development process.
