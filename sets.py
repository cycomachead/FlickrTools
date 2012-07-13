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

# STUFF FOR THE FUTURE
# Add insane amounts of type checking and error handling because it's good
# Add some tests
# Try actually doing TDD! :O


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
    
    def set(self,index):
        """Like the others, but it returns the whole dict"""
        if index > len(flickrset._registry)-1:
           raise IndexError
        return flickrset._registry[index]
        
        # Making the class iterable
    def __iter__(self):
        """docstring for __iter__"""
        return iter(flickrset._registry)
    
    def next(self):
        """docstring for next"""
        index = 0
        if index >= len(flickrset._registry):
            raise StopIteration
        else:
            ret = flickrset._registry[index]
            index += 1
            return ret

class photo(object):
    """class to represent a set photo
    each photo needs a photo id and a URL
    
    Flikr URL Format:
    http://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}_[mstzb].jpg
    
    This will be implemented very similarly to the flickrset class which means it will have a list which contains dictionaries
     
    """
    _registry = []
    __metaclass__ = IterRegistry
    flickr_size = 'q' #this is the large sqaure size I'll use for building thumbs.
    
    def __init__(self):
        """docstring for __init__"""
        return None
    
    def new(self, pid, sid, uid='64724295@N08'):
        """Doesn't require much, but it does require each photo to be attached to a set."""
        new_photo = {"pid":pid,"set":sid,"url":None,"farmid":None,"serverid":None,"secret":None}
        photo._registry.append(new_photo)

        # GETTER METHODS
        # All take in an index and return the item requested for the dictionary.
        
    def pid(self,index):
        if index > len(photo._registry)-1:
           raise IndexError
        return photo._registry[index]["pid"]
             
    def url(self,index):
        if index > len(photo._registry)-1:
           raise IndexError
        elif not photo._registry[index]["url"]:
            raise ValueError("Requested Value Not Present")
        return photo._registry[index]["url"]
       
    def sid(self,index):
        """returns the sid of the set for which the photo is connected for the purposes of my project"""
        if index > len(photo._registry)-1:
           raise IndexError
        return photo._registry[index]["sid"]
    
    def farmid(self,index):
        if index > len(photo._registry)-1:
           raise IndexError
        elif not photo._registry[index]["farmid"]:
            raise ValueError("Requested Value Not Present")
        return photo._registry[index]["farmid"]
       
    def secret(self,index):
        if index > len(photo._registry)-1:
           raise IndexError
        elif not photo._registry[index]["secret"]:
            raise ValueError("Requested Value Not Present")
        return photo._registry[index]["secret"]
    
    def serverid(self,index):
        if index > len(photo._registry)-1:
           raise IndexError
        elif not photo._registry[index]["serverid"]:
            raise ValueError("Requested Value Not Present")
        return photo._registry[index]["serverid"]
       
    def image(self,index):
        """Like the others, but it returns the whole dict"""
        if index > len(photo._registry)-1:
           raise IndexError
        return photo._registry[index]
    
    def all(self):
        """returns all the images"""
        return photo._registry
    
        # SETTER METHODS
        # Setts take in an index (the image) and whatever values are required to build the object
        # They also return have the option to return the value if by specifying True as the last arg
        # If I really feel like it, I should have these methods use the getters....
    
    def set_farmid(self,index,fid,ret=False):
        """docstring for set_farmid
        Takes in an index, the farmid, and sets it.
        Optionally returns the value too, if the last (optional) arg is false
        """
        if index > len(photo._registry)-1:
           raise IndexError
        else:
            photo._registry[index]["farmid"] = fid
            if ret:
                return fid
                
    def set_serverid(self,index,serverid,ret=False):
        """docstring for set_serverid
        Takes in an index, the serverid, and sets it.
        Optionally returns the value too, if the last (optional) arg is false
        """
        if index > len(photo._registry)-1:
           raise IndexError
        else:
            photo._registry[index]["serverid"] = serverid
            if ret:
                return serverid
    
    def set_secret(self,index,secret,ret=False):
        """docstring for set_secret
        Takes in an index, the secret, and sets it.
        Optionally returns the value too, if the last (optional) arg is false
        """
        if index > len(photo._registry)-1:
           raise IndexError
        else:
            photo._registry[index]["secret"] = secret
            if ret:
                return secret
                
    def set_url(self,index,ret=False):
        """docstring for set_farmid
        Takes in an index, and sets the URL based on existing variables.
        A class size, farmid,serverid,photoid,and secret are REQUIRED for the URL to work.
        
        Optionally returns the value too, if the last (optional) arg is false
        http://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}_[mstzb].jpg
        """
        if index > len(photo._registry)-1:
           raise IndexError
        img = photo._registry[index]
        if not photo.flickr_size or not img["farmid"] or not img["serverid"] \
            or not img["secret"] or not img["pid"]:
            raise ValueError("One or more of the parameters if missing for the image: Farmid, Serverid, Secret, Photo ID,or Class Size. \n The URL could no be set.")
        else:
            new_url = "http://farm" + img["farmid"] + ".staticflickr.com/" + img["serverid"] + "/" + img["pid"] + "_" + img["secret"] + "_" + photo.flickr_size + ".jpg" #PHEW.......        
            img["url"] = new_url
            if ret:
                return img["url"]
    
# ############################################################################


# now here is where I need to do the work to set up a list of sets


# Create Empty sets and empty images
all_sets = flickrset()
all_images = photo()
#get all sets and put them in the new class
for item in sets.find('photosets').findall('photoset'):
    #Set init vals: UID, Title, Description, SID
    all_sets.new(item.find('title').text,item.find('description').text,item.attrib['id'])

# get the first image for each set and add it to the list
for s in all_sets:
        curr_set = flickr.walk_set(s["sid"],) #this doesnt work
        for i in range(1):
            # Until I find a better way, I'm going to just use the first photo of each set.
            # Need to check: Is the sets generator ordered? If not....problems.
            print(curr_set)
    
    
