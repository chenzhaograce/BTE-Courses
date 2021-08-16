import yahoo_fin.stock_info as si
import time

get_live_data = False

if get_live_data:
    while True:
        print("NVIDIA live stock price change: ", si.get_live_price("NVDA"))
        time.sleep(60)
else:
    nvda = si.get_data("NVDA")
    print(nvda)
    