# GeoAI

GeoAI Services.

## Deploy locally with Docker

In the repo, with Control Tower running, execute:
```bash
./geoAI.sh develop
```


## Trends

Examine long-term changes in a 1-D dataset, using moving average (box-car) detreding and
Monte Carlo resampling to calculate the significance of the low-pass variance.


```python
#url = "https://api.skydipper.com/v1/geoai/trends"
url = "http://localhost:4504/api/v1/geoai/trends"

querystring = {"mc_number":"10000",
               "bin_number":"100",
               "window":"5"}

payload = "{\"timeseries\": {\"2001\": 8523609.893269539, \"2002\": 9219075.336818695, \"2003\": 5745394.048210621, \"2004\": 16352804.901271343, \"2005\": 11950375.210030556, \"2006\": 18535092.244664192, \"2007\": 15964553.06836462, \"2008\": 12015146.018202782, \"2009\": 17515508.700252533, \"2010\": 14973976.22736454, \"2011\": 10555302.132576942, \"2012\": 19785808.554305553, \"2013\": 15784503.92861414, \"2014\": 18598649.662708282, \"2015\": 16366608.645088673, \"2016\": 26919829.052940845, \"2017\": 24389565.014420033, \"2018\": 31650039.900456905}}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache"
    }

response = requests.post(url, data=payload, headers=headers, params=querystring)

print(response.text)
```

Example response:

```json
{
  "data": {
    "attributes": {
      "anomaly": 13226686.577202797,
      "anomaly_uncertainty": 6605963.307585477,
      "bin_number": 100,
      "description": "Increase of 1.3e+07 over observation period has an associated p-value of 0.001\u00b1 1.000 0.948.",
      "lower_p": 0.9480426688037374,
      "mc_number": 10000,
      "p": 0.9994235963381208,
      "upper_p": 0.9999994544351509,
      "window": 5
    },
    "id": null,
    "type": "mc_timeseries_analysis"
  }
}
```