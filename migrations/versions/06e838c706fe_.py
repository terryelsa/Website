"""empty message

Revision ID: 06e838c706fe
Revises: 
Create Date: 2021-05-14 14:57:49.294185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06e838c706fe'
down_revision = None
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
    sa.ForeignKeyConstraint(['customers_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('total_price'),
    sa.UniqueConstraint('total_price')
    )
    op.add_column('customers', sa.Column('order_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'customers', 'orders', ['order_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customers', type_='foreignkey')
    op.drop_column('customers', 'order_id')
    op.drop_table('orderdetails')
    # ### end Alembic commands ###
