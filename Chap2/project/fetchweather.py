import requests
import json

API = 'https://api.seniverse.com/v3/weather/now.json'
history_input = []

# 调用心知天气API
def fetch_weather(location):
    result = requests.get(API, params = {
        'key': '20xip20c8tvv42wg',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=1)
    return result.text

# 整理API    
def return_weather(text_weather):
    json_result = json.loads(text_weather)
    weather = json_result['results'][0]['now']['text']
    temperature = json_result['results'][0]['now']['temperature']
    last_update = json_result['results'][0]['last_update']
    w = "%s的天气为%s ，温度为%s摄氏度，更新时间：%s ." % (city_input, weather,temperature, last_update)
    return w 

def history():
    print(history_input)


while True:
    city_input = input("请输入指令或你要查询的城市名：")
    
    if city_input == "help":
        print('''
        \t输入城市名，查询该城市天气；
        \t输入 help，获取帮助文档；
        \t输入 history，获取查询历史；
        \t输入 quit，退出天气查询系统；
        ''')

    elif city_input == "history":
        history()

    elif city_input == "quit":
        quit()

    else:
        fetch_text = fetch_weather(city_input)
        return_history = return_weather(fetch_text)
        print(return_history)
        history_input.append(return_history)
        


