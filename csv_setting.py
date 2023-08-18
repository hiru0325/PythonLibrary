import csv

def csv_write(a_strFileName, a_aryFieldHeader, a_aryFieldInfoList):
    with open(a_strFileName, 'w') as CSV_file:
        writer = csv.DictWriter(CSV_file, fieldnames=a_aryFieldHeader)
        # ----- ヘッダー -----
        writer.writeheader()
        # ----- ボディ -----
        for intRowCnt in range(len(a_aryFieldInfoList)):
            writer.writerow({a_aryFieldHeader[intRowCnt]: a_aryFieldInfoList[intRowCnt]})
