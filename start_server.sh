cd interface
ls -la
python3 manage.py migrate
echo "server running at port 8008"
echo "Author = $AUTHOR"
python3 manage.py runserver 0.0.0.0:8008