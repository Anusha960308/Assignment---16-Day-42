#!/usr/bin/env python
# coding: utf-8

# In[1]:


attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present')
)

class Head_of_department(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name 

class Employee(models.Model):
    first_name = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=True)
    head_of_department = models.ForeignKey('Head_of_department', on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(max_length=100)

     def __str__(self):
        return self.first_name + ' ' + self.last_name

class Attendance(models.Model):
    head_of_department = models.ForeignKey('Head_of_department', on_delete=models.SET_NULL, blank=True, null=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, )
    attendance = models.CharField(max_length=8, choices=attendance_choices, blank=True)


# In[ ]:




