1. Create Project

2. Start Server and navgiate to browser
python manage.py runserver 0.0.0.0:8000

3. Run Migration
python manage.py migrate

4. Create a file to hold view (views.py)

5. Modify url file

6. Create courses App
python manage.py startapp courses

7. Modify settings.py, include 'courses' app and change timezone

8. Modify courses model.py

9. Migrate database

    9.1 Create Migration File
    python manage.py makemigrations courses

    9.2 Run migration
    python manage.py migrate courses

10. Go into Django shell to create database records
python manage.py shell

    10.1 Import model
    from courses.models import Course
    
    10.2 Query Course to see what exists
    Course.objects.all()
    
    10.3 Create a new Course record
    c = Course()
    c.title = "Python Basics"
    c.description = "Learn the basics of Python"
    c.save()
    
11. Let's do that again, but a different way

    11.1 Import model
    from courses.models import Course
    
    11.2 Create new Course record
    Course(title="Python Collections", description="Learn about list, dict, and tuple").save()
    
12. Third method for record creation

    12.1 Import model
    
    12.2 Create new Course record
    Course.objects.create(title="Object-Oriented Python", description="Learn about Python's classes")
    
    
13. Define how we display (stringify) this object

    13.1 Modify models.py for Course
    
    13.2 View all courses in python shell
    python manage.py shell
    from courses.models import Course
    Course.objects.all()
    
14. Update courses views.py
    
15. Create a urls.py for this new view in courses app

16. Modify learning_site urls.py

17. Create user for admin account

    17.1 python manage.py createsuperuser
    
    17.2 edit admin.py in courses app
    
    17.3 Visit /admin interface in app, mind blown

18. Create HTML template for courses

    18.1 Create "templates" directory in courses app
    mkdir courses/templates
    
    18.2 Inside templates, create a directory with same name as app
    mkdir courses/templates/courses
    
    18.2 Create file inside templates/courses called course_list.html
    touch templates/courses/course_list.html
    
    18.3 In courses views.py, edit to use template
    
19. Create template for home page

    19.1 Create "templates" directory in top-level of workspace
    mkdir templates
    
    19.2 In learning_site/settings.py, add 'templates' spec to DIR dictionary in TEMPLATES list
    
    19.3 Create "home.html" in new templates directory
    
    19.4 Edit learning_site views to include "home.html" template
    
    19.5 View result in browser
    
20. Template Inheritance
    
    20.1 Create layout.html under top-level templates directory
    touch templates/layout.html
    
    20.2 Modify home.html to include layout.html

21. Adding static assets (css files)
    
    21.1 In learning_site/settings.py, create a reference for STATICFILES_DIRS

    21.2 Add another import and line in urls.py
    
    21.3 Modify layout.html
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    