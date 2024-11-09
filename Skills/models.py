from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.




class Skills(models.Model):
    left_side_skill_name = models.CharField(max_length=30,null=True,blank=True)
    
    left_side_skill_percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)],null=True
    )
    right_side_skill_name = models.CharField(max_length=30,null=True,blank=True)
    
    right_side_skill_percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)],null=True
    )


    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Skills"  # Plural name (same as singular, to avoid pluralization)
 



