ls -la
cd interface
python manage.py migrate
echo "server running at port 8008"
echo "Author = $AUTHOR"
python manage.py runserver 0.0.0.0:8008