from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=50)
    img_name = models.CharField(max_length=50)
    score = models.FloatField(default=1600)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s : %30d' % (self.name, self.score)

