from datetime import datetime

from django.core.management.base import BaseCommand

from ...models import Loan


class Command(BaseCommand):
    help = 'Updating loans'

    def handle(self, *args, **options):
        print(f'[{datetime.now()}] {self.help}')
        Loan.expire_loans()
