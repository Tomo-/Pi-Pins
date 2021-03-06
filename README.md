# Pi-Pins
Provides a simple interface for reading and controlling the GPIO pins on the Raspberry Pi model B, B+, Raspberry Pi 2 from a Web Browser. Pi-Pins is used as the back end in PiSwitch iOS App.



#Installation

####Run Each Command Individually

###Install LAMP

    sudo su
    
    apt-get update && apt-get upgrade

    apt-get install apache2 php5 mysql-client mysql-server tomcat6 vsftpd

    cd /var/www

###Install GPIO Python library

    wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.11.tar.gz

    tar zxf RPi.GPIO-0.5.11.tar.gz

    cd RPi.GPIO-0.5.11
    
    sudo apt-get install python-dev

    sudo python setup.py install

**While in the www directory** clone the Pi-Pins folder:

    cd /var/www

    git clone https://github.com/Tomo-/Pi-Pins.git
    
    cd Pi-Pins
    
    sudo mv *.py *.php /var/www
    
    
    
In order to allow the PHP to use the Python scripts the PHP user needs to be added to the sudoers file.

To enter the sudoers file use the command

    sudo visudo

Next add the following line to the end of the file and save it.

    www-data ALL=(ALL) NOPASSWD: ALL

#Usage Instructions


##Reading Pins

In order to read pin 0 the URL is:

    PiAddress/pi-read.php?pin=0

Simply replace the "0" with the pin number you wish to read ranging from 0-27.


##Writing

In order to set the value of pin 0 to high the URL is:

    PiAddress/pi-write.php?io=1&pin=0

To set value to low change

    io=1

to

    io=0

#*The "PiAddress"should be changed to the IP address of your Raspberry Pi.*
