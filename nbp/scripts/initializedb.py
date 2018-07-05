import os
import sys
import transaction

from pyramid.view import view_config
from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.waluta import (
    DBSession,
    Base,
    ExchangeRates
)
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )

from ..services.exRates_table import Nbp


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    data = Nbp.nbp_data()

    with transaction.manager:
        DBSession= get_tm_session(session_factory, transaction.manager)

        for a, b in data['ArrayOfExchangeRatesTable']['ExchangeRatesTable']['Rates'].items():
            for c in b:
                val = ExchangeRates(currency=c['Currency'], code=c['Code'], mid=(c['Mid']))
                DBSession.add(val)