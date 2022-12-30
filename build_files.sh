# build_files.sh

echo " BUILD START"
python 3.8 pip install -r requirements.txt
Python 3.8 manage.py collectstatic --noinput --clear
echo " BUILD END"