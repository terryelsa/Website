"""empty message

Revision ID: 9f7fbe64d601
Revises: 28befda59db9
Create Date: 2021-05-29 09:27:31.346537

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9f7fbe64d601'
down_revision = '28befda59db9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shoppingcart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('categories', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('price', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_table('shoppingcart')
    # ### end Alembic commands ###
