# Generated by Django 2.0.6 on 2019-07-05 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0007_auto_20190705_1006'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_test_name', models.CharField(max_length=64, verbose_name='流程接口名')),
                ('api_test_desc', models.CharField(max_length=64, verbose_name='描述')),
                ('api_test_res', models.CharField(max_length=64, verbose_name='测试结果')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('api_tester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='执行人')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.Product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '用例',
                'verbose_name_plural': '用例',
                'db_table': 'ApiTest',
            },
        ),
        migrations.CreateModel(
            name='ApiTestStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=100, verbose_name='用例名称')),
                ('api_url', models.CharField(max_length=200, verbose_name='接口URL')),
                ('api_step', models.CharField(max_length=100, null=True, verbose_name='测试步骤')),
                ('api_param_val', models.CharField(max_length=800, verbose_name='请求参数与值')),
                ('api_method', models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=200, null=True, verbose_name='接口方法')),
                ('api_result', models.CharField(max_length=200, verbose_name='接口预期结果')),
                ('api_response', models.CharField(blank=True, max_length=5000, null=True, verbose_name='响应数据')),
                ('api_status', models.BooleanField(verbose_name='测试结果')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('api_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pro_Api.ApiTest')),
            ],
            options={
                'verbose_name': '用例方法',
                'verbose_name_plural': '用例方法',
                'db_table': 'ApiTestStep',
            },
        ),
    ]
