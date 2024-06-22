from django.db.models.signals import (pre_save, 
                                      post_save, 
                                      pre_delete, 
                                      post_delete)
from django.dispatch import receiver

from app.models import Register, detail


@receiver(pre_save, sender=Register)
def pre_save_handler(sender, instance, **kwargs):
    # Check if the Register instance has been saved previously
    
    if instance.pk:
        # If the Register instance exists, create a related detail object
        value = detail.objects.create(name="", register=instance)
    data=Register.objects.last().age    
    
@receiver(post_save, sender=Register)
def post_save_handler(sender, instance, created, **kwargs):

    # if created:
        
    #     instance.age = instance.age + 1
    #     instance.save()
        
    data=Register.objects.last().age
   
@receiver(pre_delete, sender=Register)
def pre_delete_handler(sender, instance, **kwargs):
    if instance.name == "example":
        # Disconnect pre_delete signal temporarily
        pre_delete.disconnect(pre_delete_handler, sender=sender)
        # Register.objects.filter(name="example").delete()
        # pre_delete.connect(pre_delete_handler, sender=sender)  # Reconnect pre_delete signal
        

@receiver(post_delete, sender=Register)
def post_delete_handler(sender, instance, **kwargs):
    
    pass 