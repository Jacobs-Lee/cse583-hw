mkdir pronto
cd pronto
echo "This folder contains Pronto trip data" > README.txt

mkdir data
cd data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head 2015_trip_data.csv
