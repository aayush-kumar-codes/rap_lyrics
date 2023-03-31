from django.db import models

from authentication.models import Account


class Competition(models.Model):
    """
    Model to represent a Rap Lyrics competition.
    """
    organizer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'O'}
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_participants = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Submission(models.Model):
    """
    Model to represent a user's submission for a specific competition.
    """
    rapper = models.ForeignKey(
        to=Account,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'R'}
        )
    competition = models.ForeignKey(to=Competition, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    lyrics = models.TextField()
    rules = models.JSONField()
    upvote = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"
    


class Vote(models.Model):
    """
    Model to represent a user's vote for a specific submission in a competition.
    """
    user = models.ForeignKey(
        to=Account,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'N', 'role': 'R'}
    )
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    vote = models.BooleanField(null=True)   # vote True will be counted as upvote

    def __str__(self):
        return f"{self.user.username} voted for {self.submission.title}"
