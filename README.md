

### Setup

```
conda create -n empapi_venv
conda activate empapi_venv
pip install -r requirements.txt

django-admin startproject emp_api .
django-admin startapp api_main
```



### Update your settings to reflect the following:

```py
INSTALLED_APPS = [
    'rest_framework',
    'api_main'
]



REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

SCHEDULER_CONFIG = {
    "apscheduler.jobstores.default": {
        "class": "django_apscheduler.jobstores:DjangoJobStore"
    },
    'apscheduler.executors.processpool': {
        "type": "threadpool"
    },
}
SCHEDULER_AUTOSTART = True

```

### Running the API


+ To get the payments report for the rest of the year: GET `api/api_main/getdata/` --body: empty
+ To get Employee details: POST `api/api_main/empdetails/` --body: {"emp_id": desired employee id}
+ To create new employee data: POST `api/api_main/newemp/` --body: {"emp_id": new id, "salary": new salary, "bonus": new bonus rate}
+ To edit a certain employee bonus rate: PUT `api/api_main/editbonus/` --body: {"emp_id": desired employee id, "new_bonus": new bonus}
+ To delete employee data: DELETE `api/api_main/delete/` --body: {"emp_id": desired employee id}




### Scheduling emailing to system admin

Make sure to edit these variables at `/api_main/scheduler.py`

+ `toaddr` : this shall have the admin's email, to whom the script shall report monthly payments 2 days before due
+ `fromaddr`: this shall have the user's email, from which we're going to send the reports
+ `password`: this shall have the user's email password to connect


