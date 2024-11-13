"""empty message

Revision ID: 8ee0680921d4
Revises: 37c45cfd2963
Create Date: 2024-11-13 23:34:59.794195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ee0680921d4'
down_revision = '37c45cfd2963'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_set', schema=None) as batch_op:
        batch_op.add_column(sa.Column('publico', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_set', schema=None) as batch_op:
        batch_op.drop_column('publico')

    # ### end Alembic commands ###
