cp -R /home/pi/led /home/pi/backup

ftp -v -n<<!
open 147.46.214.228
user ftp2 70023133
cd cw/plot1/below
lcd led
prompt
mput *.txt
bye
!

rm -f -r /home/pi/led
mkdir led/
#sudo reboot
