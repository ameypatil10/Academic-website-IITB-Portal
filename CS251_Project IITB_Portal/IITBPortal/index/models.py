## \package models
# \package Permission
# \package User
# \package settings
# \package forms
# \package datetime

## \mainpage
# IITB-Portal  is a website designed to help students, both in-campus and outside, to efficiently learn courses in which they are interested. \\
# The website is also there to extrapolate their interests and be more informed while learning. Hence, the website offers a news feed with links to articles from all over the internet about researches, current breakthroughs and events around. \\ The portal will help students by providing framework for online test taking, onlign assignment submissions and findind course materials.

from django.db import models
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django import forms
from datetime import datetime
# Create your models here.

## \brief Student database. Contains the details of the Students or the Professors. Every row in database is unique to a particular user. This is confirmed by unique username and password.
# \note isProfessor is a Boolean field. If checked, it means the corresponding User gets the priveleges of a professor. This can only be set by the django-admin.
class Student(models.Model):
    user = models.ForeignKey(User)
    email_id = models.EmailField(max_length=150,default='')
    login_id = models.CharField(max_length=100,default='')
    first_name = models.CharField(max_length=250,default='')
    last_name = models.CharField(max_length=250,default='')
    phone = models.CharField(max_length=250,default='')
    university = models.CharField(max_length=250,default='')
    city = models.CharField(max_length=250,default='')
    profile_pic = models.FileField(default='blank-user.jpg')
    is_professor = models.BooleanField(default=False)

    ## \brief This function shows what to display whenever the row object itself is requested to be displayed.
    # \param self The row object with all its column values
    # \return A string

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' : ' + self.login_id


## \brief Course Database. Contains list of all courses having course name, course code and basic course info. Each row has a many to many relation with rows in Student Database.
# \note ManyToManyField has been used here to create a many to many relation with Student. It means many 'Students' can be uniquely determined to the same row and many Courses ca

class Course(models.Model):
    course_code = models.CharField(max_length=20,default="")
    course_name = models.CharField(max_length=250,default="")
    course_info = models.CharField(max_length=500, default='')
    all_students = models.ManyToManyField(Student)

    ## \brief This function shows what to display whenever the row object itself is requested to be displayed.
    # \param self The row object with all its column values
    # \return A string

    def __str__(self):
        return self.course_code + ' : ' + self.course_name


## \brief Topic Database. Contains list of all topics in a particular course.

class Topic(models.Model):
    course = models.ForeignKey(Course)
    topic_name = models.CharField(max_length=100, default='')
    topic_info = models.CharField(max_length=500, default='')

    ## \brief This function shows what to display whenever the row object itself is requested to be displayed.
    # \param self The row object with all its column values
    # \return A string

    def __str__(self):
        return self.topic_name


## \brief Assignment Database. Contains Information about assignments. Row contains the name, information, topic, course, deadline and the file uploaded.
# \note Many to Many Field with User

class Assignment(models.Model):
    assignment_name = models.CharField(max_length=250, default='')
    assignment_info = models.CharField(max_length=500, default='')
    parent_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=None)
    assignment_content_file = models.FileField(null=True, blank=True,)
    date_added = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField(default=datetime.now)

    ## \brief This function shows what to display whenever the row object itself is requested to be displayed.
    # \param self The row object with all its column values
    # \return A string

    def __str__(self):
        return self.assignment_name + ' : ' + self.parent_topic.topic_name


class Assignment_Submission(models.Model):
    submission_user = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    submission_assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, default=None)
    marks_scored = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.submission_user.login_id) + ' : ' + str(self.submission_assignment.assignment_name)


## \brief Course_Material Database. Contains information about the course material and the file uploaded.

class Course_Material(models.Model):
    course_material_name = models.CharField(max_length=250)
    course_material_info = models.TextField()
    parent_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=None)
    course_content_file = models.FileField(null=True, blank=True,)

    # \brief This function shows what to display whenever the row object itself is requested to be displayed.
    # \param self The row object with all its column values
    # \return A string

    def __str__(self):
        return self.course_material_name + ' : ' + self.parent_topic.topic_name


## \brief Interest Database. Contains the interests of every user.

class Interest(models.Model):
    interest_name = models.CharField(max_length=250, default='')
    all_students = models.ManyToManyField(Student)

    ## \brief This function shows what to display whenever the row object itself is requested to be displayed.
    # \param self The row object with all its column values
    # \return A string

    def __str__(self):
        return self.interest_name


## \brief Quiz Database. Contains quiz topic and information.

class Quiz(models.Model):
    parent_topic = models.ForeignKey(Topic, default=None)
    quiz_name = models.CharField(max_length=100, default='')
    quiz_info = models.CharField(max_length=500, default='' )

    # \brief This function shows what to display whenever the row object itself is requested to be displayed.
    # \param self The row object with all its column values
    # \return A string

    def __str__(self):
        return self.quiz_name


# \brief This function shows what to display whenever the row object itself is requested to be displayed.
# \param self The row object with all its column values
# \return A string

class Question(models.Model):
    parent_quiz = models.ForeignKey(Quiz, default=None)
    question_text = models.CharField(max_length=500, default='')
    is_subjective = models.BooleanField(default=True)
    option1 = models.CharField(max_length=100,default='')
    option2 = models.CharField(max_length=100, default='')
    option3 = models.CharField(max_length=100, default='')
    option4 = models.CharField(max_length=100, default='')
    correct_answer = models.CharField(max_length=20, default='')

    # \brief This function shows what to display whenever the row object itself is requested to be displayed.
    # \param self The row object with all its column values
    # \return A string

    def __str__(self):
        return str(self.id) + ' ' + self.parent_quiz.quiz_name + ' ' + self.parent_quiz.parent_topic.topic_name


## \brief Newsfeed Database. Contains information required to display the newsfeed. Contains links to articles and images.
# \note Contains tag information required to be compared with the interest tag of the student, to help in recommendation o

class News_feed(models.Model):

    image_url = models.CharField(max_length=500,default="")
    href_url = models.CharField(max_length=500, default="")
    topic = models.CharField(max_length=500,default="")
    desc = models.CharField(max_length=1000, default="")
    date = models.CharField(max_length=100, default="")
    tag = models.CharField(max_length=500, default="")
    my_tag = models.CharField(max_length=500, default="")

    # \brief This function shows what to display whenever the row object itself is requested to be displayed.
    # \param self The row object with all its column values
    # \return A string

    def __str__(self):
        return self.topic
