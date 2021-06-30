"""empty message

Revision ID: 28befda59db9
Revises: 080ced757228
Create Date: 2021-05-29 09:26:03.247856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28befda59db9'
down_revision = '080ced757228'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('price', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('categories', 'price')
    # ### end Alembic commands ###
