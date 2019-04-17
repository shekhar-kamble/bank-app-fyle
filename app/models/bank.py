from .. import db#,app_ctx
from sqlalchemy.orm import relationship, backref
from sqlalchemy import desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import orm

Base = declarative_base()

class Bank_Branches(Base):
	__abstract__ = True
	# extend_existing=False
	# __tablename__ = 'bank_branches'
	# db.metadata.clear()
	__table__ = db.Table(
		"bank_branches", Base.metadata,
		db.Column("bank_id",db.Integer),
		db.Column("branch",db.String(64), index=True),
		db.Column("address",db.String(128), index=True),
		db.Column("ifsc",db.String(64), index=True, primary_key=True),
		db.Column("city",db.String(64), index=True),
		db.Column("district",db.String(64)),
		db.Column("state",db.String(64)),
		db.Column("bank_name",db.String(64), index=True),
		autoload=True,
		autoload_with=db.engine
	)

	def __repr__(self):
		return str({"branch": self.branch.encode('ascii','ignore'), "address": self.address.encode('ascii','ignore'),
		 "ifsc_code": self.ifsc.encode('ascii','ignore'),"city": self.city.encode('ascii','ignore'),
		  "district": self.district.encode('ascii','ignore'), "state": self.state.encode('ascii','ignore'),
		   "bank_name": self.bank_name.encode('ascii','ignore')})

	@classmethod
	def __init_mapper__(cls):
		orm.mapper(cls, cls.__table__)

	@staticmethod
	def search(**kwargs):
		if "bank_name" not in kwargs:
			kwargs["bank_name"] = ""
		if "city" not in kwargs:
			kwargs["city"] = ""
		if "page" not in kwargs:
			kwargs["page"] = 1
		# print kwargs,Bank_Branches
		# result = Bank_Branches.query
		# print result			
		Session = orm.sessionmaker(bind=db.engine)
		result = []
		raw_result = Session().query(Bank_Branches).filter(Bank_Branches.bank_name.ilike('%'+kwargs["bank_name"]+'%'),
			 Bank_Branches.city.ilike('%'+kwargs["city"]+'%'))#\
			#  .paginate(kwargs["page"], 10, False)
		for i in range(raw_result.count()):
			result.append(raw_result[i])
		print result
		Session().close()
		return result

	@staticmethod
	def search_by_ifsc(ifsc_code):
		Session = orm.sessionmaker(bind=db.engine)
		result = Session().query(Bank_Branches).filter_by(ifsc=ifsc_code).first()
		print result, type(result)
		Session().close()
		return result
