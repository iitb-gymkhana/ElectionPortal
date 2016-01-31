from django.db import models
from election.models import Election


class Post(models.Model):
    POST_TYPE = [
        [0, 'ALL'],
        [1, 'UG'],
        [2, 'PG'],
    ]
    name = models.CharField(max_length=32, db_index=True)
    number = models.IntegerField(default=1)
    election = models.ForeignKey(Election, related_name='posts', db_index=True)
    type = models.IntegerField(choices=POST_TYPE, default=0)

    def __str__(self):
        type_string = ''
        if self.type == 1:
            type_string = ' [UG]'
        elif self.type == 2:
            type_string = ' [PG]'
        return self.name + type_string


class Candidate(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    image = models.ImageField(null=True, blank=True)
    post = models.ForeignKey(Post, related_name='candidates', db_index=True)

    def __str__(self):
        return self.name