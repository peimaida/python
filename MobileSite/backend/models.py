from django.db import models

# Create your models here.
class Administrator(models.Model):
    id = models.AutoField(db_index=True,primary_key=True)
    username = models.CharField(max_length=100,help_text='用户名')
    password = models.CharField(max_length=500,editable=True)
    pw = models.CharField(max_length=500,editable=True)
    salt = models.IntegerField(help_text='盐值(用于加强MD5加密强度)')
    tel = models.CharField(max_length=11,help_text='分机号')
    status = models.IntegerField(help_text='状态')
    last_login_ip = models.CharField(max_length=100,help_text='最后登录IP')
    last_login_time = models.IntegerField(default=0,help_text='最后登录时间')
    expire_time = models.IntegerField(default=0,help_text='过期时间')
    create_time = models.IntegerField(help_text='创建时间')
    update_time = models.IntegerField(help_text='更新时间')
    permission = models.NullBooleanField(max_length=2,default=0,help_text='管理员权限(0:普通,1:超级)')
  	
    def __str__(self):
      return self.id

class Posts(models.Model):
    id = models.AutoField(db_index=True,primary_key=True)
    post_author = models.IntegerField(default=0,help_text='发布作者ID')
    post_admin = models.IntegerField(default=0,help_text='发布管理员ID')
    update_admin = models.IntegerField(default=0,help_text='更新管理员ID')
    post_content = models.TextField(help_text='新闻内容')
    post_title = models.CharField(max_length=255,help_text='新闻标题')
    status = models.IntegerField(default=0,help_text='状态')
    tag_id = models.IntegerField(default=0,help_text='标签ID')
    origin_image_name = models.CharField(max_length=255,help_text='新闻详情页图片原名')
    origin_title_image_name = models.CharField(max_length=255,help_text='首页新闻图片原名')
    source_image = models.CharField(max_length=255,help_text='新闻详情页图片原图')
    source_title_image = models.CharField(max_length=255,help_text='首页新闻图片原图')
    create_time = models.IntegerField(help_text='创建时间')
    update_time = models.IntegerField(help_text='更新时间')
    start_time = models.IntegerField(help_text='新闻开始时间')
    end_time = models.IntegerField(help_text='新闻结束时间')
    show_flag = models.IntegerField(default=0,help_text='公开标识')
  	
    def __str__(self):
      return self.id

class Events(models.Model):
    id = models.AutoField(db_index=True,primary_key=True)
    event_author = models.IntegerField(default=0,help_text='发布作者ID')
    event_admin = models.IntegerField(default=0,help_text='发布管理员ID')
    update_admin = models.IntegerField(default=0,help_text='更新管理员ID')
    event_content = models.TextField(help_text='活动内容')
    event_title = models.CharField(max_length=255,help_text='活动标题')
    status = models.IntegerField(default=0,help_text='状态')
    origin_image_name = models.CharField(max_length=255,help_text='活动详情页图片原名')
    origin_title_image_name = models.CharField(max_length=255,help_text='首页活动图片原名')
    source_image = models.CharField(max_length=255,help_text='活动详情页图片原图')
    source_title_image = models.CharField(max_length=255,help_text='首页活动图片原图')
    create_time = models.IntegerField(help_text='创建时间')
    update_time = models.IntegerField(help_text='更新时间')
    start_time = models.IntegerField(help_text='活动开始时间')
    end_time = models.IntegerField(help_text='活动结束时间')
    show_flag = models.IntegerField(default=0,help_text='公开标识')
  	
    def __str__(self):
      return self.id

class Banners(models.Model):
    id = models.AutoField(db_index=True,primary_key=True)
    banner_title = models.CharField(max_length=255,default=0,help_text='banner图名称')
    banner_admin = models.IntegerField(default=0,help_text='发布管理员ID')
    update_admin = models.IntegerField(default=0,help_text='更新管理员ID')
    status = models.IntegerField(default=0,help_text='状态')
    origin_image_name = models.CharField(max_length=255,help_text='banner图片原名')
    source_image = models.CharField(max_length=255,help_text='banner图片原图')
    create_time = models.IntegerField(help_text='创建时间')
    update_time = models.IntegerField(help_text='更新时间')
    start_time = models.IntegerField(help_text='banner开始时间')
    end_time = models.IntegerField(help_text='banner结束时间')
    show_flag = models.IntegerField(default=0,help_text='公开标识')
    url = models.CharField(max_length=255,help_text='banner图片的URL链接')
  	
    def __str__(self):
      return self.id

class Author(models.Model):
    id = models.AutoField(db_index=True,primary_key=True)
    author = models.CharField(max_length=255,help_text='作者名')
    status = models.IntegerField(help_text='状态')
    createdby = models.CharField(max_length=255,help_text='创建者')
    create_time = models.IntegerField(help_text='创建时间')
    update_time = models.IntegerField(help_text='更新时间')
  	
    def __str__(self):
      return self.id

class Tags(models.Model):
    id = models.AutoField(db_index=True,primary_key=True)
    tag_name = models.CharField(max_length=255,help_text='标签名')
    status = models.IntegerField(help_text='状态')
    createdby = models.CharField(max_length=255,help_text='创建者')
    create_time = models.IntegerField(help_text='创建时间')
    update_time = models.IntegerField(help_text='更新时间')
  	
    def __str__(self):
      return self.id

class Maintenance(models.Model):
    id = models.AutoField(db_index=True,primary_key=True)
    create_admin_id = models.IntegerField(help_text='创建管理员ID')
    update_admin_id = models.IntegerField(help_text='更新管理员ID')
    status = models.IntegerField(help_text='状态')
    useless = models.IntegerField(default=0,help_text='废弃标识')
    create_time = models.IntegerField(help_text='创建时间')
    update_time = models.IntegerField(help_text='更新时间')
    start_time = models.IntegerField(default=0,help_text='维护开始时间')
    end_time = models.IntegerField(default=0,help_text='维护结束时间')
  	
    def __str__(self):
      return self.id

class Online(models.Model):
    id = models.AutoField(db_index=True,primary_key=True)
    admin_id = models.IntegerField(help_text='管理员ID')
    create_time = models.IntegerField(help_text='创建时间')
  	
    def __str__(self):
      return self.id