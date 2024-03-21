from django.contrib import admin

from .models import Auction, AuctionCategory, Bid, Documents, Lot

auction_models = [Auction, Lot, Bid, Documents, AuctionCategory]
admin.site.register(auction_models)
