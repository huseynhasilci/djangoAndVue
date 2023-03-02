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
