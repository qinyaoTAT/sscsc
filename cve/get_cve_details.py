
import os
import time
import requests

url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'


class CVE:
    '''
    当前cve来源于NVD
    获取时间：2023/04/14 14:00
    '''
    def __init__(self):
        self.startIndex = 0

    def get_all_cve(self):

        while True:
            req_url = url + '?resultsPerPage=2000&startIndex=' + str(self.startIndex)
            try:
                response = requests.get(req_url)
                if response.status_code == 200:
                    # cve_details = json.loads(response.text)
                    with open(os.path.join('nvd', str(self.startIndex) + '.json'), 'w', encoding='utf-8') as f:
                        f.write(response.text)
                        print("写入文件： " + str(self.startIndex))
            except Exception as e:
                print(req_url)
            self.startIndex += 2000
            time.sleep(6)

    def main(self):
        self.get_all_cve()


if __name__ == '__main__':
    CVE().main()
