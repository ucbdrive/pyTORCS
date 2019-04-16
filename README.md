## PyTORCS
Python interface for [The Open Racing Car Simulator (TORCS)](http://torcs.org/)

### Configure graphics driver (Important!)
1. Go to "Software & Updates" in Ubuntu 16.04 system settings, check "source code" in "Ubuntu Software" tab. 
2. Download [NVIDIA-Linux-x86_64-415.25.run](http://us.download.nvidia.com/XFree86/Linux-x86_64/415.25/NVIDIA-Linux-x86_64-415.25.run)
(for other versions, visit [NVIDIA's official website](https://www.nvidia.com/Download/index.aspx?lang=en-us)).
3. Blacklist Nouveau.
    ```bash
    sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nouveau.conf"
    sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nouveau.conf"
    sudo update-initramfs -u
    sudo reboot
    ```
4. Install graphics driver with `--no-opengl-files` flag.
    ```bash
    sudo chmod a+x NVIDIA-Linux-x86_64-415.25.run
    sudo service lightdm stop
    sudo bash NVIDIA-Linux-x86_64-415.25.run --no-opengl-files
    ```

### Install TORCS and PyTORCS
Note that in order to install torcs on your computer system, you may need to 
install CUDA driver without opengl libs. The gym-TORCS environment
has only been tested on Ubuntu 16.04 environment, and currently it does not
support windows or macOSX environment. 

```bash
git clone https://github.com/ucbdrive/pyTORCS
bash install.sh
```

### Usage of PyTORCS
```python
import numpy as np
import gym
import py_TORCS

env = gym.make('TORCS-v0')
obs, info = env.reset()
obs, reward, terminal, info = env.step(np.array([1.0, 0.0]))
```

Have fun!
