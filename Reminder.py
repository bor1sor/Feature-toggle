import time
print("what to remind?")
text = str(input())
print("after how many minutes?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)