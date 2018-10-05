import gym
import py_TORCS
import time
import numpy as np
import cv2

def naive_driver(info, continuous=False):
    if info['angle'] > 0.2 or (info['trackPos'] < -2 and info['angle'] > 0):
        return np.array([0.5, 1]) if continuous else 0
    elif info['angle'] < -0.2 or (info['trackPos'] > 2 and info['angle'] < 0):
        return np.array([0.5, -1]) if continuous else 2
    return np.array([0.5, 0]) if continuous else 1

def draw_from_pred(seg):
    illustration = np.zeros(seg.shape + (3,), dtype=np.uint8)
    illustration[:, :, 0] = 255
    illustration[seg == 1] = np.array([0, 255, 0])
    illustration[seg == 2] = np.array([0, 0, 0])
    illustration[seg == 3] = np.array([0, 0, 255])
    return illustration

if __name__ == '__main__':
    game_config = '/home/cxy/pyTORCS/py_TORCS/py_TORCS/game_config/michigan.xml'
    env1 = gym.make('TORCS-v0')#torcs_envs(num = 1, game_config=game_config, isServer = 0, continuous=False, resize=False)
    env1.init(game_config=game_config, isServer=0, continuous=False, resize=False)
    obs1 = env1.reset()
    # video = cv2.VideoWriter("right.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 20.0, (640, 480), True)

    # with open('actions0.txt', 'r') as f:
    #     actions = eval(f.readlines()[0])
    # for i in range(len(actions)):
    #     obs1, reward1, done1, info1 = env1.step(actions[i])
    #     print(info1['pos'])
    #     time.sleep(0.01)
    #     if i > 220:
    #     	break

    for i in range(20):
        if i < 200:
            action = naive_driver(env1.get_info())
        else:
            action = int(input())
        obs1, reward1, done1, info1 = env1.step(action)
        # seg1 = draw_from_pred(env1.get_segmentation())
        # cv2.imwrite('observation.png', cv2.cvtColor(obs1, cv2.COLOR_BGR2RGB))
        # cv2.imwrite('segmentation.png', cv2.cvtColor(seg1, cv2.COLOR_BGR2RGB))
        time.sleep(0.01)
        # input()
        # video.write(cv2.cvtColor(obs1, cv2.COLOR_BGR2RGB))

    # actions = [2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
    # for action in actions:
    #     obs1, reward1, done1, info1 = env1.step(action)
    #     time.sleep(0.01)
    #     video.write(cv2.cvtColor(obs1, cv2.COLOR_BGR2RGB))

    # actions = []
    # for i in range(230):
    #     action = naive_driver(env1.get_info())
    #     actions.append(action)
    #     obs1, reward1, done1, info1 = env1.step(action)
    #     print(info1['pos'], info1['trackPos'])
    #     time.sleep(0.01)
    # for i in range(100):
    #     action = int(input())
    #     if action < 0:
    #         break
    #     actions.append(action)
    #     obs1, reward1, done1, info1 = env1.step(action)
    #     print(info1['trackPos'])
    #     time.sleep(0.01)
    # with open('actions.txt', 'w') as f:
    #     f.write(str(actions))
    # imsave('choice.png', obs1)

    # video.release()
    env1.close()
