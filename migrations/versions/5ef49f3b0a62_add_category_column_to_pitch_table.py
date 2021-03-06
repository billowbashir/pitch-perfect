"""add category column to pitch table

Revision ID: 5ef49f3b0a62
Revises: 90bf7142d7be
Create Date: 2018-09-10 11:50:08.894000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ef49f3b0a62'
down_revision = '90bf7142d7be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###
