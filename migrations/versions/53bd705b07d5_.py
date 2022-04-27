"""empty message

Revision ID: 53bd705b07d5
Revises: bb7f67d5a04f
Create Date: 2022-04-26 10:51:01.685023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53bd705b07d5'
down_revision = 'bb7f67d5a04f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('presets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('volume', sa.Numeric(precision=5), nullable=False),
    sa.Column('octave', sa.Float(precision=5), nullable=False),
    sa.Column('attack', sa.Float(precision=5), nullable=False),
    sa.Column('decay', sa.Float(precision=5), nullable=False),
    sa.Column('sustain', sa.Numeric(precision=10), nullable=False),
    sa.Column('release', sa.Float(precision=5), nullable=False),
    sa.Column('waveforms', sa.Float(precision=5), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('spatial_ref_sys')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.drop_table('presets')
    # ### end Alembic commands ###
