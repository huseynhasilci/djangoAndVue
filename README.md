# djangoAndVue

# Install and setup (Django)

python3 -m venv enviroment_3_8_2

> .\[Virtual Environment Folder Name]\Scripts\activate
Example,
> .\sample_venv\Scripts\activate
>
> pip install virtualenv
>
> pip install django
> pip install django-rest-framework
> pip install django-cors-headers
> pip install djoser
> pip install pillow
> pip install stripe
>
> django-admin startproject djackets_django --> projeyi oluşturdu
>
> settings içerisindeki INSTALLED_APPS içerisine :
> 'rest_framework', 'rest_framework.authtoken', 'corsheaders', 'djoser' bunları ekledik 
> daha sonra INSTALLED_APPS altına CORS_ALLOWED_ORIGINS = ["http://localhost:8080",] ekledik
>
> Daha sonra MIDDLEWARE içerisine 'corsheaders.middleware.CorsMiddleware', bunu ekledik

> bunun ardından urls içerisine aşağıda bulunan kod bloğunu ekledik

> from django.contrib import admin
>from django.urls import path, include
>urlpatterns = [
>    path('admin/', admin.site.urls),
>    path('api/v1/',include('djoser.urls')),
>    path('api/v1/',include('djoser.urls.authtoken')),
>]

> python manage.py makemigrations migration yapmak için bunu yazdık
> python manage.py migrate ardından bunu yazdık

> python .\manage.py createsuperuser admin kulanıcısı oluşturduk

> python .\manage.py runserver ayağa kaldırdık


# VUE için Yükleme Yöntemi

> vue create djackets_vue
> ? Please pick a preset: Manually select features
> ? Check the features needed for your project: Babel, Router, Vuex, CSS Pre-processors
> ? Choose a version of Vue.js that you want to start the project with 3.x
> ? Use history mode for router? (Requires proper server setup for index fallback in production) Yes
> ? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by default): Sass/SCSS (with dart-sass)
> ? Where do you prefer placing config for Babel, ESLint, etc.? In dedicated config files
> ? Save this as a preset for future projects? No

> npm install axios
> npm install bulma

# Include font awsome index.html içerisine cdn ekleyeceğiz.
> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css">

# Setup the base template
> App.vue dosyası içerisinde navbar template'ini oluşturuduk html ile ve bulma frameworkünün css'ini import edip html classlarında kullandık 
> daha sonra homeview içerisindeki componentlerde kullanılan hello worldu sildik


Daha sonra Django üzerinde app oluşturduk ve model ayarlama işlemi
> python manage.py startapp product 
> oluşturduğumuz appi INSTALLED_APPS içerisine atacağız
> python .\manage.py makemigrations
> python .\manage.py migrate
> settings içerisine MEDIA_URL = '/media/' ekledik
> settings içerisine MEDIA_ROOT = BASE_DIR / 'media/' ekledik 
> daha sonra urls.py içerisine from django.conf import settings ekledik
> daha sonra urls.py içerisine from django.conf.urls.static import static


Create a serializer and views for the products --> databaseden alıp json'a döndüren yer
> yeni seralizers diye bir dosya oluşturduk daha sonra bunun içerisinde frontendde kullanacağımız parametreleri söyledik
>  from rest_framework import serializers
> from .models import Category, Product
> bu import işlemlerini yaptık
> 
> daha sonra views içerisine girdik
> buraya 
> from .serializers import ProductSerializers
> from .models import Product
> from rest_framework.views import APIView
> from rest_framework.response import Response
> ekleme işlemini yaptık 
> daha sonra bunlarla ilgili serialize yapan class'ı ekledik 
>
> Bunların ardından product içerisinde bir urls.py dosyası açtık
> buraya 
> from django.urls import path, include
> from product import views
> bu importları yaptık
> daha sonra 
> urlpatterns = [
>    path('latest-products/', views.LatestProductsList.as_view())
> ]
> ekledik ve ana proje içerisindeki urls.py dosyası içerisine bu urls'i import ettik
> 
> ve urlpattern listesi içerisine path('api/v1/',include('product.urls')) bu uzantıyı ekledik
> bunların sayesinde 
![image info](requestOutput.png)
> bunların ardından admin.py dosyasına giderek modelleri import edip admin ile register ettik

> from .models import Category, Product
> admin.site.register(Category)
> admin.site.register(Product)
> bunları yaptıktan sonra veri tabanına gidip istediğimiz verileri alabildik
>

Daha sonra Home.vue içerisinde değişiklikler yaptık script içerisine şunları ekledik

```Javascript
<script>
import axios from "axios";

export default {
  name: 'HomeView',
  data(){
    return{
      latestProducts: []
    }
  },
  components: {
    
  },
  mounted(){
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts(){
      axios.get("/api/v1/latest-products/")
      .then(response => {
        this.latestProducts.push(response.data)
      })
      .catch(err => {
        console.log('err :>> ', err);
      })
    }
  }
}
</script>

<style scoped>
  .image{
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
```

Daha sonra main.js dosyası içerisine kodlarını ekledik ki djangoda çalışan url'e gitisn diye
>import axios from "axios"
>axios.defaults.baseURL = 'http://127.0.0.1:8000'
>createApp(App).use(store).use(router, axios).mount('#app')

View a product
> burada views içerisine productdetail getirmek için bir kod yazdık
```Python
class ProductDetail(APIView):
    
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

```
> bu kodu yazdık daha sonra urls içerisine 
> path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),


> Şimdide Product.vue adında bir dosya oluşturduk
> içerisine yapmak istediğimiz şeyleri yaptık ve görüntüsünü oluşturduk 
> daha sonra router içerisindeki index.js içerisine
```Javascript
{
    path: '/:category_slug/:product_slug/',
    name: 'Product',
    component: Product

}
```
> kodunu ekledik. ardından Product.vue içerisinde product'a dönen değerleri ekleyen bir yapı kurduk