"""delete language from post

Revision ID: 3c666cbce3f6
Revises: 2270dd6b283a
Create Date: 2023-06-06 11:32:04.882432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c666cbce3f6'
down_revision = '2270dd6b283a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.VARCHAR(length=5), nullable=True))

    # ### end Alembic commands ###
