from django.db import models

# Create your models here.


    
class Category(models.Model):
    name=models.CharField(max_length=60)
    slug=models.SlugField(default='test')
    parent=models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    
    class Meta:
        unique_together =('slug','parent')
        verbose_name_plural = 'categories'
        
    def __str__(self):
        full_path=[self.name]
        k=self.parent
        while k is not None: 
            full_path.append(k.name)
            k=k.parent
        return '->'.join(full_path[::-1])
    
    
class Product(models.Model):
    name=models.CharField(max_length=60)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    parent=models.ForeignKey('Category',null=True, blank=True, on_delete=models.CASCADE)
    slug=models.SlugField(default='/')
    
    def __str__(self):
        return self.name
    
    def get_prod_list(self):
        k=self.category
        breadcrumb=['dummy']
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]
    
    