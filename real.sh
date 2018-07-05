#!/bin/bash

DATE=$(date +"%Y_%m_%d_%H_%M_%S")

raspistill -o /home/pi/camera/real/$DATE-cam-real.jpg -r -ev -10

