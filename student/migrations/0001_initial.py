# Generated by Django 3.1.1 on 2020-12-30 16:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_ID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_num', models.CharField(help_text='00001,00002, etc.', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(help_text='Eg- IT 19, IT 20, MGT 20 etc', max_length=100)),
                ('section', models.CharField(help_text='Eg- 1, 2, 3 etc', max_length=10)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_code', models.IntegerField()),
                ('subject_creation_date', models.DateTimeField(auto_now_add=True)),
                ('subject_update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectCombination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentclass')),
                ('select_subject', models.ManyToManyField(to='student.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_roll', models.IntegerField(unique=True)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=8)),
                ('student_date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('student_reg', models.DateField(auto_now_add=True)),
                ('student_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student_id')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentclass')),
            ],
        ),
        migrations.CreateModel(
            name='DeclareResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.JSONField(blank=True)),
                ('select_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentclass')),
                ('select_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
