"""empty message

Revision ID: c5452098739f
Revises: f43718809ab3
Create Date: 2022-02-14 02:52:18.108805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5452098739f'
down_revision = 'f43718809ab3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('conference_equipments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('num', sa.Integer(), nullable=True))

    with op.batch_alter_table('reserves', schema=None) as batch_op:
        batch_op.add_column(sa.Column('starttime', sa.String(length=30), nullable=False))
        batch_op.add_column(sa.Column('endtime', sa.String(length=30), nullable=False))
        batch_op.alter_column('purpose',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.drop_column('time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reserves', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time', sa.VARCHAR(length=30), nullable=False))
        batch_op.alter_column('purpose',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('endtime')
        batch_op.drop_column('starttime')

    with op.batch_alter_table('conference_equipments', schema=None) as batch_op:
        batch_op.drop_column('num')

    # ### end Alembic commands ###
