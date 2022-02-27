# Gratitude-Journal
This repo is a clone of the personal gratitude journal I have built based on the project found here: https://realpython.com/django-diary-project-python/. 
I have upgraded the styling, and will be adding more features as I progress. Download and make this journal your own. 

One amazing aspect of this project is the ability host this locally so that all of your data is YOURS! Don't be afraid to style this project as you see fit, it's your personal space. 

## How To Run `Gratitude-Journal`

Type the following commands into a terminal to create and activate a virtual environment and install the requirements:

```sh
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
```

Then run the database migrations and create a superuser:

```sh
$ python manage.py migrate
$ python manage.py createsuperuser
```

Finally, run the local Django development server:

```sh
$ python manage.py runserver
```

## To-DO
- Custom Color Options
- Mood Tracker(Bacend & Frontend)
- Change labels of form

## License

Distributed under the MIT license.
