from django.contrib import admin
from .models import Employee, Asset, Assignment, InventoryItem, RepairTicket


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "department")
    search_fields = ("name", "email")
    list_filter = ("department",)


class AssetAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "asset_type", "purchase_date")
    search_fields = ("name", "serial_number")
    list_filter = ("asset_type",)
    ordering = ("purchase_date",)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Assignment)
admin.site.register(InventoryItem)
admin.site.register(RepairTicket)