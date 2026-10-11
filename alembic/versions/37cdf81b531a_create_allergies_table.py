"""create allergies table

Revision ID: 37cdf81b531a
Revises: 7ca0a42f897d
Create Date: 2026-09-30 02:13:58.619002

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "37cdf81b531a"
down_revision: Union[str, Sequence[str], None] = "7ca0a42f897d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create allergies table."""

    op.create_table(
        "allergies",

        sa.Column(
            "allergy_id",
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
            "allergy_name",
            sa.String(length=255),
            nullable=False,
        ),

        sa.Column(
            "allergy_type",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "reaction",
            sa.String(length=500),
            nullable=True,
        ),

        sa.Column(
            "severity",
            sa.String(length=50),
            nullable=True,
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

        sa.PrimaryKeyConstraint("allergy_id"),
    )


def downgrade() -> None:
    """Drop allergies table."""

    op.drop_table("allergies")