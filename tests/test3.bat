@echo off
chcp 65001 > nul
python ../src/main.py rand https://crates.io "" 0.10.3 1 ""
pause