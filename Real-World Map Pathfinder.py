# -*- coding: utf-8 -*-
"""
Created on Sun Jan 4 16:40:56 2026

@author: ekans
"""

import tkinter as tk
import heapq
import math
import random

WIDTH, HEIGHT = 700, 500
NODE_RADIUS = 12

nodes = {}
edges = {}
node_count = 0
selected = []
algorithm = "astar"

root = tk.Tk()
root.title("Real-World Map Pathfinder")

# Canvas for map
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid(row=0, column=0)

# Frame for commands
cmd_frame = tk.Frame(root)
cmd_frame.grid(row=0, column=1, sticky="n")

tk.Label(cmd_frame, text="Commands / Controls", font=("Arial", 14, "bold")).pack(pady=10)

commands = [
    "Left Click: Add Node",
    "Right Click (two nodes): Connect Road",
    "R: Random City",
    "D: Set Dijkstra",
    "A: Set A*",
    "Space: Run Algorithm",
    "Start: First Node",
    "Goal: Last Node"
]

for cmd in commands:
    tk.Label(cmd_frame, text=cmd, anchor="w").pack(fill="both")

# Info labels
info_algo = tk.Label(cmd_frame, text="Algorithm: A*", font=("Arial", 12), fg="blue")
info_algo.pack(pady=5)
info_cost = tk.Label(cmd_frame, text="Total Cost: 0", font=("Arial", 12), fg="green")
info_cost.pack(pady=5)
info_explored = tk.Label(cmd_frame, text="Nodes Explored: 0", font=("Arial", 12), fg="orange")
info_explored.pack(pady=5)

def distance(a, b):
    x1, y1 = nodes[a]
    x2, y2 = nodes[b]
    return math.hypot(x2 - x1, y2 - y1)

def draw():
    canvas.delete("all")
    for u in edges:
        for v, w in edges[u].items():
            x1, y1 = nodes[u]
            x2, y2 = nodes[v]
            canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)
            mx, my = (x1+x2)//2, (y1+y2)//2
            canvas.create_text(mx, my, text=str(int(w)), fill="gray")
    for n, (x, y) in nodes.items():
        color = "black"
        if n == list(nodes.keys())[0]:
            color = "red"
        if n == list(nodes.keys())[-1]:
            color = "purple"
        canvas.create_oval(x-NODE_RADIUS, y-NODE_RADIUS, x+NODE_RADIUS, y+NODE_RADIUS, fill=color)
        canvas.create_text(x, y-15, text=n)

def find_node(event):
    """Return node clicked on (if any)"""
    for n, (x, y) in nodes.items():
        if math.hypot(event.x - x, event.y - y) <= NODE_RADIUS:
            return n
    return None

def add_node(event):
    global node_count
    name = chr(65 + node_count)
    nodes[name] = (event.x, event.y)
    edges[name] = {}
    node_count += 1
    draw()

def select_node(event):
    node = find_node(event)
    if not node:
        return
    selected.append(node)
    if len(selected) == 2:
        a, b = selected
        if b not in edges[a]:
            w = distance(a, b)
            edges[a][b] = w
            edges[b][a] = w
        selected.clear()
        draw()

def run_algorithm(start, goal, use_heuristic):
    pq = []
    heapq.heappush(pq, (0, start))
    cost = {start: 0}
    parent = {}
    explored_count = 0

    while pq:
        _, u = heapq.heappop(pq)
        if u == goal:
            break
        explored_count += 1
        ux, uy = nodes[u]
        canvas.create_oval(ux-14, uy-14, ux+14, uy+14, outline="orange", width=3)
        info_explored.config(text=f"Nodes Explored: {explored_count}")
        root.update()

        for v, w in edges[u].items():
            new_cost = cost[u] + w
            if v not in cost or new_cost < cost[v]:
                cost[v] = new_cost
                h = distance(v, goal) if use_heuristic else 0
                heapq.heappush(pq, (new_cost + h, v))
                parent[v] = u

    total = cost.get(goal, 0)
    info_cost.config(text=f"Total Cost: {int(total)}")

    node = goal
    while node != start:
        prev = parent.get(node)
        if not prev:
            break
        x1, y1 = nodes[node]
        x2, y2 = nodes[prev]
        canvas.create_line(x1, y1, x2, y2, fill="green", width=4)
        node = prev
        root.update()

def run(event):
    if len(nodes) < 2:
        return
    start_node = list(nodes.keys())[0]
    goal_node = list(nodes.keys())[-1]
    run_algorithm(start_node, goal_node, algorithm=="astar")

def random_city(event):
    global nodes, edges, node_count
    nodes, edges = {}, {}
    node_count = 0
    for _ in range(7):
        x = random.randint(50, WIDTH-50)
        y = random.randint(50, HEIGHT-50)
        nodes[chr(65+node_count)] = (x, y)
        edges[chr(65+node_count)] = {}
        node_count += 1
    keys = list(nodes.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            if random.random() < 0.4:
                w = distance(keys[i], keys[j])
                edges[keys[i]][keys[j]] = w
                edges[keys[j]][keys[i]] = w
    draw()
    info_explored.config(text="Nodes Explored: 0")
    info_cost.config(text="Total Cost: 0")

def set_dijkstra(event):
    global algorithm
    algorithm = "dijkstra"
    info_algo.config(text="Algorithm: Dijkstra")

def set_astar(event):
    global algorithm
    algorithm = "astar"
    info_algo.config(text="Algorithm: A*")

canvas.bind("<Button-1>", add_node)
canvas.bind("<Button-3>", select_node)
root.bind("<space>", run)
root.bind("r", random_city)
root.bind("d", set_dijkstra)
root.bind("a", set_astar)

draw()
root.mainloop()
