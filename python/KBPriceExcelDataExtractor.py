from ExcelData

class KBPriceExcelData(ExcelData):
    
    # def extrate_rawdata(self, path):
    #     wb = xw.Book(path)
    #     sheet = wb.sheets[data_type]

    #     시작열 = sheet.range((1,1)).end('down').end('down').end('down').row
    #     데이터_범위 = 'A2:GE' + str(시작열)
    #     return sheet[데이터_범위].options(pd.DataFrame, index=False, header=True).value


    def create_table(self, raw_data): 
        record = self.__날짜포멧변환(self.__컬럼가공(raw_data))
        record.set_index(pd.to_datetime(idx_list), inplace=True)
        return record.drop(('구분', '구분'), axis=1)


    def range(self, sheet):
        시작열 = sheet.range((1,1)).end('down').end('down').end('down').row
        데이터_범위 = 'A2:GE' + str(시작열)
        return 시작열, 데이터_범위;


    def __컬럼가공(raw_data):
        상위_cols = list(raw_data.columns)
        하위_cols = list(raw_data.iloc[0])

        for num, 지역구_데이터 in enumerate(하위_cols):
            if 지역구_데이터 == None:
                하위_cols[num] = 상위_cols[num]
            if num == 제주_서귀포_하위_COLUMN_IDX:
                하위_cols[num] = '서귀포'

            check = num
            while True:
                if 상위_cols[check] in 대표_지역구s:
                    상위_cols[num] = 상위_cols[check]
                if check == 경기도_광주_상위_COLUMN_IDX: 상위_cols[num] = '경기'
                    break
                else:
                    check = check - 1
                    
        raw_data.columns = [상위_cols, 하위_cols]
        return raw_data.drop([0,1])



    def __날짜포멧변환(record):
        date_list = list(record['구분']['구분'])
        idx_list = []
        for num, raw_date in enumerate(date_list):
            temp = str(raw_date).split(".")
                if int(temp[0]) > 12:
                    if len(temp[0]) == 2:
                        idx_list.append('19' + temp[0] + '.' + temp[1])
                    else:
                        idx_list.append(temp[0] + '.' + temp[1])
                else:
                    idx_list.append(idx_list[num-1].split('.')[0] + '.' + temp[0])
        
        return idx_list
