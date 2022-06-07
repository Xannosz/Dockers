mkdir /logs/start && mkdir /logs/weekly && mkdir /logs/hourly
/script/runner.sh start >> /logs/start/`date +%F_%H.%M.%S`.log 2>&1
