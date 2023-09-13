import gymnasium as gym
import PyFlyt.gym_envs
import PyFlyt.gym_envs.quadx_envs.quadx_base_env 
from PyFlyt.gym_envs import FlattenWaypointEnv



env = gym.make("PyFlyt/QuadX-Waypoints-v1", render_mode="human")
metadata = env.metadata
print(metadata)
for i in range(100):
    observation, _ = env.reset()
    observation, reward, _ = env.step(env.action_space.sample())


"""
Citation:

@article{tai2023pyflyt,
  title={PyFlyt--UAV Simulation Environments for Reinforcement Learning Research},
  author={Tai, Jun Jet and Wong, Jim and Innocente, Mauro and Horri, Nadjim and Brusey, James and Phang, Swee King},
  journal={arXiv preprint arXiv:2304.01305},
  year={2023}
}"""