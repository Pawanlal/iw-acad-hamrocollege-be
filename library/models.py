from django.db import models
from college.models import SubjectList
from account.models import User
from datetime import date, timedelta, datetime

class Author(models.Model):
    firstname = models.CharField(max_length=200, blank=False)
    lastname = models.CharField(max_length=200, blank=False)    
    
    def __str__(self):
        return self.firstname + " " + self.lastname
    
    class Meta:
        ordering = ['lastname']


class Publisher(models.Model):
    name = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name + " " + self.country

    
    class Meta:
        ordering = ['name']


class Book(models.Model):
    book_id = models.CharField(max_length=10, blank=False, primary_key=True)    
    title = models.CharField(max_length=200, blank=False)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    isbn = models.BigIntegerField(blank=False)
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE)   
    edition = models.BigIntegerField(blank=False, default=0)

    def __str__(self):
        return self.book_id + " - " + self.title    

    class Meta:
        ordering = ['title']


class BookIssue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(blank=True, null=True, default=None)
    return_date = models.DateField(blank=True, null=True, default=None)
    #fine = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + ' ' + self.book.title


class Fine(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book_issue= models.ForeignKey(BookIssue,on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username 


class BookRequest(models.Model):
    class STATUS_TYPE(models.TextChoices):
        PENDING = 'Pending'
        REJECTED = 'Rejected'
        ONPROCESS = 'On-process'
        APPROVED = 'Approved'   	     

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_TYPE.choices, default='Approved',max_length=10)
    request_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.status + ' - ' + self.user.username


