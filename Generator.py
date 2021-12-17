from subprocess import Popen
import base64
import os


class Generator:
    source_file_name = 'binded_source.py'
    source_template_filename = 'source_template.py'
    template = ''

    def __init__(self, files, result_name):
        self.files = files
        self.result_name = result_name

        self.get_source_template()
        self.write_python_file()
        self.get_exe()

    def get_source_template(self):
        template_data = ''

        with open(self.source_template_filename, 'r') as template:
            template_data = template.read()

        self.template = template_data

    def write_python_file(self):
        exes_binaries = ''

        for file_ in self.files:
            with open(file_, 'rb') as file_obj:
                file_data = file_obj.read()
                data_encoded = base64. b64encode(file_data)
                exes_binaries += f'exes.append({data_encoded})\n'

        with open(self.source_file_name, 'w') as source:
            source.write(self.template.replace('#EXES-BINARY#', exes_binaries))

    def get_exe(self):
        command = f'pyinstaller --noconsole --onefile --name {self.result_name} {self.source_file_name}'

        os.system(command)

        print('DONE!')
