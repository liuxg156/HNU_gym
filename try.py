import requests;
import datetime;
import json
url='http://gym.hnu.edu.cn/gym/api/gym/order/create';
#确定预约订单头文件
headers={}#自己获取，获取方法见说明文件
#设定目标时间
star_time=datetime.datetime.now()+datetime.timedelta(minutes=0.1);
#确定预约订单信息
json_data={
    "account":"个人学号",#个人学号
    "paymentType":1,
    "clientType":1,
    "gymVenues":{"id":46,"name":"南校区乒乓球房"},#id和台号是匹配的，可以查看excel文件
    "gymBooking":[
        {"startTime":"2024-04-09 20:10:00",#开始时间，只能按照一个小时预约
                   "endTime":"2024-04-09 21:10:00",
                   "gymSite":{
                       "id":115,
                     "name":"9号台"
                              }
                   }
        ],
    "goods":[]};
json_data2={
    "account":"个人学号",#个人学号
    "paymentType":1,
    "clientType":1,
    "gymVenues":{"id":68,"name":"南校区羽毛球馆"},#id和台号是匹配的，可以查看excel文件
    "gymBooking":[
        {"startTime":"2024-04-09 21:10:00",#开始时间，只能按照一个小时预约
                   "endTime":"2024-04-09 22:10:00",
                   "gymSite":{
                       "id":317,
                     "name":"8号场"
                              }
                   }
        ],
    "goods":[]};
k=0;
while(((datetime.datetime.now()-star_time)).total_seconds()<20):
    if(abs((datetime.datetime.now()-star_time)).total_seconds()<1):
     print(round((datetime.datetime.now()-star_time).total_seconds(),3));
    if(datetime.datetime.now()>star_time and(((datetime.datetime.now()-star_time).total_seconds())<0.01)):
          #发起预约订单
          response=requests.post(url,headers=headers,json=json_data);
          response2=requests.post(url,headers=headers,json=json_data2);
          #输出预约订单结果
          response_data=json.loads(response.text);
          result_data=response_data['msg'];
          response_data2=json.loads(response2.text);
          result_data2=response_data2['msg'];
          k=k+1;
          if(result_data=='操作成功'or result_data2=='操作成功'):
              #print('预约状态为：',result_data);
              print('预约成功时间为：',datetime.datetime.now());
              print('----------%%%%%%%%%%%%%%%%%%%%----------')
              print('预约状态为：',result_data2);
              print('预约成功时间为：',datetime.datetime.now());
              break;
          if((result_data!='操作成功'and result_data2!='操作成功') and (k<=5)):
              print('预约状态为：',result_data);
              print('----------%%%%%%%%%%%%%%%%%%%%----------')
              print('预约状态为：',result_data2);
              break;
          if(k>=5):
              print('预约状态为：预约超时。');
              print('----------%%%%%%%%%%%%%%%%%%%%----------')
              print('预约状态为：预约超时。');
              break;
print(k);
