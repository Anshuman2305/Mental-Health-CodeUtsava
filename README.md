
<p align="center">
  <a>
    <h1 align="center">Mental Health - Team Vinci Code</h1>
    <p align="center">A Depression Detection WebApp using <a href="https://scikit-learn.org/stable/">Sklearn</a> and <a href="https://flask.palletsprojects.com/en/2.0.x/">Flask</a></p>
  </a>
</p>

<div align="center">

[![dsad](https://img.shields.io/badge/python-2.8.2-blueviolet.svg?style=for-the-badge)](https://www.python.org/)
[![dsad](https://img.shields.io/badge/Gunicorn-server-brightgreen.svg?style=for-the-badge)](https://gunicorn.org/)
[![dsad](https://img.shields.io/badge/Flask-Deployment-brightgreen.svg?style=for-the-badge)](https://flask.palletsprojects.com/en/2.0.x/)
[![dsad](https://img.shields.io/badge/Javascript-Website-brightgreen.svg?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![dsad](https://img.shields.io/badge/Sklearn-Training-brightgreen.svg?style=for-the-badge)](https://scikit-learn.org/stable/)    
[![dsad](https://img.shields.io/badge/Panda-Data_Analysis-brightgreen.svg?style=for-the-badge)](https://www.w3schools.com/python/pandas/default.asp)
[![dsad](https://img.shields.io/badge/Firebase-Realtime_Database-brightgreen.svg?style=for-the-badge)](https://firebase.google.com/?gclid=CjwKCAiAjoeRBhAJEiwAYY3nDB14zlhMZWk1DwLCUqBAe2-NluQew_fKtIZEzNfYav_C-MzRxPDOPhoC-RUQAvD_BwE&gclsrc=aw.ds)

    
</div>

<div style="text-align: justify">
    
To create an informative AI-based tool that should be able to give alerts and identify cases of mental health issues in children and also track the improvement status in identified cases. It should be able to track mental health issues prevalent in children from birth to the ones which they acquired later in their life for remediation and counselling. The tool should support teacher’s assessment as well as parental and self-assessment.
    
</div>

![App Screenshot](Screenshots/Result.png)

<p align="center">
  <a>
    <h1 align="left">Firebase Integration</h1>
    <p align="left">All the data collected through form is stored in Realtime Database of Firebase. The Firebase Realtime Database is a cloud-hosted NoSQL database that lets you store and sync data between your users in realtime.</p>
  </a>
</p>

![App Screenshot](Screenshots/Firebase.png)

> Based on your Answers, it will show the extent of your depression. 

![App Screenshot](Screenshots/Questions.png)


# Documentation

## Installing

Go to your project directory and create a virtual env to run flask app:

```sh
$ cd myproject
$ python3 -m venv venv
```
Activate your virtual env :

```sh
$ . venv/bin/activate
```
Within the activated environment, use the following command to install Flask:

```sh
$ pip install Flask
```
To run the application, use the flask command or python -m flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

```sh
$ export FLASK_APP=app
$ flask run
 * Running on http://127.0.0.1:5000/
```
