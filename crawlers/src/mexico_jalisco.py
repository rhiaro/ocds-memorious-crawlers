def get_record_urls(context, data):
    init_url = context.get('url')
    result = context.http.get(init_url)
    for package in result.json:
        data = {
            'url': package['URIContract'],
            'ocid': package['ocid'],
            'data_type': 'record_package'
        }
        context.emit(data=data)


def get_release_urls(context, data):
    with context.http.rehash(data) as response:
        if response.json.get('packages'):
            for release_url in response.json.get('packages'):
                release_data = {
                    'url': release_url,
                    'data_type': 'release_package'
                }
                context.log.info("Found additional release: [{}]".format(release_url))
                context.emit(rule='release', data=release_data)
    
    context.log.info("Storing record package [{}]".format(data.get('url')))
    context.emit(data=data)
