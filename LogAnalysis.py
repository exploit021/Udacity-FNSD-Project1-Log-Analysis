#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Udacity Full Stack Web Developer Nanodegree
# Project 1: Logs Analysis
# Author: Youngseo Kim
# Date: 2/17/2019

import psycopg2

# Set a database name
DBNAME = "news"


# 1. What are the most popular three articles of all time?


QUERY1 = """
select articles.title as Title, count(log.id) as Views
from log
inner join articles
    on log.path = '/article/' || articles.slug
where log.status like '200%'
group by articles.title
order by views desc
limit 3;
"""


def question1():
    # Connect to the database
    db = psycopg2.connect(database=DBNAME)

    # Execute the query and retrieve the results
    c = db.cursor()
    c.execute(QUERY1)
    rows = c.fetchall()

    # Disconnect from the database
    db.close()

    # Show the results
    print("Question 1: What are the most popular three articles of all time?")
    for row in rows:
        print('"{0}" - {1} Views'.format(row[0], row[1]))


# 2. Who are the most popular article authors of all time?


QUERY2 = """
select authors.name as Name, count(log.id) as Views
from log
inner join articles
    on log.path = '/article/' || articles.slug
inner join authors
    on articles.author = authors.id
where log.status like '200%'
group by authors.name
order by views desc;
"""


def question2():
    # Connect to the database
    db = psycopg2.connect(database=DBNAME)

    # Execute the query and retrieve the results
    c = db.cursor()
    c.execute(QUERY2)
    rows = c.fetchall()

    # Disconnect from the database
    db.close()

    # Show the results
    print("Question 2: Who are the most popular article authors of all time?")
    for row in rows:
        print('"{0}" - {1} Views'.format(row[0], row[1]))


# 3. On which days did more than 1% of requests lead to errors?


QUERY3 = """
 select totalRequests.DateTime,
    (errors.Counts::float / totalRequests.Counts::float * 100) as Percentage
 from
 (
     select log.time::date as DateTime, count(log.id) as Counts
     from log
     group by log.time::date
 ) as totalRequests
 inner join (
    select log.time::date as DateTime, count(log.id) as Counts
    from log
    where log.status like '4%' OR log.status like '5%'
    group by log.time::date
    ) as errors
on errors.DateTime = totalRequests.DateTime
where (errors.Counts::float / totalRequests.Counts::float * 100) > 1
order by percentage desc
limit 1;
"""


def question3():
    # Connect to the database
    db = psycopg2.connect(database=DBNAME)

    # Execute the query and retrieve the results
    c = db.cursor()
    c.execute(QUERY3)
    rows = c.fetchall()

    # Disconnect from the database
    db.close()

    # Show the results
    print("Question 3: On which days did more than \
1% of requests lead to errors?")
    for row in rows:
        print('{0:%B %d, %Y} - {1:.2%} errors'.format(row[0], row[1] / 100))


if __name__ == '__main__':
    print("====================")
    question1()
    print("====================")
    question2()
    print("====================")
    question3()
    print("====================")
