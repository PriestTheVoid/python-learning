import time
from plyer import notification

while True:
    notification.notify(
        title='Riso без LLM', 
           message='НАПОМИНАЮ!\nпора оторваться от стула и потрогать траву', 
        timeout=10
    )   
    time.sleep(3600)