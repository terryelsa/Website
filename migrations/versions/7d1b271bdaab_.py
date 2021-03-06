"""empty message

Revision ID: 7d1b271bdaab
Revises: 09e2f03ce687
Create Date: 2021-05-14 15:21:35.307546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d1b271bdaab'
down_revision = '09e2f03ce687'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('customer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'orders', 'customers', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_column('orders', 'customer_id')
    # ### end Alembic commands ###
