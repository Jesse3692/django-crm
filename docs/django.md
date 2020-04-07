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

### 修改语言

```python
# \django_crm\settings.py
LANGUAGE_CODE = 'zh-hans'
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

## 使用modelforms在前端生成表单

### 首先编写modelforms类

```python
# crm\forms.py
from django import forms
from crm import models
from django.core.exceptions import ValidationError
import hashlib


# 注册的form
class RegForm(forms.ModelForm):
    class Meta:
        # 元类
        model = models.UserProfile  # 指定model
        fields = '__all__'
```

### 然后在视图函数中应用

```python
# 注册
def register(request):
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        print(form_obj)
        if form_obj.is_valid():
            form_obj.save()
            print(form_obj.is_valid())
        return render(request, 'register.html')
    else:
        form_obj =RegForm()
        return render(request, 'register.html', {'form_obj':form_obj})
```

### 最后在前端页面中应用

```html
<div class="col-md-8 col-md-offset-2" style="margin-top: 80px;">
        <form action="" class="form-horizontal" novalidate method="POST">
            {% csrf_token %}
            <!-- 用户名 -->
            <div class="form-group">
                <label for="{{ form_obj.username.id_for_lable }}" class="col-sm-2 control-lable">
                    {{ form_obj.username.lable }}
                </label>
                <div class="col-sm-10">{{ form_obj.username }}</div>
            </div>
            <!-- .... -->
            <button type="submit">提交</button>
        </form>
</div>
```

