from django.core.validators import FileExtensionValidator
from django.db import models


class File(models.Model):
    file = models.FileField(
        'Файл',
        upload_to='',
        null=False,
        blank=False,
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf', 'png', 'txt']
        )],
        unique=True
    )
    uploaded_at = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
    )
    processed = models.BooleanField(
        'Статус проверки',
        default=False,
    )

    def delete(self, *args, **kwargs):
        self.file.delete()
        super(File, self).delete(*args, **kwargs)
