import gym
import random
import numpy as np

class Agent():
    def __init__(self, env):
        self.is_discrete_action = type(env.action_space) == gym.spaces.discrete.Discrete
        self.is_multibinary_action = type(env.action_space) == gym.spaces.multi_binary.MultiBinary
        # checking action space is dicrete or not
        if self.is_discrete_action or self.is_multibinary_action:
            self.action_size = env.action_space.n
            print("Action size:", self.action_size)
        else:
            self.action_low = env.action_space.low
            self.action_high = env.action_space.high
            self.action_shape = env.action_space.shape
            print("Action range:", self.action_low, self.action_high)
        
    def getAction(self, state):
        # returning random action
        if self.is_discrete_action or self.is_multibinary_action:
            action = random.choice(range(self.action_size))
        else:
            action = np.random.uniform(self.action_low,
                                       self.action_high,
                                       self.action_shape)
        return action