# Generated by Django 3.2.15 on 2022-08-08 09:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('comment_text', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('note_name', models.CharField(max_length=512)),
                ('creator', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=512)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_no', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoteUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notesapp.note')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notesapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='CommentUser',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notesapp.comment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notesapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='note',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notesapp.note'),
        ),
    ]
