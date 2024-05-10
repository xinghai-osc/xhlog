import datetime
import os

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
file_path = "./log/" + current_time.strftime("%Y-%m-%d") + '.log'

# 检查并创建目录
log_dir = "./log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def info(message):
    print("\033[94m[" + formatted_time + "]\033[0m\033[92m[INFO]\033[0m" + message)
    with open(file_path, 'a') as f:
        f.write("[" + formatted_time + "][信息/INFO]" + message + "\n")

def warning(message):
    # 修改这里，将 WARN 设为黄色
    print("\033[94m[" + formatted_time + "]\033[0m\033[93m[WARN]\033[0m" + message)
    with open(file_path, 'a') as f:
        f.write("[" + formatted_time + "][警告/WARN]" + message + "\n")

def error(message, exit_bool=False):
    # 修改这里，将 ERROR 设为亮红色
    print("\033[94m[" + formatted_time + "]\033[0m\033[91m[ERROR]\033[0m" + message)
    with open(file_path, 'a') as f:
        f.write("[" + formatted_time + "][错误/ERROR]" + message + "\n")
    if exit_bool == True:
        exit(0)
    else:
        pass

if __name__ == "__main__":
    info("测试信息")
    warning("测试警告")
    error("测试错误", exit_bool=True)