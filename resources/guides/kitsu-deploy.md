# Deploy cgwire Kitsu for 

A summary of steps mentioned in [zou.cg-wire](https://zou.cg-wire.com/) <br>

This guide can be later on converted to a bash script to deploy `kitso` for production automatically. <br>

Alternatively, you can use [cgwire kitsu docker image](https://hub.docker.com/r/cgwire/cgwire) but keep in mind they mentioned that : 
>It is not recommended to use this image in production. It is aimed at testing purposes.
<br>

---
<br>

# Steps : 
## Install and run password generator
    
    sudo apt update
    sudo apt install pwgen 
    pwgen 16

## Variables: 

    DB_USER=postgres
    DB_PASSWORD=database_password
    SECRET_KEY=generated_password 
    PORT=80
    SERVER_NAME=server_name.com
    ZOU_ADMIN_USER=admin@yourstudio.com
    ZOU_ADMIN_PASS=admin@123456

Additional variables, I didn't use them in this guide however you can

    KITSU_API_TARGET=http://localhost:5000
    KITSU_EVENT_TARGE=http://localhost:5001

## Install third parties software

    sudo apt-get install postgresql postgresql-client postgresql-server-dev-all -y
    sudo apt-get install redis-server -y
    sudo apt-get install python3 python3-pip -y
    sudo apt-get install git -y
    sudo apt-get install nginx -y 
    sudo apt-get install ffmpeg -y


## Create zou user 

    sudo useradd --home /opt/zou zou 
    sudo mkdir /opt/zou
    sudo chown zou: /opt/zou
    sudo mkdir /opt/zou/backups
    sudo chown zou: /opt/zou/backups

## Install Zou and its dependencies:

    sudo pip3 install virtualenv
    cd /opt/zou
    sudo virtualenv zouenv
    sudo /opt/zou/zouenv/bin/pip3 install zou
    sudo chown -R zou:www-data .

## Create previews folder

    sudo mkdir /opt/zou/previews
    sudo chown -R zou:www-data /opt/zou

## Create full text search indexes folder
    
    sudo mkdir /opt/zou/indexes
    sudo chown -R zou:www-data /opt/zou/indexes

## Create temp files folder

    sudo mkdir /opt/zou/tmp
    sudo chown -R zou:www-data /opt/zou/tmp


## Prepare database
    sudo su -l $DB_USER
    psql -c 'create database zoudb;' -U $DB_USER
    
    psql 

In psql interactive mode 

    \password 
    $DB_PASSWORD
    $DB_PASSWORD
    \q

## Exit `sudo su`

    exit

## Create database tables:

    sudo -u zou DB_PASSWORD=$DB_PASSWORD /opt/zou/zouenv/bin/zou init-db


## Prepare key value store:

    sudo nano /etc/sysctl.conf

Add to the end of the file:

    vm.overcommit_memory = 1


## Create Gunicorn configuration folder

    sudo mkdir /etc/zou

## Gunicorn configuration:

    sudo nano /etc/zou/gunicorn.conf

Add to the end of the file: 

    accesslog = "/opt/zou/logs/gunicorn_access.log"
    errorlog = "/opt/zou/logs/gunicorn_error.log"
    workers = 3
    worker_class = "gevent"


## Create Log Folder:

    sudo mkdir /opt/zou/logs
    sudo chown zou: /opt/zou/logs

## Daemonize the gunicorn process 
Create zou service:

    sudo nano /etc/systemd/system/zou.service

Add these:

    [Unit]
    Description=Gunicorn instance to serve the Zou API
    After=network.target

    [Service]
    User=zou
    Group=www-data
    WorkingDirectory=/opt/zou
    # Append DB_USERNAME=username DB_HOST=server when default values aren't used
    # ffmpeg must be in PATH
    Environment="DB_PASSWORD=$DB_PASSWORD"
    Environment="SECRET_KEY=$SECRET_KEY"
    Environment="PATH=/opt/zou/zouenv/bin:/usr/bin"
    Environment="PREVIEW_FOLDER=/opt/zou/previews"
    Environment="TMP_DIR=/opt/zou/tmp"
    ExecStart=/opt/zou/zouenv/bin/gunicorn  -c /etc/zou/gunicorn.conf -b 127.0.0.1:5000 zou.app:app

    [Install]
    WantedBy=multi-user.target 

Create gunicorn-events

    sudo nano /etc/zou/gunicorn-events.conf

Add these:

    accesslog = "/opt/zou/logs/gunicorn_events_access.log"
    errorlog = "/opt/zou/logs/gunicorn_events_error.log"
    workers = 1
    worker_class = "geventwebsocket.gunicorn.workers.GeventWebSocketWorker"

Create zou-events

    sudo nano /etc/systemd/system/zou-events.service

add these : 

    [Unit]
    Description=Gunicorn instance to serve the Zou Events API
    After=network.target

    [Service]
    User=zou
    Group=www-data
    WorkingDirectory=/opt/zou
    # Append DB_USERNAME=username DB_HOST=server when default values aren't used
    Environment="PATH=/opt/zou/zouenv/bin"
    Environment="SECRET_KEY=$SECRET_KEY" # Same one than zou.service
    ExecStart=/opt/zou/zouenv/bin/gunicorn -c /etc/zou/gunicorn-events.conf -b 127.0.0.1:5001 zou.event_stream:app

    [Install]
    WantedBy=multi-user.target


## Configure Nginx

sudo nano /etc/nginx/sites-available/zou

Add these:

    server {
        listen $PORT;
        server_name $SERVER_NAME; 

        location /api {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_pass http://localhost:5000/;
            client_max_body_size 500M;
            proxy_connect_timeout 600s;
            proxy_send_timeout 600s;
            proxy_read_timeout 600s;
            send_timeout 600s;
        }

        location /socket.io {
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
            proxy_pass http://localhost:5001;
        }
    }


## Remove default configuration
    
    sudo rm /etc/nginx/sites-enabled/default

## Enable Nginx configuration
    sudo ln -s /etc/nginx/sites-available/zou /etc/nginx/sites-enabled

## start daemons
    sudo systemctl enable zou
    sudo systemctl enable zou-events
    sudo systemctl start zou
    sudo systemctl start zou-events
    sudo systemctl restart nginx

## Update zou package 
    cd /opt/zou
    sudo /opt/zou/zouenv/bin/pip3 install --upgrade zou

## Update database schema

    cd /opt/zou
    sudo -u zou DB_PASSWORD=$DB_PASSWORD /opt/zou/zouenv/bin/zou upgrade-db

## Restart Zou service

    sudo chown -R zou:www-data .
    sudo systemctl restart zou
    sudo systemctl restart zou-events



## checkpoint

 At this point you can test zou api using tools like postman. 
 API Reference: https://myzoudomain.com/api



## Deploying Kitsu

    cd /opt/
    sudo git clone -b build https://github.com/cgwire/kitsu
    cd kitsu
    sudo git config --global --add safe.directory /opt/kitsu
    sudo git checkout build

## Re-configure Nginx

    sudo nano /etc/nginx/sites-available/zou

Overwrite file as follows

    server {
        listen $PORT;
        server_name kitsu-prism.com; 

            location /api {
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Host $host;
            proxy_pass http://localhost:5000/;
            client_max_body_size 500M;
            proxy_connect_timeout 600s;
            proxy_send_timeout 600s;
            proxy_read_timeout 600s;
            send_timeout 600s;
        }

        location /socket.io {
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
            proxy_pass http://localhost:5001;
        }

        location / {
            autoindex on;
            root  /opt/kitsu/dist;
            try_files $uri $uri/ /index.html;
        }
    }

## Restart nginx

    sudo systemctl restart nginx

## To update Kitsu

    cd /opt/kitsu
    sudo git reset --hard
    sudo git pull --rebase origin build

## Add Admin User
    cd /opt/zou/
    sudo -u zou DB_PASSWORD=$DB_PASSWORD /opt/zou/zouenv/bin/zou create-admin $ZOU_ADMIN_USER --password $ZOU_ADMIN_PASS


## Initialize data 

    cd /opt/zou/
    sudo -u zou DB_PASSWORD=$DB_PASSWORD /opt/zou/zouenv/bin/zou init-data