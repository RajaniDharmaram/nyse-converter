source /home/rajani_d/nyse-converter/nc-venv/bin/activate
export SRC_DIR=/home/rajani_d/nyse-converter/data/nyse_all/nyse_data
export LOG_FILE_PATH=/home/rajani_d/nyse-converter/logs/nc.log
rm -rf /home/rajani_d/nyse-converter/data/nyse_all/nyse_json
mkdir -p /home/rajani_d/nyse-converter/logs
nysec
deactivate