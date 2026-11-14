@echo off
chcp 65001 > nul
python ../src/main.py base64 https://crates.io "" 0.23.1 1 ""
pause