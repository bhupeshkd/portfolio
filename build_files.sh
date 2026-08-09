echo "BUILD START"
pip install -r requirements.txt --break-system-packages
python manage.py collectstatic --noinput --clear
echo "BUILD END"