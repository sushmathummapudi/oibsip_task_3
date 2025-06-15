Chat Application (Client-Server Model)
Developed as part of internship at Oasis Infobyte

Project Overview
This is a Python-based Chat Application that allows multiple users to communicate in real-time over a network. The project was developed as part of my Python Development Internship at Oasis Infobyte. It implements socket programming with multithreading to handle multiple users simultaneously.

The application consists of two parts:

Server Program: Listens for client connections, manages nicknames, and broadcasts messages.

Client Program: Allows individual users to connect, set their nickname, send, and receive messages.

Features
Real-time messaging with multiple clients

Unique nickname selection for each user

Broadcast messages to all connected clients

Handles client disconnections gracefully

Uses multithreading to support multiple users at the same time

How It Works
Start the Server: Listens on a specified port for incoming client connections.

Client Connects: User enters a nickname, connects to the server, and joins the chat.

Chat Functionality: Messages are sent by each client and broadcast to all others.

Graceful Exit: If a client disconnects, the server notifies others.

Technologies Used
Python

Socket Programming

Multithreading

Learning Outcome
Gained practical knowledge of network communication in Python

Learned to build client-server applications using sockets

Applied multithreading to manage multiple concurrent users
