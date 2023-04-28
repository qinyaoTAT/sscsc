import os

from src.java.maven import analyzer as maven_analyzer
from src.utils.common import serch_vlun, gen_report


class ANALYZE:
    def __init__(self, path, output, language='all'):
        self.path = path
        self.output = output
        self.language = language
        self.files = {
            'python': [],
            'java': {
                'maven': [],
                'gradle': []
            }
        }
        self.process_file()

    def run(self):
        all_dependency = {}
        if self.language == 'all':
            maven_analyzer.run(self.files['java']['maven'])
        else:
            language_list = self.language.split(',')
        if all_dependency:
            serch_vlun(all_dependency)



    def process_file(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                if 'requirements' in file and file.endswith('txt'):
                    self.files['python'].append(file_path)
                elif 'pom.xml' in file:
                    self.files['java']['maven'].append(file_path)
