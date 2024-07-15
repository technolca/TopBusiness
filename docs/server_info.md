To access server:  ssh root@162.55.57.106
Password : 7TT3fpXtuFWRrsufjKNHTop@2024.

Port: 8017
User service: odooe
Configuraton file location: /etc/odooe-server.conf
Logfile location: /var/log/odooe
User PostgreSQL: odooe
Code location: odooe
Addons folder: odooe/odooe-server/addons/
Password superadmin (database): admin
Start Odoo service: sudo service odooe-server start
Stop Odoo service: sudo service odooe-server stop
Restart Odoo service: sudo service odooe-server restart
custom addons path: /odooe/custom/addons/TopBusiness

To access server enter this url : http://162.55.57.106:8017
DB :  TBG_TEST_DB_1_e 
Username : odooe
Password : odooe

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