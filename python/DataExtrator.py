from abc import *
from KBPriceExcelData

class DataExtractor():

    def exrate_excel_data(path)
        wb = xw.Book(path)
        sheet = wb.sheets[data_type]

        시작열, 데이터_범위 = KBPriceExcelData.range(sheet)
        raw_data = sheet[데이터_범위].options(pd.DataFrame, index=False, header=True).value

        return KBPriceExcelData.create_table(raw_data)
        
    def exrate_api_data(url)
        return

    def exrate_db_date(conn, sql)
        return
