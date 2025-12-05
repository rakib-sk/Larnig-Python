''' 4. 📱 Mobile Balance Tracker
প্রতিদিন কত টাকা খরচ হলো (MB/Call/SMS) ইনপুট নাও।
Loop দিয়ে:
- মোট খরচ
- কোন দিনে সবচেয়ে বেশি খরচ হয়েছে বের করো
'''
total_cost_list =[]

while True:
    mb = int(input("Enter your cost money for MB: "))
    call = int(input("Enter your cost money for Call: "))
    sms = int(input("Enter your cost money for SMS: "))
    
    total_cost_list.append(mb)
    total_cost_list.append(call)
    total_cost_list.append(sms)
    
for i in total_cost_list:
    print(i)
          