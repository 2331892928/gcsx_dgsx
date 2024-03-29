import datetime
import json
import random
import time
import traceback

import requests

#########---------------------默认第一个实习计划，不可更改#######
#  为保证cookie存活，请设置cron表达式为 0 1/1 * * * *  也就是每一分钟一次，本脚本会自动判断时间，早上8点签到，晚上4点日报
#  cookie,具体查看https://github.com/2331892928/gcsx_dgsx
TOKEN = ""
#  实习完整区域：城市+区+街道+具体地址
internshipLocation = "重庆市重庆市江津区科教北路"

# 实习计划课程号
course_no = 0
#  实习城市
city = "重庆市"
#  日报内容
dai_reportContent = "进行大数据技能大赛备赛,及准备4月1日的专升本"
# 周报内容
weeklyReportContent = "进行大数据技能大赛备赛，顺便进行专升本考试的准备，两手准备。虽然专升本准备因为比赛拖延到至今，但我相信只要自己努力，肯定能考个200~250分"
# 月报内容
monthlyReportContent = "进行大数据技能大赛备赛，顺便进行专升本考试的准备，两手准备。虽然专升本准备因为比赛拖延到至今，但我相信只要自己努力，肯定能考个200~250分"


#########---------------------#######

class User_Agent:
    def __init__(self):
        self.user_agent = {
            "browsers": {
                "chrome": [
                    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
                    "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
                    "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
                    "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
                    "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
                    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
                    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"
                ],
                "opera": [
                    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
                    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
                    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
                    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
                    "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
                    "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
                    "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
                    "Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00",
                    "Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0",
                    "Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
                    "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62",
                    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
                    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52",
                    "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51",
                    "Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50",
                    "Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50",
                    "Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11",
                    "Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11",
                    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11",
                    "Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10",
                    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10",
                    "Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10",
                    "Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1",
                    "Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01",
                    "Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
                    "Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
                    "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
                    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01",
                    "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
                    "Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00",
                    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00",
                    "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00",
                    "Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00",
                    "Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.7.62 Version/11.00",
                    "Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00",
                    "Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00",
                    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00"
                ],
                "firefox": [
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
                    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
                    "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
                    "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
                    "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
                    "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
                    "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
                    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
                    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
                    "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0",
                    "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0",
                    "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0",
                    "Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0",
                    "Mozilla/5.0 (Microsoft Windows NT 6.2.9200.0); rv:22.0) Gecko/20130405 Firefox/22.0",
                    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1",
                    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1",
                    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:21.0.0) Gecko/20121011 Firefox/21.0.0",
                    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0",
                    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0",
                    "Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20130514 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.2; rv:21.0) Gecko/20130326 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130401 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130330 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101 Firefox/21.0",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0",
                    "Mozilla/5.0 (Windows NT 6.2; Win64; x64;) Gecko/20100101 Firefox/20.0",
                    "Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0",
                    "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/19.0",
                    "Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/18.0.1",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0)  Gecko/20100101 Firefox/18.0",
                    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6"
                ],
                "internetexplorer": [
                    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
                    "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko",
                    "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
                    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)",
                    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
                    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
                    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
                    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
                    "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
                    "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)",
                    "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
                    "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)",
                    "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
                    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)",
                    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)",
                    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)",
                    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)",
                    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
                    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)",
                    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8",
                    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)",
                    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)",
                    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
                    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)"
                ],
                "safari": [
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
                    "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
                    "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ko-KR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; fr-FR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; sv-se) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ko-kr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-fr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; es-es) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-gb) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; de-de) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.0; hu-HU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/534.16+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-ch) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; ar) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
                    "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
                    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
                    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5"
                ]
            },
            "randomize": {
                "0": "chrome",
                "1": "chrome",
                "2": "chrome",
                "3": "chrome",
                "4": "chrome",
                "5": "chrome",
                "6": "chrome",
                "7": "chrome",
                "8": "chrome",
                "9": "chrome",
                "10": "chrome",
                "11": "chrome",
                "12": "chrome",
                "13": "chrome",
                "14": "chrome",
                "15": "chrome",
                "16": "chrome",
                "17": "chrome",
                "18": "chrome",
                "19": "chrome",
                "20": "chrome",
                "21": "chrome",
                "22": "chrome",
                "23": "chrome",
                "24": "chrome",
                "25": "chrome",
                "26": "chrome",
                "27": "chrome",
                "28": "chrome",
                "29": "chrome",
                "30": "chrome",
                "31": "chrome",
                "32": "chrome",
                "33": "chrome",
                "34": "chrome",
                "35": "chrome",
                "36": "chrome",
                "37": "chrome",
                "38": "chrome",
                "39": "chrome",
                "40": "chrome",
                "41": "chrome",
                "42": "chrome",
                "43": "chrome",
                "44": "chrome",
                "45": "chrome",
                "46": "chrome",
                "47": "chrome",
                "48": "chrome",
                "49": "chrome",
                "50": "chrome",
                "51": "chrome",
                "52": "chrome",
                "53": "chrome",
                "54": "chrome",
                "55": "chrome",
                "56": "chrome",
                "57": "chrome",
                "58": "chrome",
                "59": "chrome",
                "60": "chrome",
                "61": "chrome",
                "62": "chrome",
                "63": "chrome",
                "64": "chrome",
                "65": "chrome",
                "66": "chrome",
                "67": "chrome",
                "68": "chrome",
                "69": "chrome",
                "70": "chrome",
                "71": "chrome",
                "72": "chrome",
                "73": "chrome",
                "74": "chrome",
                "75": "chrome",
                "76": "chrome",
                "77": "chrome",
                "78": "chrome",
                "79": "chrome",
                "80": "chrome",
                "81": "chrome",
                "82": "chrome",
                "83": "chrome",
                "84": "chrome",
                "85": "chrome",
                "86": "chrome",
                "87": "chrome",
                "88": "chrome",
                "89": "chrome",
                "90": "chrome",
                "91": "chrome",
                "92": "chrome",
                "93": "chrome",
                "94": "chrome",
                "95": "chrome",
                "96": "chrome",
                "97": "chrome",
                "98": "chrome",
                "99": "chrome",
                "100": "chrome",
                "101": "chrome",
                "102": "chrome",
                "103": "chrome",
                "104": "chrome",
                "105": "chrome",
                "106": "chrome",
                "107": "chrome",
                "108": "chrome",
                "109": "chrome",
                "110": "chrome",
                "111": "chrome",
                "112": "chrome",
                "113": "chrome",
                "114": "chrome",
                "115": "chrome",
                "116": "chrome",
                "117": "chrome",
                "118": "chrome",
                "119": "chrome",
                "120": "chrome",
                "121": "chrome",
                "122": "chrome",
                "123": "chrome",
                "124": "chrome",
                "125": "chrome",
                "126": "chrome",
                "127": "chrome",
                "128": "chrome",
                "129": "chrome",
                "130": "chrome",
                "131": "chrome",
                "132": "chrome",
                "133": "chrome",
                "134": "chrome",
                "135": "chrome",
                "136": "chrome",
                "137": "chrome",
                "138": "chrome",
                "139": "chrome",
                "140": "chrome",
                "141": "chrome",
                "142": "chrome",
                "143": "chrome",
                "144": "chrome",
                "145": "chrome",
                "146": "chrome",
                "147": "chrome",
                "148": "chrome",
                "149": "chrome",
                "150": "chrome",
                "151": "chrome",
                "152": "chrome",
                "153": "chrome",
                "154": "chrome",
                "155": "chrome",
                "156": "chrome",
                "157": "chrome",
                "158": "chrome",
                "159": "chrome",
                "160": "chrome",
                "161": "chrome",
                "162": "chrome",
                "163": "chrome",
                "164": "chrome",
                "165": "chrome",
                "166": "chrome",
                "167": "chrome",
                "168": "chrome",
                "169": "chrome",
                "170": "chrome",
                "171": "chrome",
                "172": "chrome",
                "173": "chrome",
                "174": "chrome",
                "175": "chrome",
                "176": "chrome",
                "177": "chrome",
                "178": "chrome",
                "179": "chrome",
                "180": "chrome",
                "181": "chrome",
                "182": "chrome",
                "183": "chrome",
                "184": "chrome",
                "185": "chrome",
                "186": "chrome",
                "187": "chrome",
                "188": "chrome",
                "189": "chrome",
                "190": "chrome",
                "191": "chrome",
                "192": "chrome",
                "193": "chrome",
                "194": "chrome",
                "195": "chrome",
                "196": "chrome",
                "197": "chrome",
                "198": "chrome",
                "199": "chrome",
                "200": "chrome",
                "201": "chrome",
                "202": "chrome",
                "203": "chrome",
                "204": "chrome",
                "205": "chrome",
                "206": "chrome",
                "207": "chrome",
                "208": "chrome",
                "209": "chrome",
                "210": "chrome",
                "211": "chrome",
                "212": "chrome",
                "213": "chrome",
                "214": "chrome",
                "215": "chrome",
                "216": "chrome",
                "217": "chrome",
                "218": "chrome",
                "219": "chrome",
                "220": "chrome",
                "221": "chrome",
                "222": "chrome",
                "223": "chrome",
                "224": "chrome",
                "225": "chrome",
                "226": "chrome",
                "227": "chrome",
                "228": "chrome",
                "229": "chrome",
                "230": "chrome",
                "231": "chrome",
                "232": "chrome",
                "233": "chrome",
                "234": "chrome",
                "235": "chrome",
                "236": "chrome",
                "237": "chrome",
                "238": "chrome",
                "239": "chrome",
                "240": "chrome",
                "241": "chrome",
                "242": "chrome",
                "243": "chrome",
                "244": "chrome",
                "245": "chrome",
                "246": "chrome",
                "247": "chrome",
                "248": "chrome",
                "249": "chrome",
                "250": "chrome",
                "251": "chrome",
                "252": "chrome",
                "253": "chrome",
                "254": "chrome",
                "255": "chrome",
                "256": "chrome",
                "257": "chrome",
                "258": "chrome",
                "259": "chrome",
                "260": "chrome",
                "261": "chrome",
                "262": "chrome",
                "263": "chrome",
                "264": "chrome",
                "265": "chrome",
                "266": "chrome",
                "267": "chrome",
                "268": "chrome",
                "269": "chrome",
                "270": "chrome",
                "271": "chrome",
                "272": "chrome",
                "273": "chrome",
                "274": "chrome",
                "275": "chrome",
                "276": "chrome",
                "277": "chrome",
                "278": "chrome",
                "279": "chrome",
                "280": "chrome",
                "281": "chrome",
                "282": "chrome",
                "283": "chrome",
                "284": "chrome",
                "285": "chrome",
                "286": "chrome",
                "287": "chrome",
                "288": "chrome",
                "289": "chrome",
                "290": "chrome",
                "291": "chrome",
                "292": "chrome",
                "293": "chrome",
                "294": "chrome",
                "295": "chrome",
                "296": "chrome",
                "297": "chrome",
                "298": "chrome",
                "299": "chrome",
                "300": "chrome",
                "301": "chrome",
                "302": "chrome",
                "303": "chrome",
                "304": "chrome",
                "305": "chrome",
                "306": "chrome",
                "307": "chrome",
                "308": "chrome",
                "309": "chrome",
                "310": "chrome",
                "311": "chrome",
                "312": "chrome",
                "313": "chrome",
                "314": "chrome",
                "315": "chrome",
                "316": "chrome",
                "317": "chrome",
                "318": "chrome",
                "319": "chrome",
                "320": "chrome",
                "321": "chrome",
                "322": "chrome",
                "323": "chrome",
                "324": "chrome",
                "325": "chrome",
                "326": "chrome",
                "327": "chrome",
                "328": "chrome",
                "329": "chrome",
                "330": "chrome",
                "331": "chrome",
                "332": "chrome",
                "333": "chrome",
                "334": "chrome",
                "335": "chrome",
                "336": "chrome",
                "337": "chrome",
                "338": "chrome",
                "339": "chrome",
                "340": "chrome",
                "341": "chrome",
                "342": "chrome",
                "343": "chrome",
                "344": "chrome",
                "345": "chrome",
                "346": "chrome",
                "347": "chrome",
                "348": "chrome",
                "349": "chrome",
                "350": "chrome",
                "351": "chrome",
                "352": "chrome",
                "353": "chrome",
                "354": "chrome",
                "355": "chrome",
                "356": "chrome",
                "357": "chrome",
                "358": "chrome",
                "359": "chrome",
                "360": "chrome",
                "361": "chrome",
                "362": "chrome",
                "363": "chrome",
                "364": "chrome",
                "365": "chrome",
                "366": "chrome",
                "367": "chrome",
                "368": "chrome",
                "369": "chrome",
                "370": "chrome",
                "371": "chrome",
                "372": "chrome",
                "373": "chrome",
                "374": "chrome",
                "375": "chrome",
                "376": "chrome",
                "377": "chrome",
                "378": "chrome",
                "379": "chrome",
                "380": "chrome",
                "381": "chrome",
                "382": "chrome",
                "383": "chrome",
                "384": "chrome",
                "385": "chrome",
                "386": "chrome",
                "387": "chrome",
                "388": "chrome",
                "389": "chrome",
                "390": "chrome",
                "391": "chrome",
                "392": "chrome",
                "393": "chrome",
                "394": "chrome",
                "395": "chrome",
                "396": "chrome",
                "397": "chrome",
                "398": "chrome",
                "399": "chrome",
                "400": "chrome",
                "401": "chrome",
                "402": "chrome",
                "403": "chrome",
                "404": "chrome",
                "405": "chrome",
                "406": "chrome",
                "407": "chrome",
                "408": "chrome",
                "409": "chrome",
                "410": "chrome",
                "411": "chrome",
                "412": "chrome",
                "413": "chrome",
                "414": "chrome",
                "415": "chrome",
                "416": "chrome",
                "417": "chrome",
                "418": "chrome",
                "419": "chrome",
                "420": "chrome",
                "421": "chrome",
                "422": "chrome",
                "423": "chrome",
                "424": "chrome",
                "425": "chrome",
                "426": "chrome",
                "427": "chrome",
                "428": "chrome",
                "429": "chrome",
                "430": "chrome",
                "431": "chrome",
                "432": "chrome",
                "433": "chrome",
                "434": "chrome",
                "435": "chrome",
                "436": "chrome",
                "437": "chrome",
                "438": "chrome",
                "439": "chrome",
                "440": "chrome",
                "441": "chrome",
                "442": "chrome",
                "443": "chrome",
                "444": "chrome",
                "445": "chrome",
                "446": "chrome",
                "447": "chrome",
                "448": "chrome",
                "449": "chrome",
                "450": "chrome",
                "451": "chrome",
                "452": "chrome",
                "453": "chrome",
                "454": "chrome",
                "455": "chrome",
                "456": "chrome",
                "457": "chrome",
                "458": "chrome",
                "459": "chrome",
                "460": "chrome",
                "461": "chrome",
                "462": "chrome",
                "463": "chrome",
                "464": "chrome",
                "465": "chrome",
                "466": "chrome",
                "467": "chrome",
                "468": "chrome",
                "469": "chrome",
                "470": "chrome",
                "471": "chrome",
                "472": "chrome",
                "473": "chrome",
                "474": "chrome",
                "475": "chrome",
                "476": "chrome",
                "477": "chrome",
                "478": "chrome",
                "479": "chrome",
                "480": "chrome",
                "481": "chrome",
                "482": "chrome",
                "483": "chrome",
                "484": "chrome",
                "485": "chrome",
                "486": "chrome",
                "487": "chrome",
                "488": "chrome",
                "489": "chrome",
                "490": "chrome",
                "491": "chrome",
                "492": "chrome",
                "493": "chrome",
                "494": "chrome",
                "495": "chrome",
                "496": "chrome",
                "497": "chrome",
                "498": "chrome",
                "499": "chrome",
                "500": "chrome",
                "501": "chrome",
                "502": "chrome",
                "503": "chrome",
                "504": "chrome",
                "505": "chrome",
                "506": "chrome",
                "507": "chrome",
                "508": "chrome",
                "509": "chrome",
                "510": "chrome",
                "511": "chrome",
                "512": "chrome",
                "513": "chrome",
                "514": "chrome",
                "515": "chrome",
                "516": "chrome",
                "517": "chrome",
                "518": "chrome",
                "519": "chrome",
                "520": "chrome",
                "521": "chrome",
                "522": "chrome",
                "523": "chrome",
                "524": "chrome",
                "525": "chrome",
                "526": "chrome",
                "527": "chrome",
                "528": "chrome",
                "529": "chrome",
                "530": "chrome",
                "531": "chrome",
                "532": "chrome",
                "533": "chrome",
                "534": "chrome",
                "535": "chrome",
                "536": "chrome",
                "537": "chrome",
                "538": "chrome",
                "539": "chrome",
                "540": "chrome",
                "541": "chrome",
                "542": "chrome",
                "543": "chrome",
                "544": "chrome",
                "545": "chrome",
                "546": "chrome",
                "547": "chrome",
                "548": "chrome",
                "549": "chrome",
                "550": "chrome",
                "551": "chrome",
                "552": "chrome",
                "553": "chrome",
                "554": "chrome",
                "555": "chrome",
                "556": "chrome",
                "557": "chrome",
                "558": "chrome",
                "559": "chrome",
                "560": "chrome",
                "561": "chrome",
                "562": "chrome",
                "563": "chrome",
                "564": "chrome",
                "565": "chrome",
                "566": "chrome",
                "567": "chrome",
                "568": "chrome",
                "569": "chrome",
                "570": "chrome",
                "571": "chrome",
                "572": "chrome",
                "573": "chrome",
                "574": "chrome",
                "575": "chrome",
                "576": "chrome",
                "577": "chrome",
                "578": "chrome",
                "579": "chrome",
                "580": "chrome",
                "581": "chrome",
                "582": "chrome",
                "583": "chrome",
                "584": "chrome",
                "585": "chrome",
                "586": "chrome",
                "587": "chrome",
                "588": "chrome",
                "589": "chrome",
                "590": "chrome",
                "591": "chrome",
                "592": "chrome",
                "593": "chrome",
                "594": "chrome",
                "595": "chrome",
                "596": "chrome",
                "597": "chrome",
                "598": "chrome",
                "599": "chrome",
                "600": "chrome",
                "601": "chrome",
                "602": "chrome",
                "603": "chrome",
                "604": "chrome",
                "605": "chrome",
                "606": "chrome",
                "607": "chrome",
                "608": "chrome",
                "609": "chrome",
                "610": "chrome",
                "611": "chrome",
                "612": "chrome",
                "613": "chrome",
                "614": "chrome",
                "615": "chrome",
                "616": "chrome",
                "617": "chrome",
                "618": "chrome",
                "619": "chrome",
                "620": "chrome",
                "621": "chrome",
                "622": "chrome",
                "623": "chrome",
                "624": "chrome",
                "625": "chrome",
                "626": "chrome",
                "627": "chrome",
                "628": "chrome",
                "629": "chrome",
                "630": "chrome",
                "631": "chrome",
                "632": "chrome",
                "633": "chrome",
                "634": "chrome",
                "635": "chrome",
                "636": "chrome",
                "637": "chrome",
                "638": "chrome",
                "639": "chrome",
                "640": "chrome",
                "641": "chrome",
                "642": "chrome",
                "643": "chrome",
                "644": "chrome",
                "645": "chrome",
                "646": "chrome",
                "647": "chrome",
                "648": "chrome",
                "649": "chrome",
                "650": "chrome",
                "651": "chrome",
                "652": "chrome",
                "653": "chrome",
                "654": "chrome",
                "655": "chrome",
                "656": "chrome",
                "657": "chrome",
                "658": "chrome",
                "659": "chrome",
                "660": "chrome",
                "661": "chrome",
                "662": "chrome",
                "663": "chrome",
                "664": "chrome",
                "665": "chrome",
                "666": "chrome",
                "667": "chrome",
                "668": "chrome",
                "669": "chrome",
                "670": "chrome",
                "671": "chrome",
                "672": "chrome",
                "673": "chrome",
                "674": "chrome",
                "675": "chrome",
                "676": "chrome",
                "677": "chrome",
                "678": "chrome",
                "679": "chrome",
                "680": "chrome",
                "681": "chrome",
                "682": "chrome",
                "683": "chrome",
                "684": "chrome",
                "685": "chrome",
                "686": "chrome",
                "687": "chrome",
                "688": "chrome",
                "689": "chrome",
                "690": "chrome",
                "691": "chrome",
                "692": "chrome",
                "693": "chrome",
                "694": "chrome",
                "695": "chrome",
                "696": "chrome",
                "697": "chrome",
                "698": "chrome",
                "699": "chrome",
                "700": "chrome",
                "701": "chrome",
                "702": "chrome",
                "703": "chrome",
                "704": "chrome",
                "705": "chrome",
                "706": "chrome",
                "707": "chrome",
                "708": "chrome",
                "709": "chrome",
                "710": "chrome",
                "711": "chrome",
                "712": "chrome",
                "713": "chrome",
                "714": "chrome",
                "715": "chrome",
                "716": "chrome",
                "717": "chrome",
                "718": "chrome",
                "719": "chrome",
                "720": "chrome",
                "721": "chrome",
                "722": "chrome",
                "723": "chrome",
                "724": "chrome",
                "725": "chrome",
                "726": "chrome",
                "727": "chrome",
                "728": "chrome",
                "729": "chrome",
                "730": "chrome",
                "731": "chrome",
                "732": "chrome",
                "733": "chrome",
                "734": "chrome",
                "735": "chrome",
                "736": "chrome",
                "737": "chrome",
                "738": "chrome",
                "739": "chrome",
                "740": "chrome",
                "741": "chrome",
                "742": "chrome",
                "743": "chrome",
                "744": "chrome",
                "745": "chrome",
                "746": "chrome",
                "747": "chrome",
                "748": "chrome",
                "749": "chrome",
                "750": "chrome",
                "751": "chrome",
                "752": "chrome",
                "753": "chrome",
                "754": "chrome",
                "755": "chrome",
                "756": "chrome",
                "757": "chrome",
                "758": "chrome",
                "759": "chrome",
                "760": "chrome",
                "761": "chrome",
                "762": "chrome",
                "763": "chrome",
                "764": "chrome",
                "765": "chrome",
                "766": "chrome",
                "767": "chrome",
                "768": "chrome",
                "769": "chrome",
                "770": "chrome",
                "771": "chrome",
                "772": "internetexplorer",
                "773": "internetexplorer",
                "774": "internetexplorer",
                "775": "internetexplorer",
                "776": "internetexplorer",
                "777": "internetexplorer",
                "778": "internetexplorer",
                "779": "internetexplorer",
                "780": "internetexplorer",
                "781": "internetexplorer",
                "782": "internetexplorer",
                "783": "internetexplorer",
                "784": "internetexplorer",
                "785": "internetexplorer",
                "786": "internetexplorer",
                "787": "internetexplorer",
                "788": "internetexplorer",
                "789": "internetexplorer",
                "790": "internetexplorer",
                "791": "internetexplorer",
                "792": "internetexplorer",
                "793": "internetexplorer",
                "794": "internetexplorer",
                "795": "internetexplorer",
                "796": "internetexplorer",
                "797": "internetexplorer",
                "798": "internetexplorer",
                "799": "internetexplorer",
                "800": "internetexplorer",
                "801": "internetexplorer",
                "802": "internetexplorer",
                "803": "internetexplorer",
                "804": "internetexplorer",
                "805": "internetexplorer",
                "806": "internetexplorer",
                "807": "internetexplorer",
                "808": "internetexplorer",
                "809": "internetexplorer",
                "810": "internetexplorer",
                "811": "internetexplorer",
                "812": "internetexplorer",
                "813": "firefox",
                "814": "firefox",
                "815": "firefox",
                "816": "firefox",
                "817": "firefox",
                "818": "firefox",
                "819": "firefox",
                "820": "firefox",
                "821": "firefox",
                "822": "firefox",
                "823": "firefox",
                "824": "firefox",
                "825": "firefox",
                "826": "firefox",
                "827": "firefox",
                "828": "firefox",
                "829": "firefox",
                "830": "firefox",
                "831": "firefox",
                "832": "firefox",
                "833": "firefox",
                "834": "firefox",
                "835": "firefox",
                "836": "firefox",
                "837": "firefox",
                "838": "firefox",
                "839": "firefox",
                "840": "firefox",
                "841": "firefox",
                "842": "firefox",
                "843": "firefox",
                "844": "firefox",
                "845": "firefox",
                "846": "firefox",
                "847": "firefox",
                "848": "firefox",
                "849": "firefox",
                "850": "firefox",
                "851": "firefox",
                "852": "firefox",
                "853": "firefox",
                "854": "firefox",
                "855": "firefox",
                "856": "firefox",
                "857": "firefox",
                "858": "firefox",
                "859": "firefox",
                "860": "firefox",
                "861": "firefox",
                "862": "firefox",
                "863": "firefox",
                "864": "firefox",
                "865": "firefox",
                "866": "firefox",
                "867": "firefox",
                "868": "firefox",
                "869": "firefox",
                "870": "firefox",
                "871": "firefox",
                "872": "firefox",
                "873": "firefox",
                "874": "firefox",
                "875": "firefox",
                "876": "firefox",
                "877": "firefox",
                "878": "firefox",
                "879": "firefox",
                "880": "firefox",
                "881": "firefox",
                "882": "firefox",
                "883": "firefox",
                "884": "firefox",
                "885": "firefox",
                "886": "firefox",
                "887": "firefox",
                "888": "firefox",
                "889": "firefox",
                "890": "firefox",
                "891": "firefox",
                "892": "firefox",
                "893": "firefox",
                "894": "firefox",
                "895": "firefox",
                "896": "firefox",
                "897": "firefox",
                "898": "firefox",
                "899": "firefox",
                "900": "firefox",
                "901": "firefox",
                "902": "firefox",
                "903": "firefox",
                "904": "firefox",
                "905": "firefox",
                "906": "firefox",
                "907": "firefox",
                "908": "firefox",
                "909": "firefox",
                "910": "firefox",
                "911": "firefox",
                "912": "firefox",
                "913": "firefox",
                "914": "firefox",
                "915": "firefox",
                "916": "firefox",
                "917": "firefox",
                "918": "firefox",
                "919": "firefox",
                "920": "firefox",
                "921": "firefox",
                "922": "firefox",
                "923": "firefox",
                "924": "firefox",
                "925": "firefox",
                "926": "firefox",
                "927": "firefox",
                "928": "firefox",
                "929": "firefox",
                "930": "firefox",
                "931": "firefox",
                "932": "firefox",
                "933": "firefox",
                "934": "firefox",
                "935": "firefox",
                "936": "firefox",
                "937": "safari",
                "938": "safari",
                "939": "safari",
                "940": "safari",
                "941": "safari",
                "942": "safari",
                "943": "safari",
                "944": "safari",
                "945": "safari",
                "946": "safari",
                "947": "safari",
                "948": "safari",
                "949": "safari",
                "950": "safari",
                "951": "safari",
                "952": "safari",
                "953": "safari",
                "954": "safari",
                "955": "safari",
                "956": "safari",
                "957": "safari",
                "958": "safari",
                "959": "safari",
                "960": "safari",
                "961": "safari",
                "962": "safari",
                "963": "safari",
                "964": "safari",
                "965": "safari",
                "966": "safari",
                "967": "safari",
                "968": "safari",
                "969": "opera",
                "970": "opera",
                "971": "opera",
                "972": "opera",
                "973": "opera",
                "974": "opera",
                "975": "opera",
                "976": "opera",
                "977": "opera",
                "978": "opera",
                "979": "opera",
                "980": "opera",
                "981": "opera",
                "982": "opera",
                "983": "opera",
                "984": "opera"
            }
        }

    def random(self):
        a = str(random.randint(0, 984))
        b = self.user_agent['randomize'][a]
        c = random.randint(0, len(self.user_agent["browsers"][b]) - 1)
        return self.user_agent["browsers"][b][c]

    def chrome(self):
        a = str(random.randint(0, 771))
        b = self.user_agent['randomize'][a]
        c = random.randint(0, len(self.user_agent["browsers"][b]))
        return self.user_agent["browsers"][b][c]

    def internetexplorer(self):
        a = str(random.randint(772, 812))
        b = self.user_agent['randomize'][a]
        c = random.randint(0, len(self.user_agent["browsers"][b]))
        return self.user_agent["browsers"][b][c]

    def firfox(self):
        a = str(random.randint(813, 936))
        b = self.user_agent['randomize'][a]
        c = random.randint(0, len(self.user_agent["browsers"][b]))
        return self.user_agent["browsers"][b][c]

    def safari(self):
        a = str(random.randint(937, 968))
        b = self.user_agent['randomize'][a]
        c = random.randint(0, len(self.user_agent["browsers"][b]))
        return self.user_agent["browsers"][b][c]

    def opera(self):
        a = str(random.randint(969, 984))
        b = self.user_agent['randomize'][a]
        c = random.randint(0, len(self.user_agent["browsers"][b]))
        return self.user_agent["browsers"][b][c]


