"""empty message

Revision ID: bfce7928d952
Revises: e9359cd71ef0
Create Date: 2023-07-06 11:47:28.513460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfce7928d952'
down_revision = 'e9359cd71ef0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('createdAt',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('updatedAt',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('updatedAt',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('createdAt',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###