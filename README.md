### INF601 - Advanced Programming in Python
### Benjamin Odell
### Mini Project 4
 
 
# Note Web App
 
This is a simple web app for taking notes. You can create, edit, and delete note. There is also a public visibility toggle for you let everyone view your note

 
## Getting Started
 
### Dependencies

install the python dependencies with the command
```angular2html
pip install -r requirements.txt
```
 
### Installing
 
Make sure to CD into the folder with the manage.py file<br>
Run the command
```angular2html
python manage.py makemigrations
```
* This makes  the SQL that we need for the database<br>
Then run the command to apply the migration
```angular2html
python manage.py migrate
```

* You can set up the admin account with the command
```angular2html
python manage.py createsuperuser
```
 
### Executing program

Now you can run the server by running the command
```
python manage.py runserver
```

You can then access the site at [localhost:8000](http://localhost:8000/)<br>
You can find the admin page at [localhost:8000/admin](http://localhost:8000/admin)


 
## Authors

Benjamin Odell - benjamin.m.odell@proton.me

## Acknowledgments
 
Inspiration, code snippets, etc.
* [Django Docs](https://www.djangoproject.com/start/)
* [Bootstrap v5.3 Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Deep Seek Chat: used for homepage text](https://chat.deepseek.com/share/0d5xc5w2xrp8xurvwz)