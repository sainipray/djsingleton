from django.db import models
from django.utils.translation import gettext as _


class SingletonModel(models.Model):
    """
    This model will save only one entry of model
    """

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_object(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        abstract = True


class SingletonActiveQueryset(models.query.QuerySet):
    def delete(self):
        for obj in self:
            if not obj.active:
                obj.delete()


class SingletonActiveModel(models.Model):
    """
    This model 'active' field value will True for single entry.
     Ex: If you have multiple API keys,
      So you can only activate any key at a time.
    """
    active = models.BooleanField(default=False)
    objects = SingletonActiveQueryset.as_manager()

    def save(self, *args, **kwargs):
        count = self.__class__.objects.count()
        if not count or (count == 1 and self.pk):
            self.active = True
            self.pk = 1
        elif self.active:
            self.__class__.objects.filter(active=True).update(active=False)
        elif not self.active and self.pk:
            self.active = True
        super().save(*args, **kwargs)

    @classmethod
    def get_object(cls):
        obj, created = cls.objects.get_or_create(active=True)
        return obj

    def delete(self, *args, **kwargs):
        if self.active:
            raise Exception(_('Active entry will not delete.'))
        return super().delete(*args, **kwargs)

    class Meta:
        abstract = True
