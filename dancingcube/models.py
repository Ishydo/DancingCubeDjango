from django.db import models

class Map(models.Model):
    title = models.CharField(max_length=200)
    music = models.CharField(max_length=200)
    EASY = '1'
    MEDIUM = '2'
    HARD = '3'
    diff_rates = [
        (EASY, 'easy'),
        (MEDIUM, 'medium'),
        (HARD, 'hard'),
    ]
    difficulty = models.CharField(
        max_length=1,
        choices=diff_rates,
        default=EASY
        )
    uploader = models.CharField(max_length=200)
    map = models.FileField(upload_to='media/maps/')

    def __str__(self):
        return self.title
