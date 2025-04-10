import os
from Database.Gemini import gemini


genai=gemini()

name=input("Enter template name: ")

query=input("Enter topics article is going to generate for: ")

genai.ArticleGenarate(query)

directory="templates"

intro="""{% extends "base.html" %}

{% block headtitle %}
      
{% endblock %}

{% block title %}
     
{% endblock %}

{% block intro %}

{% endblock %}
"""

contentbegin="""
{% block content %}
"""

if type(genai.GetQuery(query))==type([]):
    response=genai.GetQuery(query)[0]
else:
    response="trying again"
contentend="""
{% endblock %}
"""

conclusion="""
{% block conclusion %}

{% endblock %}

{% block prev %}
    <a href="">Prev</a>
{% endblock %}

{% block next %}
    <a href="">Next</a>
{% endblock %}
"""

filepath=os.path.join(directory,f"{name}.html")

os.makedirs(directory,exist_ok=True)

with open(filepath,'w') as f:
    f.write(intro+contentbegin+response+contentend+conclusion)