"""empty message

Revision ID: 9580cd041470
Revises: 99db51c0d9c5
Create Date: 2021-06-26 21:04:15.818832

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9580cd041470'
down_revision = '99db51c0d9c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('department', sa.String(length=60), nullable=True))
    op.drop_index('dept', table_name='departments')
    op.create_unique_constraint(None, 'departments', ['department'])
    op.drop_column('departments', 'dept')
    op.create_foreign_key(None, 'employees', 'departments', ['department'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employees', type_='foreignkey')
    op.add_column('departments', sa.Column('dept', mysql.VARCHAR(length=60), nullable=True))
    op.drop_constraint(None, 'departments', type_='unique')
    op.create_index('dept', 'departments', ['dept'], unique=False)
    op.drop_column('departments', 'department')
    # ### end Alembic commands ###