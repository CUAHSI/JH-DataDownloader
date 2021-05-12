
The following steps are necessary to run this app as a systemd service

1. move directory to /srv
2. give root permissions
3. copy jh-download.service to /etc/systemd/system
4. sudo systemctl reload-daemon
5. sudo systemctl enable jh-download.service
6. sudo systemctl start jh-download.service

