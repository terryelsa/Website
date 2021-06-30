"""empty message

Revision ID: 080ced757228
Revises: 2782a38655e2
Create Date: 2021-05-18 19:31:02.106016

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '080ced757228'
down_revision = '2782a38655e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shippers', sa.Column('contact', sa.String(length=150), nullable=True))
    op.drop_column('shippers', 'mobile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shippers', sa.Column('mobile', mysql.VARCHAR(length=45), nullable=True))
    op.drop_column('shippers', 'contact')
    # ### end Alembic commands ###
