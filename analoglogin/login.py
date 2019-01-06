# -*- coding: utf-8 -*- 

import requests
from bs4 import BeautifulSoup
import re
import time
from .hex2b64 import HB64 
from .RSAJS import RSAKey
import json
import getpass
import sys


class Loginer():

    sessions = requests.Session()
    time = int(time.time())

    def __init__(self, user, passwd):                       
        self.user = str(user)
        self.passwd = str(passwd)
    
    def reflush_time(self):
        self.time = int(time.time())
        
    def get_public(self):                      
        url = 'http://202.119.206.62/jwglxt/xtgl/login_getPublicKey.html?time='+str(self.time)
        r = self.sessions.get(url)
        self.pub = r.json()

    def get_csrftoken(self):                    
        url = 'http://202.119.206.62/jwglxt/xtgl/login_slogin.html?language=zh_CN&_t='+str(self.time)
        r = self.sessions.get(url)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        self.token = soup.find('input', attrs={'id': 'csrftoken'}).attrs['value']

    def process_public(self, str):               
        self.exponent = HB64().b642hex(self.pub['exponent'])   
        self.modulus = HB64().b642hex(self.pub['modulus'])        
        rsa = RSAKey()
        rsa.setPublic(self.modulus, self.exponent)                         
        cry_data = rsa.encrypt(str)
        return HB64().hex2b64(cry_data)

    def post_data(self):                   
        try:
            url = 'http://202.119.206.62/jwglxt/xtgl/login_slogin.html'
            header = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',	
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Connection':'keep-alive',
                'Content-Length':'470',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'202.119.206.62',
                'Referer':'http://202.119.206.62/jwglxt/xtgl/login_slogin.html?language=zh_CN&_t='+str(self.time),
                'Upgrade-Insecure-Requests':'1',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',	
            }
            self.header = header 
            data = {
                'csrftoken': self.token,
                'mm': self.process_public(self.passwd),            
                'mm': self.process_public(self.passwd),            
                'yhm': self.user
            }
            self.req = self.sessions.post(url, headers = header, data = data)
            self.cookie = self.req.request.headers['cookie']
            ppot = r'用户名或密码不正确'
            if re.findall(ppot, self.req.text):
                print('用户名或密码错误,请查验..')
                sys.exit()
        except:
            print('登录失败,请检查网络配置或检查账号密码...')
            sys.exit()

            
class Grades(Loginer):

    def __init__(self, user, passwd, year="none", term="none"):
        super().__init__(user, passwd)
        self.year = year
        self.term = term
        self.url1 = 'http://202.119.206.62/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default&su='+user        
        self.url2 = 'http://202.119.206.62/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005'

    def welcome(self):
        try:
            stu_name = self.req_2['items'][0]['xm']
            sch_stu = self.req_2['items'][0]['xslb']
            institute = self.req_2['items'][0]['jgmc']
            classss = self.req_2['items'][0]['bj']
            print('')
            print('')
            print(stu_name+'同学,欢迎您!!!')
            print('')
            print('姓名:{}\t学历:{}\t\t学院:{}\t班级:{}'.format(stu_name,sch_stu,institute,classss))
            print('')
            time.sleep(1)
        except:
            print('无当前学期,请重试')
    def post_gradedata(self):
        try:
            data = {'_search':'false',
                    'nd':int(time.time()),
                    'queryModel.currentPage':'1',
                    'queryModel.showCount':'15',
                    'queryModel.sortName':'',	
                    'queryModel.sortOrder':'asc',
                    'time':'0',
                    'xnm':self.year,
                    'xqm':self.term
                    }
            req_1 = self.sessions.post(self.url1, data = data, headers = self.header)
            req_2 = self.sessions.post(self.url2, data = data, headers = self.header)
            self.req_2 = req_2.json()
        except:
            print('获取失败,请重试...')
            sys.exit()

    def print_geades(self):
        try:
            plt = '{0:{4}<15}\t{1:{4}<6}\t{2:{4}<6}\t{3:{4}<4}' 
            gk = 0
            zkm = 0
            print('')
            print('--------------------------------------------------------------------------------')
            print(plt.format('课程','成绩','绩点','教师',chr(12288)))
            print('--------------------------------------------------------------------------------')
            for i in self.req_2['items']:
                print(plt.format(i['kcmc'], i['bfzcj'], i['jd'], i['jsxm'], chr(12288)))
                if i['bfzcj'] < 60:
                    gk +=1
                zkm += 1
            print('--------------------------------------------------------------------------------')
            print('')
            print('通过科目数:{}{}'.format(zkm-gk, '门'))
            print('挂科科目数:'+str(gk)+'门')
            print('')
            print('')
        except:
            print('无当前学期,请重试')
if __name__ == '__main__':
    print('')
    print('*************************************************************************************')
    print('                            CUMT成绩查询')
    print('')
    print('')
    print('                                                       ————Made By Eddie_Ivan')
    print('*************************************************************************************')
    user = 1
    passwd = 1
    while type(user)!=str or type(passwd)!=str: 
        user = input('请输入学号:').strip()
        passwd = getpass.getpass('请输入密码(密码不回显,输入完回车即可):') .strip()
    cumt_grades = Grades(str(user), str(passwd))
    cumt_grades.get_public()
    cumt_grades.get_csrftoken()
    cumt_grades.post_data()
    while True:
        year = 1
        term = 1        
        while type(year)!=str or type(term)!=str:
            year = input('请输入查询年份(2016-2017即输入2016):').strip()
            term = input('请输入学期(1或2):').strip()
        if term == '1':
            term = '3'
        elif term == '2':
            term = '12'
        else:
            print('输入有误,请重试...')
            sys.exit()
        cumt_grades.year = year
        cumt_grades.term = term
        cumt_grades.post_gradedata()
        cumt_grades.welcome()
        cumt_grades.print_geades()
        status = input('输入c继续查询,输入e退出程序:')
        if status == 'c':
            continue
        elif status == 'e':
            sys.exit()
        else:
            print('输入有误,退出...')
            sys.exit()

