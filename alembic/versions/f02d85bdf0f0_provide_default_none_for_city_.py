"""Provide default None for City.additional_info

Revision ID: f02d85bdf0f0
Revises: b5b18833c60e
Create Date: 2024-03-05 21:12:22.290801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f02d85bdf0f0'
down_revision: Union[str, None] = 'b5b18833c60e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
