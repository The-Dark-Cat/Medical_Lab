<html lang="EN">
<body>
<h2>Medical Lab</h2>
<p>
<h3>About project</h3>
<a>This is a test work. 
The project is based on Django and is a REST API with an admin panel. 
We have doctors and their specializations. 
Through the admin panel, you can add and change information about doctors and specializations, sort them. 
Through the API, information is received with the possibility of filtering and sorting</a>
<p>
<h3>API Routing</h3>
<a>
<ul>
<li>http://127.0.0.1:8000/doctors/doctors_list/
<p>Return list of a doctors<br>Params:<br>
<ul>
<li>ordering: sort by field (can sort by work_experience, name, date_of_birth)<br>
<li>min_work_experience: filter by minimal work experience</li>
<li>specialization_name: filter by specialization name</li>
<li>name: filter by name</li>
<li>date_of_birth: filter by date of birth</li>
<li>date_of_employment: filter by date of employment</li>
</ul>
</li>
<li>http://127.0.0.1:8000/doctors/doctors_details/&lt doctor_id &gt/<br>
<p>Returns full information about the doctor by id<br></p></li>
<li>http://127.0.0.1:8000/doctors/specializations_list/<br>Return list of specializations<br></li>
</ul>
</a>
<p>
<h3>Install</h3>
<a>
<ul>
<li>install docker and docker-compose if you have`nt installed docker</li>
<li>run "docker-compose up -d db" for run database</li>
<li>run "docker-compose run django python manage.py makemigrations" for create migrations files</li>
<li>run "docker-compose run django python manage.py migrate" for apply migrations</li>
<li>run "docker-compose run django python manage.py createsuperuser" for create admin user</li>
<li>run "docker-compose up runserver" for run the server</li>
<li>run "docker-compose up tests" for running REST API tests</li>
</ul>
</a>
</body>
</html>