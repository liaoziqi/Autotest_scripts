#coding:utf-8
#-*- coding : utf-8 -*-
import  pycurl



c = pycurl.Curl()


def BaseInfo():
    address = raw_input(unicode('请输入访问链接：','utf-8').encode('gb2312'))
    time = raw_input(unicode('请输入访问次数：','utf-8').encode('gb2312'))
    url = str('http://' + address)
    times = int(time)
    listbase = [url,times]
    return listbase


def gethttp(tips):
    serverreq_time = dict()
    failedtimes = 0
    for i in range(1, tips+1):
        c.perform()
        pretrans_time = c.getinfo(pycurl.PRETRANSFER_TIME)  # 从发起请求到准备传输所消耗的时间
        starttrans_time = c.getinfo(pycurl.STARTTRANSFER_TIME)  # 从发起请求到接收第一个字节的时间
        rescode = c.getinfo(pycurl.HTTP_CODE)  # 返回状态
        if rescode == 200:
            serverreq_time[i] = float("%.3f" % (starttrans_time - pretrans_time))
        else:
            failedtimes = failedtimes+1
            continue
    return serverreq_time

def Resultloadtime(times):
    loadtime = gethttp(times).values()
    avertime = (sum(loadtime)/len(loadtime))
    maxtime = max(loadtime)
    mintime = min(loadtime)
    result = [avertime,maxtime,mintime]
    return result


def output():
    listbase = BaseInfo()
    url = listbase[0]
    times = listbase[1]
    c.setopt(pycurl.URL, url)
    result = Resultloadtime(times)
    print u'链接访问次数：%d' %times
    print u'服务器处理平均时间：%.3f' %result[0]
    print u'服务器处理最大时间：%.3f' %result[1]
    print u'服务器处理最小时间：%.3f' %result[2]


if __name__=='__main__':
    output()



