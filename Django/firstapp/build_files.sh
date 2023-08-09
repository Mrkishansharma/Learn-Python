echo " BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
myenv/Scripts/activate
echo " BUILD END"