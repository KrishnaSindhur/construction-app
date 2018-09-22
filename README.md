# construction-app
simple django apis for construction like industry<br>

This django using python 3 so python 3 must be installed along with pip<br>

Once the repository is cloned then we can install all libraries by <br>
$ pip install -r requirements.txt<br>

so then you can run app from inside cloned directory<br>
$ python src/manage.py runserver<br>

## APIs

### To download all activities from masterplan

http://127.0.0.1:8000/api/activity/ <br>

### To View activities start date and end date

http://127.0.0.1:8000/api/activitydates/{activity}<br>

### To download activities sorted by WBS 

http://127.0.0.1:8000/api/sortedactivity/ <br>

### To download sorted master plan based on start date and WBS

http://127.0.0.1:8000/api/sortedmasterplan/<br>


