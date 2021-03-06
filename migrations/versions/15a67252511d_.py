"""empty message

Revision ID: 15a67252511d
Revises: 6dbe821e1b42
Create Date: 2021-06-29 20:23:37.670819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15a67252511d'
down_revision = '6dbe821e1b42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'employees', 'departments', ['department'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employees', type_='foreignkey')
    # ### end Alembic commands ###
