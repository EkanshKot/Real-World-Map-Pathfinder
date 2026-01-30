# Real-World-Map-Pathfinder
Hi Guys Now this is a basic pathfinder i built like 20 days ago I am excited to post it here 


This is an interactive project I built to visualize how computers can find the shortest path on a real-world map. You can create nodes (intersections), connect them with weighted edges (roads), generate random cities, and watch two algorithms—**Dijkstra** and **A\***—explore and find the shortest path in real-time.

I built this to understand how navigation systems like GPS work and to see algorithms thinkst ep by step after reading a X thread about Nav system fundamentals.
This is like a very Basic rendation and most of my time infact went towrds the Ui

 Here are the features of this code

- Interactive Map Creation
  - Left click to add intersections (nodes)
  - Right click on two nodes to connect them with roads
- **Random City Generator**
  - Automatically creates nodes and random connections
- **Algorithm Toggle**
  - Compare **Dijkstra** and **A*** visually
- **Live Visualization**
  - Orange: explored nodes  
  - Green: final shortest path  
  - Shows total path cost and number of nodes explored
- **Command Panel**
  - All controls displayed on the side for easy reference

## Controls

| Action | Control |
|--------|---------|
| Add Node | Left Click |
| Connect Nodes | Right Click on two nodes sequentially |
| Random City | R key |
| Set Dijkstra | D key |
| Set A* | A key |
| Run Algorithm | Space key |
| Start Node | First node added |
| Goal Node | Last node added |

## How It Works

The map is treated as a **graph**, where nodes are intersections and edges are roads with distances (weights). When the algorithm runs, it explores nodes step by step:

- **Dijkstra** explores all possible paths systematically  
- **A\*** uses a heuristic (Euclidean distance to the goal) to explore smarter  

The visualization highlights the exploration process and the final shortest path, while live metrics show how many nodes were explored and the total path cost. This gives an intuitive sense of **algorithm efficiency** in real-time.

---

## Fundamental Principles

This project is grounded in a few core CS concepts:

- **Graph Theory**: Representing a city as nodes and edges to model paths  
- **Shortest Path Algorithms**: Understanding how Dijkstra and A* find optimal routes  
- **Heuristics**: How A* uses a simple “distance-to-goal” estimate to explore more efficiently  
- **Priority Queues**: Using heaps to select the next node to explore efficiently  
- **Visualization & UX**: How showing the process step by step helps understand abstract algorithms  

---

## What I Learned

Working on this project initially started as to get to know abt nav systems but i also learnt more as i continued it such as:

- How abstract algorithms like **Dijkstra** and **A\*** connect to real-world problems like GPS navigation  
- How heuristics can drastically improve efficiency without compromising correctness  
- How priority queues and careful data structures can make algorithms run faster  
- How visualization can make complex processes tangible and easier to understand
- While running it intially i understood how users would face dificulty in understanding the controlos and operations so i added the controls in the output module only




## Tech Stack(Reddit told me its Good habit to add this also)

- Python 3  
- Tkinter (GUI visualization)  
- Standard libraries: `heapq`, `math`, `random`

- These were the three projects i had ready i also have a roullete whell simulator ready which i built like a year ago and a very very basic blackjack simulator i might post it after some time (like a day)thank you

