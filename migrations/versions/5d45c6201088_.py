"""empty message

Revision ID: 5d45c6201088
Revises: 069a195b67a4
Create Date: 2021-09-05 06:01:50.872368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d45c6201088'
down_revision = '069a195b67a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lecturers',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nidn', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('students',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nim', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=False),
    sa.Column('first_lecturer', sa.BigInteger(), nullable=True),
    sa.Column('second_lecturer', sa.BigInteger(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['first_lecturer'], ['lecturers.id'], ),
    sa.ForeignKeyConstraint(['second_lecturer'], ['lecturers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('lecturers')
    # ### end Alembic commands ###
