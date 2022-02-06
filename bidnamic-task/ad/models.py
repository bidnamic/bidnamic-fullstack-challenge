from django.db import models

# Create your models here.
class Campaign(models.Model):
    structure_value = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.structure_value

class Adgroup(models.Model):
    # STATUS_OPTIONS=[('ENABLED', 'ENABLED'),('REMOVED', 'REMOVED')]
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    alias = models.CharField(max_length=250)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.alias

class SearchTerm(models.Model):
    ad_group = models.ForeignKey(Adgroup, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    clicks = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    conversion_value = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    conversions = models.IntegerField()
    search_term = models.CharField(max_length=250)
    roas = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    date = models.DateField(null=False, blank=False)

    class Meta:
        ordering = ['-roas']

    def __str__(self):
        return self.search_term
