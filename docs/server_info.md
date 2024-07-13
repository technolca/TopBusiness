To access server:  ssh root@162.55.57.106

Port: 8069
User service: odoo
Configuraton file location: /etc/odoo-server.conf
Logfile location: /var/log/odoo
User PostgreSQL: odoo
Code location: odoo
Addons folder: odoo/odoo-server/addons/
Password superadmin (database): obcVUFkt6Eca188o
Start Odoo service: sudo service odoo-server start
Stop Odoo service: sudo service odoo-server stop
Restart Odoo service: sudo service odoo-server restart

DB :  TBG_TEST_DB_1 
un : admin
pw : admin

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
- sudo kill -9 no_off_service 