
The following steps are necessary to run this app as a systemd service

Basic
-----

1. make sure root has access to code
2. copy jh-download.service to /etc/systemd/system
3. sudo systemctl daemon-reload
4. sudo systemctl enable jh-download.service
5. sudo systemctl start jh-download.service

Multiple Ports
--------------
1. $ sudo cp jh-download-multi@.service /etc/systemd/system
2. $ sudo systemctl daemon-reload
3. $ sudo start-multi.sh

