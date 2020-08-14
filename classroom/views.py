from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Classroom, ClassroomDiscussion , ClassroomMember

# Create your views here.

class CreateClassroom(CreateView):
    model = Classroom
    # fields = '__all__'
    template_name = 'classroom/create.html'
    success_url = reverse_lazy('classroom:member')

class AddMembers(CreateView):
    model = ClassroomMember
    # fields = '__all__'
    template_name = 'classroom/addMember.html'
    success_url = reverse_lazy('classroom:member')

class DiscussionForum(CreateView):
    model = ClassroomDiscussion
    # fields = '__all__'
    template_name = 'classroom/forum.html'
    success_url = reverse_lazy('classroom:create')


