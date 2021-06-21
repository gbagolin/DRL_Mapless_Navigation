from gym_unity.envs import UnityToGymWrapper
from mlagents_envs.side_channel.engine_configuration_channel import EngineConfigurationChannel
from mlagents_envs.environment import UnityEnvironment

# from stable_baselines.common.policies import MlpPolicy
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2, DQN
from stable_baselines.common import make_vec_env

import tensorflow as tf

channel = EngineConfigurationChannel()
unity_env = UnityEnvironment(file_name=None, side_channels=[channel])
channel.set_configuration_parameters(time_scale=100.0)
env = UnityToGymWrapper(unity_env)
env = DummyVecEnv([lambda: env])

model = DQN.load(
    "maze_train/ddqn-turtlebot.zip",
    tensorboard_log="tensorboard/dqn_turtblebot_tensorboard/DQN_1")

model.set_env(env)

model.learn(total_timesteps=500_000)
model.save("ddqn-turtlebot")
