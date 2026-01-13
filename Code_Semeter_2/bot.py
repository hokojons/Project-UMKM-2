import webbrowser, time
url = input("URl")
duration= int(input("Duration"))
for i in range(60):
    webbrowser.open_new(url)
    time.sleep(duration)