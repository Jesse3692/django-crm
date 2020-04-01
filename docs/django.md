# 初始化相关

## 项目相关

### 创建项目

```python
django-admin startproject project_name
```

### 启动项目

```python
# 进入项目的根目录
python manage.py runserver 0.0.0.0:8888
```

### 创建应用

```python
python manage.py startapp app_name
```

## 项目配置

### 在项目中使用mysql数据库

修改配置文件

```python
# 使用MySQL数据库
DATABASES = {DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
```

修改项目的主目录的`__init__.py`

```python
# 为了在Django中使用pymysql
import pymysql
pymysql.install_as_MySQLdb()
```

### 添加模板配置

```python
# 需要渲染的模版
TEMPLATES = [TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
    }
]]
```

### 添加时区配置

```python
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
```

### 配置静态文件

```python
# 静态文件
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
```

### 在项目的主目录的路由中添加应用的路由

```python
from django.conf.urls import url,include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crm/', include('crm.urls')),
]
```
