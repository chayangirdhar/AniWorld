from django.db import models

# Create your models here.
class AnimeDatabase(models.Model):
    id = models.BigAutoField(primary_key= True)
    mal_id = models.BigIntegerField( blank=True, null=False)
    title = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    trailer = models.TextField(blank=True, null=True)
    titles = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    episodes = models.BigIntegerField(blank=True, null=True)
    aired = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    rank = models.BigIntegerField(blank=True, null=True)
    popularity = models.BigIntegerField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Anime_database'
    
    def __str__(self):
        return self.title
    
