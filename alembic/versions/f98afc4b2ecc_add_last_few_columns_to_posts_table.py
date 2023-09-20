"""add last few columns to posts table

Revision ID: f98afc4b2ecc
Revises: 713eec3b9b26
Create Date: 2023-09-19 16:44:21.757638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f98afc4b2ecc'
down_revision: Union[str, None] = '713eec3b9b26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'publshed')
    op.drop_column('posts', 'created_at')
    pass
