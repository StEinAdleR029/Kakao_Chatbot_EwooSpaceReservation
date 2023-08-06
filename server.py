from flask import Flask, jsonify,request
import sys, json, datetime
import random
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import urllib.request
import pickle
import datetime
from pytz import timezone
application = Flask(__name__)

#initial process

with open('data.p', 'wb') as f:
  pickle.dump(8, f)

# kakao-spreadsheet 연동 변수




@application.route("/date",methods=["POST"])
def space_date():
    server_time = datetime.datetime.now(timezone('Asia/Seoul'))
    request_data=json.loads(request.get_data(), encoding='utf-8')
    params= request_data["action"]["params"]
    school_num = params['school_num']
    name = params['name']
    date_num = params['date']
    space = params['space']
    purpose = params['purpose']
    time = params['time']
    email = params['email']
    response={
        "version":"2.0",
        "template":{
            "outputs" : [
                {
                    "simpleText" : {
                        "text": school_num
                    }
                }
            ]
        }
    }
    
    month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    url = 'http://www.google.com'
    date = urllib.request.urlopen(url).headers['Date'][5:-4]
    d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], date[12:14], date[15:17], date[18:]

    # 스프레드시트 관련 코드

    scope = ['https://spreadsheets.google.com/feeds'] # Google API 요청 시 필요한 권한 유형
    json_file_name = 'key.json' # 서비스계정의 KEY. JSON Key File 경로
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope) #사용자 계정의 자격증명
    gc = gspread.authorize(credentials) #Google API에 로그인

    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1RB1PXHu5lL8THOYx-S56onLG0xrBPbrXjUNw6-fiEyo/edit#gid=0' # 구글 스프레드시트 URL
    doc = gc.open_by_url(spreadsheet_url) # 스프레드 시트 Open
    worksheet = doc.worksheet('실시간 공간 예약 현황') # 스프레드 시트의 워크시트 선택

    # num 값 가져오기

    with open('data.p', 'rb') as f:
      num = pickle.load(f)


    # 스프레드시트에 쓰기

    worksheet.update_acell('B' + str(num), str(server_time.date()) + " " + str(server_time.time()))
    worksheet.update_acell('C' + str(num), school_num)
    worksheet.update_acell('D' + str(num), name)
    worksheet.update_acell('E' + str(num), date_num)
    worksheet.update_acell('F' + str(num), time)
    worksheet.update_acell('G' + str(num), space)
    worksheet.update_acell('H' + str(num), purpose)
    worksheet.update_acell('I' + str(num), email)

    # num 값 저장하기

    num = num + 1

    with open('data.p', 'wb') as f:
      pickle.dump(num, f)
    
    return jsonify(response)
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)
