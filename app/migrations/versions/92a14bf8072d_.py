"""empty message

Revision ID: 92a14bf8072d
Revises: c5452098739f
Create Date: 2022-02-17 06:30:34.647549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92a14bf8072d'
down_revision = 'c5452098739f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('conference_equipments', schema=None) as batch_op:
        batch_op.alter_column('conference_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('equipment_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('conference_equipments', schema=None) as batch_op:
        batch_op.alter_column('equipment_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('conference_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
