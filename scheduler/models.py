from app import db
class GlobalDb:
    
    def update(u_id,p_id):
        db.users.update_one({'_id':u_id, 'products._id':p_id},{'$set':{"products.$.done":True}})
        return

    def get_users():
        return list(db.users.find({'products': {'$gt': {'$size': 1}}}))