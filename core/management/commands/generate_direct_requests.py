from django.core.management.base import BaseCommand
from core.services.job_service import JobService
from core.models import Business

class Command(BaseCommand):
    help = 'Generate direct requests for a specific business'

    def add_arguments(self, parser):
        parser.add_argument('business_id', type=int, help='Business ID')

    def handle(self, *args, **kwargs):
        business_id = kwargs['business_id']
        try:
            business = Business.objects.get(pk=business_id)
            JobService.generate_direct_requests(business)
            self.stdout.write(self.style.SUCCESS('Direct requests generated successfully.'))
        except Business.DoesNotExist:
            self.stdout.write(self.style.ERROR('Business not found.'))