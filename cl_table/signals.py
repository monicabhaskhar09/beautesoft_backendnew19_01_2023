from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
# from cl_app.models import Site_Group, Item_SiteList
from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
# from cl_app.models import LoggedInUser

# @receiver(pre_delete, sender=Site_Group, dispatch_uid='Site_Group_signal')
# def log_deleted_site_group(sender, instance, using, **kwargs):
#     print(instance,"instance***")
#     # d = Deleted()
#     # d.question = instance.id
#     # d.dt = datetime.datetime.now() 
#     # d.save()    

# @receiver(post_delete)
# def site_group_post_delete(sender, instance, *args, **kwargs):
#     print(sender,"sender rdhfd")
    # if sender == Comment:
    #     # do something    



# @receiver(user_logged_in)
# def on_user_logged_in(sender, request, **kwargs):
#     # print(sender,"sender")
#     # print(request,"request")
#     # print(kwargs,"kwargs")
#     # print(request.session.session_key,"Signals")
#     LoggedInUser.objects.get_or_create(user=kwargs.get('user'))


# @receiver(user_logged_out)
# def on_user_logged_out(sender, **kwargs):
#     LoggedInUser.objects.filter(user=kwargs.get('user')).delete()    