# This is buildpack-run.sh
echo "Hello World"

pip3 install . ;
cd Brie ; pwd ; python3 manage.py runserver
