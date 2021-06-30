"""empty message

Revision ID: e17ee16ddb3c
Revises: f3e260660cb2
Create Date: 2021-05-18 16:30:48.343424

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e17ee16ddb3c'
down_revision = 'f3e260660cb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('country', sa.String(length=50), nullable=False))
    op.add_column('customers', sa.Column('city', sa.String(length=50), nullable=False))
    op.add_column('customers', sa.Column('contact', sa.String(length=50), nullable=False))
    op.add_column('customers', sa.Column('address', sa.String(length=50), nullable=False))
    op.add_column('customers', sa.Column('zipcode', sa.String(length=50), nullable=False))
    op.add_column('customers', sa.Column('date_registered', sa.DateTime(), nullable=False))
    op.create_unique_constraint(None, 'customers', ['contact'])
    op.drop_index('ix_employees_username', table_name='employees')
    op.drop_column('employees', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('username', mysql.VARCHAR(length=150), nullable=True))
    op.create_index('ix_employees_username', 'employees', ['username'], unique=False)
    op.drop_constraint(None, 'customers', type_='unique')
    op.drop_column('customers', 'date_registered')
    op.drop_column('customers', 'zipcode')
    op.drop_column('customers', 'address')
    op.drop_column('customers', 'contact')
    op.drop_column('customers', 'city')
    op.drop_column('customers', 'country')
    # ### end Alembic commands ###
