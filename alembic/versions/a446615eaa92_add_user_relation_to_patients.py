"""add user relation to patients

Revision ID: a446615eaa92
Revises: 4bc1056b7f72
Create Date: 2026-10-08 16:58:50.226915

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a446615eaa92'
down_revision: Union[str, Sequence[str], None] = '4bc1056b7f72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "patients",
        sa.Column("user_id", sa.Integer(), nullable=True)
    )

    op.create_foreign_key(
        "fk_patients_user_id_users",
        "patients",
        "users",
        ["user_id"],
        ["user_id"]
    )

    op.create_unique_constraint(
        "uq_patients_user_id",
        "patients",
        ["user_id"]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "uq_patients_user_id",
        "patients",
        type_="unique"
    )

    op.drop_constraint(
        "fk_patients_user_id_users",
        "patients",
        type_="foreignkey"
    )

    op.drop_column("patients", "user_id")