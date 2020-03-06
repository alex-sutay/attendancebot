import os
import time
import RPi.GPIO as GPIO
import csh_ldap
from config import PASSWORD, BIND

instance = csh_ldap.CSHLDAP(BIND,PASSWORD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
 
print(time.strftime("%c"))
  
base_dir = '/sys/devices/w1_bus_master1/w1_master_slaves'
delete_dir = '/sys/devices/w1_bus_master1/w1_master_remove'
   
def main():
 
  
  GPIO.output(18,GPIO.HIGH)
  
  while True:
  
    # iButton Read
    f = open(base_dir, "r")
    ID = f.readline().strip()
    f.close()
    if ID != 'not found.\n':
        print("using username")
        user1 = instance.get_member("sutay", uid=True)
        print(user1)
        # The ID as is from the read
        print("using: " + str(ID))
        user = instance.get_member_ibutton(ID)
        print(user)
        # The changes made by Harold
        ID = "*" + ID[3:].strip() + "01"
        print("using: " + str(ID))
        user = instance.get_member_ibutton(ID)
        print(user)
        # what I know is my ibutton code
        ID = "*0000018BF5C801"
        print("using: " + str(ID))
        user = instance.get_member_ibutton(ID)
        print(user)
        # using the ibutton code lifted straight from the instance
        ID = user1.ibutton
        print("using: " + str(ID))
        user = instance.get_member_ibutton(ID)
        print(user)
        time.sleep(10)
        d = open(delete_dir, "w")
        d.write(ID)
    else:
        pass
  
if __name__ == '__main__':
  
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
