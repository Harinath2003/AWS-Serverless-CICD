#!/bin/bash
echo "Running BeforeInstall hook..."
sudo systemctl stop myapp.service || true
