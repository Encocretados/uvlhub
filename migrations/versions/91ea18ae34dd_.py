"""empty message

Revision ID: 91ea18ae34dd
Revises: 
Create Date: 2024-12-17 22:48:01.213795

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "91ea18ae34dd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("webhook")
    with op.batch_alter_table("data_set", schema=None) as batch_op:
        batch_op.add_column(sa.Column("publico", sa.Boolean(), nullable=True))

    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(sa.Column("key_code", sa.String(length=6), nullable=True))
        batch_op.alter_column(
            "is_developer",
            existing_type=mysql.TINYINT(display_width=1),
            nullable=True,
            existing_server_default=sa.text("0"),
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.alter_column(
            "is_developer",
            existing_type=mysql.TINYINT(display_width=1),
            nullable=False,
            existing_server_default=sa.text("0"),
        )
        batch_op.drop_column("key_code")

    with op.batch_alter_table("data_set", schema=None) as batch_op:
        batch_op.drop_column("publico")

    op.create_table(
        "webhook",
        sa.Column(
            "id", mysql.INTEGER(display_width=11), autoincrement=True, nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_general_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    # ### end Alembic commands ###