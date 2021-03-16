"""empty message

Revision ID: 261dbec433b5
Revises: 12643b2a90ce
Create Date: 2021-03-16 05:04:33.272703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '261dbec433b5'
down_revision = '12643b2a90ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('likes', sa.Integer(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'likes')
    # ### end Alembic commands ###
