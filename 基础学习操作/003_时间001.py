from datetime import datetime

# time1 = datetime(1970, 1, 3, 0, 0)
# print(time1)
# time1_stamp = time1.timestamp()
# print(time1_stamp)
#
# print('')
#
# back2time = datetime.fromtimestamp(time1_stamp)
# print(back2time)
#
# print('')

# time_now = datetime.now()
# print(time_now)
# print(datetime.utcfromtimestamp(time_now.timestamp()))

# shijian = datetime.strptime('2019-4-13 20:26:04', '%Y-%m-%d %H:%M:%S')
# print(shijian)
# print(datetime.utcfromtimestamp(shijian.timestamp()))
# utctime1 = datetime.utcfromtimestamp(shijian.timestamp())
# print(utctime1.strftime('%Y, %m %d - %H:%M:%S'))


from datetime import timedelta
# timenow = datetime.now()
# print(timenow - timedelta(days=3,hours=22,minutes=42,seconds=34,weeks=2))
# print(timenow + timedelta(days=3,hours=22,minutes=42,seconds=34,weeks=2))


from datetime import timezone
uct8 = timezone(timedelta(hours=8))
xianzai = datetime.now()
print(xianzai)
changetz = xianzai.replace(tzinfo=uct8)
print(changetz)