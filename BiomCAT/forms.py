from django import forms
from BiomCAT.models import TestSubject

class TestSubjectForm(forms.ModelForm):
    class Meta:
        model = TestSubject
        exclude = ['control_group', 'user', 'completed_survey', 'current_question']