from django.db import models

"""
id <- automatically created (bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,)
uuid <- uuid of the train (varchar(36) NOT NULL,)
name <- name of the train (varchar(30) NOT NULL,)
voie <- voie of the train (varchar(10) NOT NULL,)
wagon <- wagon of the train (varchar(30) NOT NULL,)
date <- date of the train (varchar(30) NOT NULL)
heure <- heure of the train (varchar(5) NOT NULL,)
cargaison <- cargaison of the train (varchar(16) NOT NULL,)

"""



class Train(models.Model):

    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=36)
    name = models.CharField(max_length=30)
    track = models.CharField(max_length=10)
    wagon = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    hour = models.CharField(max_length=5)
    freight = models.CharField(max_length=16)

    def __str__(self):
        return self.name
    

