from selenium import webdriver

chrome_driver_path = "C:/Users/John Low/Desktop/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# driver.get("https://www.amazon.com/Titleist-Speed-Balls-White-Dozen/dp/B00QN6LC9I/ref=sr_1_1_sspa?dchild=1&keywords=golf+balls&qid=1622414982&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMzlMWE5KWloyRzFEJmVuY3J5cHRlZElkPUEwNDQ5OTI0MkdRRERPTUZUUUE0MiZlbmNyeXB0ZWRBZElkPUEwNjgzOTgwMk42MEZGN09XSDRPNSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)
#
# driver.close()

driver.get("https://www.python.org")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.close()