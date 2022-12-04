from django.utils import timezone

from apps.user.models import User


class LastActivity: 
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            assert hasattr(request, 'user')
            for user in User.objects.all():
                if user == request.user:
                    user.last_activity=timezone.now()
                    user.is_online = True
                    user.save()
                if (timezone.now() - user.last_activity) > timezone.timedelta(minutes=1):
                    user.is_online = False
                    user.save()
        except Exception as ex:
            print(ex)