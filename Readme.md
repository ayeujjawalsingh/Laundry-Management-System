<h1 align="center" > Hi 👋🏻, I'm Ujjawal Singh </br> 
</h1>

<p align="center">
<a href="https://auth.geeksforgeeks.org/user/ayeujjawalsingh/practice" target="_blank"><img alt="" src="https://img.shields.io/badge/GeeksforGeeks-000?logo=GeeksforGeeks&logoColor=2FF200&style=for-the-badge" style="vertical-align:center" /></a>
<a href="https://linkedin.com/in/ayeujjawalsingh" target="_blank"><img alt="" src="https://img.shields.io/badge/LinkedIn-000?logo=linkedin&logoColor=0A66C2&style=for-the-badge" style="vertical-align:center" /></a>
<a href="https://github.com/ayeujjawalsingh" target="_blank"><img alt="" src="https://img.shields.io/badge/Github-000?logo=github&logoColor=0A66C2&style=for-the-badge" style="vertical-align:center" /></a>
<a href="https://leetcode.com/ayeujjawalsingh/" target="_blank"><img alt="" src="https://img.shields.io/badge/Leetcode-000?logo=leetcode&logoColor=FFF926&style=for-the-badge" style="vertical-align:center" /></a></p>

# <p align="center" >`Project Installations in Local System`</p>
## `Tools & Technology Required`

- Python
- Django
- HTML
- CSS
- Javascript

## `Run Locally`

- Download the Project and Unzip it
- Open Commant Prompt
> You must have Python3 installed in your system


Go to the project directory
```bash
    cd Laundry-Management-System
```

Create Virtual Envoirnment of Python
```bash
    pip install virtualenvwrapper-win
```

Make Virtual Envoirnment as I named it `venv`
```
    mkvirtualenv venv
```
Open Virtual Envoirnment as

```bash
    workon venv
```

<!-- Install Dependencies

```bash
    pip install -r requirenments.txt
```

Start the Server
```bash
    python manage.py runserver
``` -->

>   Development Server started at `localhost:8000`

<hr>

# <p align="center"> `Development Documentations`</p>

**Install Django in Virtual Envoirnment**

## `Installation`
Run this command to install `virtual wrapper` which will allows you to make virtual envoirnment
```
pip install virtualenvwrapper-win
```

Make Virtual Envoirnment as name `venv`
```
mkvirtualenv venv
```

Open the Command Prompt in Project Directory as
F:\Users\Ujjawal\Coding\Developement> `workon venv`

```
workon venv
```

Install `Django` in Virtual Envoirnment as
(venv) F:\Users\Ujjawal\Coding\Developement>pip install django
```
pip install django
```

Run this to Check `django-admin` Available Subcommands:
```
django-admin
```

Now, Create Django-Project by using django-admin subcommands
as `django-admin startproject` (projectName)
```
django-admin startproject project
```

Then Change you directory inside the folder name `project`
<hr>

## `Setup files and folders`
Now, create django app as `python manage.py startapp` (appName)
```
python manage.py startapp backend
```

Add this folder `backend` in `setting.py` file of our `project` file inside INSTALLED_APPS
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend', # Added here
]
```

Now, Add Static files and urls in same file as (static file created by us to store all static webpage contents)
`import os`
```python
STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
```

Now, open `urls.py` file of `project` folder

Add urls of `backend` file as

`import include` from `django.urls`
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('backend.urls')), # Added here
]
```
<hr>

### urls.py
Create `urls.py` file in `backend` folder
```python
from django.urls import path
from . import views
```

> path will be use to make `urlpatterns`
> importing `views` from the same directory so we use ( . )

Now, create `urlpatterns` from routing from one path to other as
```python
from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('', views.home, name ='home'),
]
```
`path('address', function defined on views , name)`

<hr>

### Templates
Create a folder name `templates` in `backend` directory
Inside this folder, we will store all `html` file/templates


#### index.html
create a sample index.html file to display with your django development server as
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="{% static 'css/style.css'%}" rel="stylesheet">
</head>
<body>
    <h1>Hello Ujjawal Singh</h1>
</body>
</html>
```
<hr>

### Static
Create a folder name `static` in `backend` directory
Inside this folder, we will store all `css` `js` `img` and other files

#### css
Create folder as `css` in `static` directory and then create `style.css` file in `css` directory and write all css components there
and add this link in `head` tag of `index.html` as
```html
<link href="{% static 'css/style.css'%}" rel="stylesheet">
```

>Must add `{% load static %}` on `html` file to include the external `static` directory

<hr>

### views.py
define function in your views as
```python
from django.shortcuts import render

def home(request):
    return render(request, 'templates/index.html')
```
`return render( request , return )`

> In this file, we will define our all function and backend logic to render it to the output screen

# <p align="center">`Project Demonstration`</p>

## `Signup`

![Home Screenshot](./Image/Sign_Up.png)

## `Signin`
![Service Screenshot](./Image/Sign_In.png)

## `Home Page`
![Laundry Management System](./Image/Home_Page.png)
![Laundry Management System](./Image/Home_Page_Down.png)

## `Laundry Request`
![Laundry Management System](./Image/Request.png)
![Laundry Management System](./Image/Request%20_Fill.png)

## `Laundry Request Submission`
![Laundry Management System](./Image/Request_Result.png)

## `Laundry Status`
![Laundry Management System](./Image/Status.png)

## `Laundry Status Result`
![Laundry Management System](./Image/Status_Result.png)

## `About us`
![Laundry Management System](./Image/About_Us.png)

## `Admin Signin Page`
![Laundry Management System](./Image/Admin_SignIn.png)

## `Admin Home Page`
![Laundry Management System](./Image/Admin_Home_Page.png)

---
## Video 

https://user-images.githubusercontent.com/86152228/212467229-277be5ab-031c-4301-9cd8-935bd889a6af.mp4

