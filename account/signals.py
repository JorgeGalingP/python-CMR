from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Customer


def customer_profile(sender, instance, created, **kwargs):
    # if is a create method 
    if created:
        # add user instance to customer group
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        # create the customer attached to the user instance just created
        Customer.objects.create(
            user=instance,
            name=instance.username,
        )

post_save.connect(customer_profile, sender=User)