import os

name=input("Enter template name: ")


directory="templates"

filepath=os.path.join(directory,f"{name}.html")

os.makedirs(directory,exist_ok=True)

with open(filepath,'w') as f:
    f.write("""{% extends "base.html" %}

{% block headtitle %}
      
{% endblock %}

{% block title %}
     
{% endblock %}

{% block intro %}

{% endblock %}

{% block content %}

{% endblock %}

{% block conclusion %}

{% endblock %}

{% block prev %}
    <a href="">Prev</a>
{% endblock %}

{% block next %}
    <a href="">Next</a>
{% endblock %}
        """
    )