from main import app
import json

def test_shorten_and_stats():
    client = app.test_client()
    response = client.post('/api/shorten', json={'url': 'http://localhost:5000/api/shorten.com'})
    assert response.status_code == 200
    data = response.get_json()
    code = data['short_code']

    # Test redirect
    redirect_response = client.get(f'/{code}', follow_redirects=False)
    assert redirect_response.status_code == 302

    # Test stats
    stats = client.get(f'/api/stats/{code}')
    stats_data = stats.get_json()
    assert stats_data['url'] == 'https://localhost:5000.com'
    assert stats_data['clicks'] == 1
