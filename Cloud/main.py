def sync(request):    
    project = request.args.get('project')
    
    device = request.args.get('device')
    address = request.args.get('address')
    port = request.args.get('port', type=int)
    drop = request.args.get('drop', False, type=bool)
    
    if project:
        from google.cloud import firestore
        import google.cloud.exceptions
        
        # Instantiates a client
        db = firestore.Client()
        
        projects_ref = db.collection(u'projects')
        
        if projects_ref:
            
            doc_ref = projects_ref.document(project)
            
            if not doc_ref.get().exists:
                doc_ref.create({})
                
            if device:                
                if drop:
                    doc_ref.update({device: firstore.DELETE_FIELD})
                    
                elif address and port:
                    from datetime import datetime as dt
                    doc_ref.update({device: {u'address': address, u'port': port, u'timestamp': dt.strftime(dt.utcnow(), '%Y-%m-%d %H:%M:%S.%f')}})
            
            doc = doc_ref.get()
            
            import json
            
            return json.dumps(doc.to_dict())
        else:
            return u'collection not found'
    else:
        return u'no project specified'
