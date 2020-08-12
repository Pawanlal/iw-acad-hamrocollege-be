from django import forms

from classroom.models import Classroom , ClassDiscussion , ClassroomMember

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['classroom_title','classroom_creator','classroom_faculty']



class ClassroomMemberForm(forms.ModelForm):
    class Meta:
        model = ClassroomMember
        fields = ['user_id']


class ClassDiscussionForm(forms.ModelForm):
    class Meta:
        model = ClassDiscussion
        fields = ['user_id','comment']




