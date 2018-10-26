# lumis

This tool creates a JSON output that can be used as input for [brilcalc](https://cms-service-lumi.web.cern.ch/cms-service-lumi/brilwsdoc.html).

It does so by accessing the Tracker workspace of the Run Registry via a [custom Run Registry client](https://github.com/ptrstn/python-runregistryclient).
The website is deployed using [OpenShift](http://information-technology.web.cern.ch/services/PaaS-Web-App) (CERN web services) and can be accessed via [http://lumis.web.cern.ch/](http://lumis.web.cern.ch/). 

Currently only the *Tracker* workspace is supported. 

Feel free to contribute by creating [issues](https://github.com/ptrstn/lumis/issues) or [pull requests](https://github.com/ptrstn/lumis/pulls).

## Develop

Following steps need to be done to develop on this project:

### Prerequisites

- Python 3.5 or Python 3.6
- Access to the CERN GPN 

### Clone the project

```bash
git clone https://github.com/ptrstn/lumis.git
cd lumis
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

On Linux:

```bash
source venv/bin/active
```

On Windows:

```bash
venv\Scripts\active
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Setup environment variables

You can generate a secret key with web tools like [this](https://www.miniwebtool.com/django-secret-key-generator/).

#### Option 1:

Export DJANGO_SECRET_KEY environment variable

```
DJANGO_SECRET_KEY=&ij2_mx6*jw)zkpzdkejcyw(d!e-xo%*)ljq*_ozqjh^p^5-!v
```

#### Option 2 (recommended):

Create a ```.env``` file containing the environment variables

```bash
echo "DJANGO_SECRET_KEY=^4u&cx=kn24gjaw)(q2vw56tgnadyhok0!!pdjf38ndr5bajci" > .env
```

Make sure that you never commit the ```.env``` file, so that your secret key is not revealed.

### Collect static files

```bash
python manage.py collectstatic
```

Rerun this command whenever you make changes to static files.

### Run project

```bash
python manage.py runserver
```

The website can then be accessed locally at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Links

- http://lumis.web.cern.ch/
- https://github.com/valdasraps/resthub
- https://github.com/ptrstn/python-runregistryclient
- https://docs.djangoproject.com/en/1.11/intro/tutorial01/