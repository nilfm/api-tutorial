# Tutorial on APIs

This repo is meant to be an introduction to APIs, both from the role of a client and a server.

## What is an API?

An [API (Application Programming Interface)](https://en.wikipedia.org/wiki/API) is an interface which defines how a system interacts with programs. In this tutorial we are going to focus on web APIs, in which transactions typically happen over [the HTTP protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol).

In this tutorial we are going to communicate with some APIs using the `requests` library in Python and create our own API using the `flask` framework.

## Preliminaries

Install the required libraries ([Flask](https://flask.palletsprojects.com/en/master/) and [Requests](https://requests.readthedocs.io/en/master/)):

```
pip3 install -r requirements.txt --user
```

In case you don't have `pip3` installed, run the following command:

```
sudo apt install python3-pip
```

## Exercises

### Exercise 1

Obtain the current weather at a given city. Use [this API](https://rapidapi.com/community/api/open-weather-map).

### Exercise 2

Use the [Google Translate API](https://rapidapi.com/googlecloud/api/google-translate1) to detect the language from a snippet of text and to translate text between two languages. 

### Exercise 3

Set up a Flask server which offers the following information about you and your friends: name, age and favorite subject. 

There should be a `/users` endpoint which returns a list of the possible names and a `/user/<name>` endpoint which returns a dictionary with the aforementioned information about the user that is given. If the name is not found in the data, raise a 404 (Not Found) error using the `abort` function in Flask. 

Then, set up a client which requests this information in some way. Run the server in localhost and make sure it works!

### Solutions

The `solutions` directory contains proposed solutions for each of these exercises. To run the programs, simply `cd` to the appropriate directory and run
```
python3 <filename>
```

## Extras

### Extra 1 

Choose an API of your liking from [this list](https://github.com/public-apis/public-apis) and try to build a client to fetch information from it. Can you process the data to visualize it in interesting ways? 

### Extra 2

Build an API which allows `GET`, `POST` and `DELETE` requests to manipulate the data that it holds. For example, a service that stores which people are currently inside a store, with a capacity limit (emit the proper status code if it is surpassed!). Also, build a client that can read keyboard input and communicate with this server.
