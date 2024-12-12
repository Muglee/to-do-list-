# Generated by Django 4.2.16 on 2024-11-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Custom User'},
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='update_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='completed_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='status',
            field=models.CharField(default='On_Going', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='update_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='categoryName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='taskName',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together={('username', 'email')},
        ),
        migrations.AlterUniqueTogether(
            name='taskmodel',
            unique_together={('categoryName', 'taskName')},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='to_do_list_table',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='date',
        ),
    ]
