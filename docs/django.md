# Django项目

## 项目前置操作

### 对系统的应用进行初始化操作

Django项目本身是会带有一些，系统相关的表的有`admin`， `auth`， `contenttypes`， `sessions`

```python
python manage.py makemigrations
python manage.py migrate
```

### 创建超级管理员账号

```python
python manage.py createsuperuser  # 账号默认为当前计算机用户，邮箱可为空，密码最少8位必须包含字母和数字
```

### 在后台管理中注册客户类

```python
# \crm\admin.py
from django.contrib import admin
from crm import models

# Register your models here.
admin.site.register(models.Customer)
```

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

## 数据库相关

### 进行数据库迁移

```python
# 将model层转化为迁移文件
python manage.py makemigrations app_name
# 执行迁移文件，更新数据库
python manage.py migrate app_name
```

### 查看迁移文件的执行状态

```python
python manage.py showmigrations
```

