# TeachEvaluation
江西财经大学自动评教软件

## 简介
江西财经大学每学期末都要对所选课程进行评价，内容包括对老师进行打分，留言等

## 评教过程
1. 首先通过数字校园统一身份认证系统，登录进校园百合平台
2. 进入学生评教页面，获取所有待评教的课程信息，包括课程号，班次，课程名称，老师姓名  
![课程详情页](https://github.com/xNathan/TeachEvalution/raw/master/screenshot/course_details.jpg)  
3. 进入课程评教页面，填写里面的内容  
![评教详情页](https://github.com/xNathan/TeachEvalution/raw/master/screenshot/evaluate_detail.jpg)  
4. 提交数据，完成评教

----

## 软件评教过程
1. 先设置登录用户名和密码  
    `USERNAME = 'YOUR_USERNAME'  # 一卡通账号`  
    `PASSWORD = 'YOUR_PASSWORD'  # 密码`

2. 设置评教的最高分和最低分  
    `MIN_GRADE = 85  # 评教的最低分`  
    `MAX_GRADE = 95  # 评教的最高分`

3. 运行软件  
    命令： `python main.py`  
    软件自动登录，并获取还未评教的课程信息，对于各项要打分的字段，将会在最低分到最高分之间随机生成一个分数。最后提交数据，完成评教

## 免责声明
1. 软件不会记录账号和密码，如果发生账号信息泄露，请自行查找原因；
2. 所有分数均为随机生成，作者不对评价客观真实性做保证，建议自己按真实客观的原则，**人为对评教信息进行修改**；
3. 本软件只供学习和参考，如果因为使用此软件而造成任何法律后果，作者不承担任何责任。