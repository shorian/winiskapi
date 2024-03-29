"""Allow custom genders

Revision ID: 67b1b42b5ffe
Revises:
Create Date: 2022-06-10 17:44:50.212560

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "67b1b42b5ffe"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "contacts",
        "gender",
        existing_type=postgresql.ENUM("U", "N", "M", "F", name="gender"),
        type_=sa.String(length=30),
        server_default=None,
        existing_nullable=True,
        existing_server_default=sa.text("'U'::gender"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "contacts",
        "gender",
        existing_type=sa.String(length=30),
        type_=postgresql.ENUM("U", "N", "M", "F", name="gender"),
        existing_nullable=True,
        existing_server_default=None,
        server_default=sa.text("'U'::gender"),
    )
    # ### end Alembic commands ###
