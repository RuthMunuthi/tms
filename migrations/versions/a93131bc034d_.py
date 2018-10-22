"""empty message

Revision ID: a93131bc034d
Revises: 8ce1977cf907
Create Date: 2018-08-21 16:58:05.594707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a93131bc034d'
down_revision = '8ce1977cf907'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('deletion_marker', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.String(length=200), nullable=True),
    sa.Column('updated_by', sa.String(length=200), nullable=True),
    sa.Column('deleted_by', sa.String(length=200), nullable=True),
    sa.Column('type_id', sa.String(length=100), nullable=False),
    sa.Column('category_id', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=100), nullable=False),
    sa.Column('company_name', sa.String(length=200), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.public_id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['usertype.public_id'], ),
    sa.PrimaryKeyConstraint('public_id')
    )
    op.create_index(op.f('ix_user_category_id'), 'user', ['category_id'], unique=False)
    op.create_index(op.f('ix_user_created_by'), 'user', ['created_by'], unique=False)
    op.create_index(op.f('ix_user_deleted_by'), 'user', ['deleted_by'], unique=False)
    op.create_index(op.f('ix_user_updated_by'), 'user', ['updated_by'], unique=False)
    op.create_table('token',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=False),
    sa.Column('user_public_id', sa.String(length=100), nullable=True),
    sa.Column('token', sa.Text(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('scopes', sa.Text(), nullable=True),
    sa.Column('revoked', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_public_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_token_user_public_id'), 'token', ['user_public_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_token_user_public_id'), table_name='token')
    op.drop_table('token')
    op.drop_index(op.f('ix_user_updated_by'), table_name='user')
    op.drop_index(op.f('ix_user_deleted_by'), table_name='user')
    op.drop_index(op.f('ix_user_created_by'), table_name='user')
    op.drop_index(op.f('ix_user_category_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###