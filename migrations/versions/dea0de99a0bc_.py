"""empty message

Revision ID: dea0de99a0bc
Revises: b5e81d4a3c04
Create Date: 2017-07-19 01:04:55.757053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dea0de99a0bc'
down_revision = 'b5e81d4a3c04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('endereco', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('enterprise_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enterprise_id'], ['enterprises.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enterprise_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Float(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('enterprise_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enterprise_id'], ['enterprises.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enterprise_ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('enterprise_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enterprise_id'], ['enterprises.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('enterprise_item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enterprise_item_id'], ['enterprise_items.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_ratings')
    op.drop_table('enterprise_ratings')
    op.drop_table('enterprise_items')
    op.drop_table('comments')
    op.drop_table('items')
    # ### end Alembic commands ###
