from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to="img/services")
    adImage = models.ImageField(upload_to="img/services/ads", blank=True, null=True)
    description = models.CharField(max_length=1000, default="")
    short = models.CharField(max_length=500, default="")

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Service")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default="Team Member")
    gender = models.CharField(max_length=10, choices=[("MALE", "Male"), ("FEMALE", "Female")])
    image = models.ImageField(upload_to="img/members", default="img/members/male.png")
    phrase = models.CharField(max_length=500, default="Don't wait for an opportunity, create it")
    twitter_handle = models.CharField(max_length=1000, default="#")
    fb = models.CharField(max_length=1000, default="#")
    linkedIn = models.CharField(max_length=1000, default="#")
    instangram = models.CharField(max_length=1000, default="#")

    class Meta:
        verbose_name = _("TeamMember")
        verbose_name_plural = _("TeamMember")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("TeamMember_detail", kwargs={"pk": self.pk})

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.gender == "FEMALE" and self.image == "img/members/male.png":
            self.image = "img/members/female.png"
        super(TeamMember, self).save()


class ContactMessage(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        title = self.name
        if title is None: title = self.email
        return f"{self.subject} from {title}"
