# Health Booklet digitalization
Instructions to run the software

1. First Clone the repository in your local machine
2.Open terminal in directory in which you have downloaded the code.
3. Run the following Code to download the dependencies:
  $ pip install -r requirement.txt
4. Now to make database migrations run: 
  $ python3 manage.py makemigrations
5. Then run command
  $ python3 manage.py migrate
6. Now to run the website run :
  $ python3 manage.py runserver
7. now in your browser enter the following url to access website:
 "http://127.0.0.1:8000/"

You can create all users but Admin is fixed choose below credentials to access the Admin:
    admin ID: Admin
    admin Password: Admin
