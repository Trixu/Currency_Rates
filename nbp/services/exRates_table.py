import sqlalchemy
import transaction
import xmltodict

from urllib.request import urlopen
from ..models.waluta import ExchangeRates
from ..models.waluta import (
    ExchangeRates,
    DBSession
    )



class Nbp:

    @classmethod
    def nbp_data(cls):
        file = urlopen('http://api.nbp.pl/api/exchangerates/tables/A/?format=xml')
        data = file.read()
        file.close()
        data = xmltodict.parse(data)
        return data


class ExRatesData(object):

    @classmethod
    def all(cls, request):
        query = request.dbsession.query(ExchangeRates)
        return query.with_labels()


class UpdateDataBase(object):

    @classmethod
    def whole(cls, request, code, value):
        request.dbsession.query(ExchangeRates).filter(ExchangeRates.code == code).update({
            ExchangeRates.mid: value}, synchronize_session=False)