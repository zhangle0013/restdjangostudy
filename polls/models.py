#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
# 用户数据模型
# 所有模型都继承自models.Model
# blank = True 意思是在验证的时候允许有空值


class OUsers(models.Model):
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    # 登录名 le.zhang
    uLogName = models.CharField(max_length=50, default='')
    # 密码
    uPassword = models.CharField(max_length=32, default='')
    # 全名，名字完整写法，中文名
    uRealName = models.CharField(max_length=50, default='')
    # 首字母缩写名，在这里指公司人为指定的三个字母名 lez
    uAcronyName = models.CharField(max_length=10, default='')
    # 名字拼写 ZhangLe
    uSpellName = models.CharField(max_length=50, default='')
    # 姓 zhang
    uFirstName = models.CharField(max_length=50, default='')
    # 名 le
    uLastName = models.CharField(max_length=50, default='')
    # 用户是否被删除 true false
    uIsDel = models.BooleanField(default=False)
    # 小头像地址，
    uThumbnailSmall = models.ImageField(blank=True, upload_to='user', default='')
    # 大头像地址，FilePathField是用来选择文件的，FileField是上传文件字段
    # ImageField是专用的图像上传字段，依赖python的 Python Imaging Library(PIL)库
    uThumbnail = models.ImageField(blank=True, upload_to='user', default='')
    # 是否第一次登陆？
    uIsFirst = models.BooleanField(default=True)
    # 邮箱
    uEmail = models.EmailField(blank=True, default='')
    # 电话
    uPhone = models.CharField(max_length=50, blank=True, default='')
    # QQ号码
    uQQ = models.CharField(max_length=50, blank=True, default='')
    # 生日
    uBirthday = models.DateTimeField(blank=True, null=True)
    # 入职日期,
    uEntryDate = models.DateTimeField(blank=True, auto_now_add=True)
    # 离职日期,auto_now_add自动创建
    uLeaveDate = models.DateTimeField(blank=True, null=True)
    # 身份证号,比如我的身份证号是18位，有没有更长的号码呢？
    uIdentity = models.CharField(max_length=18, blank=True, default='')
    # 性别
    uGender = models.CharField(max_length=2, choices=SEX_CHOICES, default='F')
    # 部门  三维，跟踪等
    uDepartment = models.CharField(max_length=50, blank=True, default='')
    # 职位 comp vfx 贴图师，
    uDuty = models.CharField(max_length=50, blank=True, default='')
    # 等级，初级，中级，资深，总监，客户？
    uLevel = models.SmallIntegerField(blank=True, null=True)
    # 0：实习；1：试用；2：正式；3：自由职业；4：客户
    uDutyStatus = models.SmallIntegerField(blank=True, null=True)
    # 工资,数据类型money
    uWage = models.IntegerField(blank=True, null=True)
    # 评论，摘要，附注,无最大值限定
    uRemark = models.TextField(blank=True, default='')
    # 加一个权限组

    def __unicode__(self):
        return self.uLogName

    def spellname(self):
        self.uSpellName = self.uFirstName + self.uLastName
        return self.uSpellName