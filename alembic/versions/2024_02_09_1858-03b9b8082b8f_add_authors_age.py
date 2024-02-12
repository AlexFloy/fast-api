"""Add authors age

Revision ID: 03b9b8082b8f
Revises: 628df2fd9888
Create Date: 2024-02-09 18:58:03.055247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03b9b8082b8f'
down_revision: Union[str, None] = '628df2fd9888'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authors', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authors', 'age')
    # ### end Alembic commands ###
