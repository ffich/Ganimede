from machine import RTC

rtc = RTC()

# Set a specific date and time
rtc.datetime((2022, 1, 1, 1, 0, 0, 0, 0)) # y-m-d-wd-h-m-s-ms

# Get date and time
print('Current date and time: ' + str(rtc.datetime()))

# Set an alarm
rtc.alarm(RTC.ALARM0, 5000)

# Do nothing if the alarm is not expired
while rtc.alarm_left(RTC.ALARM0) > 0:
        pass

print('Alarm expired!')
