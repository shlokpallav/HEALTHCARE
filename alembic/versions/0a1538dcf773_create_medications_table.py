"""create medications table

Revision ID: 0a1538dcf773
Revises: 37cdf81b531a
Create Date: 2026-09-30 13:37:11.391674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a1538dcf773'
down_revision: Union[str, Sequence[str], None] = '37cdf81b531a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "medications",
        sa.Column(
            "medication_id",
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
            "medicine_name",
            sa.String(length=255),
            nullable=False,
        ),
        sa.Column(
            "dosage",
            sa.String(length=100),
            nullable=True,
        ),
        sa.Column(
            "frequency",
            sa.String(length=100),
            nullable=True,
        ),
        sa.Column(
            "route",
            sa.String(length=50),
            nullable=True,
        ),
        sa.Column(
            "start_date",
            sa.Date(),
            nullable=True,
        ),
        sa.Column(
            "end_date",
            sa.Date(),
            nullable=True,
        ),
        sa.Column(
            "reason",
            sa.String(length=500),
            nullable=True,
        ),
        sa.Column(
            "prescribed_by",
            sa.String(length=255),
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
        sa.PrimaryKeyConstraint("medication_id"),
    )


def downgrade() -> None:
    op.drop_table("medications")
