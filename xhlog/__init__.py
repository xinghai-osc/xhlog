import datetime

def info(message):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\033[94m[" + formatted_time + "]\033[0m\033[92m[INFO]\033[0m" + message)
    with open("./log/"+current_time.strftime("%Y-%m-%d") + '.log', 'a', encoding='utf-8') as f:
        f.write("[" + formatted_time + "][信息/INFO]" + message + "\n")

def warning(message):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\033[94m[" + formatted_time + "]\033[0m\033[91m[WARN]\033[0m" + message)
    with open("./log/"+current_time.strftime("%Y-%m-%d") + '.log', 'a', encoding='utf-8') as f:
        f.write("[" + formatted_time + "][警告/WARN]" + message + "\n")

def error(message,exit=False):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\033[94m[" + formatted_time + "]\033[0m\033[31m[ERROR]\033[0m" + message)
    with open("./log/"+current_time.strftime("%Y-%m-%d") + '.log', 'a') as f:
        f.write("[" + formatted_time + "][错误/ERROR]" + message + "\n")
    if exit==True:
        exit(1)
    else:
        pass