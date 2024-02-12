from celery import shared_task
from celery.utils.log import get_task_logger

from .models import File

logger = get_task_logger(__name__)


@shared_task(name='file_handling')
def file_handling(id):
    file = File.objects.get(id=id)
    logger.info(f'Starting to handle file {file}')
    file.processed = True
    file.save()
    logger.info(f'File handling complete')

