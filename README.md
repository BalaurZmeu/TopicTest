# TopicTest - a testing service.

The original text of the test task was found while googling the search query **"junior Python developer test task"** 

[Here's the link](https://qna.habr.com/q/212981)

---

### Here's the translated and edited text:

We need to create a straightforward testing service covering various topics. This involves questions with multiple answer options, where one or more options can be correct. These questions are organized into tests that users can take to view their results. The testing service should be implemented using Django.

Functionalities of the service should include:

- User Registration
- User Authentication

Registered users can:

- Take any of the tests

For a seamless experience, users should provide answers to all questions. Each question is displayed on a new page, ensuring users can't skip or leave any questions unanswered. After completing a test, users can view the results, including the number of correct/incorrect answers and the percentage of correct answers.

The admin panel is a standard Django admin panel with sections for:

- Registered Users
- Tests

In the admin panel, administrators can:

- Create new tests
- Add questions/answers
- Mark correct answers on the question page

There are validations to ensure there is at least one correct option per question and that not all options are marked as correct. Admins can also delete and modify questions/answers/correct answers when editing a test.

---

### How to use it:

#### 1. Create a virtual environment. (Recommended)
After downloading the files on your computer, open the terminal and navigate to the TopicTest directory.
Run the following command to create a virtual environment in the TopicTest directory:
```bash
python -m venv venv
```
Run this command to activate the virtual environment:
```bash
source venv/bin/activate
```

#### 2. Install the dependencies.
```bash
pip install -r requirements.txt
```

#### 3. Add a secret key to the settings.py file.
Generate a Django secret key using one of the websites (e.g. https://djecrety.ir/). 
Navigate to `TopicTest-main/topic_test/topic_test`
Open the settings.py file, add the secret key:
```python
...

# SECURITY WARNING: keep the secret key used in production secret!
# generate a key and paste it inside the '' quotemarks
# or use this one:  -h6n3+w)@p6)y8zmodzmj31v87h#(xn-0_2-0^^$0%6vmiwf-g
SECRET_KEY = ''

...
```
Save the file.

#### 4. Create a database.
Navigate to `TopicTest-main/topic_test`
Run this command to create a database:
```bash
python manage.py migrate
```

#### 5. Create superuser.
Create superuser using this command:
```bash
python manage.py createsuperuser
```
Enter a name and a password.

#### 6. Load json tests into the database.
There are some tests on programming inside the json_tests directory.
Run this command:
```bash
python manage.py loaddata ./json_tests/tests.json
```

#### 7. Run the development server.
```bash
python manage.py runserver 8080
```
Then open your browser and enter the address `localhost:8080`
Now you can create regular users using the register page.
Log in using a regular account or the superuser account and take any of the tests.

If you want to create a new test, edit existing tests, or manage users,
you can do this by accessing the admin page `localhost:8080/admin`.
There you will be asked to type in the name and password of the superuser.
