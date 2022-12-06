
# Prepare environments

```bash
# Create + activate venv
if [ ! -d venv ]
then
    python -m venv venv
fi
source venv/bin/activate

# Start mysql
# If the container doesn't exist:
docker run --name django-mysql -e MYSQL_ROOT_PASSWORD=toor -d mysql:8.0
# If the container already exists:
docker start mysql

# Install necessary python packages
pip install -r requirements.txt
# or 
# pip install Django
```

# Start a webserver without Django

## WSGI

```bash
cd nofw
python start.py
```

## Static files

```
python -m http.server
```

# Create a Django project

```bash
django-admin startproject mysite
django-admin startapp polls
```

# Run a Django project

```bash
cd mysite
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Accessing API shell

```bash
python manage.py shell
```

```python
from polls.models import Choice, Question
from django.utils import timezone

# insert
# SQL: INSERT INTO polls_question(question_text, pub_date) VALUES ('What\'s new?', now)
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id


q.question_text
q.pub_date

# update
# SQL: UPDATE polls_question SET question_text = 'What\'s up?' WHERE id=1
q = Question.objects.get(id=1)
q.question_text = "What's up?"
q.save()

# filter

# SQL: SELECT * FROM polls_question WHERE id=1
Question.objects.get(id=1) # hasilnya Question

# handle error (in case of data not found)
try:
    q = Question.objects.get(id=1) # hasilnya Question
except Exception as e:
    print('data not found')

# SQL: SELECT * FROM polls_question WHERE question_text='What\'s new?'
Question.objects.filter(question_text="What's new?") # hasilnya QuerySet

# SQL: SELECT * FROM polls_question WHERE not (question_text='What\'s new?')
Question.objects.exclude(question_text="What's new?") # hasilnya QuerySet

# SQL: SELECT * FROM polls_question WHERE question_text LIKE='%new?%'
Question.objects.filter(question_text__contains='new')
# more: https://docs.djangoproject.com/en/4.1/ref/models/querysets/#methods-that-return-new-querysets

# SQL: SELECT * FROM polls_question order by id asc
Question.objects.order_by('id')
# SQL: SELECT * FROM polls_question order by id desc
Question.objects.order_by('-id')

# SQL: SELECT * FROM polls_question LIMIT 5 OFFSET 10
Question.objects.all()[10:15]

# SQL: SELECT * FROM polls_question
Question.objects.raw("SELECT * FROM polls_question")

# delete
# SQL: DELETE polls_question WHERE id=1
q = Question.objects.get(id=1)
Question.delete(q)
```

# Creating super user

```bash
python manage.py createsuperuser
```