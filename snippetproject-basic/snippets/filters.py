import django_filters
from .models import Snippet

class SnippetFilter(django_filters.FilterSet):
    
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    
    ordering = django_filters.ChoiceFilter(label = 'Ordering',
                                           choices = CHOICES,
                                           method = 'filter_by_order')
    
    class Meta:
        model = Snippet
        # fields = '__all__'
        # fields = ('title', 'body', 'created')
        fields = {
		        'title': ['icontains'],
		        'body': ['icontains'],	
	        }
        
    def filter_by_order(self, queryset, name, value):
        # created ascending, -created descending
        expression = 'created' if value == 'ascending' else '-created'
        return queryset.order_by(expression)
        