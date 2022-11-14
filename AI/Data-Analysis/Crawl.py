import requests
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import warnings
import time

warnings.filterwarnings(action='ignore')

header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
          "Accept" : "test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
          "Accept-Encoding" : "br, gzip, deflate"}
classCodeUrl = "https://www.agrion.kr/portal/fdp/fpi/selectFrmprdPcInfoRealClasscodeList.do"
classCodeUrlJson = {"cc_arr" : "", "ccName" : "", "eDate" : "20220511", "flag" : "lClassCode",
                    "lcate" : "prd","lClassCode" : "", "mClassCode" : "",
                    "sClassCode_arr" : "", "sClassName" : "", "sDate" : "20220511", "sort" : "desc", "sortGbn" : "",
                    "wc_arr" : "", "wcName" : ""}
infoUrl = "https://www.agrion.kr/portal/fdp/fpi/selectRltmAucBrkNewsTobeList.do"
infoUrlJson = {"cc_arr" : "", "ccName" : "", "eDate" : "20220511",
               "lcate" : "prd","lClassCode" : "08", "limit" : 100000, "mClassCode" : "", "pageIndex" : 1,
               "sClassCode_arr" : "", "sClassName" : "", "sDate" : "20220511", "sort" : "desc", "sortGbn" : "",
               "wc_arr" : "", "wcName" : ""}

# 필요에 따라 변경
csvCount = 42
start = datetime.strptime("20181208", "%Y%m%d")
end = datetime.strptime("20221110", "%Y%m%d")

codeDict =  {'건제품': '89', '과실류': '06', '과일과채류': '08', '과채류': '09', '근채류': '11', '기타화훼': '28', '냉동 해면갑각류': '83', '냉동 해면기타': '85', '냉동 해면어류': '81', '냉동 해면연체류': '84', '농림가공': '91', '두류': '03', '맥류': '02', '버섯류': '17', '산채류': '14', '서류': '05', '수산가공': '93', '수실류': '07', '숙근류': '24', '식물성단미사료': '52', '신선 내수면기타': '78', '신선 내수면어류': '77', '신선 해면갑각류': '73', '신선 해면기타': '75', '신선 해면어류': '71', '신선 해면연체류': '74', '신선 해면패류': '72', '신선 해조류': '76', '약용작물류': '19', '양채류': '13', '엽경채류': '10', '인삼류': '18', '잡곡류': '04', '조미채소류': '12', '초화류': '21', '특용작물류': '16', '활 해면기타': '65', '활 해면어류': '61', '활 해면연체류': '64', '활 해면패류': '62'}


def prepCodeUrlJson(json, date) :
    json['eDate'] = date
    json['sDate'] = date

    return json

def prepInfoUrlJson(json, date, classCode) :
    json['eDate'] = date
    json['sDate'] = date
    json['lClassCode'] = classCode

    return json


df = pd.DataFrame(columns=['dates', 'bidtime', 'unitnameorder', 'unitname', 'price', 'tradeamt', 'lclassname', 'mclassname',
                           'sclassname', 'sanji', 'marketname', 'coname', 'gradename'])
noResponse = []

category = "과일과채류"
code = codeDict[category]

while start <= end :
    start += timedelta(1)
    try :
        response = requests.post(classCodeUrl, json=prepCodeUrlJson(classCodeUrlJson, start.strftime("%Y%m%d")), headers=header, timeout=20)
        if len(response.json()['resultList']) == 0 :
            continue
        else :
            flag = False
            for stuff in response.json()['resultList'] :
                if stuff['lclasscode'] == code :
                    flag = True
                    break
            if flag == False :
                continue
            print(start.strftime("%Y%m%d"))
            time.sleep(0.13)
            html = requests.post(infoUrl, json=prepInfoUrlJson(infoUrlJson, start.strftime("%Y%m%d"), code), headers=header, timeout=25)
            data = pd.DataFrame(html.json()['resultList'])
            data = data.drop(labels=['unitco', 'sanco', 'coco', 'auctype', 'auctypeName', 'lclasscode',
                                   'mclasscode', 'sclasscode', 'marketcode', 'cocode', 'gradecode', 'rnum',
                                   'listRnum', 'totCount'], axis=1)
            df = df.append(data)
            print(category, len(html.json()['resultList']), f"현재 개수:{len(df.index)}")
            if len(df.index) > 1000000 :
                df.to_csv(f"{category}{csvCount}.csv", index=False)
                csvCount += 1
                df = pd.DataFrame(columns=['dates', 'bidtime', 'unitnameorder', 'unitname', 'price', 'tradeamt', 'lclassname',
                                           'mclassname', 'sclassname', 'sanji', 'marketname', 'coname', 'gradename'])
    except :
        noResponse.append(start.strftime("%Y%m%d"))

df.to_csv(f"{category}{csvCount}.csv", index=False)


df = pd.DataFrame(noResponse)
df.to_csv("MissingDates1.csv", index=False, header=False) ##필요에 따라 변경
