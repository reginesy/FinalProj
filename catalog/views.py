from django.shortcuts import render
from .models import Item, ItemInstance, Owner, Category
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin #pearl needed
# Create your views here.

def index(request):
	num_items = Item.objects.all().count()
	num_instances = ItemInstance.objects.all().count()

	num_instances_available = ItemInstance.objects.filter(status__exact='a').count()
	num_owners = Owner.objects.count()

	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1

	return render(
		request,
		'index.html',
		context = {'num_items':num_items, 'num_instances':num_instances, 'num_instances_available':num_instances_available,
		'num_owners':num_owners, 'num_visits':num_visits},
	)

class ItemListView(generic.ListView):
	model = Item

	def get_context_data(self, **kwargs):
		context = super(ItemListView, self).get_context_data(**kwargs)
		return context

class ItemDetailView(generic.DetailView):
	model = Item

class OwnerListView(generic.ListView):
	model = Owner

	def get_context_data(self, **kwargs):
		context = super(OwnerListView, self).get_context_data(**kwargs)
		return context

class OwnerDetailView(generic.DetailView):
	model = Owner

class LoanedItemsListView(LoginRequiredMixin,generic.ListView):
	model = ItemInstance
	template_name ='catalog/iteminstance_list_borrowed.html'

	def get_queryset(self):
		return ItemInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
