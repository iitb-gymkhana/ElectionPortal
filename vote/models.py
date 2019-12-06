from django.db import models
from simple_history.models import HistoricalRecords

from core.core import VOTE_TYPE_CHOICES
from election.models import Election
from post.models import Candidate


class VoteSession(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    election = models.ForeignKey(
        Election, related_name='vote_sessions', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.timestamp)


class VoteIPMap(models.Model):
    election = models.ForeignKey(
        Election, related_name='vote_ips', on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    votes = models.PositiveIntegerField(default=1)
    history = HistoricalRecords()


class Vote(models.Model):
    session = models.ForeignKey(
        VoteSession, related_name='votes', on_delete=models.CASCADE)
    candidate = models.ForeignKey(
        Candidate, related_name='votes', on_delete=models.CASCADE)
    vote = models.SmallIntegerField(
        choices=VOTE_TYPE_CHOICES, null=True, blank=True)
