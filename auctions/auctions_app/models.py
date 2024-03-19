from django.db import models


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


class AuctionCategory(models.Model):
    description = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )


class Documents(models.Model):
    description = models.CharField(
        max_length="100",
        null=True,
        blank=True,
        verbose_name="Descrição",
    )


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
