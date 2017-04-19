#coding:utf-8
#-*- coding : utf-8 -*-
import  pycurl


L = raw_input(unicode('请输入网址：','utf-8').encode('gb2312'))
url = str('http://' + L)
#print url
time = raw_input(unicode('请输入请求次数：','utf-8').encode('gb2312'))
d = int(time)
#print d
c = pycurl.Curl()
c.setopt(pycurl.URL, url)


def gethttp(tips):
    a = dict()
    j = 0
    for i in range(1, tips+1):
        c.perform()
        rescode = c.getinfo(pycurl.HTTP_CODE)
        #rescode = 100 #测试代码
        if rescode == 200:
            #print "request success!" 调试代码
            totle_time = c.getinfo(pycurl.TOTAL_TIME)
            a[i] = totle_time
        else:
            j=j+1
            #print "request failed!" 调试代码
            break
    if a:
        #print 'a字典非空'
        print u'第（%d）次请求失败' %(i + 1)
        print u'共有（%d）次请求失败' % j
        return a
    else:
        #print 'a字段为空'
        print u'第（%d）次请求失败' % i
        print u'共有（%d）次请求失败' % j
        return


def output(num):
    b = gethttp(num)
    i = b.values()
    #print '加载时间列表:',i #调试代码
    print u'加载次数：（%d）' %d
    print u'网页加载平均时间: (%.3f)' % (sum(i) / len(i))
    print u'网页加载最长时间：(%.3f)' % (max(i))
    print u'网页加载最短时间：(%.3f)' % (min(i))


if __name__=='__main__':
    output(d)



