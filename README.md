# UCL Resolve Backend
This is the api section github repository for UCL Resolve, Team 10's project for UCL Portico 5.0. 
The api hosted at [heroku](https://ucl-report-estate.herokuapp.com/)
The frontend section is located at [Here](https://github.com/ucl-hackathon-2022/frontend).

Below is the procedure for installing and running the backend part of the project.

## Install

A virtual environment should be set up. To set it up follow the shell commands below:

### Linux / iOS
```
$ python -m venv venv
$ source venv/bin/activate
```

### Windows
```
$ venv\Scripts\activate
```

After setting up the virtual environment, install flask and other dependencies:

``` 
$ pip install -r requirements.txt
```

## Run the Application

To run UCL Resolve, type the following shell command:
```
$ flask run
```
