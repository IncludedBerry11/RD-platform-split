@echo off
chcp 65001 > nul
echo 确定执行正则替换吗
pause
python glsl_reduce.py
timeout /t 3 /nobreak
pause