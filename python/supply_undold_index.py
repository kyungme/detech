import requests
import pandas as pd
from datetime import datetime as dt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def unsold_preprocessing(start_dt, end_dt):
    api_url = 'http://stat.molit.go.kr/portal/openapi/service/rest/getList.do?key=6e6f2f34780740c095705cda5cf6292b&form_id=2082&style_num=128&start_dt='+start_dt+'&end_dt='+end_dt
    headers = ['서울','부산','대구','인천','광주','대전','울산','경기','강원','충북','충남', '세종','전북','전남','경북','경남','제주']

    r = requests.get(api_url)
    r.raise_for_status()
    raw_data = r.json()
    data_list = raw_data['result_data']['formList']
    data_list = sorted(data_list, key = lambda i: i['date'])

    temp_list = []
    date_list = []
    
    return data_list

    idx_date = start_dt
    temp = []
    for i, item in enumerate(data_list):
        # 구를 여기서는 다루지 않음
        if '계' == item['시군구'] and '전국' != item['구분']:
            # 데이터 줄바꿈
            if '제주' == item['구분']:
                temp.append(item['미분양현황'])
                temp_list.append(temp)
                date_list.append(item['date'][:4] + '-' + item['date'][4:6])
                temp = []
            # 세종시 빈칸 적용
            elif '충남' == item['구분']:
                temp.append(item['미분양현황'])
                if dt.strptime('201207', "%Y%m") > dt.strptime(item['date'], "%Y%m"):
                    temp.append(None)
            else:
                # 미분양현황이 없는 구분row가 있음
                if '미분양현황' in item:
                    temp.append(item['미분양현황'])
                else:
                    temp.append(None)
                    

    df = pd.DataFrame(temp_list)
    df.columns = headers
    transposed_df = df.T
    transposed_df.columns = date_list
    return transposed_df.T


unsold = unsold_preprocessing('200701', '202008')
# unsold = unsold_preprocessing('200701', '202007')
# # unsold['서울']['2009']
pd.DataFrame(unsold)
