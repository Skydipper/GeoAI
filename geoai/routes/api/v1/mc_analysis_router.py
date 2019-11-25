"""API ROUTER"""
import logging
from flask import jsonify, request, Blueprint
from geoai.errors import MCAnalysisError
from geoai.middleware import get_mc_info
from geoai.routes.api import error
from geoai.serializers import serialize_mc
from geoai.services.analysis.mc_analysis_service import TrendService


trend_analysis_endpoints_v1 = Blueprint('trend_analysis_endpoints_v1', __name__)

def analyze(timeseries, window=None, mc_number=None, bin_number=None):
    """Analyze Monte Carlo"""
    if not timeseries:
        return error(status=400, detail='A timeseries is required')
    #logging.info(f'[ROUTER MC]: timeseries={timeseries}')
    try:
        data = TrendService.analyze(
            timeseries=timeseries,
            window=window,
            mc_number=mc_number,
            bin_number=bin_number)
        #logging.info(f"[MC router] data: {data}")
        data['mc_number']= mc_number
        data['window']= window
        data['bin_number']= bin_number
    except MCAnalysisError as e:
        #logging.error(f'[ROUTER MC error]:  {e.message}')
        return error(status=500, detail=e.message)
    except Exception as e:
        #logging.error(f'[ROUTER MC generic error]: {e}')
        return error(status=500, detail='Generic Error')
    #logging.info(f"[MC router] serialiser: {serialize_mc(data, 'mc_timeseries_analysis')}")
    return jsonify(data=serialize_mc(data, 'mc_timeseries_analysis')), 200


@trend_analysis_endpoints_v1.route('/', strict_slashes=False, methods=['POST'])
@get_mc_info
def get_timeseries(timeseries, window, mc_number, bin_number):
    """Analyze timeseries"""
    logging.info(f'[ROUTER MC getter]: {timeseries}, {window}, {mc_number}, {bin_number}')
    return analyze(timeseries=timeseries, window=window,
                     mc_number=mc_number, bin_number=bin_number)

