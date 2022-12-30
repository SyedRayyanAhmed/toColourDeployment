# build_files.sh

echo " BUILD START"
python3.9 pip install -r requirements.txt
Python3.9 manage.py collectstatic --noinput --clear
echo " BUILD END"