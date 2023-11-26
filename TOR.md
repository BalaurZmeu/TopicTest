# Terms of Reference for the Project "TopicTester"

The original text of the test task was found while googling the search query **"junior Python developer test task"** 

Here's the link:  https://qna.habr.com/q/212981

---

### Here's the edited and more understandable version of the text:

We need to create a straightforward testing service covering various topics. This involves questions with multiple answer options, where one or more options can be correct. These questions are organized into tests that users can take to view their results.

Functionalities of the service include:

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

Requirements for the project:

- The code should be stored in a GitHub repository.
- Dependencies should be listed in `requirements.txt`.
- Development should be in a `virtualenv`, and the `virtualenv` directory should be added to `.gitignore`.
- Settings should be stored in `settings.py`, and `settings_local.py` can override settings in `settings.py`. The `settings_local.py` file is also added to `.gitignore`, allowing developers and beta servers to use custom settings, such as database connections.

The database structure can be created using either the built-in `manage.py syncdb` or migrations via South (which would be a plus). Front-end requirements are flexible, and the interface can be designed based on personal preference, using frameworks like Twitter Bootstrap if desired.

---
### Here's the original text:

Одно из заданий, которое давал джуниорам:  
  
Нужно сделать простой сервис проведения тестирования по каким-либо темам. Т.е. есть тесты с вариантами ответов, один или несколько вариантов должны быть правильными. Тесты группируются в наборы тестов, которые затем пользователь может проходить и видеть свой результат.  
Функциональные части сервиса:  
Регистрация пользователей  
Аутентификация пользователей  
Зарегистрированные пользователи могут  
Проходить любой из тестовых наборов  
Последовательный ответ на все вопросы, каждый вопрос должен выводится на новой странице с отправкой формы (перескакивать через тесты или оставлять неотмеченными нельзя)  
После завершения тестирования смотреть результат:  
количество правильных/неправильных ответов  
процент правильных ответов  
  
  
  
Админка. Стандартная админка Django. Разделы:  
Стандартный раздел пользователей  
Раздел с наборами тестов  
Возможность на странице набора тестов добавлять вопросы/ответы к вопросам/отмечать правильные ответы  
Валидация на то, что должен быть хотябы 1 правильный вариант  
Валидация на то, что все варианты не могут быть правильными  
Удаление вопросов/вариантов ответов/изменение правильных решений при редактировании тестового набора  
  
  
Требования  
Код в репозитории на GitHub.  
Список всех зависимостей должен храниться в requirements.txt, соответственно можно установить их командой pip install -r requirements.txt.  
Разработка должны вестись в virtualenv, но сама директория с virtualenv должна быть добавлена в .gitignore.  
Настройки должны храниться в settings.py, но также, при наличии settings_local.py в той же директории, настройки из settings_local.py должны переопределять настройки в settings.py. Т.е. если есть файл settings_local.py, то определенные в нем параметры имеют больший приоритет. Сам файл settings_local.py добавляется в .gitignore. Таким образом у каждого девелопера и на бета сервере можно использовать кастомные настройки, например для соединения с БД.  
Должен работать один из способо создания структуры БД. Встроенный manage.py syncdb или миграции через South (будет плюсом).  
По фронт-енду требований никаких не предъявляется. Интерфейс на твое усмотрение и он не буде оцениваться. Можно использовать любимый фреймворк или, например, воспользоваться Twitter Bootstrap.

> Written with [StackEdit](https://stackedit.io/).
