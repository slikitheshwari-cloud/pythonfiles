from datetime import datetime
now=datetime.now()
print(now)

from datetime import datetime
now=datetime.now()
print(now.strftime("%y-%m-%d %H:%M:%s"))

from datetime import date
today=date.today()
print(today)

from datetime import time
current_time=datetime.now().strftime("%H:%M:%s") 
print(current_time)

                   
