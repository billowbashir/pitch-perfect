"""change relationships again

Revision ID: 9ea30142de39
Revises: 00cb68331cfa
Create Date: 2018-09-10 15:18:03.292464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ea30142de39'
down_revision = '00cb68331cfa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('pitches_comment_id_fkey', 'pitches', type_='foreignkey')
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.drop_column('pitches', 'comment_id')
    op.drop_constraint('users_pitch_id_fkey', 'users', type_='foreignkey')
    op.drop_constraint('users_comment_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'comment_id')
    op.drop_column('users', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('comment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_comment_id_fkey', 'users', 'comments', ['comment_id'], ['id'])
    op.create_foreign_key('users_pitch_id_fkey', 'users', 'pitches', ['pitch_id'], ['id'])
    op.add_column('pitches', sa.Column('comment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_foreign_key('pitches_comment_id_fkey', 'pitches', 'comments', ['comment_id'], ['id'])
    op.drop_column('pitches', 'user_id')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###
