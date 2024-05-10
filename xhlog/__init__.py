import datetime

def info(log):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\033[94m[" + formatted_time + "]\033[0m\033[92m[INFO]\033[0m" + log)
    with open("./log/"+current_time.strftime("%Y-%m-%d") + '.log', 'a') as f:
        f.write("[" + formatted_time + "][信息/INFO]" + log + "\n")

def warning(log):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\033[94m[" + formatted_time + "]\033[0m\033[91m[WARN]\033[0m" + log)
    with open("./log/"+current_time.strftime("%Y-%m-%d") + '.log', 'a') as f:
        f.write("[" + formatted_time + "][警告/WARN]" + log + "\n")

def error(log,exit=False):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("\033[94m[" + formatted_time + "]\033[0m\033[31m[ERROR]\033[0m" + log)
    with open("./log/"+current_time.strftime("%Y-%m-%d") + '.log', 'a') as f:
        f.write("[" + formatted_time + "][错误/ERROR]" + log + "\n")
    if exit==True:
        exit(1)
    else:
        pass