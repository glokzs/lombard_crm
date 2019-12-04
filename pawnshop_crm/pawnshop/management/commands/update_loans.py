from django.core.management.base import BaseCommand

from ...models import Loan


class Command(BaseCommand):
    help = 'Updating loans'

    def handle(self, *args, **options):
        Loan.expire_loans()
