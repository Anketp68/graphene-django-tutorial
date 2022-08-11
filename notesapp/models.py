from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    name = models.CharField(max_length=512)
    email = models.EmailField(null=True)
    phone_no = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    note_name = models.CharField(max_length=512)
    creator = models.CharField(max_length=512)


class NoteUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, null=True, on_delete=models.CASCADE)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    note = models.ForeignKey(Note, null=True, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=512)


class CommentUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True,
                                on_delete=models.CASCADE)