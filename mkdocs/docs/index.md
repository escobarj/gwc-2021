# KHS GWC Exercises

## Exercise 1

### Create your first Django web application

1. Log into your [PythonAnywhere](https://www.pythonanywhere.com) account.
1. Select **Web** from the navigation menu.
1. Click the **Add a new web app** button.
    1. Click next on the first section called **Your web app's domain name**.
    2. Select **Django** from the list of web frameworks.
    3. Select **Python 3.8** from the Python version options.
    4. Name your project `gwc_site` and leave the directory as is.
    5. Wait a bit while your web app is created.

### Use `git` to `clone` our starter project from GitHub into your work space

1. Select **Consoles** from the navigation menu.
2. Under **Start a new console**, select **Bash**.
3. Enter the following commands into the console. Press enter after each one.
    1. `rm -rf gwc_site/*`
    1. `git clone https://github.com/escobarj/gwc-2021.git gwc_site`

### Update the code to work with your PythonAnywhere account

1. Select **Files** from the navigation menu.
2. Browse to the `gwc_site/gwc_site` folder.
3. Select the `settings.py` file to open it in a file editor.
4. Find the line `ALLOWED_HOSTS = ['escobarj.pythonanywhere.com']` and replace `escobarj` with your own PythonAnywhere username.
5. Save the file.
6. Select **Web** from the navigation menu.
7. Click the green reload button.
8. Check that the web site is working by clicking the web link above the reload button.

### Experiment with html elements

#### `<h1>` Heading. 1-6 different levels. 1 being the largest
`<h1>This is a heading</h1>`
`<h2>This is a subheading</h2>`

#### `<p>` Paragraph
`<p>This is a block of text</p>`

#### `<a>` Anchor, a.k.a link
`<a href="http://www.girlswhocode.com">Visit this site</a>`

#### `<br>` Line break
`<p>This is a block of text<br>has a line break in it</p>`

#### `<img>` Image
`<img src="dog.jpg" alt="A cute dog" width="500" height="600">`

#### `<em>` Emphasis, a.k.a italics
`<p>This <em>word</em> will be emphasized in italics.</p>`

#### `<strong>` Strong, a.k.a bold
`<p>This <strong>word</strong> will be bold.</p>`

More html tags [here](https://www.w3schools.com/html/default.asp)

### Experiment with css

[CSS color pallet](https://www.w3schools.com/colors/colors_palettes.asp)

## Exercise 2

### How to compare things in Python

* [https://tutorial.djangogirls.org/en/python_introduction/#compare-things](https://tutorial.djangogirls.org/en/python_introduction/#compare-things)

### Experiment with the "word count" page

1. Log into your [PythonAnywhere](https://www.pythonanywhere.com) account.
2. Go to the **Console** section and open a `bash` console.
   1. Type the following commands
      1. `cd gwc_site`
      2. `git pull`
3. Go to the **Files** section.
4. Open separate browser tabs for each of the following files;
    * gwc_site/gwc/views.py
    * gwc_site/gwc/templates/gwc/count.html
    * gwc_site/gwc/templates/gwc/result.html
5. Experiment with changes to the `count` and `result` fucntions in `views.py`
6. Experiment with changes to the `count.html` and `result.html` html template files

<!--
## Resources

* [Girls Who Code HQ](https://hq.girlswhocode.com)
* [PythonAnywhere](https://www.pythonanywhere.com)
* [Django Girls Tutorial](https://tutorial.djangogirls.org/en) -->


## Exercise 3

Use the info and code snippets below to create new pages for our website.

### Create a new page

Add a `route` so your new page can be found. In this example we'll add a page called `events`.

1. Add a new `path` to `gwc_site/gwc/url.py`
```python
urlpatterns = [
    ...
    path('events/', views.events, name='events'),
]
```
2. Add a new function in `gwc_site/gwc/views.py`
```python
def events(request):
    context = {'nav_events': 'active'}
    return render(request, 'gwc/events.html', context)
```
3. Add a the new events page to the navigation bar in `gwc_site/gwc/templates/gwc/base.html`
```html
<li class="nav-item">
 <a class="nav-link {{ nav_events }}" href="{% url 'events' %}">Events</a>
</li>
```
4. Create a new `html` file `gwc_site/gwc/templates/gwc/events.html` and enter the starter code below
```htmldjango
{% extends 'gwc/base.html'%}
{% load static %}

{% block content %}

<!-- The body of the page goes here
    between the "{% block content %}" and {% endblock %} -->

{% endblock %}
```
5. Reload your site so `django` can see that a the new page was added.

### Add content

After you have the new page created, you need to add the text, images, links, etc that will be the content of your new page.

You can use the `html` elements from [exercise 2](#exercise-2) and the new snippets below as a templates to add to you page.

You can add images either by uploading to `gwc_site/static/images/` or using a web link to an image already on the web.

All the examples below can be seen [here](https://escobarj.pythonanywhere.com/demo/)

## Small Image Card

```htmldjango
<div class="card" style="width: 18rem;">
  <img src="{% static 'images/dog.png' %}" class="card-img-top" alt="Picture of a dog">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a class="btn btn-primary btn-lg" href={% url 'home' %}>Home</a>
  </div>
</div>
```

## Large Image Card

```htmldjango
<div class="card mb-3">
  <img src="{% static 'images/dog.png' %}" class="card-img-top" alt="Picture of a dog">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
    <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
  </div>
</div>
```

## Horizontal Image Card

```htmldjango
<div class="card mb-3" style="max-width: 800px;">
  <div class="row g-0">
    <div class="col-md-4">
      <img src="{% static 'images/dog.png' %}" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a wider card with supporting text to the side as a natural lead-in to additional content. This content is a little bit longer.</p>
        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
      </div>
    </div>
  </div>
</div>
```

## Card Group

This example is a 3 card grouping, you can add or remove cards as needed.

```htmldjango
<div class="card-group">
   <div class="card" style="width: 18rem;">
     <img src="{% static 'images/dog.png' %}" class="card-img-top" alt="Picture of a dog">
     <div class="card-body">
       <h5 class="card-title">Small Image Card</h5>
       <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
       <a class="btn btn-primary btn-lg" href={% url 'home' %}>Home</a>
     </div>
   </div>
   <div class="card" style="width: 18rem;">
     <img src="{% static 'images/dog.png' %}" class="card-img-top" alt="Picture of a dog">
     <div class="card-body">
       <h5 class="card-title">Small Image Card</h5>
       <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
       <a class="btn btn-primary btn-lg" href={% url 'home' %}>Home</a>
     </div>
   </div>
   <div class="card" style="width: 18rem;">
     <img src="{% static 'images/dog.png' %}" class="card-img-top" alt="Picture of a dog">
     <div class="card-body">
       <h5 class="card-title">Small Image Card</h5>
       <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
       <a class="btn btn-primary btn-lg" href={% url 'home' %}>Home</a>
     </div>
   </div>
</div>
```

If you're interested in learning more about all the html elements you can create. We are using a "CSS framework" called Bootstrap and you can learn more about it at [https://getbootstrap.com](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
