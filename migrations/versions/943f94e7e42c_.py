"""empty message

Revision ID: 943f94e7e42c
Revises: 7d1b271bdaab
Create Date: 2021-05-14 19:46:20.202398

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '943f94e7e42c'
down_revision = '7d1b271bdaab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'customer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('customer_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###