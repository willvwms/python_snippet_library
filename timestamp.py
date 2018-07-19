from datetime import datetime

x = datetime.now()

date = x.strftime("%m/%d/%y") # 03/13/28
time = x.strftime("%I:%M %p") # 10:10 AM
print(date)
print(time)

out_file = open('test.txt','a') 
out_file.write('\n')
out_file.write('Timestamp:')
out_file.write('\n')
out_file.write(date)
out_file.write('\n')
out_file.write(time)
out_file.write('\n') 
out_file.close() 
