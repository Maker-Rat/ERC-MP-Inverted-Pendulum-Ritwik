import gym
import time

env_name = 'CartPole-v1'
env = gym.make(env_name)

'''
r = reference (pole angle = 0)
x = state (current pole angle)
Kp = p factor
Ki = i factor
Kd = d factor
a = input to system (control variable)
e = error
e_sum = summation of errors
old_e = stores last error
cmd = final command (discrete 0 or 1)
'''

r = 0
Kp = 0.01
Ki = 0.00001
Kd = 0.075
e_sum = 0
old_e = 0


def command(cur_state):
    global e_sum, old_e
    x = cur_state[2]
    e = r - x
    e_sum += e
    rate_of_e = (e - old_e)
    a = (e * Kp) + (e_sum * Ki) + (rate_of_e * Kd)
    # print(a)
    old_e = e

    if a <= 0:
        return 1
    else:
        return 0


# print(env.observation_space)
state = env.reset()
old_e = r - state[2]
command(state)


points = 0.0

while True:
    action = command(state)
    state, reward, done, info = env.step(action)
    env.render()
    # time.sleep(0.08)

    if done:
        break
    else:
        points += reward

print(f"You scored {points} points!!")
