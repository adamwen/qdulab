from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Lesson(models.Model):
    name = models.TextField(null=True, blank=False,
                            verbose_name=_('Lesson Name'))
    description = models.TextField(null=True, blank=False,
                                   verbose_name=_('Lesson Description'))
    created_at = models.DateTimeField(auto_now_add=True)
    place = models.TextField(null=True, blank=False,
                             verbose_name=_('Lesson Place'))
    time = models.DateTimeField(blank=False, null=True,
                                verbose_name=_('Lesson Time'))
    users = models.ManyToManyField(User, blank=True)
    total_person = models.IntegerField(blank=True, null=True,
                                       verbose_name=_('Lesson Max person'))

    @property
    def remaining_num(self):
        return self.total_person - self.users.count()

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')
