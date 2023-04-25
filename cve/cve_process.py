import os
import json


def year():
    all_cve = {}
    for file in os.listdir(os.path.join('', 'nvd')):
        print(file)
        with open(os.path.join('nvd', file), 'r', encoding='utf8') as f:
            data = json.loads(f.read())
            for i in data['vulnerabilities']:
                cve = i['cve']['id']
                year = cve.split('-')[1]
                if year not in all_cve:
                    all_cve[year] = []
                all_cve[year].append(i)

    for i in all_cve:
        with open(os.path.join('year', 'cve-' + i + '.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(all_cve[i], indent=2, ensure_ascii=False, sort_keys=False))
            print('write file: ' + os.path.join('', 'year', 'cve-' + i + '.json'))



def language():
    all_cve = {}
    language_set = set()
    no_cpe_cve = set()
    vul_type_count = {
        'a': 0,
        'h': 0,
        'o': 0,
        '*': 0
    }
    for file in os.listdir(os.path.join('', 'year')):
        print(file)
        with open(os.path.join('', 'year', file), 'r', encoding='utf8') as f:
            data = json.loads(f.read())
            for i in data:
                try:
                    cpe = i['cve']['configurations'][0]['nodes'][0]['cpeMatch'][0]['criteria']
                    cpe_list = cpe.split(':')
                    vul_type = cpe_list[2]
                    if vul_type == 'a':
                        vul_type_count['a'] += 1
                    elif vul_type == 'h':
                        vul_type_count['h'] += 1
                    elif vul_type == 'o':
                        vul_type_count['o'] += 1
                    elif vul_type == '*':
                        vul_type_count['*'] += 1
                    vendor = cpe_list[3]
                    product = cpe_list[4]
                    version = cpe_list[5]
                    language = cpe_list[8]
                    language_set.add(language)
                    if 'dubbo' in cpe:
                        print(cpe)
                except:
                    no_cpe_cve.add(i['cve']['id'])

    print(language_set)
    print(vul_type_count)

if __name__ == '__main__':
    # year()
    language()

