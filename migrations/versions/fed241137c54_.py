"""empty message

Revision ID: fed241137c54
Revises: da0bd5667863
Create Date: 2024-12-16 14:23:35.101910

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "fed241137c54"
down_revision = "da0bd5667863"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("deposition", schema=None) as batch_op:
        batch_op.drop_index("doi")

    op.drop_table("deposition")
    with op.batch_alter_table("community", schema=None) as batch_op:
        batch_op.drop_constraint("community_ibfk_1", type_="foreignkey")
        batch_op.create_foreign_key(
            None, "user", ["creator_id"], ["id"], ondelete="CASCADE"
        )

    with op.batch_alter_table("community_members", schema=None) as batch_op:
        batch_op.drop_constraint("community_members_ibfk_1", type_="foreignkey")
        batch_op.drop_constraint("community_members_ibfk_2", type_="foreignkey")
        batch_op.create_foreign_key(
            None, "community", ["community_id"], ["id"], ondelete="CASCADE"
        )
        batch_op.create_foreign_key(
            None, "user", ["user_id"], ["id"], ondelete="CASCADE"
        )

    with op.batch_alter_table("user", schema=None) as batch_op:
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

    with op.batch_alter_table("community_members", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.create_foreign_key(
            "community_members_ibfk_2", "community", ["community_id"], ["id"]
        )
        batch_op.create_foreign_key(
            "community_members_ibfk_1", "user", ["user_id"], ["id"]
        )

    with op.batch_alter_table("community", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.create_foreign_key("community_ibfk_1", "user", ["creator_id"], ["id"])

    op.create_table(
        "deposition",
        sa.Column(
            "id", mysql.INTEGER(display_width=11), autoincrement=True, nullable=False
        ),
        sa.Column(
            "dep_metadata",
            mysql.LONGTEXT(charset="utf8mb4", collation="utf8mb4_bin"),
            nullable=False,
        ),
        sa.Column("status", mysql.VARCHAR(length=50), nullable=False),
        sa.Column("doi", mysql.VARCHAR(length=250), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        mysql_collate="utf8mb4_general_ci",
        mysql_default_charset="utf8mb4",
        mysql_engine="InnoDB",
    )
    with op.batch_alter_table("deposition", schema=None) as batch_op:
        batch_op.create_index("doi", ["doi"], unique=True)

    # ### end Alembic commands ###
