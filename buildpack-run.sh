# This is buildpack-run.sh
echo "Hello World"

apt-get update
apt-get install python3.6
apt-get install python3-pip
python3 --version
pip3 --version
