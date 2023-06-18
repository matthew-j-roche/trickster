"""empty message

Revision ID: d2e87e094cd9
Revises: 
Create Date: 2023-06-17 22:41:32.259248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2e87e094cd9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('notes', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('block_id', sa.Integer(), nullable=False),
    sa.Column('is_business', sa.Boolean(), nullable=True),
    sa.Column('notes', sa.String(length=512), nullable=True),
    sa.ForeignKeyConstraint(['block_id'], ['blocks.id'], name=op.f('fk_locations_block_id_blocks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('completed_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_user_games_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_games_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('is_tricked', sa.Boolean(), nullable=True),
    sa.Column('is_treated', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], name=op.f('fk_user_locations_location_id_locations')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_locations_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_locations')
    op.drop_table('user_games')
    op.drop_table('locations')
    op.drop_table('users')
    op.drop_table('games')
    op.drop_table('blocks')
    # ### end Alembic commands ###
