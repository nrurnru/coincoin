from django.db import models

# Create your models here.
class Agenda(models.Model):
    agenda_text = models.CharField(max_length=200)
    agenda_detail = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    agenda_num = models.IntegerField(primary_key=True, default=0)

    def __str__(self):
        return self.agenda_text

class Reply(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.reply_text
    