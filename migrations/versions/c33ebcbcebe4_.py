"""empty message

Revision ID: c33ebcbcebe4
Revises: 0c8a987dc3de
Create Date: 2021-05-14 15:05:14.532820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c33ebcbcebe4'
down_revision = '0c8a987dc3de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orderdetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customers_id', sa.Integer(), nullable=True),
    sa.Column('products_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('total_price', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customers_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('total_price'),
    sa.UniqueConstraint('total_price')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderdetails')
    # ### end Alembic commands ###
