from django.contrib import admin
from .models import Item, ItemInstance, Owner, Category

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name','date_of_birth','location')

class ItemsInstanceInline(admin.TabularInline):
	model = ItemInstance

class ItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner','get_category')
	inlines = [ItemsInstanceInline]

class ItemInstanceAdmin(admin.ModelAdmin):
	list_display = ('item', 'status', 'borrower', 'due_back', 'id')
	list_filter = ('status','due_back')

	fieldsets = (
		(None, {
			'fields': ('item','id')
			}),
		('Availability', {
			'fields': ('status', 'borrower', 'due_back')
			}),
		)

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemInstance, ItemInstanceAdmin)
admin.site.register(Category)