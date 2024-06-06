from db_config.gino_connect import db

class Campaign(db.Model):
    __tablename__ = 'campaign'
    campaign_id = db.Column(db.Integer, primary_key=True, default=lambda: db.Sequence('campaign_campaign_id_seq').next_value())
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    goal_amount = db.Column(db.Numeric)
    raised_amount = db.Column(db.Numeric)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    category = db.Column(db.Text)
    media = db.Column(db.LargeBinary)
    status = db.Column(db.Boolean)
