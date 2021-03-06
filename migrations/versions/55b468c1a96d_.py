"""empty message

Revision ID: 55b468c1a96d
Revises: 
Create Date: 2022-02-27 19:45:02.945428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55b468c1a96d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ad_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('create_date', sa.Date(), nullable=True),
    sa.Column('owner', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ad_model_description'), 'ad_model', ['description'], unique=False)
    op.create_index(op.f('ix_ad_model_owner'), 'ad_model', ['owner'], unique=False)
    op.create_index(op.f('ix_ad_model_title'), 'ad_model', ['title'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ad_model_title'), table_name='ad_model')
    op.drop_index(op.f('ix_ad_model_owner'), table_name='ad_model')
    op.drop_index(op.f('ix_ad_model_description'), table_name='ad_model')
    op.drop_table('ad_model')
    # ### end Alembic commands ###
