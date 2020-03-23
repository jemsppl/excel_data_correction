import pandas
from difflib import SequenceMatcher

# excel_data_local = pandas.read_excel('MasterData.xlsx', sheet_name='master_local')
excel_data_dist = pandas.read_excel('MasterData.xlsx', sheet_name='master_dist')

# json_local = excel_data_local.to_json()
json_dist = excel_data_dist.to_json()
excel_data_df = pandas.read_excel('Calicut-AP-Data-22-Mar-2020-03-42-PM-Complete-Backup.xlsx', sheet_name='Sheet1')


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def dist_id(dist_raw):
    p = 0
    result = "Un Detected"
    d_raw = str(dist_raw)
    for mast_dist in excel_data_dist.index:
        mast = str(excel_data_dist['Districts_Kerala'][mast_dist])
        district_actual_name = str(excel_data_dist['district_actual_name'][mast_dist])
        s = similar(d_raw.lower(), mast.lower())
        if s > p:
            p = s
            if s > 0.69:
                # result = d_raw+"---- is now -----"+district_actual_name
                result = district_actual_name
            else:
                result = d_raw + "***Did you Mean***" + district_actual_name
    return result


def local_id(local_r, district_n):
    district_name = dist_id(district_n).lower()
    excel_data_local = pandas.read_excel('MasterData.xlsx', sheet_name=district_name)
    t = 0
    local_result = "Un Detected"
    local_raw = str(local_r)
    for i in excel_data_local.index:
        master_l = str(excel_data_local['Local_Body'][i])
        r = similar(local_raw.lower(), master_l.lower())
        if r > t:
            t = r
            if r > 0.69:
                #local_result = local_raw + "---- is now -----" + master_l
                local_result = master_l
            else:
                local_result = local_raw + "**** Did You Mean ****" + master_l
    return local_result


for data in excel_data_df.index:
    dist = excel_data_df['District'][data]
    local = excel_data_df['Local Body'][data]

    excel_data_df['District'][data] = dist_id(dist)
    if dist_id(dist) == "Malappuram":
        if dist_id(dist) != "Un Detected":
            excel_data_df['Local Body'][data] = local_id(local, dist)
        print(dist_id(dist) + '\t' + local_id(local, dist))

excel_data_df.to_excel(r'F:\Data Mangement\Covid_Data_2020\export_dataframe2.xlsx', index=False, header=True)
