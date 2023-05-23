"""empty message

Revision ID: 326e19b551da
Revises: 
Create Date: 2023-05-23 15:06:43.956577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '326e19b551da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('puuid', sa.VARCHAR(length=100), nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('icon_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('puuid')
    )
    op.create_table('version',
    sa.Column('id', sa.VARCHAR(length=10), nullable=False),
    sa.Column('version', sa.VARCHAR(length=50), nullable=True),
    sa.Column('season', sa.Integer(), nullable=True),
    sa.Column('num1', sa.Integer(), nullable=True),
    sa.Column('num2', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('champion',
    sa.Column('id', sa.VARCHAR(length=20), nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('version_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['version_id'], ['version.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item',
    sa.Column('id', sa.VARCHAR(length=20), nullable=False),
    sa.Column('version_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=150), nullable=True),
    sa.Column('info', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['version_id'], ['version.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('match',
    sa.Column('id', sa.VARCHAR(length=20), nullable=False),
    sa.Column('gameVersion', sa.VARCHAR(length=30), nullable=True),
    sa.Column('version_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('winTeam', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['version_id'], ['version.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('perk_style',
    sa.Column('id', sa.VARCHAR(length=20), nullable=False),
    sa.Column('version_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=10), nullable=True),
    sa.ForeignKeyConstraint(['version_id'], ['version.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spell',
    sa.Column('id', sa.VARCHAR(length=20), nullable=False),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('version_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('info', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['version_id'], ['version.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('match_detail',
    sa.Column('id', sa.VARCHAR(length=30), nullable=False),
    sa.Column('match_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('champion_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('puuid', sa.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['champion_id'], ['champion.id'], ),
    sa.ForeignKeyConstraint(['match_id'], ['match.id'], ),
    sa.ForeignKeyConstraint(['puuid'], ['user.puuid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('perk',
    sa.Column('id', sa.VARCHAR(length=20), nullable=False),
    sa.Column('perkStyle_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('version_id', sa.VARCHAR(length=20), nullable=True),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.Column('slot', sa.Integer(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=20), nullable=True),
    sa.Column('shortDesc', sa.Text(), nullable=True),
    sa.Column('longDesc', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['perkStyle_id'], ['perk_style.id'], ),
    sa.ForeignKeyConstraint(['version_id'], ['version.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('perk')
    op.drop_table('match_detail')
    op.drop_table('spell')
    op.drop_table('perk_style')
    op.drop_table('match')
    op.drop_table('item')
    op.drop_table('champion')
    op.drop_table('version')
    op.drop_table('user')
    # ### end Alembic commands ###