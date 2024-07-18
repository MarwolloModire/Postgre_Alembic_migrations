"""добавление столбца в description таблицу Product

Revision ID: d179d8db4f58
Revises: c23fc23cc720
Create Date: 2024-07-18 11:09:56.196633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd179d8db4f58'
down_revision: Union[str, None] = 'c23fc23cc720'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('showcase', 'description')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('showcase', sa.Column('description', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
