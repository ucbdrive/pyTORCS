## pyTORCS

### Installation
Note that in order to install torcs on your computer system, you may need to 
install CUDA driver without opengl libs. The gym-TORCS environment
has only been tested on Ubuntu 16.04 environment, and currently it does not
support windows or macOSX environment. 

```bash
https://github.com/ucbdrive/pyTORCS
sh install.sh
```

### Usage
```python
import numpy as np
import gym
import py_TORCS

env = gym.make('TORCS-v0')
obs, info = env.reset()
obs, reward, terminal, info = env.step(np.array([1.0, 0.0]))
```

Have fun!
