#coding=utf-8
'''
刷DSP广告竞价，出价，展示，点击，loop为次数
'''
import requests
import json,os

class AdwoTest:

    base_url = "http://dsp.adwo.com/AdwoRTBBidder/BidProcesser"

    def request_ads(self):
        ''' 请求成功 '''
        loop = 10
        for i in range(0, loop):
            base_dir = str(os.path.dirname(os.path.dirname(__file__)))
            file_path = base_dir + "/config/request_640100_success.json"
            x = open(file_path, 'r')
            y = x.read()
            f = eval(y)
            f['id'] += str(i)
            f['imp'][0]['id'] += str(i)
            f['imp'][0]['banner']['id'] += str(i)
            f['device']['ext']['idfa'] += str(i)
            f['device']['ext']['udi']['idfa'] += str(i)
            print(json.dumps(f))
            headers = {'Content-Type': 'application/json'}
            r = requests.post(self.base_url, data=json.dumps(f), headers=headers)
            self.result = r.json()



    def request_nurl(self):
        nurl = self.result['seatbid'][0]['bid'][0]['nurl'].split('?')[0]
        data = self.result['seatbid'][0]['bid'][0]['nurl'].split('?')[1]
        r = requests.get(nurl, params=data)


    def request_pm(self):
        nurl = self.result['seatbid'][0]['bid'][0]['ext']['pm'][0].split('?')[0]
        data = self.result['seatbid'][0]['bid'][0]['ext']['pm'][0].split('?')[1]
        r = requests.get(nurl, params=data)


    def request_cm(self):
        self.request_ads()
        self.request_nurl()
        self.request_pm()
        nurl = self.result['seatbid'][0]['bid'][0]['ext']['cm'][0].split('?')[0]
        data = self.result['seatbid'][0]['bid'][0]['ext']['cm'][0].split('?')[1]
        r = requests.get(nurl, params=data)
        print(r)

if __name__ == '__main__':
    AdwoTest().request_cm()


