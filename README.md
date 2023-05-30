
# Shortest Path Algorithm using Dijkstra's Algorithm

This project implements a shortest path algorithm using Dijkstra's algorithm to find the best shortest path in a graph. The code is written in Python and consists of two modules: Grafo.py and main.py.

## Librosa API      

Grafo.py
The Grafo module contains the implementation of a graph and its related components:

## Vertice Class
Represents each vertex/node in the graph.
Stores information such as ID, adjacent vertices, distance, visited status, and previous node.
Provides methods to manage and retrieve information about the vertex.

## Grafo Class
Represents the graph with its vertices/nodes.
Contains methods to add vertices, add edges with weights, retrieve vertices, and draw the graph.

## shortest_path Function
Recursive function that returns the shortest path based on the destination vertex.

## BSP Function
Implements the Best Shortest Path algorithm using Dijkstra's algorithm.
Calculates the shortest path from a given origin vertex to all other vertices in the graph.

## main.py

The 'main.py' file demonstrates the usage of the Grafo module by creating a graph, adding vertices and edges, drawing the graph, and finding the shortest path between two specified vertices.

To run the program, execute main.py and follow the prompts to input the origin and destination vertices.


## Graph Map

![Graph Map](https://raw.githubusercontent.com/georgedevcode/Graph-Algorithm/main/grafo/Graph.JPG)


## Authors

- [@Jorge Cerdas Valverde](https://www.linkedin.com/in/jorgecerdas/)

