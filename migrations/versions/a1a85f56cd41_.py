"""empty message

Revision ID: a1a85f56cd41
Revises: b4c59aff4648
Create Date: 2019-04-16 12:21:37.807776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1a85f56cd41'
down_revision = 'b4c59aff4648'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bandcamp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre_text', sa.String(), nullable=True),
    sa.Column('art_id', sa.String(), nullable=True),
    sa.Column('primary_text', sa.String(), nullable=True),
    sa.Column('secondary_text', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('file', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('popular',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('pic', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('popular')
    op.drop_table('bandcamp')
    # ### end Alembic commands ###
