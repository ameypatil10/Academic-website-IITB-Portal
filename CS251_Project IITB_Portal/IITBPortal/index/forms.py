from django.contrib.auth.models import User
from django import forms
from datetime import datetime
from .models import *

## \brief UserForm for Log-In for registered users.
class UserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']

## \brief RegisterForm for new users to register into IITB-Portal.
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']

## \brief ProfileForm to fill in the details while registering.
class ProfileForm(forms.ModelForm):
    profile_pic = forms.FileField()

    class Meta:
        model = Student
        fields = ['profile_pic']

## \brief AssignmentForm for the professor to fill in while uploading the assignment question onto the mainframe.
class AssignmentForm(forms.ModelForm):
    assignment_name = forms.CharField(max_length=250)
    assignment_file = forms.FileField()
    assignment_info = forms.CharField(max_length=500)

    class Meta:
        model = Assignment
        fields = ['assignment_name','assignment_info','assignment_name']

## \brief MaterialForm for the professor to fill in while uploading the course material onto the mainframe.
class MaterialForm(forms.ModelForm):
    material_name = forms.CharField(max_length=250)
    material_file = forms.FileField()
    material_info = forms.CharField(max_length=500)

    class Meta:
        model = Course_Material
        fields = ['material_name','material_file','material_info']

## \brief TopicForm for the professor to fill in while uploading a new topic onto the mainframe.
class TopicForm(forms.ModelForm):
    topic_name = forms.CharField(max_length=250)
    topic_info = forms.CharField(max_length=1000)

    class Meta:
        model = Topic
        fields = ['topic_name','topic_info']

## \brief QuizForm for the professor to fill in while uploading a new quiz in a topic onto the mainframe.
class QuizForm(forms.ModelForm):
    quiz_name = models.CharField(max_length=100)
    quiz_info = models.CharField(max_length=500)

    class Meta:
        model = Quiz
        fields = ['quiz_name', 'quiz_info']

## \brief QuestionForm for the professor to fill to add the questions to a particular quiz onto the mainframe.
class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(max_length=500)
    #is_subjective = forms.BooleanField(required=False)
    option1 = forms.CharField(max_length=100)
    option2 = forms.CharField(max_length=100)
    option3 = forms.CharField(max_length=100)
    option4 = forms.CharField(max_length=100)
    correct_answer = forms.CharField(max_length=20)

    class Meta:
        model = Quiz
        fields = ['question_text',  'option1', 'option2', 'option3', 'option4', 'correct_answer']