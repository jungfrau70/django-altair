# Django altair

Django app that provide a simple template tag to render an altair chart into a django template.

## Installation

Currently the `django-altair` is not yet on pypi. To install the library run

```
pip3 install .
```

## Usage
```
INSTALLED_APPS = (
    ...,
    'django_altair',
)
```

In your view
```
from django.views.generic import TemplateView
from django.shortcuts import render
from vega_datasets import data

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = locals()
        source = data.cars()

        context['chart'] = alt.Chart(source).mark_circle().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin'
        ).interactive()
        return render(request, self.template_name, context)
```

and in your template use
```
{% load django_altair %}

<div>
    {% render_chart chart %}
</div>
```
to render chart.

The following script-tags must be included
```
<script src="https://cdn.jsdelivr.net/npm//vega@3.2"></script>
<script src="https://cdn.jsdelivr.net/npm//vega-lite@2.4.1"></script>
<script src="https://cdn.jsdelivr.net/npm//vega-embed@3.0"></script>
```

  912  ll
  913  python manage.py runserver
  914  python manage.py migrate
  915  python manage.py runserver
  916  python manage.py migrate
  917  python manage.py runserver
  918  python manage.py makemigrates
  919  python manage.py makemigrations
  920  python manage.py migrate
  921  python manage.py runserver
  922  python manage.py collectstatic
  923  python manage.py runserver
  924  history