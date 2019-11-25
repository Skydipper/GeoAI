"""Serializers"""
import logging


def serialize_mc(analysis, type):
    """serialised function for the Monte Carlo Analysis"""
    return {
        'id': None,
        'type': type,
        'attributes': {
            'window': analysis.get('window', None),
            'mc_number': analysis.get('mc_number', None),
            'bin_number': analysis.get('bin_number', None),
            'description': analysis.get('description', None),
            'anomaly': analysis.get('anomaly', None),
            'anomaly_uncertainty': analysis.get('anomaly_uncertainty',None),
            'upper_p': analysis.get('upper_p', None),
            'p': analysis.get('p', None),
            'lower_p': analysis.get('lower_p', None)

        }
    }
