# Discrete Deep Reinforcemente Learning for Mapless Navigation

## Introduction

Mapless Navigation is a key challenge in mobile robotics.  
In this project we focus our attention on navigation in narrow spaces.  
Specifically we invegaste whether an agent is able to navigate in a room with narrow corridors, like Maze could be. 
Thus we created an environment in Unity, and trained an agent using Double Deep Q Learning. 
Then we compared the result with the ROS navigation stack, which first needs to create the map using SLAM. 
We discovered that an agent trained with DDQN is able to navigate in narrow spaces better than the ROS navigation stack in terms on best path, and time to navigate to the goal.  
However in some cases the AI agent was not able to get to the goal. This behaviour never occured with ROS. 
We believ that training for even more epoches could improve edge cases. 

## Unity environment 
We created a Maze in unity, to train our turtlebot. 
Below the picture of the environment is available. 

<img src="img/Figure1.png" width="200" alt="Representation of the unity environment, goal behind the wall, narrow passage required">

## Training and testing. 

We tried two different approaches. 
First we tried to train a network with a fixed goal on a specific position. 
The agent was able to navigate optimally, thus,  following the best path to go the goal, Figure 2. 
But as soon as a new goal was given as input, the agent was able to get to it only if the goal was not behind a wall, Figure 3. 
Otherwise it was not able to navigate to the goal as it hitted the wall. 
This shows how the agent learned that it's job was navigating to the goal following the shortest path, but it did not learn how to overcome the wall, except for the case that he had been trained, when the goal was behind the wall. 
Therefore we trained the network using another approach. In our second experiment, the goal can be positoned in 5 different locations, Figure 4. 
We choose those places as if the robot is able to navigate to those locations, then it should also be able to navigate to other goals around the map. 

| <p align="center">Figure 2</p>          |     <p align="center">Figure 3</p>      |          <p align="center">Figure 4</p> |
| --------------------------------------- | :-------------------------------------: | --------------------------------------: |
| <img src="img/Figure2.png" width="200" alt="Unity enviroment, first experiment"> | <img src="img/Figure3.png" width="200" alt="Unity enviroment, second test with goal not behind the wall"> | <img src="img/Figure4.png" width="200" alt="Unity enviroment, train with five different goals around the map"> |

## Results 

Figure 5 shows the reward as time step increases of approach 1. 
Figure 6 shows the successfull rate as time step increases of approach 1. 
Figure 7 shows the reward as time step increases of approach 2.
Figure 8 shows the successfull rate as time step increases of approach 2.

As the pictures shows, it is clear how the agent is learning to navigate to the goal, in both approaches. 

## Gazebo environment 

We created the Maze environment in gazebo. 
Figure 9 show the envinroment. 
In order to test the navigation using the turtlebot navigation stack, a SLAM process is required first. 
Therefore, we first built the map using gmapping SLAM, and the teleoperation package to move the turtlebot in the environment. 
Secondly, in order to use the navigation, RVIz has been started. 
An inital estimation of where the turtlebot is, is required.
Then, the goal can be set and the navigation stack find the best path to the goal, using  two planner, a local planner used to avoid obstacles, and a global planner used to calculate the best path. 
Picture 10 shows the best path. 

## Navigation stack result 

In some cases, the navigation stack fails to go to the goal on first trial. 
Infact the navigation stack is not confident in passing trough narrow spaces as the AI agent is. 
The navigation stack infact, tends to prefer a worst path in terms of legth to avoid turning too close to the wall and passing in narrow passages.
Figure 11 shows the passages in which the navigation stack fails to follow the best path. 
However, we found out that the navigation stack always reach the goal, even though not in the optimal way. 
On the other hand, the AI agent, is not able to go trough a narrow passage that the navigation stack prefers, and fails to navigate to the goal, when it is set close after the narrow passage considered. 
Figure 12, shows when the where the goal is when the AI agent fails to get to it. 
We are confident that, if the network was trained more the AI agent could navigate better in those spaces. 


