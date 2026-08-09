echo "BUILD START"
python3.12 -m pip install -r requirements.txt --break-system-packages
python3.12 manage.py collectstatic --noinput
mkdir -p staticfiles_build
echo "BUILD END"