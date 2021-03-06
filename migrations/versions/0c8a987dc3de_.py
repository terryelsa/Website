"""empty message

Revision ID: 0c8a987dc3de
Revises: 06e838c706fe
Create Date: 2021-05-14 15:01:49.269934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c8a987dc3de'
down_revision = '06e838c706fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('order_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'customers', 'orders', ['order_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customers', type_='foreignkey')
    op.drop_column('customers', 'order_id')
    # ### end Alembic commands ###
