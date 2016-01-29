from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Table(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    owner_id = models.IntegerField(default=-1)
    server_id = models.IntegerField(default=-1)
    party_size = models.IntegerField(default=0)
    request_made = models.BooleanField(default=False)
    time_of_request = models.IntegerField(default=-1)
    is_finished = models.BooleanField(default=False)
    time_of_finish = models.IntegerField(default=-1)
    address_table_combo = models.CharField(max_length=255, default='', unique=True)
    new_table = models.BooleanField(default=False)

    class Meta:
        ordering = ('time_created',)

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner_id = models.IntegerField(default=-1)
    customer_id = models.IntegerField(default=-1)
    customer_email = models.CharField(max_length=255, default='')
    customer_first_name = models.CharField(max_length=255, default='')
    customer_last_name = models.CharField(max_length=255, default='')
    order_price = models.DecimalField(max_digits=5, decimal_places=2)
    order_name = models.CharField(max_length=255, default='')
    restaurant_address = models.CharField(max_length=255, default='')


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
    active_table_number = models.IntegerField(default=-1)
    active_restaurant = models.CharField(max_length=255,default='')
    address_table_combo = models.CharField(max_length=255, default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','password']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
        
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
