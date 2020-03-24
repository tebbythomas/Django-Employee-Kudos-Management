# Employee Kudos Management Portal using Django

An application that enables employees to give kudos to their colleagues in their organisation
<br />
<br />
<h2>Some of the features included:</h2>
<li>Registering and Login of employees</li>
<li>Giving kudos to only their colleagues</li>
<li>Uploading employee details and kudos details in bulk</li>
<li>Allocating a certain number of kudos for each employee each week</li>
<li> Resetting the kudos count at the end of the week</li>
<li>Using partials, base html file for template code modularity</li>
<li>Using Django alert messages for success and error messages</li>
<li>Admin section - allowing an admin/superuser to perform CRUD operations on employee, employee profile, company, kudos information</li>
<li>Using both frontend and DB constraints and checks</li>
<br />
<br />
<h2>Technical Details:</h2>
<br />
<br />
<b>Frontend:</b> HTML, JS, CSS (Bootstrap theme: https://bootswatch.com/cosmo/)
<br />
<b>Framework:</b> Python, Django authentication, messages, etc
<br />
<b>Database:</b> SQLite
<br />
<br /> 
<h2>Models used:</h2>
<br />
<br />
<b>User</b> (first_name, last_name, username, email, password)
<br />
<b>Profile</b> (user, company, kudosCount, kudosLastUpdated)
<br />
<b>Company</b> (name)
<br />
<b>Kudos</b> (fromColleague, toColleague, message, created_at)
<br />
<br />
<h2>Requirements of the app:</h2>
<br />
<a href="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/requirements.txt">Link</a>
<br />
<br />
<h2>To run the app:</h2>
<br />
<br />
<p>1. Clone the repo</p>
<br />
<pre><code>git clone https://github.com/tebbythomas/Django-Employee-Kudos-Management.git
</code></pre>
<br />
<br />
<p>2. Switch to project dir</p>
<br />
<pre><code>cd Django-Employee-Kudos-Management-master/
</code></pre>
<br />
<br />
<p>3. Create a python virtual environment</p>
<br />
<pre><code>python3 -m venv proj_env
</code></pre>
<br />
<br />
<p>4. Activate the environment</p>
<br />
<pre><code>source proj_env/bin/activate
</code></pre>
<br />
<br />
<p>5. Install requirements</p>
<br />
<pre><code>pip install -r requirements.txt
</code></pre>
<br />
<br />
<p>6. Switch to django project dir</p>
<br />
<pre><code>cd kudos_manager/
</code></pre>
<br />
<br />
<p>7. Make DB migrations</p>
<br />
<pre><code>python manage.py makemigrations
</code></pre>
<br />
<pre><code>python manage.py migrate
</code></pre>
<br />
<br />
<p>8. Create Django user to access the admin</p>
<br />
<pre><code>python manage.py createsuperuser
</code></pre>
<br />
<br />
<p>9. Run the project</p>
<br />
<pre><code>python manage.py runserver
</code></pre>
<br />
<br />
<p>10. Open <a href="http://localhost:8000">http://localhost:8000</a> in your browser</p>
<br />
<br />
<p>11. First upload sample employee data: Visit <a href="http://localhost:8000/upload/employees">http://localhost:8000/upload/employees</a> and upload following csv file:
<br />
<a href="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Sample_Data/Sample_Data_1/upload_employees_1.csv">Link</a>
<br />
<br />
<p>12. Next upload sample kudos data: Visit <a href="http://localhost:8000/upload/kudos">http://localhost:8000/upload/kudos</a> and upload following csv file:
<br />
<a href="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Sample_Data/Sample_Data_1/upload_kudos_1.csv">Link</a>
<br />
<br />
<p>Other sample csv files are here:</p>
<a href="https://github.com/tebbythomas/Django-Employee-Kudos-Management/tree/master/Sample_Data">Link</a>
<br />
<br />
<h2>Screenshots:</h2>
<br />
<br />
1. <b>Register Employee Page</b>:
<br />
<img src="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Screenshots/Register_Screen.png" hspace="20">
<br />
<br />
2. <b>Login Employee Page</b>:
<br />
<img src="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Screenshots/Login_Screen.png" hspace="20">
<br />
<br />
3. <b>Home Page / Dashboard</b>:
<br />
<img src="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Screenshots/Dashboard.png" hspace="20">
<br />
<br />
4. <b>Upload Employee Details</b>:
<br />
<img src="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Screenshots/Upload_Employees.png" hspace="20">
<br />
<br />
5. <b>Upload Kudos Details</b>:
<br />
<img src="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Screenshots/Upload_Kudos.png" hspace="20">
<br />
<br />
6.a. <b>To test Reset Kudos Count - First, login to the Admin Page->Profile table-> Choose user and change kudosLastUpdated Date to a previous week's date and save</b>:
<br />
<img src="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Screenshots/Manually_Changing_Date.png" hspace="20">
<br />
<br />
6.b. <b>To test Reset Kudos Count - Next, login and visit the homepage / dashboard of the same user, you will get an alert mentioning that the kudos count was reset</b>:
<img src="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Screenshots/Resetting_Kudos.png" hspace="20">
<br />