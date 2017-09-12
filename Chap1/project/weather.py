# 将文件内容转化为词典
weather_dict = { }

open_weather = open('weather_info.txt', 'r')

for line in open_weather:
	x = line.split(",")
	a = x[0]
	b = x[1]
	c = len(b)-1 # 去除b后面的‘\n’
	b = b[0:c]
	weather_dict[a] = b

# 输入城市，查询城市天气
history_dict = { }

while True:

	city = input("请输入指令或你要查询的城市名：")
	if city in weather_dict.keys():
		weather = weather_dict[city]
		history_dict[city] = weather
		print(f"{city}的天气状况为： {weather}")


# 在退出程序之前，打印查询过的所有城市

	if city == "history":
		for keys, values in history_dict.items():
			print(f" {keys} : {values} ")

	elif city == "quit":
		quit()

	elif city == "help":
		print("""
		输入城市名，查询该城市的天气；
		输入help， 获取帮助文档；
		输入history， 获取查询历史；
		输入quit， 退出天气查询系统；
		""")
	else:
		pass
