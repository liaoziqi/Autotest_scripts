#coding:utf-8
#-*- coding : utf-8 -*-
import  pycurl


address = raw_input(unicode('请输入网址：','utf-8').encode('gb2312'))
url = str('http://' + address)
#print url
time = raw_input(unicode('请输入请求次数：','utf-8').encode('gb2312'))
times = int(time)
#print d
c = pycurl.Curl()
c.setopt(pycurl.URL, url)


def gethttp(tips):
    d1 = dict()
    failtime = 0
    for i in range(1, tips+1):
        c.perform()
        rescode = c.getinfo(pycurl.HTTP_CODE)
        #rescode = 100 #测试代码
        if rescode == 200:
            #print "request success!" 调试代码
            totle_time = c.getinfo(pycurl.TOTAL_TIME)
            d1[i] = totle_time
        else:
            failtime=failtime+1
            #print "request failed!" 调试代码
            break
    if d1:
        #print 'a字典非空'
        print u'第（%d）次请求失败' %(i + 1)
        print u'共有（%d）次请求失败' % failtime
        return d1
    else:
        #print 'a字段为空'
        print u'第（%d）次请求失败' % i
        print u'共有（%d）次请求失败' % failtime
        return


def output(nums):
    d2 = gethttp(nums)
    loadtime = d2.values()
    #print '加载时间列表:',i #调试代码
    print u'加载次数：（%d）' %(len(loadtime))
    print u'网页加载平均时间: (%.3f)' % (sum(loadtime) / len(loadtime))
    print u'网页加载最长时间：(%.3f)' % (max(loadtime))
    print u'网页加载最短时间：(%.3f)' % (min(loadtime))


if __name__=='__main__':
    output(times)



