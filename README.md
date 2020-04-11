# library
A library site made using django backend.
### Setup 
```bash
   git clone https://github.com/vcode11/library.git
   cd library
   python3 -m venv _venv
   . _venv/bin/activate
   pip install --upgrade pip3
   pip3 install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
```
### To run the  backend server:
```bash
   cd library
   . _venv/bin/activate
   python manage.py runserver
```
### Setup for React
```bash
    sudo apt-get install nodejs
    sudo apt-get install npm
    npm install -g create-react-app
```
### To bootstrap the react application
```bash
    create-react-app library
    cd library
```