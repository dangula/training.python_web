import urllib
import urllib2
import json
from pprint import pprint


google_base = 'http://maps.googleapis.com/maps/api/geocode/json'
techSavy_base = 'http://api.techsavvy.io/jobs'
jobsearch = 'python+web'


def addressLookup(lat,lng):
    try:
        latlng = lat+","+lng
        data = {'latlng' : latlng,'sensor':'false'}
        query = urllib.urlencode(data)
        google_res = urllib2.urlopen('?'.join([google_base,query]))
        google_response = json.load(google_res)
        address = google_response['results'][0]['formatted_address']
        return address
    except urrllib2.HTTPError, e:
        print e.code
        print e.msg
    
try:
    jobsList = []
    res = urllib2.urlopen('/'.join([techSavy_base, jobsearch]))
    response = json.load(res)
    for post in response['data']:
        title = post['title']
        desc = post['description']
        address = addressLookup(post['lat'], post['lng'])
        listingInfo = {'title':title,'description':desc,'address':'address'}
        jobList.append(listingInfo)
    print "total number of Jobs are : %s" %len(jobsList)
    print "they are :"
    for jobs in jobsList:
        print jobs
        
except urllib2.HTTPError, e:
    print e.code
    print e.msg
    
    