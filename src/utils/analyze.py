import os


class ANALYZE:
    def __init__(self, path, output, language='all'):
        self.path = path
        self.output = output
        self.language = language
        self.files = {
            'python': []
        }
        self.process_file()

    def run(self):
        if self.language == 'all':
            pass
        else:
            language_list = self.language.split(',')

    def process_file(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                if 'requirements' in file and file.endswith('txt'):
                    self.files['python'].append(file_path)
