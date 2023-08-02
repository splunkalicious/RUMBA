#!/bin/sh

# Loop to run user simulator script for 30 minute intervals
# and tidying up python and chromium process between runs

while true
do
        python3 /opt/bots_load_gen/real_user_simulator.py
        echo "Script has exited, ending remaining python and chromium tasks"
        pkill python3
        pkill chrome
        pkill chromium
        sudo rm -rf /root/.local/share/pyppeteer/.dev_profile/*
        sudo /opt/bots_load_gen/snap_remover.sh
        sudo rm -rf /var/cache/*
        sudo rm -rf /var/log/*
        sudo rm -rf /var/crash/*
        sudo rm -rf /var/tmp/*
        sudo rm -rf /var/adm/*
done