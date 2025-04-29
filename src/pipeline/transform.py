async def transform( data, endpoint ):
    def transform_listen_history( data ):
        flatten_list = []
        for obj in data:
            for track_id in obj[ 'items' ]:
                flatten_list.append({
                    'user_id'    : obj[ 'user_id' ],
                    'track_id'   : track_id,
                    'created_at' : obj[ 'created_at' ],
                    'updated_at' : obj[ 'updated_at' ],
                })
        return flatten_list

    if endpoint == 'listen_history':
        return transform_listen_history( data )
    return data