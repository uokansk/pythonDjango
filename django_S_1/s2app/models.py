from django.db import models


class HeadsTails(models.Model):
    res = models.CharField(max_length=100)
    date_res = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'res: {self.res}, date_res: {self.date_res}'
