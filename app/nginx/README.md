
Copy nginx config 

	$ sudo cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak 
	$ sudo cp nginx.conf /etc/nginx/nginx.conf
        $ sudo systemctl restart nginx

Turn off selinux preventing upstream connections

	$ sudo setsebool httpd_can_network_connect on

Watch logs for errors

	$ sudo tail -f /var/log/nginx/error.log
	$ sudo tail -f /var/log/nginx/access.log
