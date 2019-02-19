## API

The task was to design a set of base APIs mirroring Practo.

## Dependencies

```
django
django-rest-framework
django-filter

```

## Installation

```
pip install -r requirements.txt
python manage.py migrate
``` 

## Description

- Doctor APIs for adding,listing,filtering and searching based on locality and their speciality
- Interaction API basically for liking and un-liking a Doctor
- An availability API for knowing if the doctor is available for appointment


The admin route is enables for creating and updating users

Decided to use `django-rest-framework` and `django-filter` for it's robust and easy to use structure because of the time constraint.

`django-rest-framework`s Viewsets helps in enabling GET-POST-PUT-DELETE APIs in an instant

Available API routes

| Route                     	| Method 	|                                                      Summary                                                     	|
|---------------------------	|--------	|:----------------------------------------------------------------------------------------------------------------:	|
| /api/doctors              	| GET    	| List of available doctors                                                                                        	|
| /api/doctors              	| PUT    	| For adding a new doctor                                                                                          	|
| /api/doctors/<id>         	| GET    	| Retrieving a specific doctor detail                                                                              	|
| /api/doctors/<id>         	| DELETE 	| For deleting the doctor by id                                                                                    	|
| /api/doctors?<parameters> 	| GET    	| For filtering and searching based on `location`,`speciality` and `gender`                                              	|
| /api/likes                	| GET    	| List of available interactions                                                                                   	|
| /api/likes/               	| GET    	| Retrieving a specific interactions detail                                                                        	|
| /api/likes/               	| DELETE 	| For deleting the interactions by id                                                                              	|
| /api/like/                	| POST   	| For liking a specific doctor. Accepts doctor_id as the POST parameter. Requires user authentication              	|
| /api/availability         	| GET    	| List of availability of doctors                                                                                  	|
| /api/availability         	| PUT    	| For adding a new availability with doctor as foreign key                                                         	|
| /api/availability/<id>    	| GET    	| Retrieving a specific doctor availability by id                                                                  	|
| /api/availability/        	| DELETE 	| For deleting the availability by id                                                                              	|
| /api/doctors?<parameters> 	| GET    	| For filtering and searching on knowing a doctor's availability. Accepts `doctor_id` and `availability` as parameters 	|