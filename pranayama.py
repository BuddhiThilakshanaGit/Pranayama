from time import sleep

# Breathing
print("\n\nGet 30 short and deep breaths ,then Press Enter")

x = input()

# Holding_on
print("Stop Breathing for 1 minute")
sleep(3)
for x in range(4, 61):
    if (60-x) % 5 == 0:
        print(60-x, "sec(s) >> Hold on Hold on<<")
    else:
        print(60-x, "sec(s)")
    sleep(1)

# Exhaling
print("Exhale for 30 seconds")
sleep(3)
for x in range(4, 31):
    if (30-x) % 5 == 0:
        print(30-x, "sec(s) >> Keep it Going <<")
    else:
        print(30-x, "sec(s)")
    sleep(1)

print("Tada.. You are Done !!!")
