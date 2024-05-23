import datetime
import os

log_dir = "./log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

current_time = datetime.datetime.now()
log_name = "./log/"+current_time.strftime("%Y-%m-%d") + '.log'

def info(message):
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\033[94m[" + formatted_time + "]\033[0m\033[92m[INFO]\033[0m" + message)
    with open(log_name, 'a', encoding='utf-8') as f:
        f.write("[" + formatted_time + "][信息/INFO]" + message + "\n")

def warning(message):
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\033[94m[" + formatted_time + "]\033[0m\033[91m[WARN]\033[0m" + message)
    with open(log_name, 'a', encoding='utf-8') as f:
        f.write("[" + formatted_time + "][警告/WARN]" + message + "\n")

def error(message,exit=False):
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\033[94m[" + formatted_time + "]\033[0m\033[31m[ERROR]\033[0m" + message)
    with open(log_name, 'a', encoding='utf-8') as f:
        f.write("[" + formatted_time + "][错误/ERROR]" + message + "\n")
    if exit==True:
        exit(1)
    else:
        pass