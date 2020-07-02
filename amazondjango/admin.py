from django.contrib import admin
from .models import Customer, ProductTV, ProductPictureTV, CarouselTV1, CarouselTV2, ProductShofa, ProductPictureShofa, ProductReview, ProductType, User, UserProfileInfo

# Register your models here.
admin.site.register(Customer)
admin.site.register(ProductTV)
admin.site.register(ProductPictureTV)
admin.site.register(ProductShofa)
admin.site.register(ProductPictureShofa)
admin.site.register(ProductReview)
admin.site.register(ProductType)
admin.site.register(CarouselTV1)
admin.site.register(CarouselTV2)
# admin.site.register(Transaction)
# admin.site.register(TransactionDetail)
admin.site.register(UserProfileInfo)