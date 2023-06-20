from django.utils.deprecation import MiddlewareMixin
from core.models import BlockedIps

class GetUsersIpsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # print(request.META.get('REMOTE_ADDR'))
        if request.user.is_authenticated:
            ip = request.META.get('REMOTE_ADDR')
            if not request.user.ips:
                request.user.ips = []
            if ip not in request.user.ips:
                request.user.ips.append(ip)
            

class BlockUsersIpsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        x = BlockedIps.objects.filter(ip_address = ip)
        if x:
            raise PermissionError()