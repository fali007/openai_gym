import gym
env = gym.make('CartPole-v0')
print(env.action_space)
print(env.observation_space)
# obs bounds given by
print(env.observation_space.high)
print(env.observation_space.low)

from gym import spaces

space=spaces.Discrete(5)
for i in range(100):
    x=space.sample()
    print(x,end=',')