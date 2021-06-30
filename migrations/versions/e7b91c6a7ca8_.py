"""empty message

Revision ID: e7b91c6a7ca8
Revises: 3854f0fac56c
Create Date: 2021-05-30 22:38:48.100864

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e7b91c6a7ca8'
down_revision = '3854f0fac56c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('department', sa.String(length=60), nullable=True))
    op.drop_index('name', table_name='departments')
    op.drop_index('name_2', table_name='departments')
    op.create_unique_constraint(None, 'departments', ['department'])
    op.drop_column('departments', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('name', mysql.VARCHAR(length=60), nullable=True))
    op.drop_constraint(None, 'departments', type_='unique')
    op.create_index('name_2', 'departments', ['name'], unique=False)
    op.create_index('name', 'departments', ['name'], unique=False)
    op.drop_column('departments', 'department')
    # ### end Alembic commands ###