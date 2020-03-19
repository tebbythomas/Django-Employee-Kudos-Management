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
<p>Clone the repo</p>
<br />
<pre><code>git clone https://github.com/tebbythomas/Django-Employee-Kudos-Management.git
</code></pre>
<br />
<br />
<p>Switch to project dir</p>
<br />
<pre><code>cd Django-Employee-Kudos-Management/
</code></pre>
<br />
<br />
<p>Create a python virtual environment</p>
<br />
<pre><code>python3 -m venv proj_env
</code></pre>
<br />
<br />
<p>Activate the environment</p>
<br />
<pre><code>source proj_env/bin/activate
</code></pre>
<br />
<br />
<p>Install requirements</p>
<br />
<pre><code>pip install -r requirements.txt
</code></pre>
<br />
<br />
<p>Switch to django project dir</p>
<br />
<pre><code>cd kudos_manager/
</code></pre>
<br />
<br />
<p>Make Python migrations</p>
<br />
<pre><code>python manage.py makemigrations
</code></pre>
<br />
<pre><code>python manage.py migrate
</code></pre>
<br />
<br />
<p>Create Django user to access the admin</p>
<br />
<pre><code>python manage.py createsuperuser
</code></pre>
<br />
<br />
<p>Run the project</p>
<br />
<pre><code>python manage.py runserver
</code></pre>
<br />
<br />
<p>Open http://localhost:8000 in your browser</p>
<br />
<br />
<p>To upload sample employee data, visit http://localhost:8000/upload/employees and upload following csv file:
<br />
<a href="#"></a>
<br />
<br />
<p>To upload sample kudos data, visit http://localhost:8000/upload/kudos and upload following csv file:
<br />
<a href="#"></a>
<br />
<br />
<p>Other sample csv files are here:</p>
<br />
<a href="#"></a>
<br />
<br />
<b>Screenshots:</b>
<br />
1. <b>Register Employee Page</b>:
<br />
<img src="https://github.com/tebbythomas/Django_Blog_Project/blob/master/Screenshots/blog-register_user.png" hspace="20">
<br />
<br />
2. <b>Login Employee Page</b>:
<br />
<img src="https://github.com/tebbythomas/Django_Blog_Project/blob/master/Screenshots/blog-login.png" hspace="20">
<br />
<br />
3. <b>Home Page / Dashboard</b>:
<br />
<img src="https://github.com/tebbythomas/Django_Blog_Project/blob/master/Screenshots/blog-home_page.png" hspace="20">
<br />
<br />
4. <b>Upload Employee Details</b>:
<br />
<img src="https://github.com/tebbythomas/Django_Blog_Project/blob/master/Screenshots/blog-add_post.png" hspace="20">
<br />
<br />
5. <b>Upload Kudos Details</b>:
<br />
<img src="https://github.com/tebbythomas/Django_Blog_Project/blob/master/Screenshots/blog-post_page.png" hspace="20">
<br />
<br />