import logging
import os

from src.utils import args
from src.utils import analyze

logging.basicConfig(format="%(asctime)s | %(levelname)s | %(message)s", level=logging.INFO)
VERSION = '1.0.0'


class SSCSC:
    def __init__(self):
        self.path = args.arg_parse().path
        self.output = args.arg_parse().output
        self.language = args.arg_parse().language
        if not os.path.exists(self.path):
            logging.error('please specify the correct scan path!!!')
            exit(-1)
        if not os.path.exists(self.output):
            logging.error('please specify the correct output directory!!!')
            exit(-1)

    def run(self):
        analyze.ANALYZE(self.path, self.output, self.language).run()


if __name__ == '__main__':
    SSCSC().run()
