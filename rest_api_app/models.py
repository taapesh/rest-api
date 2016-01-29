from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Table(models.Model):
    timeCreated = models.DateTimeField(auto_now_add=True)
    ownerId = models.IntegerField(default=-1)
    serverId = models.IntegerField(default=-1)
    partySize = models.IntegerField(default=1)
    ownerEmail = models.CharField(max_length=255, default='')
    ownerFirstName = models.CharField(max_length=255, default='')
    ownerLastName = models.CharField(max_length=255, default='')
    requestMade = models.BooleanField(default=False)
    timeOfRequest = models.IntegerField(default=-1)
    isFinished = models.BooleanField(default=False)
    timeOfFinish = models.IntegerField(default=-1)
    tableNumber = models.IntegerField(default=-1)

    class Meta:
        ordering = ('created',)


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ownerId = models.IntegerField(default=-1)
    customerId = models.IntegerField(default=-1)
    customerEmail = models.CharField(max_length=255, default='')
    customerFirstName = models.CharField(max_length=255, default='')
    customerLastName = models.CharField(max_length=255, default='')
    orderPrice = models.DecimalField(max_digits=5, decimal_places=2)
    orderName = models.CharField(max_length=255, default='')
    restaurantAddress = models.CharField(max_length=255, default='')


class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password):
        """
        Create and save a user
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        """
        Create a superuser
        """
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=255,
        unique=False,
        default='',
    )
    last_name = models.CharField(
        max_length=255,
        unique=False,
        default='',
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','password']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
        
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
