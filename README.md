
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
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id


q.question_text
q.pub_date

# update
q.question_text = "What's up?"
q.save()

# filter
Question.objects.get(id=1)
Question.objects.filter(question_text="What's new?")
Question.objects.filter(question_text__contains='new')
Question.objects.raw("SELECT * FROM polls_question")

# delete
Question.delete(q)
```
