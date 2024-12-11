"""Add is_developer to User

Revision ID: c56f7a8d3800
Revises: 001
Create Date: 2024-11-11 18:43:37.783559
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c56f7a8d3800'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    # Agregar la columna is_developer a la tabla user
    op.add_column('user', sa.Column('is_developer', sa.Boolean(), nullable=False, server_default=sa.false()))


def downgrade():
    # Eliminar la columna is_developer en caso de rollback
    op.drop_column('user', 'is_developer')