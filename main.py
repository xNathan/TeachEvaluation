# coding: utf-8
# @ Author: xNathan
# @ GitHub: https://github.com/xNathan
# @ Date: 2015-12-11 23:24
"""Description
对本学期已选课程进行自动评教，简化复杂的填表过程。
适用对象：江西财经大学的学生
可以自由设定分值下限和上限，所有分数均为随机生成，作者不对评价客观真实性做保证。
本软件只供学习和参考，如果因为使用此软件而造成任何法律后果，作者不承担任何责任。
"""
import requests
from random import randint
from bs4 import BeautifulSoup


USERNAME = 'YOUR_USERNAME'  # 一卡通账号
PASSWORD = 'YOUR_PASSWORD'  # 密码
MIN_GRADE = 85  # 评教的最低分
MAX_GRADE = 95  # 评教的最高分


login_url = 'http://cas.jxufe.edu.cn/cas/login?username={}&password={}&service=http://xfz.jxufe.edu.cn/portal/sso/login&renew=true'.format(
    USERNAME, PASSWORD)
base_url = 'http://xfz.jxufe.edu.cn/portal/main.xsp/page/-1/?.a.p=aT0lMkZ4Znpwb3J0YWwlMkZwZ25ldyZ0PXImcz1ub3JtYWwmZXM9ZGV0YWNoJm09dmlldw==&mlinkf='
post_url = base_url + 'pg/pg1.jsp'
index_url = base_url + 'pg/index.jsp'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (NT 6.3; WOW64) Gecko/20100101 Firefox/34.0',
}
post_data = {
    'courseName': '',  # 课程名称
    'teacherName': '',  # 老师姓名
    'courseCode': '',  # 课程代码
    'classNO': '',  # 班级代号
    'teachattitude': '',  # 教学态度
    'teachmethod': '',  # 教学水平
    'teacheffect': '',  # 教学效果
    'stmemo': '',  # 早退、表扬、建议
    'teachcontent': '',  # 课件评价
    'coursepleased': '',  # 课程价值
    'teachjc': '',  # 教材评价
    'jcmemo': '',  # 课程教材留言评价
    'coursememo': '',  # 课程设置留言评价
}

s = requests.Session()
s.headers.update(headers)


def login():
    """登录百合信息平台"""
    try:
        res = s.get(login_url, timeout=3)
        return res.url == 'http://xfz.jxufe.edu.cn/portal/main.xsp/page/-1'
    except:
        return False


def get_list():
    """获取课程列表"""
    page = s.get(index_url).content
    soup = BeautifulSoup(page, 'lxml')
    out_put = []
    for item in soup.find('table', class_='Table').findAll('tr'):
        out_put.append([i.get_text().encode('utf-8')
                        for i in item.findAll('td')])
    course_list = out_put[1:]  # 去除第一行表头
    return course_list


def get_evaluate_list():
    """获取等待评教的课程列表"""

    # 先获取所有课程列表
    course_list = get_list()
    result = []
    for item in course_list:
        # item[-2] 有数据即已评教， 无数据则待评教
        if not item[-2]:
            result.append(item)
    return result


def evaluate(courseCode, classNO,
             courseName, teacherName):
    """进行评教
    Args:
        courseCode: 课程代码
        classNO: 班级代号
        courseName: 课程名称
        teacherName: 老师姓名
    Returns:
        Bool 值，True or False
        是否提交成功
    """

    post_data['courseCode'] = courseCode
    post_data['classNO'] = classNO
    post_data['courseName'] = courseName
    post_data['teacherName'] = teacherName

    post_data['teachattitude'] = randint(MIN_GRADE, MAX_GRADE+1)
    post_data['teachmethod'] = randint(MIN_GRADE, MAX_GRADE+1)
    post_data['teacheffect'] = randint(MIN_GRADE, MAX_GRADE+1)
    post_data['stmemo'] = u'都有'.encode('utf-8')
    post_data['teachcontent'] = randint(MIN_GRADE, MAX_GRADE+1)
    post_data['coursepleased'] = randint(MIN_GRADE, MAX_GRADE+1)
    post_data['teachjc'] = randint(MIN_GRADE, MAX_GRADE+1)
    post_data['jcmemo'] = u'教材适用'.encode('utf-8')
    post_data['coursememo'] = u'课程设置合理，易于接受'.encode('utf-8')
    res = s.post(post_url, data=post_data)
    return u'操作成功' in res.text


def main():
    # 先登录
    if login():
        evaluate_list = get_evaluate_list()  # 获取待评教课程
        if evaluate_list:
            for item in get_evaluate_list():
                courseCode = item[0]
                classNO = item[1]
                courseName = item[3]
                teacherName = item[4]
                print courseCode, classNO, courseName, teacherName
                flag = evaluate(courseCode, classNO,
                                courseName, teacherName)
                if flag:
                    print '-----Success------\n'
                else:
                    print'------Error-----\n'
        else:
            print 'No course to evaluate'
    else:
        print 'Login error'

if __name__ == '__main__':
    main()
