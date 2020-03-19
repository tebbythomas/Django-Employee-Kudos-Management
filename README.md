# Employee Kudos Management Portal using Django

An application that enables employees to give kudos to their colleagues in their organisation
<br />
<br />
Some of the features included:
<li><b>Registering and Sign ins of employees</b></li>
<li><b>Give kudos to only their colleagues</b></li>
<li><b>Uploading employee details and kudos details in bulk</b></li>
<li><b>Allocating a certain number of kudos for each employee each week and resetting the kudos count at the end of the week</b> </li>
<li><b>Using partials, base html file for template code modularity</b></li>
<li><b>Using Django alert messages for success or error messages</b></li>
<li><b>Admin section</b> - allowing an admin/superuser to perform any CRUD operation on employee, employee profile, company, kudos information</li>
<li><b>Using bootstrap for the front end</b></li>
<br />
<br />
Requirements of the app listed:
<br />
<a href="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/requirements.txt">Link</a>
<br />
<br />
<b>To run the app:</b>
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
<pre><code>cd Django-Employee-Kudos-Management/
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
<p>7. Make Python migrations</p>
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
<p>10. Open http://localhost:8000 in your browser</p>
<br />
<br />
<p>To upload sample employee data, visit http://localhost:8000/upload/employees and upload following csv file:
<br />
<a href="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Sample_Data/Sample_Data_1/upload_employees_1.csv">Link</a>
<br />
<br />
<p>To upload sample kudos data, visit http://localhost:8000/upload/kudos and upload following csv file:
<br />
<a href="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Sample_Data/Sample_Data_1/upload_kudos_1.csv">Link</a>
<br />
<br />
<p>Other sample csv files are here:</p>
<br />
<a href="https://github.com/tebbythomas/Django-Employee-Kudos-Management/tree/master/Sample_Data">Link</a>
<br />
<br />
<b>Screenshots:</b>
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
6.a. <b>Reset Kudos Count - Manually change date</b>:
<br />
<img src="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Screenshots/Manually_Changing_Date.png" hspace="20">
<br />
<br />
6.b. <b>Reset Kudos Count and alert screenshot</b>:
<img src="https://github.com/tebbythomas/Django-Employee-Kudos-Management/blob/master/Screenshots/Resetting_Kudos.png" hspace="20">
<br />