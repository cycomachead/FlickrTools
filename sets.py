"""This file pulls the sets from from flickr for a given user"""

import flickrapi

#my flickr credentials and info
api_key = '948b85af8b1b9df0a4d38febe7ce75d6'
api_secret = '2a394b9079033cf8'
uid = '64724295@N08'

#basic setup for flickr api - which uses a flickr object for all the work
flickr = flickrapi.FlickrAPI(api_key,api_secret)
#photos = flickr.photos_search(user_id=uid, per_page='100')
sets = flickr.photosets_getList(user_id=uid)

"""<tr>
	<td>	
	<div class="setImg">
		<img class="pho2" src="http://media.tumblr.com/tumblr_m1hfsvRmha1qjg6k8.jpg" alt="Black and White"/>
		<div class="caption">
			<p>A collection of Black and White images</p>
		</div>
	</div>
	</td>
	<td>
	<div class="setImg">
		<img class="pho2" src="http://static.tumblr.com/puzghsv/r8km1hg07/_mg_5277_-_version_2.jpg" alt="UC Berkeley"/>
		<div class="caption">
			<p>A collection of photos taken at UC Berkeley</p>	
		</div>
	</div>
	</td>
</tr>
<tr class="photoslinks">
	<td><a href="http://www.flickr.com/photos/cycomachead/sets/72157629456632509/">Black and White</a></td>
	<td><a href="http://www.flickr.com/photos/cycomachead/sets/72157629125152291/">UC Berkeley</a></td>
</tr>"""




#HTML Tags
#tags generally follow the structure of the html name followed by
# b for begin and e for end
t_begin = """<table style="text-align: middle; margin-right:auto; margin-left: auto;">
<tbody>"""
t_end = """</tbody>
</table>"""
tre = """</tr>"""
trb = """<tr class="{0}">""" #either none or 'photoslinks' for like rows
tdb = """<td>"""
img = """<img class="{0}" src="{1}" alt="{2}" />""" # pho 2, an image link and the set title
divb = """<div class="{0}">""" #either setImg or caption
dive = """</div>"""
a = """<a href="{0}">{1}</a>""" #link to set and then set title
p = """<p>{0}</p>""" #set description

table = """"""
table += t_begin

# THINGS EACH SET NEEDS
# Title and Caption
# Set Photo and a link to the set photo
class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class flickrset(object):
    """A Simple object to represent sets in a format I like
    each set has a title, description and a url, sid, and uid.
    
    A set object will contain a list of dictionaries where each dictionary has the data for each set
    
    """
    _registry = []
    __metaclass__ = IterRegistry
    def __init__(self):
        """docstring for __init__"""
        return None
    
    def new(self, title, description, sid, uid='64724295@N08'):
        new_set = {"title":title,"description":description,"sid":sid,"uid":uid,"url":"http://www.flickr.com/photos/" + str(uid) + "/sets/" + str(sid) + "/"}
        flickrset._registry.append(new_set)
       
    def title(self,index):
        """returns the set title for a set in the list"""
        if index > len(flickrset._registry)-1:
                raise IndexError
        return flickrset._registry[index]["title"]
        
    def description(self,index):
        """returns the set description"""
        if index > len(flickrset._registry)-1:
            raise IndexError
        return flickrset._registry[index]["description"]

    def sid(self,index):
        if index > len(flickrset._registry)-1:
            raise IndexError
        return flickrset._registry[index]["sid"]

    def url(self,index):
        """docstring for url"""
        if index > len(flickrset._registry)-1:
           raise IndexError
        return flickrset._registry[index]["url"]

    def all(self):
        """docstring for all
           Returns the class list of all sets.
           """
        return flickrset._registry


class photo(object):
    """class to represent a set photo
    each photo needs a photo id and a URL
    
    Flikr URL Format:
    http://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}_[mstzb].jpg
    
    """
    
    _registry = []
    __metaclass__ = IterRegistry
    
    def __init__(self, uid, pid, s=None):
        self._registry.append(self)
        self.pid = pid
        self.set = s
        self.url = url
        self.farmid = None
        self.serverid = None
        self.secret = None
        self.size = 'q' 
        # right now this is the flickr size I want, a 150x105 sq image, but if I set it this way I can change it in the future
        
    @property
    def pid(self):
        return self.pid
    
    @property
    def set(self):
        return self.set
        
    @property
    def url(self):
        return self.url
    
    def getset(self):
        self.set = "SOMETHING"
        return self.set
    
    def geturl(self):
        self.url = "SOMETHING"
        return self.url


# now here is where I need to do the work to set up a list of sets



all_sets = flickrset()
for item in sets.find('photosets').findall('photoset'):
    #Set init vals: UID, Title, Description, SID
    all_sets.new(item.find('title').text,item.find('description').text,item.attrib['id'])
    
print(all_sets.all())
    
    
    
    
    
    
    
    
    