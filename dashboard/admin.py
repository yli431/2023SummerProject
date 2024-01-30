from django.contrib import admin

from import_export import resources
from .models import Book

class BookResource(resources.ModelResource):

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'price',)
        export_order = ('id', 'price', 'author', 'name')
        exclude = ('imported', )
        
    def for_delete(self, row, instance):
        return self.fields['delete'].clean(row)
    
