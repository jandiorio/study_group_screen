output_data = {
    'company': 'WWT',
    'email': 'craig.kemmerer@wwt.com',
    'first_name': 'Craig',
    'github_username': 'craigkemmerer',
    'last_name': 'Kemmerer'
}
import yaml
f = open('ckemmerer.yaml', 'w+')
yaml.dump(output_data, f)