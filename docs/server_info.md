To access server:  ssh root@162.55.57.106

Port: 8017
User service: odoo17_
Configuraton file location: /etc/odoo17_-server.conf
Logfile location: /var/log/odoo17_
User PostgreSQL: odoo17_
Code location: odoo17_
Addons folder: odoo17_/odoo17_-server/addons/
Password superadmin (database): admin
Start Odoo service: sudo service odoo17_-server start
Stop Odoo service: sudo service odoo17_-server stop
Restart Odoo service: sudo service odoo17_-server restart
custom addons path: /odoo17_/custom/addons/TopBusiness

To access server enter this url : http://162.55.57.106:8017
DB :  TBG_TEST_DB_1 
Username : admin
Password : admin

to see log file : sudo tail -f /var/log/odoo/odoo-server.log
to getout from log file : ctrlx ctrlc (without space)

add custom addons :
- cd /odoo
- ls
- cd custom/
- ls
- cd addons/

to force stop odoo service :
- ps axu||grep
- get odoo service no from the first column 
- sudo kill -9 83485

TO get full directory path : pwd