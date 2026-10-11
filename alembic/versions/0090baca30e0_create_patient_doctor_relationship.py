"""create patient doctor relationship

Revision ID: 0090baca30e0
Revises: a446615eaa92
Create Date: 2026-10-08 17:17:40.470151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '0090baca30e0'
down_revision: Union[str, Sequence[str], None] = 'a446615eaa92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'patient_doctors',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('patient_id', sa.Integer(), nullable=False),
        sa.Column('doctor_id', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False),
        sa.Column('assigned_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['doctor_id'], ['doctors.doctor_id']),
        sa.ForeignKeyConstraint(['patient_id'], ['patients.patient_id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('patient_doctors')