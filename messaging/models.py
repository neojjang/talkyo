from django.db import models
from django.urls import reverse


class Conversation(models.Model):
    class Meta:
        default_related_name = 'conversations'

    users = models.ManyToManyField('users.User')
    bot = models.ForeignKey('bots.Bot', models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    node = models.ForeignKey('bots.Node', models.SET_NULL, null=True,
                             blank=True)

    def get_absolute_url(self):
        return reverse('messaging:conversation',
                       kwargs={'conversation_id': self.id})

    def __str__(self):
        return ', '.join(str(user) for user in self.users.all())


class Message(models.Model):
    class Meta:
        default_related_name = 'messages'
        ordering = ['timestamp']

    user = models.ForeignKey('users.User', models.CASCADE,
                             related_name='messages', null=True, blank=True)
    bot = models.ForeignKey('bots.Bot', models.CASCADE,
                            related_name='messages', null=True, blank=True)
    conversation = models.ForeignKey('Conversation', models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    @property
    def author(self):
        return str(self.user or self.bot)

    def __str__(self):
        return str(self.author) + ': ' + self.text
