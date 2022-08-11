import graphene
from .fields import UserClass, CommentClass, NoteClass
from notesapp.models import User, Note, Comment
from notesapp.mutations import create_user, create_note, create_comment, delete


class Query(graphene.ObjectType):
    users = graphene.List(UserClass)
    user = graphene.Field(UserClass, id=graphene.ID())
    notes = graphene.List(NoteClass)
    note = graphene.Field(NoteClass, id=graphene.ID())
    comments = graphene.List(CommentClass)
    comment = graphene.Field(CommentClass, id=graphene.ID())

    def resolve_users(root, info):
        return User.objects.all()

    def resolve_user(root, info, id):
        return User.objects.get(id=id)

    def resolve_notes(root, info):
        return Note.objects.all()

    def resolve_note(root, info, id):
        return Note.objects.get(id=id)

    def resolve_comments(root, info):
        return Comment.objects.all()

    def resolve_comment(root, info, id):
        return Comment.objects.get(id=id)


class Mutation(graphene.ObjectType):
    create_user = create_user.Field()
    create_book = create_note.Field()
    create_comment = create_comment.Field()
    delete = delete.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

