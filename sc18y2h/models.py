from django.db import models


class module(models.Model):
    ID = models.IntegerField("ID", primary_key=True)
    module_ID = models.CharField("module_ID", max_length=50)
    module_Name = models.CharField("module_Name", max_length=50)
    Year = models.IntegerField("Year")
    Semester = models.IntegerField("Semester")

class users(models.Model):
    Username = models.CharField("Username", primary_key=True, max_length=50)
    Email = models.CharField("Email", max_length=50)
    Password = models.CharField("Password", max_length=50)


class professors(models.Model):
    pro_ID = models.CharField("pro_ID", primary_key=True, max_length=50, default="HYQ")
    pro_Name = models.CharField("pro_Name", max_length=50)


class module_pro_score(models.Model):
    ID = models.ForeignKey(module, verbose_name="ID", on_delete=models.CASCADE)
    pro_Name = models.ForeignKey(professors, verbose_name="pro_Name", on_delete=models.CASCADE)
    score = models.IntegerField("score")

class module_pro(models.Model):
    ID = models.ForeignKey(module, verbose_name="ID", on_delete=models.CASCADE)
    pro_Name = models.ForeignKey(professors, verbose_name="pro_Name", on_delete=models.CASCADE)
