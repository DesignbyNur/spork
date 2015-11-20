#!/bin/bash
# wp installed on 1and1
. ~/.bash_profile
dir=$(basename $(pwd) )
name=${dir//.*}
# 8 char limit?
dbname=${name}
echo wp core download

echo setup database
/usr/local/mysql/bin/mysql << EOSQL
drop DATABASE  IF  EXISTS ${dbname};
CREATE DATABASE IF NOT EXISTS ${dbname} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
EOSQL
rm -f wp-config.php
wp core download
wp core config --dbname=${dbname} --dbuser=robroy --dbpass=Nur4ever  --dbhost=localhost 

wp core  install --url=http://localhost/${name} --title="${name} client demo"   --admin_user=DBNAdmin --admin_password=Nur4ever --admin_email=me@robert-e-roy.com

wp plugin  delete hello
wp plugin  delete akismet
wp plugin install  captcha 
exit
wp plugin install --activate  si-contact-form  hide-comments-feature list-category-posts wp-lightbox-2 disable-comments si-contact-form title-remover wordpress-importer
wp theme install --activate  ~/DBN-Themes/DBN-Easy.zip
wp theme list
