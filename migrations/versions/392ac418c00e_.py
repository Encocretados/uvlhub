"""empty message

Revision ID: 392ac418c00e
Revises: 077032ca34cb
Create Date: 2024-12-16 17:07:40.009521

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '392ac418c00e'
down_revision = '077032ca34cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_set', schema=None) as batch_op:
        batch_op.drop_constraint('data_set_ibfk_2', type_='foreignkey')
        batch_op.create_foreign_key(None, 'ds_meta_data', ['ds_meta_data_id'], ['id'])
        batch_op.drop_column('community_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_set', schema=None) as batch_op:
        batch_op.add_column(sa.Column('community_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('data_set_ibfk_2', 'community', ['community_id'], ['id'])

    # ### end Alembic commands ###
