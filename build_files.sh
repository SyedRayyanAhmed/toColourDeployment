# build_files.sh

echo " BUILD START"
python3.8 pip install -r requirements.txt
Python3.8 manage.py collectstatic --noinput --clear
echo " BUILD END"