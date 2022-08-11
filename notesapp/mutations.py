import graphene
from graphene_file_upload.scalars import Upload
from .fields import UserClass, NoteClass, CommentClass
from .models import User, Note, Comment, NoteUser, CommentUser


class create_user(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    user = graphene.Field(UserClass)

    class Meta:
        description = 'Add user details'

    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone_no = graphene.String()

    def mutate(
        self,
        info,
        phone_no=None,
        **kwargs
        ):
            try:
                user = User.objects.create(name=kwargs.get('name'),
                        email=kwargs.get('email'), phone_no=phone_no)
                return create_user(user=user, success=True)
            except Exception as e:
                return create_user(user=None, success=False, error=e)


class create_note(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    note = graphene.Field(NoteClass)


    class Arguments:
        user_id = graphene.ID(required=True)
        note_name = graphene.String(required=True)
        creator = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        try:
            note = Note.objects.create(note_name=kwargs.get('note_name'
                    ), creator=kwargs.get('creator'))
            note_user = NoteUser.objects.create(note_id=note.id,
                    user_id=kwargs.get('user_id'))
            return create_note(note=note, success=True)
        except Exception as e:
            return create_note(note=note, success=False, error=e)


class create_comment(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()
    comment = graphene.Field(CommentClass)

    class Arguments:
        user_id = graphene.ID(required=True)
        note_id = graphene.ID(required=True)
        body = graphene.String(required=True)


    def mutate(self, info, **kwargs):
        try:
            comment = Comment.objects.create(note_id=kwargs.get('note_id'),
                    comment_text=kwargs.get('comment_text'))
            comment_user = CommentUser.objects.create(user_id=kwargs.get('user_id'), comment_id=comment.id)
            return create_comment(success=True, comment=comment)
        except Exception as e:
            return create_comment(success=False, error=e)


class delete(graphene.Mutation):
    error = graphene.String()
    success = graphene.Boolean()

    class Arguments:
        user_id = graphene.ID()
        note_id = graphene.ID()
        comment_id = graphene.ID()

    def mutate(self, info, **kwargs):
        try:
            if kwargs.get('user_id'):
                User.objects.filter(id=kwargs.get('user_id')).delete()
            if kwargs.get('note_id'):
                Note.objects.filter(id=kwargs.get('note_id')).delete()
            if kwargs.get('comment_id'):
                Comment.objects.filter(id=kwargs.get('comment_id'
                        )).delete()
            return delete(success=True)
        except Exception as e:
            return delete(success=False, error=e)
