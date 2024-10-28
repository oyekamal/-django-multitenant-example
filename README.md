# Django Multi-Tenant Example

This project demonstrates a multi-tenant setup in Django using the `django-tenants` package. The configuration uses Docker to manage a PostgreSQL database, which is optimized for multi-tenant architecture.

## Prerequisites

- **Docker**: Ensure Docker is installed on your machine.
- **Python**: Recommended version 3.8 or higher.
- **Django**: Latest version compatible with `django-tenants`.

## Project Requirements

To set up and run this project, you need the following packages installed:

- Django
- psycopg2-binary
- django-tenants

run the database:

```bash
sudo docker-compose up --build
```


These can be installed with:

```bash
pip install -r requirements.txt
```

Step 3: Applying Migrations

```bash
python manage.py migrate_schemas --shared
```


Step 4: Creating Tenants


```bash
sudo docker-compose exec web bash
python manage.py shell
```

### First Tenant:
```python
from customers.models import Client, Domain

# create your public tenant
tenant = Client(schema_name='public',
                name='Schemas Inc.',
                paid_until='2016-12-05',
                on_trial=False)
tenant.save()

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'localhost' # `my-domain.com`  don't add your port or www here! on a local server you'll want to use localhost here
domain.tenant = tenant
domain.is_primary = True
domain.save()
```


### Second Tenant:
```python
from customers.models import Client, Domain

# create your first real tenant
tenant = Client(schema_name='tenant1',
                name='Fonzy Tenant',
                paid_until='2014-12-05',
                on_trial=True)
tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'tenant.localhost' # don't add your port or www here!
domain.tenant = tenant
domain.is_primary = True
domain.save()
```

Step 5: Create a Superuser


```bash
python manage.py createsuperuser --schema=public
```

Step 6: Running the Development Server

You can run the Django development server locally:

```bash
python manage.py runserver
```

If you want the server to handle tenant-specific domains, you might need to configure your `/etc/hosts` file to map tenant domains to localhost for testing.

For example:

```bash
127.0.0.1 tenant.localhost
127.0.0.1 tenant`.example.com
```


# Useful Multi-Tenant Management Commands

## Create a Superuser for a Tenant:

```bash

python manage.py createsuperuser --schema=tenant1

```
Load Data for a Specific Schema:

```bash

python manage.py loaddata <your_data>.json --schema=tenant_name

```

Apply Migrations for All Tenants:

```bash

python manage.py migrate_schemas --tenant
```
Migrate Only Shared Applications:

```bash

python manage.py migrate_schemas --shared
```