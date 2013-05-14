"""uppo

Revision ID: 4268dcc69af9
Revises: 116df760c448
Create Date: 2013-05-14 09:02:13.500000

"""

# revision identifiers, used by Alembic.
revision = '4268dcc69af9'
down_revision = '116df760c448'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('uppo', sa.Column('qq', sa.Integer(), nullable=True))
    op.add_column('uppo', sa.Column('cellphone', sa.Integer(), nullable=True))
    op.add_column('uppo', sa.Column('name_real', sa.String(), nullable=True))
    op.add_column('uppo', sa.Column('brief', sa.String(), nullable=True))
    op.add_column('uppo', sa.Column('sex', sa.Integer(), nullable=True))
    op.add_column('uppo', sa.Column('birthday', sa.DateTime(), nullable=True))
    op.add_column('uppo', sa.Column('avatar', sa.String(), nullable=True))
    op.add_column('uppo', sa.Column('weibo_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('uppo', 'weibo_id')
    op.drop_column('uppo', 'avatar')
    op.drop_column('uppo', 'birthday')
    op.drop_column('uppo', 'sex')
    op.drop_column('uppo', 'brief')
    op.drop_column('uppo', 'name_real')
    op.drop_column('uppo', 'cellphone')
    op.drop_column('uppo', 'qq')
    ### end Alembic commands ###