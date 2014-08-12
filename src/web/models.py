# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode


class Skill(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=255, null=False, blank=False)
    abbreviation = models.CharField(max_length=255, null=False, blank=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class State(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=255, null=False, blank=False)
    abbreviation = models.CharField(max_length=255, null=False, blank=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class City(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=255, null=False, blank=False)
    abbreviation = models.CharField(max_length=255, null=False, blank=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class Science(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    code = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.name)


class Scientist(models.Model):
    user = models.OneToOneField(User)
    date_birth = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=2, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    id_state = models.OneToOneField(State, null=True, blank=True)
    id_city = models.OneToOneField(City, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField()
    science = models.ManyToManyField(Science)
    skills = models.ManyToManyField(Skill)
    bio = models.TextField()
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)



class Coder(models.Model):
    user = models.OneToOneField(User)
    date_birth = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=2, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    id_state = models.OneToOneField(State, null=True, blank=True)
    id_city = models.OneToOneField(City, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField()
    skills = models.ManyToManyField(Skill)
    bio = models.TextField()
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.user.username)


class Project(models.Model):
    user_create = models.OneToOneField(User)
    scientists = models.ManyToManyField(Scientist, related_name='project_scientists', blank=True, null=True)
    coders = models.ManyToManyField(Coder, related_name='project_coders', blank=True, null=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    sciences = models.ManyToManyField(Science, related_name='project_sciences')
    skills = models.ManyToManyField(Skill, related_name='project_sciences')
    number_members = models.IntegerField(default=1, blank=False, null=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True, auto_now_add=False, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.name)


class Message(models.Model):
    id_sender = models.ForeignKey(User, related_name='message_usersender')
    id_receiver = models.ForeignKey(User, related_name='message_userreceiver')
    message = models.TextField()
    seen = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.message)
