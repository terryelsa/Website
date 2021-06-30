"""empty message

Revision ID: b16753c0eeeb
Revises: e355897a1fb5
Create Date: 2021-05-14 20:11:02.626511

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b16753c0eeeb'
down_revision = 'e355897a1fb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('password', sa.String(length=150), nullable=True))
    op.drop_column('customers', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('password_hash', mysql.VARCHAR(length=150), nullable=True))
    op.drop_column('customers', 'password')
    # ### end Alembic commands ###
