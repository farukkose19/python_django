from django.db import models

class Kullanici(models.Model):
    userName=models.TextField()
    password=models.TextField()
    def __str__(self):
        return self.userName

class Word(models.Model):
    name=models.TextField()
    kullanici=models.ForeignKey(Kullanici,related_name='kullanicininkelimesi')
    def __str__(self):
        return self.name

class Mean(models.Model):
    meanName=models.TextField()
    word=models.ForeignKey(Word,related_name='means',default="aaa")
    def __str__(self):
        return self.meanName

