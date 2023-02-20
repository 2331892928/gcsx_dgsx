# 重庆工程职业技术学院实习系统自动签到，自动日报周报月报
~~cookie方法：进入实习系统查看cookie，只取Admin-Token字段，不包含Admin-Token~~脚本提交日期2022年12月12日以前方法  
2022年12月12日提交日期后方法：进入重庆工程职业技术校园数字校园(电脑版本)，只取ump_token_pc-officeHall字段，不包含ump_token_pc-officeHall  
也可以取_yh_sys_ticket字段，不包含_yh_sys_ticket  
(手机版本) 抓包获取登陆包，获取返回json中ticket字段内容。具体json为：  
```json
{
  "code": "40001",
  "message": "操作成功",
  "conntent": {
    "ticket": "xxx"
  },
  "otherMsg": null
}
```  
成功获取token后，电脑版本不可再次登录数字校园或退出。手机版本不可退出  
所以推荐手机token  
#  脚本功能
自动日报
自动补日报
自动周报
自动补周报
自动月报
自动补月报
自动签到
自动补签到