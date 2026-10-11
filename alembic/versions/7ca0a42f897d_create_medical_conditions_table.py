"""create medical conditions table

Revision ID: 7ca0a42f897d
Revises: 3931eee2689e
Create Date: 2026-09-30 01:38:57.776222

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7ca0a42f897d"
down_revision: Union[str, Sequence[str], None] = "3931eee2689e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create medical_conditions table."""

    op.create_table(
        "medical_conditions",

        sa.Column(
            "condition_id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "patient_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "condition_name",
            sa.String(length=255),
            nullable=False,
        ),

        sa.Column(
            "diagnosed_date",
            sa.Date(),
            nullable=True,
        ),

        sa.Column(
            "source_report_id",
            sa.Integer(),
            nullable=True,
        ),

        sa.Column(
            "status",
            sa.String(length=20),
            nullable=False,
            server_default="pending",
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.now(),
            nullable=False,
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.func.now(),
            nullable=False,
        ),

        sa.ForeignKeyConstraint(
            ["patient_id"],
            ["patients.patient_id"],
        ),

        sa.ForeignKeyConstraint(
            ["source_report_id"],
            ["medical_reports.report_id"],
        ),

        sa.PrimaryKeyConstraint("condition_id"),
    )


def downgrade() -> None:
    """Drop medical_conditions table."""

    op.drop_table("medical_conditions")