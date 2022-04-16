# -*- coding: utf-8 -*-
from datetime import datetime
import requests

def confirm_aqc(data:list) -> str:
    """
    品質情報を確認し、データを文字列で返す
    input : list
    return : str
    """
    if data[1] == 0:
        return str(data[0])
    else:
        return "品質情報を確認して下さい"

def find_index(data:list, code:str) -> int:
    """
    対象のエリアのデータが格納されているインデックス番号を返す
    input : list
    return : int
    """
    index = [num for num, i in enumerate(data) if i["area"]["code"] == code][0]
    return index

def weather():
    """
    天気に関するデータを返す

    Returns:
        str: 当日の天気
        str: 翌日の天気
        float: 当日の気温
    """
    latest_time_url = "https://www.jma.go.jp/bosai/amedas/data/latest_time.txt"
    latest_time_req = requests.get(latest_time_url)
    latest_datetime = datetime.strptime(latest_time_req.text, "%Y-%m-%dT%H:%M:%S%z") # タイムゾーン込みで日時文字列をdatetime型へ
    yyyymmdd = latest_datetime.strftime('%Y%m%d') # 年月日　- アメダスデータ取得時に必要
    h3 = ("0" + str((latest_datetime.hour//3)*3))[-2:] # 3時間ごとの時間 - アメダスデータ取得時に必要
    area = "130000" # エリア番号 - 今回は東京都
    detail_area = "130010" # 詳細の予報エリア番号 - 今回は東京地方
    stnid = "44132" # 観測所番号 - 今回は千代田区 北の丸公園

    # 天気予報
    forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area}.json"
    forecast_req = requests.get(forecast_url)
    forecast_data = forecast_req.json()
    forecast_data = forecast_data[0]["timeSeries"][0]["areas"] #エリア毎の予報データ（天気, 風速, 風向...etc）が格納
    forecast_data_target_index = find_index(forecast_data, detail_area)
    weathers = forecast_data[forecast_data_target_index]["weathers"] # 天気
    today_weather = weathers[0]
    tommorow_weather = weathers[1]

    # アメダス
    amedas_url = f"https://www.jma.go.jp/bosai/amedas/data/point/{stnid}/{yyyymmdd}_{h3}.json"
    amedas_req = requests.get(amedas_url)
    amedas_data = amedas_req.json()
    latest_key = max(amedas_data) # 最新のアメダスデータが入っているkey
    latest_temp = confirm_aqc(amedas_data[latest_key]["temp"]) # 最新の気温データを取得, 品質情報を確認

    return today_weather,tommorow_weather,latest_temp