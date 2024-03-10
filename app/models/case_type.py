# from app.db import mysql  
from app.db import db

class CaseType(db.Model):
    __tablename__ = 'case_types'

    id = db.Column(db.Integer, primary_key=True)
    case_type = db.Column(db.String(255), nullable=False)

    @staticmethod
    def get_all_case_types():
        return CaseType.query.all()

    @staticmethod
    def get_case_type_by_id(case_type_id):
        return CaseType.query.get(case_type_id)

    @staticmethod
    def add_case_type(case_type):
        new_case_type = CaseType(case_type=case_type)
        db.session.add(new_case_type)
        db.session.commit()
        return {'case_type': new_case_type.case_type}

    @staticmethod
    def update_case_type(case_type_id, new_case_type):
        case_type = CaseType.query.get(case_type_id)
        if case_type:
            case_type.case_type = new_case_type
            db.session.commit()
            return {'case_type_id': case_type_id, 'case_type': new_case_type}
        return None

    @staticmethod
    def delete_case_type(case_type_id):
        case_type = CaseType.query.get(case_type_id)
        if case_type:
            db.session.delete(case_type)
            db.session.commit()
            return {'case_type_id': case_type_id}
        return None



