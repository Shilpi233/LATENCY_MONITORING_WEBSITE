from django.db import models

class Website(models.Model):
    url = models.URLField(max_length=200, unique=True)
    check_frequency = models.IntegerField(help_text='Frequency in minutes')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.url
    
class LatencyRecord(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    latency = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.website.url} at {self.timestamp}: {self.latency} ms'

class Measurement(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    latency = models.FloatField()

    def __str__(self):
        return f'{self.website.url} at {self.timestamp}: {self.latency} ms'

class Notification(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f'Notification for {self.website.url} at {self.timestamp}: {self.message}'

class Feedback(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    message = models.TextField()

    def __str__(self):
        return f'Feedback for {self.website.url} at {self.timestamp}: {self.message}'
    
class Issue(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('closed', 'Closed')], default='open')

    def __str__(self):
        return f'Issue for {self.website.url} at {self.timestamp}: {self.message} - Status: {self.status}'
    





