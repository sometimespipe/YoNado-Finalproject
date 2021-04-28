"""empty message

Revision ID: 1ded0681c1b5
Revises: 59628b546540
Create Date: 2021-04-27 22:22:14.347596

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1ded0681c1b5'
down_revision = '59628b546540'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity', sa.Column('lapse', sa.String(), nullable=False))
    op.drop_column('activity', 'time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity', sa.Column('time', postgresql.TIME(), autoincrement=False, nullable=False))
    op.drop_column('activity', 'lapse')
    # ### end Alembic commands ###
