"""empty message

Revision ID: 12a59ed15a6f
Revises: 6c5f34ab290c
Create Date: 2018-08-20 17:27:00.284414

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '12a59ed15a6f'
down_revision = '6c5f34ab290c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student_information', 'score_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student_information', sa.Column('score_path', mysql.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###