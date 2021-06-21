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

[!Unity training environment](./img/unity_env.png)

## Training and testing. 

We tried two different approaches. 
First we tried to train a network with a fixed goal on a specific position. 
The agent was able to navigate optimally, thus,  following the best path to go the goal, Figure 2. 
But as soon as a new goal was given as input, the agent was able to get to it only if the goal was not behind a wall, Figure 3. 
Otherwise it was not able to navigate to the goal as it hitted the wall. 
This shows how the agent learned that it's job was navigating to the goal following the shortest path, but it did not learn how to overcome the wall, except for the case that he had been trained, when the goal was behind the wall. 
Therefore we trained the network using another approach. In our second experiment, the goal can be positoned in 5 different locations, Figure 4. 
We choose those places as if the robot is able to navigate to those locations, then it should also be able to navigate to other goals. 

## Results 

Figure 5 shows the reward as time step increases of approach 1. 
Figure 6 shows the successfull rate as time step increases of approach 1. 
Figure 7 shows the reward as time step increases of approach 2.
Figure 8 shows the successfull rate as time step increases of approach 2.

