from kubernetes import client, config
from bottle import route, run
class Exporter():

    def __init__(self, use_service_account=True):
        if use_service_account:
            config.load_incluster_config()
        else:
            config.load_kube_config()
        self.v1beta = client.ExtensionsV1beta1Api()
        print("kubernetes client is ready.")

    def get_ingress_resources(self):
        result = []
        ret = self.v1beta.list_ingress_for_all_namespaces(watch=False)
        for i in ret.items:
            for r in i.spec.rules:
                result.append(r.host)
        return result

exporter = Exporter()

@route('/')
def index():
    return {'hosts': exporter.get_ingress_resources()}

run(host='0.0.0.0', port=8080)
