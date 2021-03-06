from django.contrib import admin
from treebeard.admin import TreeAdmin

from accounts import models


class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'primary_user', 'credit_limit',
                    'start_date', 'end_date', 'is_active', 'balance',
                    'date_created']
    readonly_fields = ('balance',)


class TransferAdmin(admin.ModelAdmin):
    list_display = ['reference', 'amount', 'source', 'destination',
                    'user', 'description', 'date_created']
    readonly_fields = ('amount', 'source', 'destination', 'description',
                       'user', 'username', 'date_created')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'transfer', 'account', 'amount', 'date_created']
    readonly_fields = ('transfer', 'account', 'amount', 'date_created')


class IPAddressAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'total_failures', 'consecutive_failures',
                    'is_temporarily_blocked', 'is_permanently_blocked',
                    'date_last_failure']
    readonly_fields = ('ip_address', 'total_failures', 'date_last_failure')


admin.site.register(models.AccountType, TreeAdmin)
admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Transfer, TransferAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
admin.site.register(models.IPAddressRecord, IPAddressAdmin)
