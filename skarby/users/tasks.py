from celery import Celery, shared_task
from users.models import CustomUser
from django.utils import timezone

celery = Celery('skarby')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()


@shared_task()
def count_new_users_weekly():
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=7)

    formatted_start_date = start_date.strftime('%Y-%m-%d')
    formatted_end_date = end_date.strftime('%Y-%m-%d')

    new_users_count = CustomUser.objects.filter(date_joined__gte=start_date, date_joined__lt=end_date).count()

    report_line = (f"За неделю с {formatted_start_date} по {formatted_end_date} количество зарегистрированных "
                   f"новых пользователей:  {new_users_count}.")

    # Записываем строку в файл report.txt
    with open('new_users_report.txt', 'a') as report_file:
        report_file.write(report_line + '\n')

