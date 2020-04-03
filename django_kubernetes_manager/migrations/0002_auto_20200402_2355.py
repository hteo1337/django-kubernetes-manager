# Generated by Django 3.0.5 on 2020-04-02 23:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_kubernetes_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kubernetescontainer',
            name='args',
            field=models.TextField(blank=True, help_text='Comma separated args to run with command when instantiating container.', null=True),
        ),
        migrations.AlterField(
            model_name='kubernetescontainer',
            name='command',
            field=models.TextField(blank=True, help_text='Command to run when instantiating container', null=True),
        ),
        migrations.CreateModel(
            name='KubernetesConfigMap',
            fields=[
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('deployed', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('labels', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('annotations', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('kind', models.CharField(default='ConfigMap', max_length=16)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('binary', models.BinaryField(blank=True, null=True)),
                ('override_name', models.CharField(blank=True, default='ConfigMap', max_length=32, null=True)),
                ('namespace', models.CharField(default='default', max_length=64)),
                ('cluster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.TargetCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
