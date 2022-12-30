# build_files.sh

echo " BUILD START"
pip install -r requirements.txt
Python3.8 manage.py collectstatic
echo " BUILD END"