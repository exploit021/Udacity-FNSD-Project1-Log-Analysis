# Log Analysis

## Project Overview

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.


## How to Run A Program

### Installation:
* Virtualbox
* Vagrant
* Python

### Setup Enviromnemt
* Download or Clone [Full Stack Nanodegree Virtual Machine](https://github.com/udacity/fullstack-nanodegree-vm).
* Download SQL database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Download or Clone [the project](https://github.com/exploit021/Udacity-FNSD-Project1-Log-Analysis)
* Unzip downloaded SQL database and put newsdata.sql into a folder where LogAnalysis.py located.

### Running the program

0. To find more detailed explanation, refer this [link](https://github.com/udacity/fullstack-nanodegree-vm).
1. Open command-prompt or Git Bash and navigate to downloaded Full Stack Nanodegree Virtual Machine folder.
2. Run following command to launch VM.

```$ vagrant up```

2. Once VM started, run following commandd to open and login to SSH.

```$ vagrant ssh```

3. Navigate the folder where `LogAnalysis.py` (e.g. /vagrant).
4. Load the database file in local database using following command.

```$ psql -d news -f newsdata.sql```

5. Connect database using following command.

```psql -d news```

6. Run program by using following command depends on version of Python.

```
python LogAnalysis.py
python3 LogAnalysis.py
```

## Style Guide
The PEP8 style guide is an excellent standard to follow.

You can install the `pycodestyle` tool to test this, with `pip install pycodestyle` or `pip3 install pycodestyle` (Python 3).
In order to test, run the following command.

```$ pycodestyle LogAnalysis.py```

## Questions

### This project required to answer following three questions.

#### Question 1: What are the most popular three articles of all time?

##### Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

#### Question 2: Who are the most popular article authors of all time?

##### Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

#### Question 3: On which days did more than 1% of requests lead to errors?

##### Example:

July 29, 2016 — 2.5% errors