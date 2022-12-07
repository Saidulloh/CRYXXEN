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
            user = User.objects.get(id=request.user.id)
            user.last_activity = timezone.now()
            user.save()
        except Exception as ex:
            print(f'error: {ex}')


class IsOnline:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            for user in User.objects.all():
                if (timezone.now() - user.last_activity) > timezone.timedelta(minutes=1):
                    user.is_online = False
                    user.save()
        except Exception as ex:
            print(f'error: {ex}')
