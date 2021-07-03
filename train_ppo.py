from gym_unity.envs import UnityToGymWrapper
from mlagents_envs.side_channel.engine_configuration_channel import EngineConfigurationChannel
from mlagents_envs.environment import UnityEnvironment

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2, DQN
from stable_baselines.common import make_vec_env

import tensorflow as tf

channel = EngineConfigurationChannel()
unity_env = UnityEnvironment(file_name=None, side_channels=[channel])
channel.set_configuration_parameters(time_scale=1000.0)
env = UnityToGymWrapper(unity_env)
env = DummyVecEnv([lambda: env])

model = PPO2(MlpPolicy,
            env,
            verbose=1,
            tensorboard_log="./ppo2_maze_tensorboard/")
model.learn(total_timesteps=1_000_000)
model.save("ppo2-turtlebot-maze")
