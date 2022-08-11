import graphene
from graphene_django import DjangoObjectType
from .models import User, Note, Comment, NoteUser, CommentUser


class NoteClass(DjangoObjectType):

    class Meta:
       model = Note


class UserClass(DjangoObjectType):
    # note = graphene.List(NoteClass)

    class Meta:
      model = User

    # def resolve_note(self, info, root):
    #     note_user = NoteUser.objects.filter(user_id=self.id).values_list('note_id')
    #     notes = Note.object.filter(id__in=note_user)
    #
    #     return notes


class NoteUserClass(DjangoObjectType):

    class Meta:
      model = NoteUser


class CommentClass(DjangoObjectType):

    class Meta:
       model = Comment


class CommentUserClass(DjangoObjectType):

    class Meta:
       model = CommentUser

