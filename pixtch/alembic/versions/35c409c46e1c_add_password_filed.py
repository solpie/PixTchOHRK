"""add password filed

Revision ID: 35c409c46e1c
Revises: None
Create Date: 2013-03-28 15:04:13.734375

"""

# revision identifiers, used by Alembic.
revision = '35c409c46e1c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users', sa.Column('password', sa.String(20)))
    pass


def downgrade():
    op.drop_column('users', 'password')
    pass
