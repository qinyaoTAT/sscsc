import argparse


def arg_parse():

    parser = argparse.ArgumentParser(description='ssvc')
    parser.add_argument('-p', '--path', dest='path', default='example', help='input dir path or zip path')
    parser.add_argument("-o", '--output', dest='output', help="specify the output directory.", default='output')
    parser.add_argument("-l", '--language', dest='language', help="specify languages: such as '-l java,js,python' or '-l java'", default='all')
    parser.add_argument("-v", '--version', help="show version.")

    return parser.parse_args()
