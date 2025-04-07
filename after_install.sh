#!/bin/bash
echo "Running AfterInstall hook..."
cd /home/ec2-user/my-app
pip3 install -r requirements.txt
