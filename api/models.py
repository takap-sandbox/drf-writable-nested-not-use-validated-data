from django.db import models


class Book(models.Model):
    title = models.CharField("名前", max_length=256)
    page_size = models.PositiveSmallIntegerField("ページ数")
    version = models.PositiveSmallIntegerField("版")

class CommonDetail(models.Model):
    description = models.TextField("説明", blank=True, null=True)
    creator = models.CharField("作者", max_length=256)

    book = models.OneToOneField(
        "api.Book",
        on_delete=models.CASCADE,
        verbose_name="本",
        related_name="detail",
        blank=True,
        null=True,
    )
