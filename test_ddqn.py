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
channel.set_configuration_parameters(time_scale=1.0)
env = UnityToGymWrapper(unity_env)
env = DummyVecEnv([lambda: env])

model = DQN.load(
    "/home/giovanni/Scrivania/mapless_navigation/maze_train/ddqn-turtlebot.zip")

obs = env.reset()

for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    if dones == True:
        obs = env.reset()
env.close()
