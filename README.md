Overview

This project simulates and optimizes a small-scale manufacturing line for “Product Z” (an automotive panel component) using a mobile robot that autonomously navigates between production stations. The robot transports parts across machines, completes the workflow for five (5) Product Z units, and reports real-time status during execution.

Using ROS and autonomous navigation, we modeled the shop-floor layout, planned routes between stations, and measured production performance to identify inefficiencies and bottlenecks.

Problem Statement

Traditional manufacturing flow for Product Z involved unnecessary movement, idle time between stations, and limited visibility into performance. The goal was to redesign the process with robotics automation to improve throughput and provide measurable operational insights.

System Workflow (Manufacturing Process)

End-to-end process:

Raw material processing

Part A & Part B production (station-based)

Assembly/processing into Product Z

Final delivery/drop-off

Repeat until 5 finished units are produced

The robot autonomously traveled between stations, ensuring consistent transport behavior and reducing manual handoffs.

Key Features

Autonomous Navigation: robot moves station-to-station using ROS navigation tools

Execution for 5 Units: completes the full manufacturing loop for five Product Z units

Real-Time Feedback: live updates on robot position/state while running

Factory Metrics & Bottleneck Detection: computed operational KPIs to evaluate system performance

Deliverables: full work report, demo video, and a 10-minute presentation

Performance Metrics (Measured & Reported)

Average Cycle Time — Part A

Average Cycle Time — Part B

Average Cycle Time — Product Z

Throughput Rate — per machine/station

Work In Progress (WIP)

Total Completion Time (makespan)

Machine Utilization

Bottleneck station identification + improvement suggestions

Tech Stack
Robotics / Middleware

ROS (Robot Operating System)

Navigation & Motion

move_base (action library) for goal-based navigation

ROS navigation stack (localization + path planning)

Mapping / Environment

Shop-floor layout mapping and navigation configuration (ROS-compatible map + station coordinates)

Programming

ROS nodes/scripts to control robot behavior and synchronize stage transitions
(language depends on your implementation: typically Python or C++)

Analysis & Reporting

Production metrics computation (cycle time, throughput, WIP, utilization)

Documentation + presentation + demo video

How It Works (High-Level)

Map & configure the shop floor (stations, routes, navigation parameters)

Send navigation goals to the robot (station A → station B → …)

Trigger manufacturing steps at each station (simulated or timed operations)

Log timestamps and events for every step

Compute KPIs and identify bottlenecks based on observed performance

Results & Impact

This project demonstrated how mobile robotics can:

improve workflow consistency,

reduce operator transport overhead,

increase visibility through production KPIs,

and support decisions on where to optimize (bottleneck-driven improvements).

Future Improvements

Dynamic scheduling (prioritize stations based on queue/WIP)

Multi-robot coordination for higher throughput

Smarter bottleneck mitigation (adaptive routing, load balancing)

Real-time dashboard for live KPI tracking
