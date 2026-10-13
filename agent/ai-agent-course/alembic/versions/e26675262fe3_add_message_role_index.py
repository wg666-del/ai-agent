"""add message role index

Revision ID: e26675262fe3
Revises: 2d924d7de750
Create Date: 2026-10-13 18:05:53.457290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e26675262fe3'
down_revision: Union[str, Sequence[str], None] = '2d924d7de750'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        "ix_messages_role",
        "messages",
        ["role"],
        unique=False
    )


def downgrade() -> None:
    op.drop_index(
        "ix_messages_role",
        table_name="messages"
    )
