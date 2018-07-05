from pyramid.view import (view_config)
from ..services.exRates_table import (UpdateDataBase, ExRatesData, Nbp)
import xmltodict
import pyramid.httpexceptions as exc
import requests


@view_config(route_name='home', renderer='nbp:templates/index.jinja2')
def table(request):
    table = ExRatesData.all(request)

    return {'table': table}


@view_config(request_method='POST',route_name='update', renderer='nbp:templates/index.jinja2')
def update_table(request):
    data = Nbp.nbp_data()
    for a, b in data['ArrayOfExchangeRatesTable']['ExchangeRatesTable']['Rates'].items():
        for c in b:
            UpdateDataBase.whole(request, c['Code'], c['Mid'])

    table = ExRatesData.all(request)

    return {'table': table}


