# TopicTest - a testing service.

### WORK IN PROGRESS
### The project is not finished

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

