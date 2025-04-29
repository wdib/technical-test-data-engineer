from src.pipeline.transform import transform

def test_transform_listen_history():
    fetch_data = [
        {
            'user_id': 45971,
            'items': [
                29214,
                10500,
                27582,
                27812,
                93658
            ],
            'created_at': '2023-10-12T21:16:12.640329',
            'updated_at': '2024-09-24T14:48:09.297853'
        }
    ]

    transformed_data = [   
        {
            'user_id': 45971,
            'track_id': 29214,
            'created_at': '2023-10-12T21:16:12.640329',
            'updated_at': '2024-09-24T14:48:09.297853'
        },
        {
            'user_id': 45971,
            'track_id': 10500,
            'created_at': '2023-10-12T21:16:12.640329',
            'updated_at': '2024-09-24T14:48:09.297853'
        },
        {
            'user_id': 45971,
            'track_id': 27582,
            'created_at': '2023-10-12T21:16:12.640329',
            'updated_at': '2024-09-24T14:48:09.297853'
        },
        {
            'user_id': 45971,
            'track_id': 27812,
            'created_at': '2023-10-12T21:16:12.640329',
            'updated_at': '2024-09-24T14:48:09.297853'
        },
        {
            'user_id': 45971,
            'track_id': 93658,
            'created_at': '2023-10-12T21:16:12.640329',
            'updated_at': '2024-09-24T14:48:09.297853'
        },   
    ]

    result = transform( fetch_data, 'listen_history' )

    assert result == transformed_data