class Gcsx:
    def __init__(self):
        ua = User_Agent()
        user_agent = ua.random()
        #  从2022年12月更新(可能，日志太多看不过来) cookie保活失效，改保活数字校园cookie，从数字校园跳转登陆到实习系统
        #  获取
        res = requests.get(
            # "http://ai.cqvie.edu.cn/ump/officeHall/getApplicationUrl?universityId=102574&appKey=pc-officeHall&timestamp={}&clientCategory=PC&applicationCode=HR0g30274".format(int(round(time.time()*1000))),
            "http://ai.cqvie.edu.cn/ump/officeHall/getApplicationUrl?appKey=mobileplatform&appVersion=5.3.04&applicationCode=HR0g30274&clientCategory=IOS&equipmentId=BF10F120-1894-442C-A110-F21FB273AED1&equipmentName=iPhone11&equipmentVersion=16.2&nonce=1676887542046OADFSHBWPQWWK&sign=5D27B0B10DA12FA635FC53DD03971645&timestamp={}&universityId=102574&userType=STUDENT".format(int(round(time.time()*1000))),
            cookies={
                # "ump_token_pc-officeHall": TOKEN,
                # "_yh_sys_ticket": TOKEN,
                # "_yh_sys_token": TOKEN,
                "token": TOKEN,
            }, headers={
                "User-Agent": user_agent,
                "token": TOKEN
            })
        try:

            self.redirectUrl = res.json()['content']['redirectUrl']
            self.ticket = res.json()['content']['ticket']
        except:
            print(res.content.decode())
            traceback.print_exc()

        self.headers = {
            "Referer": "https://dgsx.cqvie.edu.cn/mobile/index",
            "Origin": "https://dgsx.cqvie.edu.cn/",
            "Host": "dgsx.cqvie.edu.cn",
            "Content-Type": "application/json;charset=UTF-8",
            # "Accept": "application/json, text/plain, */*",
            "User-Agent": user_agent,
            "Authorization": "Bearer " + ""
        }
        self.cookie = {
            "sidebarStatus": "0",
            "wxSignUrl": "https://dgsx.cqvie.edu.cn/mobile/",
            "Admin-Token": "",
            "muyun_sign_javascript": ""
        }
        self.x = None
        self.y = None
        self.sign_href = "https://dgsx.cqvie.edu.cn/prod-api/internship_pending/signrecord"
        self.sign_list_href = "https://dgsx.cqvie.edu.cn/prod-api/internship_pending/signrecord/list_all"
        self.dai_href = "https://dgsx.cqvie.edu.cn/prod-api/internship_pending/dailyrecord"
        self.dai_list_href = "https://dgsx.cqvie.edu.cn/prod-api/internship_pending/dailyrecord/list"
        self.week_href = "https://dgsx.cqvie.edu.cn/prod-api/baseinfo/week/student_list"
        self.week_list_href = "https://dgsx.cqvie.edu.cn/prod-api/internship_pending/weekrecord/list"
        self.week_post_href = "https://dgsx.cqvie.edu.cn/prod-api/internship_pending/weekrecord"
        self.month_href = "https://dgsx.cqvie.edu.cn/prod-api/internship_before/month/list_all"
        self.month_post_href = "https://dgsx.cqvie.edu.cn/prod-api/internship_pending/monthrecord"
        self.get_gref = "https://dgsx.cqvie.edu.cn/prod-api/internship_pending/distribution/student_list"
        self.jwd()
        #  动态获取cookie
        #  2022年11月25日 更新了muyun验证cookie，只要是能在浏览器看到的，请求头，返回头，请求对象，返回对象，会话，都可以程序获取
        s = requests.Session()
        # r = s.get("https://dgsx.cqvie.edu.cn/index", headers=self.headers, cookies=self.cookie)  旧，采用手动填ADMIN-TOKEN
        #  新，采用数字校园token
        r = s.get(self.redirectUrl, headers={
            "Host": "dgsx.cqvie.edu.cn",
            "User-Agent": user_agent
        })
        #  得到 muyun_sign_cookie从请求头获取，这里没看到返回头setcookie，是加了跳转，前端设置的cookie
        self.cookie.update(s.cookies.get_dict())
        #  获取muyun_sign_javascript,从前端获取
        self.cookie['muyun_sign_javascript'] = self.take_middle_text(r.content.decode(), "'cookie' : \"", '",')

        cookie2 = {
            "muyun_sign_javascript":self.take_middle_text(r.content.decode(), "'cookie' : \"", '",')
        }
        s.get(self.redirectUrl,headers={
            "Host": "dgsx.cqvie.edu.cn",
            "User-Agent": user_agent
        },cookies=cookie2)
        self.cookie.update({
            "Admin-Token":s.cookies.get_dict()['Admin-Token']
        })
        self.headers.update({
            "Authorization": "Bearer " + s.cookies.get_dict()['Admin-Token']
        })




    def jwd(self):
        jwdhref = "https://api.map.baidu.com/geocoder?address={}&output=json&key=E4805d16520de693a3fe707cdc962045&city={}".format(
            internshipLocation, city)
        # 获取经纬度
        while True:
            try:
                s = requests.Session()
                res = s.get(jwdhref, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"})
                res_str = res.content.decode()
                res_json = json.loads(res_str)
                if res_json['status'] != "OK":
                    self.x = None
                    self.y = None
                    print("获取经纬度坐标错误，请联系作者或查看更新1")
                self.x = res_json["result"]["location"]["lng"]
                self.y = res_json["result"]["location"]["lat"]
                print("获取经纬度坐标成功")
                break
            except:
                # print(traceback.format_exc())
                self.x = None
                self.y = None
                time.sleep(1)
                print("获取经纬度坐标错误，重试中...")
                #  循环五次获取经纬度

    def get_student(self):
        distributionId = None
        internshipPlanId = None
        internshipPlanStartDate = None
        res = requests.get(self.get_gref, headers=self.headers, cookies=self.cookie)
        # print(res.cookies.get("muyun_sign_javascript"))
        for i in res.json()["data"]:
            if str(i['internshipPlanName']).find(str(course_no)) != -1:
                distributionId = i['distributionId']
                internshipPlanId = i['internshipPlanId']
                internshipPlanStartDate = i['internshipPlanStartDate']
        if distributionId is None:
            print("课程号不正确")
        return [distributionId, internshipPlanId, internshipPlanStartDate]
        # s = requests.Session()
        # r = s.get("https://dgsx.cqvie.edu.cn/prod-api/internship_pending/distribution/student_list",
        #           headers=self.headers, cookies=self.cookie)
        # cookies = self.take_middle_text(r.content.decode(), "'cookie' : \"", '",')
        # cookie = self.cookie
        # cookie['muyun_sign_javascript'] = cookies
        # r = s.get("https://dgsx.cqvie.edu.cn/prod-api/internship_pending/distribution/student_list",
        #           headers=self.headers, cookies=self.cookie)
        # print(r.content.decode())

    def sign(self):
        if self.x is None or self.y is None:
            return
        #  从课程开始检查，没签到的统统签到，补签
        #  获取课程信息
        student_list = G.get_student()
        internshipPlanStartDate = student_list[2]
        signInternshipPlanId = student_list[0]
        #  先签到今日
        now_time = datetime.datetime.now().isoformat()
        submit = {
            "latitude": self.y,
            "signAddress": internshipLocation,
            "signDate": now_time,
            # "2022-11-08T09:02:24.892Z"
            "longitude": self.x
        }
        submit = json.dumps(submit)

        res = requests.post(self.sign_href, data=submit, headers=self.headers, cookies=self.cookie)

        print(res.content.decode())
        #  停顿一会，防止请求过快
        time.sleep(3)

        # internshipPlanStartDate_str = str(dateparser.parse(internshipPlanStartDate).date())
        res = requests.get(self.sign_list_href + "?signInternshipPlanId=" + str(signInternshipPlanId),
                           headers=self.headers, cookies=self.cookie)
        unsignedDate = []
        all_time = []
        for i in res.json()['data']:
            all_time.append(i['signDate'])
        all_time.sort(reverse=True)
        #  提取未签到日期
        #  上一次日期减去，相差不是1则是少写日报，补上
        try:
            for i, v in enumerate(all_time):
                if i == 0:
                    continue
                #  上一次日期减去，相差不是1则是少写日报，补上
                now_time = datetime.datetime.strptime(v, "%Y-%m-%d")
                before_time = datetime.datetime.strptime(all_time[i - 1], "%Y-%m-%d")
                xc = (before_time - now_time).days
                if xc != 1:
                    #  获取未写签到日期
                    for j in range(1, xc):
                        xc_time = before_time - datetime.timedelta(days=j)
                        #  检测是否是周六周天，不进入
                        if xc_time.weekday() + 1 == 6 or xc_time.weekday() + 1 == 7:
                            continue
                        xc_time_str = xc_time.strftime("%Y-%m-%d")
                        unsignedDate.append(xc_time_str)
        except:
            return
        for i in unsignedDate:
            before_time = datetime.datetime.strptime(i, "%Y-%m-%d")
            #  伪造签到时间
            millisecond = random.randint(0, 1000000)
            now_time = str(
                datetime.datetime(before_time.year, before_time.month, before_time.day, 8, 0, 0, millisecond))
            #  现在签到时间
            if before_time.year == datetime.datetime.now().year and before_time.month == datetime.datetime.now().month and before_time.day == datetime.datetime.now().day:
                now_time = datetime.datetime.now().isoformat()
            submit = {
                "latitude": self.y,
                "signAddress": internshipLocation,
                "signDate": now_time,
                # "2022-11-08T09:02:24.892Z"
                "longitude": self.x
            }
            submit = json.dumps(submit)

            res = requests.post(self.sign_href, data=submit, headers=self.headers, cookies=self.cookie)

            print(res.content.decode())
            #  停顿一会，防止请求过快
            time.sleep(3)

    def dai(self):
        distributionId = self.get_student()[0]
        times = time.time()
        local_time = time.localtime(times)
        rq = time.strftime("%Y-%m-%d", local_time)
        #  先签到本日，否则检测未签到日期不正确
        submit = {
            "distributionId": distributionId,
            "dailyRecordDate": rq,
            "dailyRecordContent": dai_reportContent,
        }

        res = requests.post(self.dai_href, data=json.dumps(submit), headers=self.headers, cookies=self.cookie)
        print(res.content.decode())
        try:
            #  睡一会，防止请求过快
            time.sleep(3)
            #  本采用分页，但逻辑上可以全部，如需分页：pageNum页码，pageSize一页几个(10) internshipPlanSemester 实习计划，作者的字段是5，应该不要
            res = requests.get(self.dai_list_href + "?distributionId={}".format(distributionId), headers=self.headers,
                               cookies=self.cookie)
            daily_report_date_not_written = []
            all_time = []
            #  对这些先排序，res.json()['rows'],先提取其中日期
            for i, v in enumerate(res.json()['rows']):
                all_time.append(v['dailyRecordDate'])
            all_time.sort(reverse=True)

            for i, v in enumerate(all_time):
                if i == 0:
                    continue
                #  上一次日期减去，相差不是1则是少写日报，补上
                now_time = datetime.datetime.strptime(v, "%Y-%m-%d")
                before_time = datetime.datetime.strptime(all_time[i - 1], "%Y-%m-%d")
                xc = (before_time - now_time).days
                if xc != 1:
                    #  获取未写日报日期
                    for j in range(1, xc):
                        xc_time = before_time - datetime.timedelta(days=j)
                        #  检测是否是周六周天，不进入未写日报日期
                        if xc_time.weekday() + 1 == 6 or xc_time.weekday() + 1 == 7:
                            continue
                        xc_time_str = xc_time.strftime("%Y-%m-%d")
                        daily_report_date_not_written.append(xc_time_str)
        except:
            return
        for i in daily_report_date_not_written:
            submit = {
                "distributionId": distributionId,
                "dailyRecordDate": i,
                "dailyRecordContent": dai_reportContent,
            }

            res = requests.post(self.dai_href, data=json.dumps(submit), headers=self.headers, cookies=self.cookie)
            print(res.content.decode())
            #  睡一会，防止请求过快
            time.sleep(3)

    def week(self):
        detailedInformation = self.get_student()
        distributionId = detailedInformation[0]
        internshipPlanId = detailedInformation[1]
        weekRes = requests.get(self.week_href + "?internshipPlanId=" + str(internshipPlanId), headers=self.headers,
                               cookies=self.cookie)
        weekJson = json.loads(weekRes.content.decode())
        times = time.time()
        local_time = time.localtime(times)
        rq = time.strftime("%Y-%m-%d", local_time)
        if "data" not in weekJson:
            print("请求周次id错误")
            return None
        weekId = None
        for i in weekJson['data']:
            startDate = i['startDate']
            endDate = i['endDate']
            if endDate >= rq >= startDate:
                weekId = i['semesterWeekId']
                break
        if weekId is None:
            print("日报；你还没有开始实习或日期出错")
            return
        #  先写本周的，否则检测周次未写不正确
        submit = {
            "semesterWeekId": weekId,
            "distributionId": distributionId,
            "weekRecordContent": weeklyReportContent
        }
        res = requests.post(self.week_post_href, data=json.dumps(submit), headers=self.headers, cookies=self.cookie)
        print(res.content.decode())
        try:
            #  睡一会
            time.sleep(3)
            #  本采用分页，但逻辑上可以全部，如需分页：pageNum页码，pageSize一页几个(10) internshipPlanSemester 实习计划，作者的字段是5，应该不要
            #  检测周次是否未写
            res = requests.get(self.week_list_href + "?distributionId={}".format(distributionId), headers=self.headers,
                               cookies=self.cookie)
            date_weekly_report_not_written = []
            all_week = []
            all_week_json = {}
            #  先对已写排序
            for i in res.json()['rows']:
                now_week_time = self.take_middle_text(i['semesterWeekName'], "第", "周")
                last_time = self.take_middle_text(i['semesterWeekName'], "~", ")")
                all_week.append(now_week_time)
                all_week_json.update({
                    now_week_time: last_time
                })
            all_week.sort(reverse=True)
            #  上一次日期减去，相差不是1则是少写，补上，提取周次日期后提取周次id
            for i, v in enumerate(all_week):
                if i == 0:
                    continue
                sc = int(all_week[i - 1]) - int(v)
                if sc != 1:
                    for j in range(1, sc):
                        now_time = all_week_json[str(v)]
                        now_time = datetime.datetime.strptime(now_time, "%Y-%m-%d")

                        #  将第一个相差周的最后时间记录起来，相差1就是（1-1）*7+1天，相差2周就是(2-1)*7 +1
                        sc_day = (j - 1) * 7 + 1
                        sc_day_time = datetime.timedelta(days=sc_day)
                        new_time = now_time + sc_day_time
                        new_time_str = new_time.strftime("%Y-%m-%d")

                        #  根据日期区间查找周次id
                        weekRes = requests.get(self.week_href + "?internshipPlanId=" + str(internshipPlanId),
                                               headers=self.headers,
                                               cookies=self.cookie)
                        weekJson = json.loads(weekRes.content.decode())
                        if "data" not in weekJson:
                            print("请求周次id错误")
                            continue
                        weekId = None
                        for k in weekJson['data']:
                            startDate = k['startDate']
                            endDate = k['endDate']
                            if endDate >= new_time_str >= startDate:
                                weekId = k['semesterWeekId']
                                break
                        if weekId is None:
                            print("日报；你还没有开始实习或日期出错")
                            continue
                        date_weekly_report_not_written.append(weekId)
        except:
            return
        for i in date_weekly_report_not_written:
            submit = {
                "semesterWeekId": i,
                "distributionId": distributionId,
                "weekRecordContent": weeklyReportContent
            }
            res = requests.post(self.week_post_href, data=json.dumps(submit), headers=self.headers, cookies=self.cookie)
            print(res.content.decode())
            time.sleep(3)

    def month(self):
        detailedInformation = self.get_student()
        distributionId = detailedInformation[0]
        internshipPlanId = detailedInformation[1]
        monthRes = requests.get(self.month_href + "?internshipPlanId=" + str(internshipPlanId), headers=self.headers,
                                cookies=self.cookie)
        monthJson = json.loads(monthRes.content.decode())
        times = time.time()
        local_time = time.localtime(times)
        rq = time.strftime("%Y-%m_", local_time)
        rq = rq.replace("-", "年")
        rq = rq.replace("_", "月")
        if "data" not in monthJson:
            print("请求周次id错误")
            return None
        monthId = None
        for i in monthJson['data']:
            if i["monthName"] == rq:
                monthId = i['semesterMonthId']
                break
        if monthId is None:
            print("月报；你还没有开始实习或日期出错")
            return
        # 查询是否已经填写，本月
        # internshipPlanSemester个人信息页面是空的，可能固定5
        # 2023年3月23日已提取到，这是学期号，默认最新获取
        res = requests.get("https://dgsx.cqvie.edu.cn/prod-api/baseinfo/semester/list_all",headers=self.headers, cookies=self.cookie)
        internshipPlanSemester = res.json()['data'][0]['semesterId']
        res = requests.get("https://dgsx.cqvie.edu.cn/prod-api/internship_pending/monthrecord/list"
                           "?internshipPlanSemester=".format(internshipPlanSemester),
            headers=self.headers, cookies=self.cookie)
        monthListJson = json.loads(res.content.decode())

        if "rows" not in monthListJson:
            print("请求月报列表错误")
            return None
        for i in monthListJson['rows']:
            if i['monthName'] == rq:
                print("本月已填写月报")
                return None
        submit = {
            "monthRecordId": None,
            "monthRecordType": None,
            "monthWeekId": monthId,
            "studentUserId": None,
            "distributionId": distributionId,
            "monthRecordDate": None,
            "monthRecordTitle": rq + "的月报",
            "monthRecordContent": monthlyReportContent,
            "monthRecordTeacherScore": None,
            "monthRecordTeacherComment": None,
            "monthRecordTeacherUserId": None,
            "monthRecordRatifyStatus": None,
            "delFlag": None,
            "createBy": None,
            "createTime": None,
            "updateBy": None,
            "updateTime": None
        }
        res = requests.post(self.month_post_href, data=json.dumps(submit), headers=self.headers, cookies=self.cookie)
        print(res.content.decode())

    def take_middle_text(self, txt, txt_s, txt_e='', seeks=0, seeke=0):  # 取中间文本函数
        try:
            if txt_e or seeks or seeke:
                pass
            else:
                raise 1
            s_1 = txt.find(txt_s)
            if s_1 == -1:
                raise 1
            l_1 = len(txt_s)
            if txt_e:
                s_2 = txt.find(txt_e, s_1)
                if s_1 == -1 or s_2 == -1:
                    return False
                return txt[s_1 + l_1:s_2]
            if seeks:
                return txt[s_1 - seeks:s_1]
            if seeke:
                return txt[s_1 + l_1:s_1 + l_1 + seeke]
        except:
            return None


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    G = Gcsx()
    now_time = datetime.datetime.now()
    if now_time.hour == 8:
        G.sign()
    elif now_time.hour == 16:
        G.dai()
    elif now_time.weekday() + 1 == 5 and now_time.hour == 17:
        G.week()
    elif now_time.day == 28 and now_time.hour == 18:
        G.month()
    else:
        #  新。保活数字校园 在初始化类已保活
        # millis = int(round(time.time() * 1000))
        # r = requests.get("http://ai.cqvie.edu.cn/ump/serveCenter/selectSearchLog?universityId=102574&appKey=pc-officeHall&timestamp={}&nonce=19953459758032&clientCategory=PC&pageNum=1&pageSize=10".format(millis),headers={
        #     "Host": "dgsx.cqvie.edu.cn",
        #     "Referer": "http://ai.cqvie.edu.cn/new_office_hall/",
        #     "token":TOKEN,
        #     ""
        # },cookies={
        #     "ump_token_pc-officeHall":TOKEN
        # })
        # print(r.content.decode())
        distributionId = G.get_student()[0]
        print("cookie保活成功,distributionId为：{}，若报错或distributionId为空，则是cookie失效".format(distributionId))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
