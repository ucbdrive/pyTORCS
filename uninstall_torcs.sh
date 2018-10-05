#!/bin/bash
sudo rm -rf /usr/local/share/games/torcs
sudo rm -rf /usr/local/lib/torcs
sudo apt-get remove --auto-remove torcs
sudo apt-get purge --auto-remove torcs
