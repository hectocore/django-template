# Django Template
Django template for new projects, using cookiecutter.

## Django Features
This template includes multiple extra-features over a regular Django.
- [x] Possibility to use the email to login (username still available)
- [x] Customized admin style
- [x] Multi-files settings for more readability
- [x] Specific `production.py` and `development.py` in addition to other settings (reduce duplicated params)

## Usage
First, you will need to have [cookiecutter](https://github.com/cookiecutter/cookiecutter) installed:
```
$ pip install cookiecutter
```

Then, run the following command to create a project:
```
cookiecutter https://github.com/hectocore/django-template
```
