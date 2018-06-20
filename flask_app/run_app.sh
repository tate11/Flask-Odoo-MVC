echo "###############################################################################"
echo "                              Running Flask App  v1.0                              "
echo "###############################################################################"

file="db.conf"

# Functions to be used in configurations

function flask_config_db() {
  echo ""
  echo " Getting database configs....."
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter RDBMS type:"
  read db_type
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter host name/ip:"
  read db_host
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter Database name:"
  read db_name
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter Database user:"
  read db_user
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter Database password:"
  read db_passwd
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter Database port:"
  read db_port
  echo "-----------------------------------------------------------------------------"
  echo "$db_type://$db_user:$db_passwd@$db_host:$db_port/$db_name" > db.conf
  echo "DB configs saved to db.conf file successfully!!!"
  echo ""
  export FLASK_APP=$flask_app
  export DATABASE_URL='$db_type://$db_user:$db_passwd@$db_host:$db_port/$db_name'
  export FLASK_DEBUG=$debug
  export FLASK_ENV=$mode

  echo "Running flask project....."
  flask run
}


function flask_run() {
	if [ -s "$file" ]
  then
    db_access=$(head -n 1 $file)
    export FLASK_APP=$flask_app
    export DATABASE_URL=$db_access
    export FLASK_DEBUG=$debug
    export FLASK_ENV=$mode
    echo "Running flask project....."
    flask run

  else
    flask_config_db

fi
}



echo "                          Get Flask Application Configs"
echo "-------------------------------------------------------------------------------"
echo "(+) Enter main flask app file:"
read flask_app
echo "-------------------------------------------------------------------------------"
echo "(+) Enter mode to use (development or production):"
read mode
echo "-------------------------------------------------------------------------------"
echo "(+) Enter debug (True or False):"
read debug
echo "-------------------------------------------------------------------------------"
echo ""
echo "###############################################################################"

if [ -f "$file" ]
then
    flask_run
else
    flask_config_db
fi
