import logging
from geoai.services.analysis.mc_analysis_service import TrendService

def test_mc():
    """Test the MC service."""
    t = TrendService()
    assert t is not None
