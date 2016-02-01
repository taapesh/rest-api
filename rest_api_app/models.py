from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Table(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    server_id = models.IntegerField(default=-1)
    server_name = models.CharField(max_length=255, default="")
    party_size = models.IntegerField(default=1)
    request_made = models.BooleanField(default=False)
    time_of_request = models.IntegerField(default=-1)
    is_finished = models.BooleanField(default=False)
    time_of_finish = models.IntegerField(default=-1)
    address_table_combo = models.CharField(max_length=255, default="", unique=True)
    restaurant_name = models.CharField(max_length=255, default="")
    restaurant_address = models.CharField(max_length=255, default="")
    new_table = models.BooleanField(default=True)

    class Meta:
        ordering = ('time_created',)

class Order(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    customer_id = models.IntegerField(default=-1)
    order_name = models.CharField(max_length=255, default="")
    order_price = models.DecimalField(max_digits=5, decimal_places=2)
    customer_first_name = models.CharField(max_length=255, default="")
    address_table_combo = models.CharField(max_length=255, default="")
    table_number = models.IntegerField(default=-1)
    restaurant_address = models.CharField(max_length=255, default="")
    new_order = models.BooleanField(default=True)
    active_order = models.BooleanField(default=True)
    order_queued = models.BooleanField(default=False)
    payment_pending = models.BooleanField(default=False)
    receipt_id = models.IntegerField(default=-1)

class Receipt(models.Model):
    customer_id = models.IntegerField(default=-1)
    total_bill = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    restaurant_name = models.CharField(max_length=255, default="")
    restaurant_address = models.CharField(max_length=255, default="")
    server_name = models.CharField(max_length=255, default="")
    server_rating = models.IntegerField(default=-1)

class TableRequest(models.Model):
    time_of_request = models.DateTimeField(auto_now_add=True)
    address_table_combo = models.CharField(max_length=255, default="", unique=True)

class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
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
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True,)
    first_name = models.CharField(max_length=255, default="",)
    last_name = models.CharField(max_length=255, default="",)
    active_table_id = models.IntegerField(default=-1)
    active_table_number = models.IntegerField(default=-1)
    active_restaurant = models.CharField(max_length=255,default="")
    address_table_combo = models.CharField(max_length=255, default="")
    is_server = models.BooleanField(default=False)
    working_restaurant = models.CharField(max_length=255, default="")
    server_rating = models.IntegerField(default=-1)
    num_server_ratings = models.IntegerField(default=0)
    is_working = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name","password"]

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
