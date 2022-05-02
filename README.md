# Security Knowledge Management System or S-KMS
The purpose of S-KMS is to store and recover company information security expertise. The intended users would be company employees who utilize information systems on a regular basis. Users may also contribute to the knowledge-creation process by posting questions, thoughts, and solutions through the site.

# Description
The program is a Security Knowledge Management System wich the user to create username and password. The portal have a forum to fill out some of the security question that the other users can answer. You will be able to look the question by using the search function.The purpose of S-KMS is to store and recover company information security expertise. The intended users would be company workers who utilize information systems on a regular basis. Users can also contribute to the knowledge-creation process by submitting questions, thoughts, and solutions through the site. The User portal which allows the employee to Log in, sign up, and recover security credentials discussion forum for employees to Share security knowledge, answer questions, and provide insight and there is also a ranking system which differentiates privileges between employees and administrators which has the highest priority in views and reply in the discussion forum.

# User Stories 
* (Portal Navigation)  Different category of the security.
                        Diagrams showing the category. 
* (Search)             Utilize keywords to search for a specific question or answer. 
* (Reply)              Reply to a posted question.
* (Profile)            Add a bio or profile photo.
                      Change password within profile page.
* (Ranking System)     The system ranks the questions and puts the higher priority questions near the top of the list.
* (Login)              A portal in that allows the user to log into their account.
* (Signup)             Allows new users will be able to sign up using a unique password and username.


# Getting Started

## Dependencies
* Windowa 10
* macOS
* Ubuntu 20.04


## Install Django Framework
* Windows 10
   * If you have not installed Python 3, then please install Python 3
   * Upgrading Pip
   `
   python -m pip install --upgrade pip
   `
   * Creating a Project Directory
      * Change into your documents directory with the cd command
      `
      cd Documents
      `
      * Create the directory using the mkdir command
      `
       mkdir django_project
      `
      * Move into the django_project directory using the cd command
      `
       cd django_project      
      `
   * Creating the Virtual Environment
   `
   python -m venv venv
   `
   * Activating the Virtual Environment
   `
   venv\Scripts\activate
   `
   * Installing Django
   ``
   py -m pip install Django or pip install django==3.1
   ``

* macOS
   * If you have not installed Python 3, then please install Python 3
   ``
   brew install python3
   ``
   * Install pip or upgrade pip.
   `
    sudo easy_install pip
   `
   * Install virtual environment package virtualenv to isolate the Django project
   `
   sudo pip install virtualenv
   `
   * Install the Django framework using pip
   `
   sudo pip install django==3.0.1
   `
   
* Ubuntu 20.04
    * Update the package list
    `
    sudo apt update
    `
    * If you have not installed Python 3, then please install Python 3
    * Update the python version
    `
    python3 -V
    `
    * Install Django
    `
    sudo apt install python3-django
    `
    * Verify the install
    `
    django-admin --version
    `
    
## Install Pillow
* Window 10
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
or 
pip install pillow
```
* macOS
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
or 
pip3 install Pillow
```
* Ubuntu 20.04
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
or 
sudo apt install python-pi 
```

## Installing
* How to dowload S-KMS progrma
    * In the top-right corner is a green button that says Code, click on the button
    * Then, in the dropdown, select Download ZIP. All of the files will begin downloading to your computer, usually in your Downloads folder
    * Then, open your Downloads folder on your computer and find the ZIP file. You’ll want to right-click it and choose the option that says Extract All…, Unzip, or   Uncompress, and then select a folder where you want the files to end up
    * Finally, navigate to that selected folder, and you’ll find all of those Github files that we downloaded right there
* Where to download S-KMS program
    * All of the files will begin downloading to your computer, usually in your Downloads folder
    * Move the folder to documents

## Executing program
* How to run the S-KMS
    * Change the directory to were the folder is located
        * Window 10
        `
        cd Downloads\S-KMS
        `
        * macOS
        `
        cd ~Downloads/S-KMS
        `
        * Ubuntu 20.04
        `
        cd ~Downloads/S-KMS
        `
    * Run the server
    ```
    python .\manage.py runserver or python manage.py runserver
    ```
## Other Command
* Create a admin
```
python .\manage.py createsuperuser or python manage.py createsuperuser
```
* Make migration
```
python .\manage.py makemigrations or python manage.py makemigrations
```
* Migrate
```
python .\manage.py migrate or python manage.py migrate
```
* collect static file
```
python .\manage.py collectstatic or python manage.py collectstatic
```
* change password
```
python .\manage.py changepassword <username> or python manage.py changepassword <username>
```

# Authors
Contributors names

1. Roshin Roychan 
    * [@TheRoshin](https://github.com/TheRoshin)
2. William Lovelace
    * [@WilliamKL](https://github.com/WilliamKL)
3. Jaquavious Gotel
    * [@jgote1198](https://github.com/jgotell98)
4. Ankush Singh
    * [@KushAnku](https://github.com/KushAnku)




