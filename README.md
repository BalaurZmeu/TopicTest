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
`python -m venv venv`
Run this command to activate the virtual environment:
`source venv/bin/activate`

#### 2. Install the dependencies.
`pip install -r requirements.txt`

#### 3. Create superuser.
Navigate to the topic_test directory:
`cd topic_test`
Create superuser using this command:
`python manage.py createsuperuser`
Enter a name and a password.

#### 4. Load json tests into the database.
There are some tests on programming inside the json_tests directory.
Run this command:
`python manage.py loaddata ./json_tests/tests.json`

#### 5. Run the development server.
`python manage.py runserver 8080`
Then open your browser and enter the address `localhost:8080`
Now you can register a user and take any of the tests.

If you want to create a new test, edit existing tests or manage users,
you can do this by accessing the admin page `localhost:8080/admin`.
There you will be asked to type in the name and password that you created earlier.
