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

The project aims to design and implement a distributed system used for a multiplayer Rock, Paper, Scissors game. The software and system architecture aim to address key distributed system functionalities learned throughout the course. The main goal of this project is to effectively tackle the fundamental functionalities inherent in distributed systems, drawing upon the comprehensive knowledge acquired throughout the duration of the course. The application clients acting as game nodes, a central server managing game state and communication, and the ability of server replication based on the load request and game conditions.

### Project Objectives

- Design and implement a distributed system for a multiplayer Rock, Paper, Scissors game.
- Implement a straightforward method for clients to establish real-time connections with the server in a straightforward manner.
- Develop a simple resource naming mechanism and sharing mechanisms to manage game state and communication.
- Create a basic load balancing mechanism for the server node through replication.
- Modify a somewhat centralized organizational software architecture to facilitate vertical communication between the server and the clients.

### Expected Outcomes

- A simple functional multiplayer Rock, Paper, Scissors game accessible to players from different locations.
- Real-time gameplay experience with immediate feedback on match results.
- Efficient resource utilization and scalability through load balancing mechanisms.
- Demonstrated application of distributed system principles in building responsive and scalable gaming applications.
- Building a robust foundation for a game that is scalable and can be further expanded upon in the future.

## Implemented components:

  The system is structured around a Centralized logical organization, characterized by vertical communication between the server and clients. It supports multiple server and client nodes, enabling scalability. The system can have as many server nodes as it needs and as many client nodes as possible. Due to this nature, a replication mechanism aimed for load balancing was implemented, which will be discussed in detail later.

Each node functions either as a server or a client out of two clients that initiate a game, with two clients required to initiate a game.
Each connected server and client operates as a somewhat independent entity with partial autonomy. However, given the game's requirements for full engagement among all nodes involved in a game, the failure of one node results in the failure of the entire system, or instance of the game.

  In this client-server architecture project, nodes communicate by exchanging messages facilitated by the network, which is implemented as an object of itself within the system.
The client sends a variety of messages such as hard-reset, soft-reset, find-winner, and the chosen move itself, via the network interface to the server. The server then receives and processes these messages based on the data they contain.

Also, a simlpe straightforward logging process is incorporated, where the server monitors newly connected clients and any instances of server replication. The server logs these operations information in a clear and easily comprehensible way.

Relevant principles covered in the course:
- Message transmission between nodes via a clearly defined interface, ensuring strong familiarity with application semantics between clients and the server. Additionally, continuous communication is maintained between nodes through socket interfaces.
- Implementation of replication to enhance availability, particularly when accommodating a large number of players, and to effectively manage load balancing. Despite the simplicity of the program, it serves as an implementation of the replication concept itself.
- The system architecture follows a Centralized Logical Organization with a vertical structure, where clients adhere to a request/reply model. Newly generated servers, stemming from replication, adopt a concurrent multithreaded server approach. Initially, there exists a single entry server to the application, which then spawns server instances based on the number of connecting clients.
- A straightforward structured naming mechanism is also established, assigning each client a unique and non-repetitive name regardless of their connection to the server. This structured naming convention adopts the format: game_id/client_id_within_game. This simplicity in naming aims to support the project's goal of serving as a foundational building stone for future scalability, extensibility, and feature integration.

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

list resources you find helpful
