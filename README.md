# Django team manangement application 
<div align="center">
<p>A very simple implementation of team management application using Django.</p>

<img height="466px" width="403.3px" src="https://user-images.githubusercontent.com/46719079/178118460-04f023c5-9db6-405e-849e-bfcd9552ace3.gif">
</div>

## Setup guide
Setup virtual environment:
```sh
python -m venv venv/
venv/script/Activate
```
Install requirements:
```sh
pip install -r requirements.txt
```
Generate a Django secret key using [Djecrety](https://djecrety.ir/) or any similar services. Then:
```sh
echo "DJANGO_SECRET_KEY=YOUR_SECRET_KEY" >> .env
echo "DEBUG=False" >> .env
```
Apply migrations (migration file already generated, no need to run `makemigrations` again):
```sh
python manage.py migrate
```
And run the local development server:
```
python manage.py runserver
```
The app will be available at `127.0.0.1:8000`

## Development guide
This repo uses [pre-commit](https://pre-commit.com/) to enforce code quality. 
Hooks can be found at [.pre-commit-config.yaml](https://github.com/alexnguyenn/django-team-management/blob/master/.pre-commit-config.yaml)

To develop using pre-commit, simply run:
```bash
pre-commit install
```
