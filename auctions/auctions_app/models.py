from django.db import models


class AuctionCategory(models.Model):
    description = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Categoria: {self.description}"

    class Meta:
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"


class Documents(models.Model):
    description = models.CharField(
        max_length="100",
        null=True,
        blank=True,
        verbose_name="Descrição",
    )
    auction = models.ForeignKey(
        "Auction",
        on_delete=models.DO_NOTHING,
        related_name="documentos",
    )
    anexo = models.FileField(
        upload_to="../uploads/",
        max_lenght=500,
    )

    def __str__(self):
        return f"Documento: {self.description}"

    class Meta:
        verbose_name_plural = "Documentos"
        verbose_name = "Documento"


class Auction(models.Model):
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descrição",
    )
    date = models.DateTimeField(
        verbose_name="Data",
        auto_now=False,
    )
    auction_category = models.ForeignKey(
        AuctionCategory,
        on_delete=models.DO_NOTHING,
        verbose_name="Categoria",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Leilão: {self.description}"

    class Meta:
        verbose_name_plural = "Leilões"
        verbose_name = "Leilão"
        ordering = "date"


class Lot(models.Model):
    class Status(models.IntegerChoices):
        ABERTO = 1, "Lote Aberto"
        FECHADO = 2, "Lote Fechado"

    status = models.PositiveSmallIntegerField(
        choices=Status.choices,
    )
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Título",
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descrição",
    )

    auction = models.ForeignKey(
        Auction,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f"Lote: {self.title}"

    class Meta:
        verbose_name_plural = "Lotes"
        verbose_name = "Lote"


class Bid(models.Model):
    date = models.DateTimeField(
        verbose_name="Data",
        auto_now_add=True,
    )
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
    )
    lot = models.ForeignKey(
        Lot,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Lance: {self.amount}"

    class Meta:
        verbose_name_plural = "Lances"
        verbose_name = "Lance"
        ordering = "date"
