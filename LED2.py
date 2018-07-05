import time, sched  
import os 
import serial
import numpy as np

# Port 
port = '/dev/ttyACM1'
# Average time span (min)
interval = 1
# Start time
sTime = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
# File URL
url = '/home/pi/LED2_pi1.%s.txt' % (sTime)

def do():
    # Clear data list for recording
    lst = []
    # Update time
    t0 = time.localtime(time.time())
    # Start
    while 1:
        # Get data from serial port stream
        line = stream.readline().rstrip().replace(',','').split()
        # Check format
        if len(line)==4 and all([x.isdigit() for x in line]):
            # Add to data list
            lst.append(line)
            # Timing
            t = time.localtime(time.time())
            # Judge if delta time passed
            if (t.tm_min-t0.tm_min==interval) or (t.tm_min==0 and t0.tm_min==59):
                # Convert data type
                arr = np.array(lst,np.float)
                # Remove saturated data
                arr[arr==1023] = np.nan
                # Average over time interval.
                data = np.nanmean(arr,axis=0)
                # Orgnize output string
                string = ','.join('%10.3f' % x for x in data)
                # Output to screen
                print '%s, %s' % (time.strftime('%Y-%m-%d %H:%M:%S',t), string)
                # Output to file
                file = open(url,'a')
                file.write('%s, %s\n' % (time.strftime('%Y-%m-%d %H:%M:%S',t), string))
                file.close()
                # Update time
                t0 = t
                # Clear data list for recording
                lst = []


# Define stream from serial port
stream = serial.Serial(port,9600)

# Initialize scheduler  
s = sched.scheduler(time.time, time.sleep)

# Set start time
timestamp = time.mktime(time.strptime(sTime,'%Y_%m_%d_%H_%M_%S'))

# Start
s.enterabs(timestamp, 1, do, ())
s.run()
