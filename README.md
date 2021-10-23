# Make Space - Meeting Room scheduler

This web application is built based on a use case for an imaginary company that is offering a co-working space to individuals, freelancers and startups. The idea is to provide a common workspace where anyone can come and work. Along with it, they have dedicated meeting rooms that their customers can book for private discussions.
This project is to build a scheduling system to effectively schedule meetings.


![Index Page](img/indexPage.JPG)


This use case has three rooms:
| Name  | Person Capacity |
| ------------- | ------------- |
| C-Cave | 3 People
| D-Tower  | 7 People |
| G-Mansion| 20 People  |


**Person Capacity** - Maximum number of people the meeting room can accommodate.

**Buffer Time** - Buffer time is the time used to clean up the meeting room. It happens at fixed times from 09:00 - 09:15, 13:15 - 13:45 and 18:45 - 19:00. During this time, no meeting rooms will be available to book. These buffer time values are configurable in the solution



## Features Available

1. **Book Meeting Room**

As a co-working space customer, I shall schedule a meeting by giving a time period and capacity requirement.

2. **View available meeting rooms**

As a co-working space customer, I would like to view a list of available meeting rooms by giving a time period. This should print the rooms in the ascending order of the room capacity. The rooms printed should be separated by a single space character.


## Rules

1. Bookings can be made only in a single day from 00:00 to the night 23:45. It cannot overlap across days. So, you cannot book from 23:00 to 01:00, but can from 23:00 to 23:45.

2. A booking can be started and ended only in 15-minute intervals, i.e., XX:00, XX:15, XX:30, XX:45. This means a booking can be made at 01:15 or 16:00 but not 15:35 or 16:03.

3. The rooms will be allocated only to those who book them, on a first come, first served basis.

4. The most optimal room which can accommodate the number of people will be allocated. For e.g., if you asked for a 4-person capacity requirement then the D-Tower (7-person capacity) will be allocated, provided it is available.

5. In case if the room of desired capacity is not available, the next available capacity room will be allocated. For e.g., If you asked for the 4-person capacity room between 12:00 to 13:00, and the D-Tower is not available, then the G-Mansion will be allocated, provided it is available.

6. No meetings can be scheduled during the buffer time. If the booking time overlaps with the buffer time, it would display No Vacant Rooms message.

7. Bookings can be only made for 2 or more people and up to a maximum of 20 people. 


### Input Constraints


- Time will be in HH:MM (24 hours) format
- Time input should always consider the 15-minute time interval
- For all the time inputs end_time > start_time



## Software

- Python (v3.8)

## Installation and Setup

### Python 3.8 Installation

You can download python 3.8 using the [link](https://www.python.org/downloads/release/python-380/)

Download installation file based on your operating system and install Python in your local machine

### Clone

Clone this repo to your local environment using git clone

```

git clone https://github.com/vasudevan07/make_space.git

```

### Create virtual environment


Navigate to the directory under src/scheduler_scripts. Once you have navigated to the scheduler_scripts folder, open the command prompt and run the command below

```

python3 -m venv <name_of_virtualenv>

```
if "python3" is not recognized try using "py" or "python". If you still face issue, then you may need to set environment variables in your machine. You can follow instructions [here](https://geek-university.com/python/add-python-to-the-windows-path/)

### Installing required python libraries

Once the python virtual environment is created, you can activate your virtual environment by running the command below in the command prompt opened in scheduler_scripts folder

## For macOS and Linux

```

source ./<name_of_virtualenv>/bin/activate

```
## For Windows

```

<name_of_virtualenv>\scripts\activate

```
You would see something like (<name_of_virtualenv>) in the beginning of the new command line once it is activated

Now, we need to install all the requirements by running the command 

```

pip install requirements.txt

```


### Running the application

There are two things before we can get our hands on the running application

1) Start the Flask server
2) Open the index.html file under src directory

#### Start Flask Server

Navigate to scheduler_scripts directory under src. Run the command below in your command prompt

```

python3 app.py

```

#### Running the index.html page

Navigate to src folder, open the index.html file using the browser of your choice (Chrome Recommended)





## Running the unit tests

The testcases are written using the unittest python library. To run the unit tests, navigate to the scheduler_scripts folder, run the command below in your command prompt

```

python -m unittest -b

```
## Packages

### Flask
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.

#### Usage in this project
In this application, Flask is used to build the APIs for booking room and checking the vacancy

### json
json is a standard python library, used to work with json data and operations around the json data

#### Usage in this project
json is used to stringify and convert the string body payload to python dictionary object

### enum
enum is a standard python library to create enumeration. An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.

#### Usage in this project
enum is used to maintain a list of constant values which are configurable

### unittest
The _unittest_ unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages.

#### Usage in this project
This package is used to write python unit test cases for this project

## References

- Python 3.8 Documentation - https://docs.python.org/3.8/tutorial/index.html
- Flask https://flask.palletsprojects.com/en/2.0.x/
- Unittest Documentation - https://docs.python.org/3/library/unittest.html


## Credits

- Thanks to [Mohit Khandelwal](https://www.linkedin.com/in/mohitkh7/) for creating this backend coding problem called make space for [geektrust](https://www.geektrust.in/). Thanks to them for inspiring me to build something.

- Thanks to [sweetalert2](https://sweetalert2.github.io/) library for the beautiful alerts.

- Thanks to the creator of this awesome jquery timepicker plugin found [here](https://github.com/jonthornton/jquery-timepicker)
