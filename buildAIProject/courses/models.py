from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='topics')

    def __str__(self):
        return self.name

class Module(models.Model):
    title = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, related_name='modules')
    learning = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='modules')
    markdown = models.TextField()


    def __str__(self):
        return self.title
    
class ModuleProgress(models.Model):
    moduleId = models.BigIntegerField()
    accountEmail = models.EmailField()
    code = models.TextField()

    def __str__(self):
        return f"{self.title} "
