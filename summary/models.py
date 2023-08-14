from django.db import models


class FileUpload(models.Model):
    upload = models.FileField(upload_to='file/%Y/%m/%d')

    def __str__(self):
        return self.upload
