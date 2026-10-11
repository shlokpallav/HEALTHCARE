"""create medical reports table

Revision ID: 3931eee2689e
Revises: 70dcaa2f41a3
Create Date: 2026-09-29 17:04:28.393896

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3931eee2689e"
down_revision: Union[str, Sequence[str], None] = "70dcaa2f41a3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "medical_reports",

        sa.Column(
            "report_id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True
        ),

        sa.Column(
            "patient_id",
            sa.Integer(),
            sa.ForeignKey("patients.patient_id"),
            nullable=False
        ),

        sa.Column(
            "report_name",
            sa.String(255),
            nullable=False
        ),

        sa.Column(
            "report_type",
            sa.String(100),
            nullable=False
        ),

        sa.Column(
            "report_date",
            sa.Date(),
            nullable=False
        ),

        sa.Column(
            "file_url",
            sa.String(1000),
            nullable=True
        ),

        sa.Column(
            "uploaded_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.func.now()
        ),
    )


def downgrade() -> None:
    op.drop_table("medical_reports")