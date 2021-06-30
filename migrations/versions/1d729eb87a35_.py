"""empty message

Revision ID: 1d729eb87a35
Revises: 666483d87d64
Create Date: 2021-07-01 02:07:22.138697

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1d729eb87a35'
down_revision = '666483d87d64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'department_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'employees', 'departments', ['department_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employees', type_='foreignkey')
    op.alter_column('employees', 'department_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
