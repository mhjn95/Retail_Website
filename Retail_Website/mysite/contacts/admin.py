from django.contrib import admin
from .models import ContactSeller,ContactManufacturer,ContactCustomer,AllCustomer,AllManufacturer,CustomerRfqDetails,QuotesRecieved,Blog
# Register your models here.
admin.site.register(ContactSeller)
admin.site.register(ContactManufacturer)
admin.site.register(ContactCustomer)
admin.site.register(AllCustomer)
admin.site.register(AllManufacturer)
admin.site.register(CustomerRfqDetails)
admin.site.register(QuotesRecieved)
admin.site.register(Blog)
