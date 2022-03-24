


import numpy as np
import gym 
env = gym.make("Pendulum-v1")



class RandomPolicy:
    
    def __init__(self,env):
        self._max_action = self._action_space_low = env.action_space.low
        
        self._action_space_high = env.action_space.high
        
        self.policy_name = "RandomPolicy"
        
    def get_action(self, state):
        return np.random.uniform(
        low = -self._max_action , 
        high = self._max_action
        )



policy = RandomPolicy(env)

number_episodes = 4
number_moves = 100

for i in range (number_episodes):
    state = env.reset()
    done= False
    game_rew =0
    
    for j in range(number_moves):
        action = policy.get_action(state) ##random action
        next_state, rew, done, info = env.step(action)
        
        state = next_state
        game_rew += rew
        env.render()
        
        if done:
            print("Done")
            break
            
    print('Episode %d finished, reward:%d, the length of the episode:%d'% (i, game_rew, j))
    
env.close()

