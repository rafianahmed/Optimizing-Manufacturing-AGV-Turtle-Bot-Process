# Robotics Final Project: Optimizing Manufacturing Process at ISYSE (KAIST)

## Overview
This project optimizes a simulated manufacturing workflow for **Product Z** (an automotive panel component) using a **mobile robot** that autonomously navigates between production stations. The robot completes the full process for **five (5) Product Z units**, provides real-time execution feedback, and generates key manufacturing performance metrics to identify bottlenecks and improvement opportunities.

---

## Project Scope
- Orchestrate an end-to-end manufacturing flow: **raw material → Part A/Part B processes → Product Z → delivery**
- Model the shop-floor layout and station locations
- Enable autonomous navigation between stations with ROS navigation tooling
- Log events and calculate production KPIs for system-level analysis

---

## Key Objectives
### 1) Efficient Operation
- Program robot motion to manufacture **5 units** of Product Z
- Ensure smooth transitions between stations
- Provide real-time feedback (robot position/state)

### 2) Performance Metrics & Bottleneck Analysis
Computed and reported:
- **Average Cycle Time** (Part A)
- **Average Cycle Time** (Part B)
- **Average Cycle Time** (Product Z)
- **Throughput Rate** (per station/machine)
- **Work In Progress (WIP)**
- **Total Completion Time** (makespan)
- **Machine Utilization**
- **Bottleneck identification** + targeted improvement suggestions

### 3) Documentation & Presentation
- Comprehensive work report (process + results)
- Demonstration video of the automated manufacturing run
- 10-minute presentation covering methodology, implementation, and outcomes

---

## System Workflow
1. Robot starts at a home/initial location
2. Navigates to station(s) for Part A production
3. Navigates to station(s) for Part B production
4. Navigates to assembly/processing station for Product Z
5. Delivers finished Product Z to final delivery/drop-off area
6. Repeats until **5 Product Z** units are completed

---

## Tech Stack
### Robotics / Middleware
- **ROS (Robot Operating System)**

### Navigation & Motion Planning
- **move_base** (action library for goal-based navigation)
- ROS Navigation Stack (localization + global/local planning)

### Mapping / Layout
- Shop-floor mapping (ROS-compatible map)
- Station coordinates / navigation goals

### Programming
- ROS nodes and scripts to:
  - send navigation goals
  - control station-to-station logic
  - log timestamps/events
  - compute performance metrics  
*(commonly implemented in Python and/or C++ depending on the course setup)*

### Data & Metrics
- Cycle time, throughput, WIP, utilization calculations based on logged events

---

## Results (What This Project Demonstrates)
- Autonomous robotic transport across a multi-stage manufacturing line
- Repeatable production execution for a fixed batch size (5 units)
- Quantitative KPIs for evaluating efficiency and identifying bottlenecks
- Practical application of robotics + data analysis to manufacturing optimization

---

## Future Improvements
- Dynamic scheduling based on queue length / WIP
- Adaptive routing to reduce congestion and idle time
- Multi-robot coordination for higher throughput
- Live KPI dashboard (real-time monitoring)

---

## Repository Structure (Suggested)
> Update this section to match your actual repo folders.

```bash
.
├── src/                  # ROS packages / nodes
├── launch/               # launch files to run simulation/system
├── config/               # navigation params, station coordinates
├── maps/                 # shop-floor maps
├── scripts/              # logging + KPI computation scripts
├── report/               # final report
└── media/                # demo video / screenshots
